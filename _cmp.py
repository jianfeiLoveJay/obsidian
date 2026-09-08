import pdfplumber, sys
files = sys.argv[1:]
for f in files:
    try:
        with pdfplumber.open(f) as pdf:
            print("FILE:", f, "| pages:", len(pdf.pages))
            t = pdf.pages[0].extract_text() or ""
            print(t[:700])
            print("======")
    except Exception as e:
        print("ERR", f, e)
