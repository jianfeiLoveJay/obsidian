import pdfplumber,sys
with pdfplumber.open(sys.argv[1]) as pdf:
    print("pages:",len(pdf.pages))
    print((pdf.pages[0].extract_text() or "")[:900])
