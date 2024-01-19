from tkinter import*
from tkinter import Tk, ttk
from tkinter import messagebox

#cores
cor0 = "#f0f3f5"  #black
cor1 = "#feffff"  #white
cor2 = "#3fb5a3"  #green
cor3 = "#38576b"  #value
cor4 = "#403d3d"  #letters


#criando janela
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background = cor1)
janela.resizable(width=FALSE, height=FALSE)

#dividindo a janela
frame_cima = Frame(janela, width=310, height=50, bg=cor1, relief='flat')
frame_cima.grid(row=0,column=0,pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=cor1, relief='flat')
frame_baixo.grid(row=1,column=0,pady=1, padx=0, sticky=NSEW)

#config frame cima
l_nome = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'),bg=cor1, fg=cor4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'),bg=cor2, fg=cor4)
l_linha.place(x=10, y=45)


credenciais = ['joao', '123456789']

#funcao verificar senha
def verificar_senha():
    nome = e_nome.get()
    senha = e_senha.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem-vindo Admin!')
    elif credenciais[0] == nome and credenciais[1]==senha:
        messagebox.showinfo('Login', 'Seja bem-vindo de volta! ' + credenciais[0])

        for widget in frame_baixo.winfo_children():
            widget.destroy()
        
        for widget in frame_cima.winfo_children():
            widget.destroy()
            
    else:
        messagebox.showwarning('Erro', 'Verifique o nome e a senha!')



#funcao apos verificacao
def nova_janela():
    l_nome = Label(frame_cima, text='Usuário: ' +credenciais[0], anchor=NE, font=('Ivy 20'),bg=cor1, fg=cor4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'),bg=cor2, fg=cor4)
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_baixo, text='Seja bem-vindo ' +credenciais[0], anchor=NE, font=('Ivy 20'),bg=cor1, fg=cor4)
    l_nome.place(x=5, y=105)
    

        



#config frame baixo
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 15'),bg=cor1, fg=cor4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)

l_senha = Label(frame_baixo, text='Senha *', anchor=NW, font=('Ivy 15'),bg=cor1, fg=cor4)
l_senha.place(x=10, y=95)
e_senha = Entry(frame_baixo, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
e_senha.place(x=14, y=130)


b_confirm = Button(frame_baixo, command= verificar_senha, text='Entrar', width=39, height=2, font=('Ivy 8 bold'),bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_confirm.place(x=15, y=180)


janela.mainloop()

