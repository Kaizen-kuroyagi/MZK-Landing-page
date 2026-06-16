from PyPDF2 import PdfReader

reader = PdfReader('Resume MK.pdf')
text = '\n'.join((page.extract_text() or '') for page in reader.pages)
print(text[:4000])
with open('resume_text.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print('WROTE', len(text), 'chars')
