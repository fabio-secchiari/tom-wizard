# Makefile: si ferma al primo errore LaTeX (i riferimenti non definiti li risolve latexmk rieseguendo)

LATEXMK = latexmk -pdf -interaction=nonstopmode -file-line-error -halt-on-error

.PHONY: all en de fr clean

all: en de fr

en:
	$(LATEXMK) main_en.tex

de:
	$(LATEXMK) main_de.tex

fr:
	$(LATEXMK) main_fr.tex

clean:
	latexmk -C main_en.tex main_de.tex main_fr.tex || true
	-del *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz 2>nul || true