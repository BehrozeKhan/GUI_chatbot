from tkinter import*
root=Tk()
root.title("Python GUI Chat Bot")

La=Label(root,text="Enter your question:" ).pack()
global c
c=Entry(root)
c.pack()

   
Ques=["Hello","How are you?","What is your name?","What's going on?"]
Ans=["Hi","I am Fine...","I am Python GUI chatbot","Everything is OK"]

def chat(event):
    l = len(Ques)
   
    for i in range(l):
        if c.get()==Ques[i]:
            La=Label(root,text=Ans[i]).pack()
       
       
       

c.bind("<Return>",chat)


mainloop()
