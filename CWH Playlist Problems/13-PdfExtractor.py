import PyPDF2
a=PyPDF2.PdfFileReader('trail.pdf')
str1=''
for i in range(10,12):
    str1+=a.getPage(i).extractText()
with open('text.txt','w',encoding='utf-8') as f:
    f.write(str1)