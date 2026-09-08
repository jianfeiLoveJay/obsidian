import pdfplumber,sys
with pdfplumber.open(sys.argv[1]) as pdf:
    print("pages:",len(pdf.pages))
    for i in [0,1]:
        print("---PAGE",i+1,"---")
        print((pdf.pages[i].extract_text() or "")[:1200])
