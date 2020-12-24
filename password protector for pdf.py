from PyPDF2 import PdfFileReader, PdfFileWriter
print('''    Welcome to the password protector for pdf 
                                          •••by Harinath''' )
pdfwriter=PdfFileWriter()
a=input("Enter pdf location :")
name= input("Enter pdf name without extension : ")
pdf= PdfFileReader(a+name+".pdf")
for pagenum in range(pdf.numPages):
	pdfwriter.addPage(pdf.getPage(pagenum))
passw=input("Enter the password you want :")
print('please wait..')
pdfwriter.encrypt(passw)
with open (a+name+" (new).pdf",'wb') as f:
	pdfwriter.write(f)
	
	f.close()
print("Check the folder. New pdf has been created and encrypted")
