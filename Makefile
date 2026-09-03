# Makefile per compilare le 3 lingue facilmente

LATEXMK = latexmk -pdf -interaction=nonstopmode -file-line-error

.PHONY: all en de fr clean

all: en de fr

en:
	$(LATEXMK) -jobname=main_en main.tex

de:
	$(LATEXMK) -jobname=main_de -pdflatex='pdflatex %O -jobname=main_de "\def\langdir{chapters_de}\input{main.tex}"' main.tex

fr:
	$(LATEXMK) -jobname=main_fr -pdflatex='pdflatex %O -jobname=main_fr "\def\langdir{chapters_fr}\input{main.tex}"' main.tex

clean:
	latexmk -C
	rm -f main_*.pdf main_*.aux main_*.log main_*.out main_*.toc main_*.fls main_*.fdb_latexmk main_*.synctex.gz