-- Pandoc Lua filter: add a short per-image description below images that appear inside tables.
-- Rationale: images in table cells don't allow the Markdown pattern of a separate figsubcaption block.
-- Output: inserts a LineBreak + raw LaTeX \\figsubcaption{...} after each Image inline in tables.

local stringify = pandoc.utils.stringify

local function latex_escape(s)
  -- Minimal LaTeX escaping for caption-like text.
  -- We avoid complex logic (math etc.) because this is used for Eye-Tracking captions.
  local replacements = {
    ["\\"] = "\\textbackslash{}",
    ["{"] = "\\{",
    ["}"] = "\\}",
    ["$"] = "\\$",
    ["&"] = "\\&",
    ["#"] = "\\#",
    ["_"] = "\\_",
    ["%"] = "\\%",
    ["~"] = "\\textasciitilde{}",
    ["^"] = "\\textasciicircum{}",
  }
  return (s:gsub("[\\{}%$&#_%~%^]", function(ch)
    return replacements[ch] or ch
  end))
end

local function build_desc(alt)
  local stim = alt:match("(F%d+%-S%d+%-?%d*)")
  local cohort = alt:match("(%d%d%-NFS%-%d%d)")

  local typ = nil
  if alt:find("Heatmap", 1, true) then
    typ = "Heatmap"
  elseif alt:find("Fog-View", 1, true) then
    typ = "Fog-View"
  elseif alt:find("View-Map", 1, true) or alt:find("Viewmap", 1, true) then
    typ = "Viewmap"
  end

  local parts = { "Kurzbeschreibung:" }
  if typ then
    table.insert(parts, string.format("RealEye-Export (%s).", typ))
  else
    table.insert(parts, "RealEye-Export.")
  end
  if stim then
    table.insert(parts, string.format("Stimulus %s.", stim))
  end
  if cohort then
    table.insert(parts, string.format("Jahrgang %s (Gesamt).", cohort))
  end
  if not (stim or cohort or typ) then
    table.insert(parts, alt .. ".")
  end
  return table.concat(parts, " ")
end

local function process_inlines(inlines)
  local out = pandoc.List()
  for i = 1, #inlines do
    local el = inlines[i]
    out:insert(el)
    if el.t == "Image" then
      -- Avoid double-inserting if already followed by a figsubcaption raw inline.
      local next_el = inlines[i + 1]
      local already = next_el
        and next_el.t == "RawInline"
        and next_el.format == "latex"
        and next_el.text:find("\\figsubcaption", 1, true)
      if not already then
        local alt = stringify(el.caption)
        local desc = latex_escape(build_desc(alt))
        out:insert(pandoc.LineBreak())
        out:insert(pandoc.RawInline("latex", "\\figsubcaption{" .. desc .. "}"))
      end
    end
  end
  return out
end

local function process_blocks(blocks)
  local out = pandoc.List()
  for _, b in ipairs(blocks) do
    if b.t == "Para" or b.t == "Plain" then
      b.content = process_inlines(b.content)
      out:insert(b)
    else
      out:insert(b)
    end
  end
  return out
end

function Table(tbl)
  local function process_row(row)
    if not row or not row.cells then
      return
    end
    for _, cell in ipairs(row.cells) do
      if cell.contents then
        cell.contents = process_blocks(cell.contents)
      end
    end
  end

  -- Table head
  if tbl.head and tbl.head.rows then
    for _, row in ipairs(tbl.head.rows) do
      process_row(row)
    end
  end

  -- Table bodies
  if tbl.bodies then
    for _, body in ipairs(tbl.bodies) do
      if body.head then
        for _, row in ipairs(body.head) do
          process_row(row)
        end
      end
      if body.body then
        for _, row in ipairs(body.body) do
          process_row(row)
        end
      end
    end
  end

  -- Table foot
  if tbl.foot and tbl.foot.rows then
    for _, row in ipairs(tbl.foot.rows) do
      process_row(row)
    end
  end

  return tbl
end
