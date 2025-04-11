TEXFILES = \
		accidents.tex \
		Acknowledgements.tex \
		acronyms.tex \
		categories.tex \
		contributors.tex \
		Data_migration_and_Porting.tex \
		data_safety_culture.tex \
		data_safety_management_plan.tex \
		definitions.tex \
		DSAL_Customisation.tex \
		frontmatter.tex \
		guidance.tex \
		guidewords.tex \
		introduction.tex \
		lifecycle.tex \
		organisational_data_risk.tex \
		principles.tex \
		references.tex \
		supplier_data_maturity.tex \
		Vol2.tex
IMAGEFILES = \
	back cover.png \
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
	del /S /F /Q *.blg
