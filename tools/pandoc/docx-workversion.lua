local function read_inlines(markdown_text)
  local doc = pandoc.read(markdown_text, "markdown")
  if #doc.blocks == 0 then
    return {}
  end

  local first = doc.blocks[1]
  if first.t == "Para" or first.t == "Plain" then
    return first.content
  end

  return { pandoc.Str(markdown_text) }
end

local function clean_ref_text(text)
  local cleaned = text

  cleaned = cleaned:gsub("\\hyperref%[[^%]]+%]{([^{}]-)}", "%1")
  cleaned = cleaned:gsub("\\autoref%{[^}]+}", "")
  cleaned = cleaned:gsub("\\pageref%{[^}]+}", "")
  cleaned = cleaned:gsub("\\eqref%{[^}]+}", "")
  cleaned = cleaned:gsub("\\ref%{[^}]+}", "")
  cleaned = cleaned:gsub("\\label%{[^}]+}", "")
  cleaned = cleaned:gsub("\\thispagestyle%{[^}]+}", "")
  cleaned = cleaned:gsub("\\vspace%*?%b{}", "")
  cleaned = cleaned:gsub("%s*{#[-:_%w]+}", "")
  cleaned = cleaned:gsub("~", " ")
  cleaned = cleaned:gsub("%(%s*%)", "")
  cleaned = cleaned:gsub("%s%s+", " ")

  return cleaned
end

function RawInline(el)
  if el.format ~= "latex" then
    return nil
  end

  local cleaned = clean_ref_text(el.text)
  if cleaned == "" then
    return {}
  end

  return read_inlines(cleaned)
end

function RawBlock(el)
  if el.format ~= "latex" then
    return nil
  end

  local cleaned = clean_ref_text(el.text)
  if cleaned == "" then
    return {}
  end

  return pandoc.Plain(read_inlines(cleaned))
end

function Math(el)
  local normalized = el.text
  normalized = normalized:gsub("\\\\text%s*{", "\\text{")
  normalized = normalized:gsub("\\text{–}", "\\text{-}")
  normalized = normalized:gsub("\\text{—}", "\\text{-}")
  el.text = normalized
  return el
end

function Str(el)
  local text = el.text
  local cleaned = text:gsub("{#[-:_%w]+}", "")
  if cleaned == "" then
    return {}
  end
  if cleaned ~= text then
    el.text = cleaned
    return el
  end
  return nil
end

function Code(el)
  if el.text == "\\hyperref" then
    return pandoc.Code("hyperref")
  end
  return nil
end

function Header(el)
  el.identifier = ""
  return el
end
