#convert your PDFs into audiobooks
import tkinter
import PyPDF2
import pyttsx3

#function to take input
def take_inp():
    string=text_field.get()
    num=text_field2.get()
    try:
        num=int(num)
        open_pdf=open(string,'rb')
        pdfobj=PyPDF2.PdfFileReader(open_pdf)
        read(pdfobj,num)
        open_pdf.close()
    except:
        raise TypeError("You may have entered wrong path or page number that does not exist in the pdf")

#function to extract text
def read(obj,page_num):
    text=obj.getPage(page_num).extractText()
    speak(text)
    
#function to speak   
def speak(audio):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)
    engine.say(audio)
    engine.runAndWait()

#function to end the program
def end_of():
    exit()
    
root=tkinter.Tk()
root.title("AudioBooks")
root.geometry("400x400")
lable=tkinter.Label(root,text="Turn your pdfs into audiobook")
lable.pack()
l1=tkinter.Label(root,text="Enter the path of text document")
l1.pack()
text_field=tkinter.Entry(root)
text_field.place(x=100,y=40,width=200,height=25)
l2=tkinter.Label(root,text="Enter the page number")
l2.place(x=100,y=80)
text_field2=tkinter.Entry(root)
text_field2.place(x=100,y=100,width=60,height=25)
button=tkinter.Button(root,text="Start audiobook",command=take_inp)
button.place(x=100,y=140)
button2=tkinter.Button(root,text="Stop audiobook",command=end_of)
button2.place(x=200,y=140)
root.mainloop()
