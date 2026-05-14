<%*
const { exec } = require('child_process');
exec('pandoc "Wirkgefüge im digitalen Bildungsraum.md" --citeproc --bibliography="/Users/jochen_hanisch-johannsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jochen-Hanisch/Allgemein_beruflich/Research/Charité - Universitätsmedizin Berlin/Matadaten/Literaturverzeichnis.bib" --csl="/Users/jochen_hanisch-johannsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jochen-Hanisch/pandoc-templates/bibliography/apa.csl" --pdf-engine=xelatex -o "Wirkgefüge im digitalen Bildungsraum.pdf"', (err, stdout, stderr) => {
  if (err) {
    console.error(`Fehler: ${stderr}`);
  } else {
    console.log(`Ausgabe: ${stdout}`);
  }
});
%>