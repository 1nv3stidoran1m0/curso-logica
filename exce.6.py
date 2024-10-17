import tkinter as tk

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Clientes")

# Criar um rótulo para o título do menu
label = tk.Label(root, text="Cadastro de Clientes")
label.pack()

# Criar os botões das opções
button_sair = tk.Button(root, text="0 - Sair", command=root.quit)
button_incluir = tk.Button(root, text="1 - Incluir")
button_alterar = tk.Button(root, text="2 - Alterar")
button_excluir = tk.Button(root, text="3 - Excluir")
button_consultar = tk.Button(root, text="4 - Consultar")

# Posicionar os botões na janela
button_sair.pack()
button_incluir.pack()
button_alterar.pack()
button_excluir.pack()
button_consultar.pack()

# Iniciar o loop principal da aplicação
root.mainloop()
