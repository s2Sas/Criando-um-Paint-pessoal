from tkinter import *
from tkinter import ttk

dic_de_cores = {
    "Sem preenchimento": "",
    "Preto": "black",
    "Branco": "white",
    "Vermelho": "red",
    "Verde": "green",
    "Azul": "blue",
    "Cor de burro quando foge":"#6F752F" 
}


# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    cor_selecionada = cores_var.get() #pega a cor selecionada no menu

    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_selecionada)
    elif tipo_figura_var.get() == "Rabisco":
        figura_nova = ("rabisco", [(event.x, event.y)], cor_selecionada)
    elif tipo_figura_var.get() == "Oval":
        figura_nova = ("Oval", (event.x, event.y, event.x, event.y), cor_selecionada) #aqui estamos adicionando a opção oval igual fizemos com as outras formas
    elif tipo_figura_var.get() == "Retângulo":
        figura_nova = ("Retângulo", (event.x, event.y, event.x, event.y), cor_selecionada)
    elif tipo_figura_var.get() == "Quadrado":
        figura_nova = ("Quadrado", (event.x, event.y, event.x, event.y), cor_selecionada)
    else : # msm coisa de fazer tipo_figura_var.get() == "Circulo"
        figura_nova = ("Circulo", (event.x, event.y, event.x, event.y), cor_selecionada)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    cor_atual = cores_var.get() #pega a cor selecionada

    #aq temos que adicionar um novo parametro em todos, cor_atual
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
        figura_nova = ("rabisco", figura_nova[1], cor_atual)
    elif figura_nova[0] == "linha":
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_atual)
    elif figura_nova[0] == "Circulo":
        figura_nova = ("Circulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_atual)
    elif figura_nova[0] == "Oval":
        figura_nova = ("Oval", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_atual)
    elif figura_nova[0] == "Retângulo":
        figura_nova = ("Retângulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_atual)
    elif figura_nova[0] == "Quadrado": #aq temos que fazer ter o msm tamanho em todos os lados,
            x_inicio, y_inicio = figura_nova[1][0], figura_nova[1][1]

            dist_x = event.x- x_inicio #aq descobrimos o tamanho dos lados
            dist_y = event.y - y_inicio
            tamanho = max(abs(dist_x), abs(dist_y)) #aq pegamos o maior lado
            novo_x = x_inicio + tamanho * (1 if dist_x >= 0 else -1) #aq garantimos q o quadrado vai ser desenhado
            novo_y = y_inicio + tamanho * (1 if dist_y >= 0 else -1) #na posição certa
            figura_nova = ("Quadrado", (x_inicio, y_inicio, novo_x, novo_y), cor_atual)
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig, values, cor_salva in figuras:
        cor_tk = dic_de_cores.get(cor_salva, "black")

        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill=cor_tk if cor_tk != "" else "black")
        elif fig == "Circulo":
            raio = ((values[0]- values[2])**2+ (values[1] - values[3])**2) ** 0.5
            canvas.create_oval(values[0]- raio, values[1]- raio, values[0]+ raio, values[1]+ raio, fill=cor_tk, outline=cor_tk if cor_tk != "" else "black")
        elif fig == "Oval":
            canvas.create_oval(values[0], values[1], values[2], values[3], fill=cor_tk, outline=cor_tk if cor_tk != "" else "black")
        elif fig == "Retângulo":
            canvas.create_rectangle(values[0], values[1], values[2], values[3], fill=cor_tk, outline=cor_tk if cor_tk != "" else "black")
        elif fig == "Quadrado":
            canvas.create_rectangle(values[0], values[1], values[2], values[3], fill=cor_tk, outline=cor_tk if cor_tk != "" else "black")
        else : # fig == "rabisco"
            canvas.create_line(values, fill=cor_tk if cor_tk != "" else "black")

def desenhar_figura_nova():
    fig, values, cor_salva = figura_nova

    cor_tk = dic_de_cores.get(cor_salva, "black")
    
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2), fill=cor_tk if cor_tk != "" else "black")
    elif fig == "Circulo":
        raio = ((values[0]- values[2])**2+ (values[1] - values[3])**2) ** 0.5
        canvas.create_oval((values[0]- raio, values[1]- raio, values[0]+ raio, values[1]+ raio), dash=(4,2),fill=cor_tk, outline=cor_tk  if cor_tk != "" else "black")
    elif fig == "Oval":
        canvas.create_oval(values[0], values[1], values[2], values[3], dash=(4, 2), fill=cor_tk, outline=cor_tk if cor_tk != "" else "black")
    elif fig == "Retângulo":
        canvas.create_rectangle(values[0], values[1], values[2], values[3], dash= (4,2), fill=cor_tk, outline=cor_tk if cor_tk != "" else "black")
    elif fig == "Quadrado":
        canvas.create_rectangle(values[0], values[1], values[2], values[3], dash= (4,2), fill=cor_tk, outline=cor_tk if cor_tk != "" else "black")
    else : # fig == "rabisco"
        canvas.create_line(values, dash=(4, 2), fill=cor_tk if cor_tk != "" else "black")

def incompleta(figura):
    fig, values, cor = figura
    if fig == "rabisco":
        return len(values) <= 1
    else :
        return (values[0], values[1]) == (values[2], values[3]) #aq é melho inverter do q ficar dando or em todas as formas




#******* MAIN *******#

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

root = Tk() #isso aq é o "nome" da janela, então se quiserem mudar algo na janela, chamem esse
frame = Frame(root)
root.title("Meu Paint")
root.geometry("800x650")
#root.configure(background="lightgray") se quiser trocar a cor do fundo da janela

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
#label = ttk.Label(frame,  text='Minha nova arte')
#label.grid(column=0, row=0, sticky=W, **paddings)

#*****Menu de Figuras*****#
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (já vou pegar o embalo e fazer quadrado tb)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', "Circulo", "Oval", "Retângulo", "Quadrado") #aq linha é repetida pq é exigido deixar a opção padrão duas vezes
label_figura = ttk.Label(frame, text="Tipo de figura")
label_figura.grid(column=1, row=0, sticky=W, **paddings)
option_menu.grid(column=1, row=1, sticky=W, **paddings)

#*****Menu de cores de contorno*****#
contorno_var = StringVar(root) #guarda a cor selecionada
contorno_var.set("Preto") #cor padrão
option_menu_contorno = ttk.OptionMenu(frame, contorno_var,
                                      "Preto", "Preto", "Vermelho", "Verde", "Azul", "Amarelo", "Rosa", "Cor de burro quando foge")
label_contorno = ttk.Label(frame, text="Cor do contorno")
label_contorno.grid(column=2, row=0, sticky=W, **paddings)
option_menu_contorno.grid(column=2, row=1, sticky=W, **paddings)

#*****Menu de cores de preenchimento*****#
cores_var = StringVar(root) #guarda a cor selecionada
cores_var.set("Preto") #cor padrão para começar
option_menu_cores = ttk.OptionMenu(frame, cores_var,
                                   "Sem preenchimento", "Sem preenchimento", "Preto", "Vermelho", "Verde", "Azul", "Amarelo", "Rosa", "Cor de burro quando foge")
label_menu_cores = ttk.Label(frame, text="Cor de preenchimento")
label_menu_cores.grid(column=3, row=0, sticky=W, **paddings)
option_menu_cores.grid(column=3, row=1, sticky=W, **paddings)

#*******************************************#
# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=2, columnspan=4, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()