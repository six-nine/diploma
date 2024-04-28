PDFLATEX = xelatex
REPORT_PDF = report
BIBTEX = bibtex
MAKEINDEX = makeindex
RM = rm -f


all: $(REPORT_PDF).pdf 

fast: *.tex *.bib
	latexmk -pdf -xelatex $(REPORT_PDF)


$(REPORT_PDF).pdf: *.tex *.bib
	$(PDFLATEX) $(REPORT_PDF)
	$(MAKEINDEX) $(REPORT_PDF).nlo -s nomencl.ist -o $(REPORT_PDF).nls
	$(BIBTEX) $(REPORT_PDF).aux
	# Used for master paper only
	# $(BIBTEX) My.aux
	$(PDFLATEX) $(REPORT_PDF)
	# Citations count fixing
	$(PDFLATEX) $(REPORT_PDF)

cleanall: clean
	$(RM)  *.pdf

.PHONY: clean cleanall
clean:
	$(RM) *.aux *.log *.out *.toc *.gz *.gz\(busy\) *.blg *.bbl *.nlo *.nls *.fls *.xdv *.fdb_latexmk *.ilg
