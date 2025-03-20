TEXFILES = \
		introduction.tex \
		principlesprocess.tex \
		definitionsabbreviations.tex \
		objectivesoutputs.tex \
		activitiestailoring.tex \
		guidance.tex \
		workedexample.tex \
		principlesobjectives.tex \
		assessment.tex \
		culture.tex \
		maturity.tex \
		types.tex \
		guidewords.tex \
		plan.tex \
		accidents.tex \
		lifecycle.tex \
		machineLearning.tex \
		autonomy.tex \
		darkData.tex \
		darkDazzleData.tex \
		dazzleData.tex \
		cygnology.tex \
		tools.tex \
		migration.tex \
		covid19.tex \
		likelihood.tex \
		acronyms.tex \
		references.tex \
		history.tex \
		contributors.tex \
		acknowledgements.tex \
		feedback.tex
		
IMAGEFILES = \
		images/front\ cover.pdf \
		images/back\ cover.png \
		images/medicalscenario.png \
		images/manufacturer.png \
		images/healthorganisation.png \
		images/producerconsumer.png \
		images/producerconsumer.pdf \
		images/developmentlifecycleflat.pdf \
		images/operationallifecycleflat.pdf \
		images/dataacquisitionlifecycleflat.pdf \
		images/darkknowns.pdf \
		images/darkfailures.png \
		images/darkperformance.png \
		images/darknewcases.png \
		images/cygDragon.png \
		images/cygStorm.png \
		images/cygSwan.png \
		images/cygPudding.png \
		images/migration1.pdf \
		images/migration2.pdf \
		images/migration3.pdf \
	
main :  is-unsrt.bst \
		main.bib \
		$(IMAGEFILES) \
		$(TEXFILES)
	pdflatex -output-directory obj main
	bibtex -include-directory=obj obj/main
	makeindex obj/main
	makeindex obj/locationidx
	makeglossaries "main"
	pdflatex -output-directory obj main
	pdflatex -output-directory obj main
	pdflatex -output-directory obj main

.PHONY : clean
clean :
	del /F /Q $(OBJDIR)\*
	del /F /Q *.ind
	del /F /Q *.ilg
	del /F /Q *.aux
	del /F /Q *.log
	del /F /Q *.idx
	del /F /Q *.cb*
	del /F /Q *.bbl
	del /F /Q *.lof
	del /F /Q *.lot
	del /F /Q *.out
	del /F /Q *.pdf
	del /F /Q *.toc
	del /F /Q *.*glg
	del /F /Q *.*glo
	del /F /Q *.*gls
	del /F /Q *.xdy
	del /F /Q *.acn
	del /F /Q *.acr
	del /F /Q *.alg
	
	


	
	