from tkinter import *
import random

root = Tk()
root.title("Quer namorar comigo?")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg= "#F0F0F0")

def move_Button(event):
    x = random.randint(50,350) #Gera uma nova posicao do x aleatoria entre 50 e 350
    y = random.randint(50,150) #Gera uma nova posicao do y aleatoria entre 50 e 150

#Verificar se a nova posicao de x e y nao colidem com o botao SIM 
    if(x < sim_button.winfo_x() - 50 or x > sim_button.winfo_x() + 50) or (y < sim_button.winfo_y() - 50 or y > sim_button.winfo_y() + 50):
        nao_button.place(x=x, y=y) # Posicionar o botao nao na nova posicao

def show_response(response):
    if response == "sim":    
        label_response.config(text = "Voce disse SIM!", fg="#32CD32")
    elif response == "nao":
         label_response.config(text="Voce disse NAO!", fg="#FF6347")

sim_button = Button(root, text="SIM", width=10, command=lambda:show_response("sim"))
nao_button = Button(root, text="NAO", width=10, command=lambda:show_response("nao"))

sim_button.configure(bg='#32CD32', fg='#FFFFFF', font=('Helvetica',12))
nao_button.configure(bg='#FF6347', fg='#FFFFFF', font=('Helvetica',12))

label_question = Label(root, text="Quer namorar comigo?", font=('Helvetica', 14), bg=("#F0F0F0"))
label_question = Label(root, text="", font=('Helvetica', 14), bg=("#F0F0F0"))
sim_button.place(x=100, y=75)
nao_button.place(x=250, y=75)
label_question.place(x=50, y=20)
label_question.place(x= 120, y=130)

nao_button.bind("<Motion>", move_Button)

root.mainloop()
