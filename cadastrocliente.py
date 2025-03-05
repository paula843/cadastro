import tkinter
from tkinter import ttk

def inserir_dados():
    nome = entrada_nome.get()
    sobrenome = entrada_sobrenome.get()
    titulo = caixa_titulo.get()
    idade = spinbox_idade.get()
    nacionalidade = caixa_nacionalidade.get()

    num_cursos = spinbox_cursos.get()
    num_semestres = spinbox_semestres.get()

    print("Nome:", nome, "Sobrenome:", sobrenome)
    print("Título:", titulo, "Idade:", idade, "Nacionalidade:", nacionalidade)
    print("Cursos concluídos:", num_cursos, "Semestres cursados:", num_semestres)
    print("------------------------------------------")

janela = tkinter.Tk()
janela.title("Formulário de Cadastro")

# Criando um quadro principal
quadro = tkinter.Frame(janela)
quadro.pack()

# Quadro de informações do usuário
quadro_info_usuario = tkinter.LabelFrame(quadro, text="Informações do Usuário")
quadro_info_usuario.grid(row=0, column=0)

label_nome = tkinter.Label(quadro_info_usuario, text="Nome:")
label_nome.grid(row=0, column=0)
label_sobrenome = tkinter.Label(quadro_info_usuario, text="Sobrenome:")
label_sobrenome.grid(row=0, column=1)

entrada_nome = tkinter.Entry(quadro_info_usuario)
entrada_sobrenome = tkinter.Entry(quadro_info_usuario)
entrada_nome.grid(row=1, column=0)
entrada_sobrenome.grid(row=1, column=1)

label_titulo = tkinter.Label(quadro_info_usuario, text="Título:")
caixa_titulo = ttk.Combobox(quadro_info_usuario, values=["", "Sr.", "Sra.", "Dr."])
label_titulo.grid(row=0, column=2)
caixa_titulo.grid(row=1, column=2)

label_idade = tkinter.Label(quadro_info_usuario, text="Idade:")
spinbox_idade = tkinter.Spinbox(quadro_info_usuario, from_=18, to=110)
label_idade.grid(row=2, column=0)
spinbox_idade.grid(row=3, column=0)

label_nacionalidade = tkinter.Label(quadro_info_usuario, text="Nacionalidade:")
caixa_nacionalidade = ttk.Combobox(quadro_info_usuario, values=["Brasil", "Portugal", "EUA", "Argentina", "Paraguai"])
label_nacionalidade.grid(row=2, column=1)
caixa_nacionalidade.grid(row=3, column=1)

for widget in quadro_info_usuario.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Quadro de cursos
quadro_cursos = tkinter.LabelFrame(quadro, text="Informações Acadêmicas")
quadro_cursos.grid(row=1, column=0, sticky="news", padx=20, pady=20)

label_registro = tkinter.Label(quadro_cursos, text="Status de Matrícula:")
check_registro = tkinter.Checkbutton(quadro_cursos, text="Atualmente Matriculado")
label_registro.grid(row=0, column=0)
check_registro.grid(row=1, column=0)

label_cursos = tkinter.Label(quadro_cursos, text="Cursos Concluídos:")
spinbox_cursos = tkinter.Spinbox(quadro_cursos, from_=0, to='infinity')
label_cursos.grid(row=0, column=1)
spinbox_cursos.grid(row=1, column=1)

label_semestres = tkinter.Label(quadro_cursos, text="Semestres Cursados:")
spinbox_semestres = tkinter.Spinbox(quadro_cursos, from_=0, to='infinity')
label_semestres.grid(row=0, column=2)
spinbox_semestres.grid(row=1, column=2)

for widget in quadro_cursos.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Quadro de termos e condições
quadro_termos = tkinter.LabelFrame(quadro, text="Termos e Condições")
quadro_termos.grid(row=2, column=0, sticky="news", padx=20, pady=20)

check_termos = tkinter.Checkbutton(quadro_termos, text="Aceito os termos e condições.")
check_termos.grid(row=0, column=0)

# Botão de envio
botao = tkinter.Button(quadro, text="Enviar Dados", command=inserir_dados)
botao.grid(row=3, column=0, sticky="news", padx=20, pady=20)

janela.mainloop()
