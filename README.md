from tkinter import *
import random

root = Tk()
root.title("Quer namorar comigo?")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg="#F0F0F0")

# Função para mover o botão "não" e verificar a colisão
def move_Button(event):
    # Gera novas posições aleatórias para o botão "não"
    x = random.randint(50, 350)
    y = random.randint(50, 150)

    # Verifica se a nova posição do botão "não" colide com o botão "SIM"
    while (x > sim_button.winfo_x() - 50 and x < sim_button.winfo_x() + 50) and \
          (y > sim_button.winfo_y() - 50 and y < sim_button.winfo_y() + 50):
        # Se colidir, gera novas posições
        x = random.randint(50, 350)
        y = random.randint(50, 150)

    # Posiciona o botão "não" na nova posição
    nao_button.place(x=x, y=y)

# Função para mostrar a resposta
def show_response(response):
    if response == "sim":    
        label_response.config(text="Você disse SIM!", fg="#32CD32")
    elif response == "nao":
        label_response.config(text="Você disse NÃO!", fg="#FF6347")

# Criação dos botões e label
sim_button = Button(root, text="SIM", width=10, command=lambda: show_response("sim"))
nao_button = Button(root, text="NÃO", width=10, command=lambda: show_response("nao"))
label_response = Label(root, text="", font=('Helvetica', 12), bg="#F0F0F0")

# Configuração dos botões e label
sim_button.configure(bg='#32CD32', fg='#FFFFFF', font=('Helvetica', 12))
nao_button.configure(bg='#FF6347', fg='#FFFFFF', font=('Helvetica', 12))

# Criando os widgets na tela
label_question = Label(root, text="Quer namorar comigo?", font=('Helvetica', 14), bg="#F0F0F0")
label_question.place(x=120, y=20)
sim_button.place(x=100, y=75)
nao_button.place(x=250, y=75)
label_response.place(x=120, y=130)

# Bind para mover o botão "não"
nao_button.bind("<Motion>", move_Button)

root.mainloop()
