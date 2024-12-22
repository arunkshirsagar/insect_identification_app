from innovations.colordescriptor import ColorDescriptor
from innovations.searcher import Searcher
import cv2
import urllib.request as urllib2

from tkinter import *
from PIL import ImageTk,Image,ImageFilter,ImageOps
from tkinter import filedialog
from tkinter import messagebox
import cv2
from urllib.request import Request,urlopen
import numpy as np
import webbrowser



#-------------------------------------Root------------------------------------------------#

root=Tk()

root.title('Insect Identifier')

root.iconbitmap('insect_animal.ico')

#root.geometry("600x500")

#set window color
root.configure(bg='#31F097')

#Title
#✼❁✼❁✼❁
title=Label(root,text='꧁꧁꧁ Insect Identifier ꧂꧂꧂',font=('Algerian',25,'bold'),fg='green',bg='white')
title.grid(row=0,column=0,columnspan=5,sticky=W+E)

#----------------------------------Button functions----------------------------------------#
def ok():
    l=''
    active.delete(0,END)
    active3.delete(0,END)

def capture():
    camera = cv2.VideoCapture(0)
    i = 0
    while i < 1:
        #input('Press Enter to capture')
        return_value, image = camera.read()
        cv2.imwrite('test_photo.jpg', image)
        i += 1
    del(camera)
    cv2.imshow('Captured Image',image)

    # Destroy all the windows
    #cv2.destroyAllWindows()

def match(img):
    def browser(l):
        if l=='':
            
            messagebox.showerror(title='Insect Identifier',message='Invalid Image!')
            
        else:
            webbrowser.open_new(l)
   

    cd = ColorDescriptor((8, 12, 3))
    query = img
    features = cd.describe(query)
    searcher = Searcher('index.csv')
    results = searcher.search(features)
    
    results=results[0:1]
    print(results)

    out=cv2.imread(results[0][1])

    print(results[0][1])
    if results[0][0]>=7:
        messagebox.showerror(title='Invalid Image',message='Please give valid Image!')
        active.insert(0,'Invalid Image')
        active3.insert(0,'Invalid Image')
        return -1
        
    
    elif results[0][1]=='dataset\\1.jpg':
        l='https://www.britannica.com/science/pupa'
        print(l)
        #webUrl = urllib2.urlopen("https://www.britannica.com/science/pupa")
        active.insert(0,l)
        active3.insert(0,'Pupa')
        
    elif  results[0][1]=='dataset\\2.jpg':
         l='https://en.m.wikipedia.org/wiki/Cnaphalocrocis_medinalis '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Cnaphalocrocis Medinalis')
         
    elif results[0][1]=='dataset\\3.jpg':
         l='https://en.m.wikipedia.org/wiki/Caterpillar '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Caterpillar')
         
    elif results[0][1]=='dataset\\4.jpg':
         l='https://en.m.wikipedia.org/wiki/Cnaphalocrocis_medinalis '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Cnaphalocrocis Medinalis')
         
    elif results[0][1]=='dataset\\5.jpg':
         l='https://en.m.wikipedia.org/wiki/Cnaphalocrocis_medinalis '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Cnaphalocrocis Medinalis')
         
    elif results[0][1]=='dataset\\6.jpg':
         l='https://en.m.wikipedia.org/wiki/Cnaphalocrocis_medinalis '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Cnaphalocrocis Medinalis')
         
    elif results[0][1]=='dataset\\7.jpg':
         l='https://en.m.wikipedia.org/wiki/Cnaphalocrocis_medinalis '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Cnaphalocrocis Medinalis')
         
    elif results[0][1]=='dataset\\8.jpg':
         l='https://en.m.wikipedia.org/wiki/Caterpillar '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Caterpillar')
         
    elif results[0][1]=='dataset\\9.jpg':
         l='https://en.m.wikipedia.org/wiki/Cnaphalocrocis_medinalis '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Cnaphalocrocis Medinalis')
         
    elif results[0][1]=='dataset\\10.jpg':
         l='https://en.m.wikipedia.org/wiki/Cnaphalocrocis_medinalis '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Cnaphalocrocis Medinalis')
         
    elif results[0][1]=='dataset\\11.jpg':
         l='https://en.m.wikipedia.org/wiki/Cnaphalocrocis_medinalis '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Cnaphalocrocis Medinalis')
         
    elif results[0][1]=='dataset\\12.jpg':
         l='https://en.m.wikipedia.org/wiki/Diatraea_saccharalis  '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Diatraea Saccharalis')
         
    elif results[0][1]=='dataset\\13.jpg':
         l='https://es.m.wikipedia.org/wiki/Diloboderus_abderus'
         print(l)
         active.insert(0,l)
         active3.insert(0,'Diloboderus Abderus')
         
    elif results[0][1]=='dataset\\14.jpg':
         l='https://en.m.wikipedia.org/wiki/Diatraea_saccharalis'
         print(l)
         active.insert(0,l)
         active3.insert(0,'Diatraea Saccharalis')
         

    elif results[0][1]=='dataset\\15.jpg':
         l='https://en.m.wikipedia.org/wiki/Neocurtilla_hexadactyla'
         print(l)
         active.insert(0,l)
         active3.insert(0,'Neocurtilla Hexadactyla')
         

    elif results[0][1]=='dataset\\16.jpg':
         l='https://en.m.wikipedia.org/wiki/Neocurtilla_hexadactyla'
         print(l)
         active.insert(0,l)
         active3.insert(0,'Neocurtilla Hexadactyla')
         
    elif results[0][1]=='dataset\\17.jpg':
         l='https://en.m.wikipedia.org/wiki/Neocurtilla_hexadactyla'
         print(l)
         active.insert(0,l)
         active3.insert(0,'Neocurtilla Hexadactyla')
         
    elif results[0][1]=='dataset\\17.jpg':
         l='https://en.m.wikipedia.org/wiki/Neocurtilla_hexadactyla'
         print(l)
         active.insert(0,l)
         active3.insert(0,'Neocurtilla Hexadactyla')
         
    elif results[0][1]=='dataset\\18.jpg':
         l='http://en.m.wikipedia.org/wiki/Leptotrombidium '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Leptotrombidium')

    elif results[0][1]=='dataset\\19.jpg':
         l='http://en.m.wikipedia.org/wiki/Leptotrombidium '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Leptotrombidium')
         
    elif results[0][1]=='dataset\\20.jpg':
         l='http://en.m.wikipedia.org/wiki/Leptotrombidium '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Leptotrombidium')
         
    elif results[0][1]=='dataset\\21.jpg':
         l='http://en.m.wikipedia.org/wiki/Leptotrombidium '
         print(l)
         active.insert(0,l)
         active3.insert(0,'Leptotrombidium')
         
    else:
         l='Invalid insect'
         print(l)
         messagebox.showerror(title='Invalid Image',message='Please give valid Image!')
         active.insert(0,l)
         active3.insert(0,'Invalid Insect')
    
    cv2.imshow('Matched Image',out)
    butn3=Button(root,text='Open in Browser',fg='yellow',bg='black',width=30)
    butn3.grid(row=16,column=1,pady=5)
    butn3.bind("<Button-1>", lambda e: browser(l))
    

    
    # Display the resulting frame
    # When everything done, release the capture
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(results)
    
