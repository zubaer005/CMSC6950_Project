default: report.pdf
.PHONY : default

report.pdf: report.tex
	latexmk -pdf
    
task1.csv: argo_region.py
	python3 argo_region.py

clean:
	rm *.csv
	rm *.png