# Markdown (RMarkdown)

[TOC]



## Res
### Learn MD
[MarkdownGuide](https://www.markdownguide.org)
[md 写作规范](https://stdrc.cc/style-guides/markdown)

### Related Topics
↗ [Mermaid](../../../../Software%20Engineering/👾%20Web%20Dev%20&%20Ops/🖥️%20Web%20FrontEnd%20Dev/🌈%20Frontend%20Dev%20Library/JS%20Gadgets/Mermaid.md)
↗ [MathJax](../../../../Software%20Engineering/👾%20Web%20Dev%20&%20Ops/🖥️%20Web%20FrontEnd%20Dev/🌈%20Frontend%20Dev%20Library/JS%20Gadgets/MathJax.md)
↗ [Markdown Related Tools](../../../../Software%20Engineering/CASE%20(Computer-Aided%20Software%20Engineering)%20Tools/Integrated%20CASE%20Tools/Docs%20Tools/Markdown%20Related%20Tools/Markdown%20Related%20Tools.md)

↗ [MkDocs](../../../../Software%20Engineering/👾%20Web%20Dev%20&%20Ops/🖥️%20Web%20FrontEnd%20Dev/🤖%20WebApps/Documentation%20&%20Static%20Site%20Generator%20(SSG)/MkDocs.md)

### Other Res
https://hackmd.io/home
online markdown editor



## Intro
Markdown is a [markup language](https://en.wikipedia.org/wiki/Markup_language) developed by John Gruber whose original goal was enabling authors “to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML)” (https://daringfireball.net/projects/markdown/)



## RMarkdown
> 🔗 https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/rmarkdown.html
> ↗ [RStudio](../../Interpreted%20Languages/R%20Language/RStudio.md)
> ↗ [R Language](../../Interpreted%20Languages/R%20Language/R%20Language.md)
> ↗ [Document Converter](../⚙️%20Document%20Converter/Document%20Converter.md)
> ↗ [Pandoc](../⚙️%20Document%20Converter/Pandoc.md)
> ↗ [Blogdown](../⚙️%20Document%20Converter/Blogdown.md)

RMarkdown is an extension to markdown which includes the ability to embed code chunks and several other extensions useful for writing technical reports.

The `rmarkdown` package extends the `knitr` package to, in one step, allow conversion between an RMarkdown file (.Rmd) into PDF, HTML, word document, amongst others. The main function is `render` which can be used as follows:
```
library(rmarkdown)
library(knitr)
render("file.Rmd", "html_document")
render("file.Rmd", "pdf_document")
render("file.Rmd", "word_document")
```

See [this Rstudio page](http://rmarkdown.rstudio.com/formats.html) for a list of all the output formats supported. Behind-the-scenes, the conversions are typically done using [pandoc](http://pandoc.org/) which we will not cover here.



## Ref