def open():
    root.filename=filedialog.askopenfilename(initialdir='D:\BE Project\Insects',title='Select a file',filetypes=(('jpg files','*.jpg'),('all files','*.*')))
    print(root.filename)
    frame=cv2.imread(root.filename)
    cv2.imshow('Input',frame)
   
    match(frame)






#---------------------------------------Buttons and Labels--------------------------------------#

i='images.png'
j='insect.png'
l=0
a=(Image.open(i).resize((100,100)))
b=ImageTk.PhotoImage(a)


my_label=Label(image=b)
my_label.grid(row=3,column=0,padx=30)

ab=(Image.open(j).resize((400,400)))
bb=ImageTk.PhotoImage(ab)


my_labela=Label(image=bb)
my_labela.grid(row=3,column=1,padx=30,pady=20)

butn3=Button(root,text='Capture',fg='yellow',bg='black',width=30,command=capture)
butn3.grid(row=7,column=1,pady=5)


butn1=Button(root,text='Choose Image',fg='yellow',bg='black',width=30,command=open)
butn1.grid(row=9,column=1,pady=5)


butn2=Button(root,text='OK',fg='yellow',bg='black',width=30,command=ok)
butn2.grid(row=11,column=1,pady=5)

active2=Label(root,text='          Name of insect :',font=('times 16',16,'bold'),fg='red',bg='#31F097')
active2.grid(row=12,column=0)

active3=Entry(root,width=40,fg='red',font='times 12')
active3.grid(row=12,column=1,pady=5)


activel=Label(root,text='          Link :',font=('times 16',16,'bold'),fg='red',bg="#31F097")
activel.grid(row=15,column=0)

active=Entry(root,width=40,fg='red',font='times 12')
active.grid(row=15,column=1,pady=5)



root.mainloop()




























