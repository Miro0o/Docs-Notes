# Academic Writing Workflow

This folder is set up for writing academic notes and manuscripts in Obsidian while keeping references in plain text.

Use `References/library.bib` as the source of truth for bibliography entries. Keep citation keys stable, then cite them in notes with Pandoc syntax:

```md
This is a parenthetical citation [@smith2024].
This cites a page range [@smith2024, pp. 12-14].
Multiple sources can be grouped [@smith2024; @doe2023].
```

Suggested flow:

1. Add or paste BibTeX entries into `References/library.bib`.
2. Create one literature note per source in `References/Paper Notes`.
3. Put manuscript drafts in `Writing`.
4. Put PDFs in `References/PDFs` and link to them from literature notes.
5. Export drafts with Pandoc using the bibliography and CSL style in this folder.

Example terminal export:

```sh
cd "Information Science & Computer Science and Engineering/Academics 🎓 (In CS)/🗒️ My Academic Projects Workspace/_Academic Writing Workflow/Writing"
pandoc sample-manuscript.md --citeproc -o ../Exports/sample-manuscript.pdf
```

Pandoc must be installed on the machine for PDF/DOCX export and the Pandoc Reference List plugin to work fully. The Obsidian plugins and vault paths are already configured for this folder.

If you want a different citation style, add another `.csl` file to `CSL` and change the `csl:` field in the manuscript frontmatter.
