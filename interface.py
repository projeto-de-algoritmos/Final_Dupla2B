from tkinter import *
    

app = Tk()
app.title("distancia Valparaiso Ceilândia")
app.geometry("800x600")
app.configure(background="#31c6f7")
# app.widget1 = Frame(master)
# app.widget1.pack()
msg1 = Label(app, text="Mostrar todos os caminhos:",background="#008",font=100)
msg1["font"] = ("Verdana", "10", "italic", "bold")

msg2 = Label(app, text="Mostrar melhor caminho:",background="#008",font=100)
msg2["font"] = ("Verdana", "10", "italic", "bold")

msg3 = Label(app, text="Inserir engarrafamento:",background="#008",font=100)
msg3["font"] = ("Verdana", "10", "italic", "bold")

msg4 = Label(app, text="Abrir o maps com melhor caminho:",background="#008",font=100)
msg4["font"] = ("Verdana", "10", "italic", "bold")

# app.msg.pack ()
btn1 = Button(app, text="Mostrar",background="#C4C4C4")
btn2 = Button(app, text="Mostrar",background="#C4C4C4")
btn3 = Button(app, text="Inserir",background="#C4C4C4")
btn4 = Button(app, text="Abrir",background="#C4C4C4")

msg1.place(x =10, y=10, width=300, height=40)
msg2.place(x =10, y=160, width=300, height=40)
msg3.place(x =10, y=310, width=300, height=40)
msg4.place(x =10, y=500, width=350, height=40)

btn1.place(x =50, y=70, width=140, height=37)
btn2.place(x =50, y=220, width=140, height=37)
btn3.place(x =50, y=370, width=140, height=37)
btn4.place(x =50, y=550, width=140, height=37)

app.mainloop()