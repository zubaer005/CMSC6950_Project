report.pdf: report.tex task1.csv monthly.png locations.png
	latexmk -pdf

locations.png : argo_region.py
	python3 argo_region.py
    
monthly.png: makeimage.py
	python3 makeimage.py
    
task1.csv: argo_region.py
	python3 argo_region.py
	python3 makedata.py
    
clean:
	rm *.csv
	latexmk -c

.PHONY : clean

deepclean:
	rm *.png
	latexmk -c
	rm *.pdf

.PHONY : deepclean

pdfclean:
	rm *.pdf

.PHONY : pdfclean