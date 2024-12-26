# conversor_binario

import tkinter as tk
from tkinter import messagebox

def converter_binario():
    try:
        numero = int(entry.get())  # Obtém o número digitado pelo usuário
        binario = bin(numero)[2:]  # Converte o número para binário e remove o prefixo '0b'
        messagebox.showinfo("Resultado", f"O número {numero} em binário é {binario}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número inteiro válido.")

root = tk.Tk()
root.title("Conversor Binário")

tk.Label(root, text="Digite um número:").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Converter", command=converter_binario).pack()

root.mainloop()
