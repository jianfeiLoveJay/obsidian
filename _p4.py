import pdfplumber,sys
with pdfplumber.open(sys.argv[1]) as pdf:
    t=pdf.pages[0].extract_text() or ""
    print(t[1200:2800])
