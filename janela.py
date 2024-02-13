import tkinter
import customtkinter

janela = tkinter.Tk()
janela.geometry("400x200")
janela.title("teste")


def botao():
    print('botão apertado')
    
#Estilizando o botão com o CustomTkinter

botao = customtkinter.CTkButton(master=janela, corner_radius=10, command=botao, text='Entrar')
botao.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

janela.update()
janela.mainloop()