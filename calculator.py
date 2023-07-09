from tkinter import *
import ast
root=Tk()
root.title("CALCULATOR")
#root.geometry('400x300')
i=0
def get_number(num):
    global i
    display.insert(i,num)
    i+=1
def get_operation(operator):
    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length
def clear_all():
    display.delete(0,END)
def calculate():
    string=display.get()
    try:
        node=ast.parse(string,mode="eval")
        result=eval(compile(node,'<string>','eval'))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
def delete_():
    global i
    string=display.get()
    if len(string):
        string=string[:-1]
        clear_all()
        display.insert(0,string)
    else:
        clear_all()
        display.insert(0,"")







display=Entry(root,bg='black',fg='white',width=16)
display.grid(row=2,columnspan=12)
numbers=[1,2,3,4,5,6,7,8,9]
counter=0
for x in range(3):
    for y in range(3):
        button_text=numbers[counter]
        button=Button(root,bg='blue',fg='blue',text=button_text,width=2,height=2,command=lambda text=button_text:get_number(text))
        button.grid(row=x+3,column=y+1)
        counter+=1

button=Button(root,text="0",fg='blue',width=2,height=2,command=lambda :get_number(0))
button.grid(row=6,column=2)
count=0
operations=['+','-',"*","/","*3.14","%","(","**",")","**2","."]

for x in range(4):
    for y in range(3):
        if(count<len(operations)):
            button=Button(root,bg='blue',fg='red',text=operations[count],width=2,height=2,command=lambda text=operations[count]:get_operation(text))
            count+=1
            button.grid(row=x+3,column=y+6)
Button(root,text="AC",width=2,height=2,command=clear_all).grid(row=6,column=1)
Button(root,text="=",width=2,height=2,command=calculate).grid(row=6,column=6)
Button(root,text="<-",width=2,height=2,command=delete_).grid(row=6,column=7)
root.mainloop()