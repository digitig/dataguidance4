TEXFILES = \
		acknowledgements.tex \
		Acronyms.tex \
		activities_and_tailoring.tex \
		categories.tex \
		contributors.tex \
		Definitions.tex \
		Frontmatter.tex \
		Introduction.tex \
		Lifecycle.tex \
		Linking_principles_and_objectives.tex \
		Objectives_and_outputs.tex \
		Process.tex \
		References.tex \
		Tool_qualification.tex \
		Vol1.tex \
		Definitions.tex \
IMAGEFILES = \
		back cover.png \
		process diagram v3 Data Safety Only.png \
		process_diagram.png \
		producerconsumer.png
main :  is-unsrt.bst \
		main.bib \
		$(IMAGEFILES) \
		$(TEXFILES)
	pdflatex  Vol1
	bibtex -include-directory=../ Vol1
	makeindex Vol1
	makeindex locationidx
	makeglossaries "main"
	pdflatex main
	pdflatex main
	pdflatex main

.PHONY : clean
clean :
	del /S /F /Q *.ind
	del /S /F /Q *.ilg
	del /S /F /Q *.aux
	del /S /F /Q *.log
	del /S /F /Q *.idx
	del /S /F /Q *.cb*
	del /S /F /Q *.bbl
	del /S /F /Q *.lof
	del /S /F /Q *.lot
	del /S /F /Q *.out
	del /S /F /Q *.pdf
	del /S /F /Q *.toc
	del /S /F /Q *.*glg
	del /S /F /Q *.*glo
	del /S /F /Q *.*gls
	del /S /F /Q *.xdy
	del /S /F /Q *.acn
	del /S /F /Q *.acr
	del /S /F /Q *.alg
	del /S /F /Q *.gx
