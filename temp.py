from tkinter import *
root=Tk()

root.title("addition")
root.geometry("400x200")

result=Label(root)

def add():
    r=7+3
    result["text"]=r
    
btn=Button(root,text="add",command=add)   
btn.pack()
result.pack() 

def sub():
    k=7-2
    result["text"]=k
    
btn2=Button(root,text="sub",command=sub)    
btn2.pack()
result.pack()
    
        

root.mainloop()


