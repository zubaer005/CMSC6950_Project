default: report.pdf
.PHONY : default
    
report.pdf: report.tex
	latexmk -pdf

clean:
	rm *.csv
	rm *.png