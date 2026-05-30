PYTHON ?= python3
PDF_MANIFEST ?= pdf/manifest.json
PDF_HTML ?= public/pdf/book.html
PDF_OUTPUT ?= public/pdf/documentation.pdf

.PHONY: pdf pdf-html clean

pdf:
	$(PYTHON) scripts/build_pdf.py --manifest $(PDF_MANIFEST) --html $(PDF_HTML) --pdf $(PDF_OUTPUT)

pdf-html:
	$(PYTHON) scripts/build_pdf.py --manifest $(PDF_MANIFEST) --html $(PDF_HTML) --pdf $(PDF_OUTPUT) --html-only

clean:
	rm -rf public resources/_gen .hugo_build.lock
