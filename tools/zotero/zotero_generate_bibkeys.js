#!/usr/bin/env node
"use strict";

const fs = require("fs");

const STOPWORDS = new Set([
  "a", "an", "and", "auf", "aus", "bei", "das", "de", "der", "des", "die",
  "ein", "eine", "for", "im", "in", "of", "on", "the", "to", "und", "von",
  "with", "zu", "zur",
]);

function usage() {
  console.error("Usage: node tools/zotero/zotero_generate_bibkeys.js [items.json|-] [--format csv|json]");
}

function parseArgs(argv) {
  const args = { input: "-", format: "csv" };
  const rest = [...argv];
  while (rest.length) {
    const value = rest.shift();
    if (value === "--format") {
      args.format = rest.shift() || "";
    } else if (value === "-h" || value === "--help") {
      usage();
      process.exit(0);
    } else if (!value.startsWith("--")) {
      args.input = value;
    } else {
      throw new Error(`Unknown option: ${value}`);
    }
  }
  if (!["csv", "json"].includes(args.format)) {
    throw new Error("--format must be csv or json");
  }
  return args;
}

function readInput(path) {
  const raw = path === "-" ? fs.readFileSync(0, "utf8") : fs.readFileSync(path, "utf8");
  const parsed = JSON.parse(raw);
  if (Array.isArray(parsed)) return parsed;
  if (Array.isArray(parsed.items)) return parsed.items;
  throw new Error("Input must be a JSON array or an object with an items array");
}

function dataOf(item) {
  return item && item.data ? item.data : item;
}

function transliterate(value) {
  return String(value || "")
    .replace(/ä/g, "ae").replace(/ö/g, "oe").replace(/ü/g, "ue")
    .replace(/Ä/g, "Ae").replace(/Ö/g, "Oe").replace(/Ü/g, "Ue")
    .replace(/ß/g, "ss")
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "");
}

function cleanToken(value) {
  return transliterate(value).replace(/[^A-Za-z0-9]+/g, " ").trim();
}

function firstCreatorSurname(data) {
  const creators = Array.isArray(data.creators) ? data.creators : [];
  const creator = creators.find((entry) => entry.lastName || entry.name) || {};
  const name = creator.lastName || creator.name || "unknown";
  return cleanToken(name).split(/\s+/)[0] || "unknown";
}

function yearOf(data) {
  const date = data.date || data.year || "";
  const match = String(date).match(/\b(1[5-9]\d{2}|20\d{2}|21\d{2})\b/);
  return match ? match[1] : "n.d";
}

function titlePart(data) {
  const title = cleanToken(data.title || data.shortTitle || "");
  const words = title
    .split(/\s+/)
    .filter((word) => word && !STOPWORDS.has(word.toLowerCase()))
    .slice(0, 3);
  if (!words.length) return "untitled";
  return words
    .map((word, index) => {
      const lower = word.charAt(0).toLowerCase() + word.slice(1);
      if (index === 0) return lower;
      return lower.charAt(0).toUpperCase() + lower.slice(1);
    })
    .join("");
}

function baseKey(item) {
  const data = dataOf(item);
  return `${firstCreatorSurname(data).toLowerCase()}_${titlePart(data)}_${yearOf(data)}`;
}

function itemKey(item) {
  const data = dataOf(item);
  return data.key || item.key || "";
}

function generate(items) {
  const bases = items.map((item) => baseKey(item));
  const totals = new Map();
  const seen = new Map();
  for (const base of bases) totals.set(base, (totals.get(base) || 0) + 1);
  return items.map((item, index) => {
    const base = bases[index];
    const current = seen.get(base) || 0;
    seen.set(base, current + 1);
    const suffix = totals.get(base) > 1 ? String.fromCharCode(97 + current) : "";
    const data = dataOf(item);
    return {
      itemKey: itemKey(item),
      citationKey: `${base}${suffix}`,
      title: data.title || "",
      year: yearOf(data),
    };
  });
}

function csvEscape(value) {
  const text = String(value == null ? "" : value);
  return /[",\n]/.test(text) ? `"${text.replace(/"/g, '""')}"` : text;
}

function writeOutput(rows, format) {
  if (format === "json") {
    process.stdout.write(`${JSON.stringify(rows, null, 2)}\n`);
    return;
  }
  process.stdout.write("itemKey,citationKey,year,title\n");
  for (const row of rows) {
    process.stdout.write([row.itemKey, row.citationKey, row.year, row.title].map(csvEscape).join(",") + "\n");
  }
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  const items = readInput(args.input);
  writeOutput(generate(items), args.format);
}

try {
  main();
} catch (error) {
  console.error(error.message);
  usage();
  process.exit(1);
}
