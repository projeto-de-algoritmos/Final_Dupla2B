from tkinter import *  
import dijkstra
import engarrafamento
import rota
import mostra_rotas

app = Tk()
app.title("distancia Valparaiso Ceilândia")
app.geometry("800x600")
app.configure(background="#31c6f7")

msg1 = Label(app, text="Mostrar todos os caminhos:",background="#31c6f7",font=100)
msg1["font"] = ("Verdana", "10", "italic", "bold")

msg2 = Label(app, text="Mostrar melhor caminho:",background="#31c6f7",font=100)
msg2["font"] = ("Verdana", "10", "italic", "bold")

msg3 = Label(app, text="Inserir engarrafamento:",background="#31c6f7",font=100)
msg3["font"] = ("Verdana", "10", "italic", "bold")

msg4 = Label(app, text="Abrir o maps com melhor caminho:",background="#31c6f7",font=100)
msg4["font"] = ("Verdana", "10", "italic", "bold")

label1 = Entry(app)
label2 = Entry(app)
label3 = Entry(app)

def teste():
    print(label1.get())
    print(label2.get())
    print(label3.get())

btn1 = Button(app, text="Mostrar",background="#C4C4C4") 
btn2 = Button(app, text="Mostrar",background="#C4C4C4")
btn3 = Button( text="Inserir",background="#C4C4C4", command=teste)
btn4 = Button(app, text="Abrir",background="#C4C4C4")

imagem = PhotoImage(file="valparaiso_ceilandia.png")
panel = Label(app, image = imagem )
panel.place(x=280, y=10)


label1.place(x =10, y=370, width=120, height=37)
label2.place(x =140, y=370, width=120, height=37)
label3.place(x =270, y=370, width=120, height=37)

msg1.place(x =10, y=10, width=300, height=40)
msg2.place(x =10, y=160, width=300, height=40)
msg3.place(x =10, y=310, width=300, height=40)
msg4.place(x =10, y=500, width=350, height=40)

btn1.place(x =50, y=70, width=140, height=37)
btn2.place(x =50, y=220, width=140, height=37)
btn3.place(x =130, y=450, width=140, height=37)
btn4.place(x =50, y=550, width=140, height=37)

app.mainloop()