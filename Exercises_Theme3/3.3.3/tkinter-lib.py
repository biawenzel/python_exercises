from tkinter import *
from PIL import ImageTk, Image

def funcClicar():
    print("Botão pressionado")


janelaPrincipal = Tk()
texto = Label(master=janelaPrincipal, text="Minha janela exibida")
texto.pack()

pic = ImageTk.PhotoImage(Image.open("tkinter-lib-img.jpg"))
logo = Label(master=janelaPrincipal, image=pic)
logo.pack()

botao = Button(master=janelaPrincipal, text='Clique', command=funcClicar)
botao.pack()

janelaPrincipal.mainloop()
