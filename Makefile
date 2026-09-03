# Makefile tollerante agli undefined references

LATEXMK = latexmk -pdf -interaction=nonstopmode -file-line-error -f

.PHONY: all en de fr clean

all: en de fr

en:
	-$(LATEXMK) main_en.tex

de:
	-$(LATEXMK) main_de.tex

fr:
	-$(LATEXMK) main_fr.tex

clean:
	latexmk -C main_en.tex main_de.tex main_fr.tex || true
	-del *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz 2>nul || true