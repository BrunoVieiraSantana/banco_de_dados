# Bibliotecas para interface gráfica
import customtkinter
import tkinter.ttk as ttk
import tkinter
import re
from tkinter import *
from ttkwidgets.autocomplete import AutocompleteEntry

# Bibliotecas para importação de imagens
import os
from PIL import Image

# Bibliotecas para gráficos
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Importação dos códigos sql de um arquivo externo
from database import *


# Variaveis de controle
login=False
id_final = 0


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Nomear Janela e defir o tamanho
        self.title("Gerenciamento de Trânsito.py")
        self.geometry("800x600")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)



        # Carregar imagens utilizadas no projeto
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(52, 52))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home.png")), size=(27, 27))
        self.shield_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "shield-account.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "shield-account.png")), size=(27, 27))
        self.home_assistant_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home-assistant.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home-assistant.png")), size=(27, 27))
        self.home_search_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home-search.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home-search.png")), size=(27, 27))
        self.home_plus_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home-plus.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home-plus.png")), size=(25, 25))
        self.welcome_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "welcome.png")), size=(311, 243))

        

        # Barra de navegação lateral
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(7, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="""  Gerenciamento
de
Trânsito""", image=self.logo_image, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)


        # Botões barra de navegação lateral
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Visualizar",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.home_plus_image, anchor="w", command=self.frame_2_button_event)


        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Buscar",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.home_search_image, anchor="w", command=self.frame_3_button_event)


        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Gráficos",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.home_assistant_image, anchor="w", command=self.frame_4_button_event)


        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Administrar",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.shield_image, anchor="w", command=self.frame_5_button_event)


        self.frame_6_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Deslogar",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.shield_image, anchor="w", command=self.logout_event)



        # Home
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_label = customtkinter.CTkLabel(self.home_frame , text="Página de Login",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.home_frame_label.grid(row=0, pady=(90,5))
        self.home_frame_username_entry = customtkinter.CTkEntry(self.home_frame , width=200, placeholder_text="login")
        self.home_frame_username_entry.grid(row=1, pady=5)
        self.home_frame_password_entry = customtkinter.CTkEntry(self.home_frame , width=200, show="*", placeholder_text="password")
        self.home_frame_password_entry.grid(row=2, pady=5)
        self.home_frame_login_button = customtkinter.CTkButton(self.home_frame , text="Login", command=self.login_event, width=200)
        self.home_frame_login_button.grid(row=3, pady=5)
        self.home_frame_login_button = customtkinter.CTkButton(self.home_frame , text="Esqueceu sua senha?", command=self.login_event, width=200, fg_color="transparent")
        self.home_frame_login_button.grid(row=4, pady=5)
        self.home_frame_login_button = customtkinter.CTkButton(self.home_frame , text="Criar conta", command=self.login_event, width=200, fg_color="transparent")
        self.home_frame_login_button.grid(row=5, pady=5)



        # Visualizar
        self.second_frame = customtkinter.CTkTabview(self, corner_radius=20, border_width=5)
        self.second_frame.grid(row=1, column=0, padx=20, pady=10)
        self.second_frame.add("Motoristas")
        self.second_frame.add("Veiculos")
        self.second_frame.add("Multas")
        self.second_frame.tab("Motoristas").grid_columnconfigure(0, weight=1) 
        self.second_frame.tab("Veiculos").grid_columnconfigure(0, weight=1)
        self.second_frame.tab("Multas").grid_columnconfigure(0, weight=1)

        columns = ('id', 'nome', 'cpf', 'cnh')

        self.table_motorista = ttk.Treeview(master=self.second_frame.tab("Motoristas"),
                                columns=columns,
                                height=20,
                                selectmode='browse',
                                show='headings')

        self.table_motorista.column("#1", anchor="c", minwidth=50, width=50)
        self.table_motorista.column("#2", anchor="w", minwidth=165, width=165)
        self.table_motorista.column("#3", anchor="c", minwidth=120, width=120)
        self.table_motorista.column("#4", anchor="c", minwidth=120, width=120)

        self.table_motorista.heading('id', text='ID')
        self.table_motorista.heading('nome', text='Nome')
        self.table_motorista.heading('cpf', text='CPF')
        self.table_motorista.heading('cnh', text='CNH')
        self.table_motorista.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.table_motorista.bind('<Motion>', 'break')
        motoristas = verMotorista(con)
        for motorista in motoristas:
            self.table_motorista.insert('', tkinter.END, values=motorista)
        
        def display_selected_item_visualizar(a):
            selected_item = self.table_motorista.selection()[0]
            id = self.table_motorista.item(selected_item)['values'][0]
            print(f'O id selecionado é {id}')

        self.table_motorista.bind("<<TreeviewSelect>>", display_selected_item_visualizar)

        columns2 = ('id', 'placa', 'chassi', 'tipo', 'id_motorista')
        self.table_veiculos = ttk.Treeview(master=self.second_frame.tab("Veiculos"),
                                columns=columns2,
                                height=20,
                                selectmode='browse',
                                show='headings')

        self.table_veiculos.column("#1", anchor="c", minwidth=50, width=50)
        self.table_veiculos.column("#2", anchor="c", minwidth=100, width=100)
        self.table_veiculos.column("#3", anchor="c", minwidth=120, width=120)
        self.table_veiculos.column("#4", anchor="c", minwidth=120, width=120)
        self.table_veiculos.column("#5", anchor="c", minwidth=120, width=120)

        self.table_veiculos.heading('id', text='ID')
        self.table_veiculos.heading('placa', text='Placa')
        self.table_veiculos.heading('chassi', text='Chassi')
        self.table_veiculos.heading('tipo', text='Tipo')
        self.table_veiculos.heading('id_motorista', text='Motorista')
        self.table_veiculos.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.table_veiculos.bind('<Motion>', 'break')
        veiculos = vertodasTabelasVeiculos(con)
        for veiculo in veiculos:
            self.table_veiculos.insert('', tkinter.END, values=veiculo)


        columns3 = ('id_multa', 'valor', 'data', 'nome_motorista', 'placa_automovel')
        self.table_multas = ttk.Treeview(master=self.second_frame.tab("Multas"),
                                columns=columns3,
                                height=20,
                                selectmode='browse',
                                show='headings')

        self.table_multas.column("#1", anchor="c", minwidth=50, width=50)
        self.table_multas.column("#2", anchor="c", minwidth=100, width=100)
        self.table_multas.column("#3", anchor="c", minwidth=120, width=120)
        self.table_multas.column("#4", anchor="c", minwidth=120, width=120)
        self.table_multas.column("#5", anchor="c", minwidth=120, width=120)


        self.table_multas.heading('id_multa', text='Id Multa')
        self.table_multas.heading('valor', text='Valor')
        self.table_multas.heading('data', text='Data')
        self.table_multas.heading('nome_motorista', text='Motorista')
        self.table_multas.heading('placa_automovel', text='Placa')
        self.table_multas.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.table_multas.bind('<Motion>', 'break')
        multas = vertodasTabelas(con)
        for multa in multas:
            self.table_multas.insert('', tkinter.END, values=multa)


        # Buscar
        #self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame = customtkinter.CTkTabview(self, corner_radius=20, border_width=5)
        self.third_frame.grid(row=1, column=0, padx=20, pady=10)
        self.third_frame.add("Motoristas")
        self.third_frame.add("Veiculos")
        self.third_frame.add("Multas")
        self.third_frame.tab("Motoristas").grid_columnconfigure(0, weight=1) 
        self.third_frame.tab("Veiculos").grid_columnconfigure(0, weight=1)
        self.third_frame.tab("Multas").grid_columnconfigure(0, weight=1)


        # Buscar Motorista
        self.third_frame_label_search_motorista = customtkinter.CTkLabel(self.third_frame.tab("Motoristas") , text="Buscas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label_search_motorista.grid(row=0, column=0, padx=30, pady=(15, 15))
        self.third_frame_label_search_motorista = customtkinter.CTkLabel(self.third_frame.tab("Motoristas") , text="Realizar busca por Motoristas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label_search_motorista.grid(row=1, column=0, padx=30, pady=(15, 15))

        self.third_frame_entry_search_motorista = AutocompleteEntry(autocompleteList, self.third_frame.tab("Motoristas"), matchesFunction=matches)
        self.third_frame_entry_search_motorista.grid(row=2, column=0, columnspan=1, padx=(10, 0), pady=(10, 10), sticky="nsew")
        self.third_frame_button_search_motorista = customtkinter.CTkButton(self.third_frame.tab("Motoristas") , fg_color="transparent",command=self.button_search_motorista , border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.third_frame_button_search_motorista.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        columns_search_motorista = ('id', 'nome', 'cpf', 'cnh')
        self.third_frame_table_search_motorista = ttk.Treeview(master=self.third_frame.tab("Motoristas"),
                                columns=columns_search_motorista,
                                height=5,
                                selectmode='browse',
                                show='headings')
        self.third_frame_table_search_motorista.column("#1", anchor="c", minwidth=50, width=50)
        self.third_frame_table_search_motorista.column("#2", anchor="w", minwidth=165, width=165)
        self.third_frame_table_search_motorista.column("#3", anchor="c", minwidth=120, width=120)
        self.third_frame_table_search_motorista.column("#4", anchor="c", minwidth=120, width=120)
        self.third_frame_table_search_motorista.heading('id', text='ID')
        self.third_frame_table_search_motorista.heading('nome', text='Nome')
        self.third_frame_table_search_motorista.heading('cpf', text='CPF')
        self.third_frame_table_search_motorista.heading('cnh', text='CNH')
        self.third_frame_table_search_motorista.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.third_frame_table_search_motorista.bind('<Motion>', 'break')

        # Buscar Veiculo
        self.third_frame_label_search_veiculo = customtkinter.CTkLabel(self.third_frame.tab("Veiculos") , text="Buscas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label_search_veiculo.grid(row=0, column=0, padx=30, pady=(15, 15))
        self.third_frame_label_search_veiculo = customtkinter.CTkLabel(self.third_frame.tab("Veiculos") , text="Realizar busca por Veiculos",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label_search_veiculo.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.third_frame_entry_search_veiculo = customtkinter.CTkEntry(self.third_frame.tab("Veiculos") , placeholder_text="Placa ou Id")
        self.third_frame_entry_search_veiculo.grid(row=2, column=0, columnspan=1, padx=(10, 0), pady=(10, 10), sticky="nsew")
        self.third_frame_button_search_veiculo = customtkinter.CTkButton(self.third_frame.tab("Veiculos") ,command=self.button_search_veiculo, fg_color="transparent", border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.third_frame_button_search_veiculo.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        columns_search_veiculo = ('id', 'placa', 'chassi', 'tipo', 'id_motorista')
        self.third_frame_table_search_veiculo = ttk.Treeview(master=self.third_frame.tab("Veiculos"),
                                columns=columns_search_veiculo,
                                height=5,
                                selectmode='browse',
                                show='headings')

        self.third_frame_table_search_veiculo.column("#1", anchor="c", minwidth=50, width=50)
        self.third_frame_table_search_veiculo.column("#2", anchor="c", minwidth=100, width=100)
        self.third_frame_table_search_veiculo.column("#3", anchor="c", minwidth=120, width=120)
        self.third_frame_table_search_veiculo.column("#4", anchor="c", minwidth=120, width=120)
        self.third_frame_table_search_veiculo.column("#5", anchor="c", minwidth=120, width=120)

        self.third_frame_table_search_veiculo.heading('id', text='ID')
        self.third_frame_table_search_veiculo.heading('placa', text='Placa')
        self.third_frame_table_search_veiculo.heading('chassi', text='Chassi')
        self.third_frame_table_search_veiculo.heading('tipo', text='Tipo')
        self.third_frame_table_search_veiculo.heading('id_motorista', text='Id Motorista')
        self.third_frame_table_search_veiculo.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.third_frame_table_search_veiculo.bind('<Motion>', 'break')

        # Buscar Multa
        self.third_frame_label_search_multa = customtkinter.CTkLabel(self.third_frame.tab("Multas") , text="Buscas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label_search_multa.grid(row=0, column=0, padx=30, pady=(15, 15))
        self.third_frame_label_search_multa = customtkinter.CTkLabel(self.third_frame.tab("Multas") , text="Realizar busca por Multas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label_search_multa.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.third_frame_entry_search_multa = customtkinter.CTkEntry(self.third_frame.tab("Multas") , placeholder_text="Id ou Data")
        self.third_frame_entry_search_multa.grid(row=2, column=0, columnspan=1, padx=(10, 0), pady=(10, 10), sticky="nsew")
        self.third_frame_button_search_multa = customtkinter.CTkButton(self.third_frame.tab("Multas") ,command=self.button_search_multa , fg_color="transparent", border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.third_frame_button_search_multa.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        columns_search_multa = ('id_multa', 'valor', 'data', 'id_motorista', 'id_automovel')
        self.third_frame_table_search_multa = ttk.Treeview(master=self.third_frame.tab("Multas"),
                                columns=columns_search_multa,
                                height=5,
                                selectmode='browse',
                                show='headings')

        self.third_frame_table_search_multa.column("#1", anchor="c", minwidth=50, width=50)
        self.third_frame_table_search_multa.column("#2", anchor="c", minwidth=100, width=100)
        self.third_frame_table_search_multa.column("#3", anchor="c", minwidth=120, width=120)
        self.third_frame_table_search_multa.column("#4", anchor="c", minwidth=120, width=120)
        self.third_frame_table_search_multa.column("#5", anchor="c", minwidth=120, width=120)

        self.third_frame_table_search_multa.heading('id_multa', text='Id Multa')
        self.third_frame_table_search_multa.heading('valor', text='Valor')
        self.third_frame_table_search_multa.heading('data', text='Data')
        self.third_frame_table_search_multa.heading('id_motorista', text='Id Motorista')
        self.third_frame_table_search_multa.heading('id_automovel', text='Id Automovel')
        self.third_frame_table_search_multa.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.third_frame_table_search_multa.bind('<Motion>', 'break')

        # Gráficos - Abas
        self.fourth_frame = customtkinter.CTkTabview(self, corner_radius=20, border_width=5)
        self.fourth_frame.grid(row=1, column=0, padx=20, pady=10)
        # self.fourth_frame.add("Motoristas")
        self.fourth_frame.add("Veiculos")
        #self.fourth_frame.add("Multas")
        # self.fourth_frame.tab("Motoristas").grid_columnconfigure(0, weight=1) 
        self.fourth_frame.tab("Veiculos").grid_columnconfigure(0, weight=1)
        #self.fourth_frame.tab("Multas").grid_columnconfigure(0, weight=1)

        # Gráficos - Veiculos
        self.fourth_frame_label = customtkinter.CTkLabel(self.fourth_frame.tab("Veiculos") , text="Gráfico",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fourth_frame_label.grid(row=0, column=0, padx=30, pady=(15, 15))

        # Gráficos - Veiculos - figura
        self.fourth_frame_figure_multa = plt.figure(figsize=(8,4), dpi=60)
        self.fourth_frame_diagram_multa = self.fourth_frame_figure_multa.add_subplot(111)
        canva = FigureCanvasTkAgg(self.fourth_frame_figure_multa, self.fourth_frame.tab("Veiculos"))
        canva.get_tk_widget().grid(row=1, column=0)

        # Gráficos - Veiculos - dados
        def grafico_veiculo():
            geral = verAutomoveis(con)
            cont_carro = 0
            cont_moto = 0
            cont_onibus = 0
            cont_caminhao = 0
            for nome in geral:
                if nome[3] == 'Carro':
                    cont_carro = cont_carro + 1
                elif nome[3] == 'Moto':
                    cont_moto = cont_moto + 1
                elif nome[3] == 'Ônibus':
                    cont_onibus = cont_onibus + 1
                elif nome[3] == 'Caminhão':
                    cont_caminhao = cont_caminhao + 1
            return(cont_carro,cont_moto, cont_caminhao, cont_onibus)
        
        veiculos_lista = ('Carros', 'Motos', 'Caminhões', 'Ônibus')
        multas_lista = grafico_veiculo()
        y_pos = (1,2,3,4)

        self.fourth_frame_diagram_multa.barh(y_pos, multas_lista, align='center')
        self.fourth_frame_diagram_multa.set_yticks(y_pos, labels=veiculos_lista)
        self.fourth_frame_diagram_multa.invert_yaxis() 
        #self.fourth_frame_diagram_multa.set_xlabel('24 de Abril - 2023')
        self.fourth_frame_diagram_multa.set_title('Número de Veiculos Cadastrados')

        # Administrar
        self.fifth_frame = customtkinter.CTkTabview(self, corner_radius=20, border_width=5)
        self.fifth_frame.grid_columnconfigure(0, weight=1)
        self.fifth_frame.grid(row=1)
        self.fifth_frame.add("Motoristas")
        self.fifth_frame.add("Veiculos")
        self.fifth_frame.add("Multas")
        self.fifth_frame.tab("Motoristas").grid_columnconfigure(0, weight=1) 
        self.fifth_frame.tab("Veiculos").grid_columnconfigure(0, weight=1)
        self.fifth_frame.tab("Multas").grid_columnconfigure(0, weight=1)

        # Administrar - Motorista - Topbar
        self.fifth_frame_topbar_motoristas = customtkinter.CTkFrame(master=self.fifth_frame.tab("Motoristas"))
        self.fifth_frame_topbar_motoristas.grid_columnconfigure(0, weight=1)
        self.fifth_frame_topbar_motoristas.grid()

        self.fifth_frame_topbar_motoristas_button_1 = customtkinter.CTkButton(master=self.fifth_frame_topbar_motoristas ,command=self.main_button_add_motorista, text='Adicionar')
        self.fifth_frame_topbar_motoristas_button_1.grid(row=0, column=0, padx=5)
        self.fifth_frame_topbar_motoristas_button_2 = customtkinter.CTkButton(master=self.fifth_frame_topbar_motoristas ,command=self.main_button_update_motorista, text='Atualizar')
        self.fifth_frame_topbar_motoristas_button_2.grid(row=0, column=1, padx=5)
        self.fifth_frame_topbar_motoristas_button_3 = customtkinter.CTkButton(master=self.fifth_frame_topbar_motoristas ,command=self.main_button_remove_motorista, text='Remover')
        self.fifth_frame_topbar_motoristas_button_3.grid(row=0, column=2, padx=5)

        # Administrar - Adicionar Motorista
        self.fifth_frame_add_motorista = customtkinter.CTkFrame(self.fifth_frame.tab("Motoristas") , border_width=5, width=400, height=337,)
        self.fifth_frame_add_motorista.grid_columnconfigure(0, weight=1)


        self.fifth_frame_label_add_motorista = customtkinter.CTkLabel(self.fifth_frame_add_motorista , text="""Digite os dados do motorista
que deseja adicionar""",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fifth_frame_label_add_motorista.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.fifth_frame_entry_name_add_motorista = customtkinter.CTkEntry(self.fifth_frame_add_motorista, placeholder_text="Nome Completo")
        self.fifth_frame_entry_name_add_motorista.grid(row=1, column=0,  pady=(5, 5), sticky='n')
        self.fifth_frame_entry_cpf_add_motorista = customtkinter.CTkEntry(self.fifth_frame_add_motorista, placeholder_text="CPF")
        self.fifth_frame_entry_cpf_add_motorista.grid(row=2, column=0,  pady=5, sticky='n')
        self.fifth_frame_entry_cnh_add_motorista = customtkinter.CTkEntry(self.fifth_frame_add_motorista, placeholder_text="CNH")
        self.fifth_frame_entry_cnh_add_motorista.grid(row=3, column=0,  pady=5, sticky='n')
        self.fifth_frame_main_button_add_motorista = customtkinter.CTkButton(self.fifth_frame_add_motorista , fg_color="transparent",command=self.button_add_motorista  , border_width=2,text="cadastrar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_main_button_add_motorista.grid(row=6, column=0,  pady=(5, 20), sticky='n')


        # Administrar - Atualizar Motorista
        self.fifth_frame_update_motorista = customtkinter.CTkFrame(self.fifth_frame.tab("Motoristas") , border_width=5, width=400, height=337,)
        self.fifth_frame_update_motorista.grid_columnconfigure(0, weight=1)

        self.fifth_frame_label_update_motorista = customtkinter.CTkLabel(self.fifth_frame_update_motorista , text="""Busque e Selecione o motorista
que deseja atualizar""",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fifth_frame_label_update_motorista.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.fifth_frame_entry_update_motorista = customtkinter.CTkEntry(self.fifth_frame_update_motorista, placeholder_text="Nome ou Cpf")
        self.fifth_frame_entry_update_motorista.grid(row=1, column=0, pady=5, sticky="n")
        self.fifth_frame_button_update_motorista = customtkinter.CTkButton(self.fifth_frame_update_motorista , fg_color="transparent",command=self.button_search_motorista_update , border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_button_update_motorista.grid(row=2, column=0, pady=5, sticky="n")

        columns_search_update_motorista = ('id', 'nome', 'cpf', 'cnh')
        self.fifth_frame_table_search_update_motorista = ttk.Treeview(master=self.fifth_frame_update_motorista,
                                columns=columns_search_update_motorista,
                                height=5,
                                selectmode='browse',
                                show='headings')
        self.fifth_frame_table_search_update_motorista.column("#1", anchor="c", minwidth=50, width=50)
        self.fifth_frame_table_search_update_motorista.column("#2", anchor="w", minwidth=165, width=165)
        self.fifth_frame_table_search_update_motorista.column("#3", anchor="c", minwidth=120, width=120)
        self.fifth_frame_table_search_update_motorista.column("#4", anchor="c", minwidth=120, width=120)
        self.fifth_frame_table_search_update_motorista.heading('id', text='ID')
        self.fifth_frame_table_search_update_motorista.heading('nome', text='Nome')
        self.fifth_frame_table_search_update_motorista.heading('cpf', text='CPF')
        self.fifth_frame_table_search_update_motorista.heading('cnh', text='CNH')
        self.fifth_frame_table_search_update_motorista.grid(row=3, column=0, sticky='nsew', padx=10, pady=(5,5))
        self.fifth_frame_table_search_update_motorista.bind('<Motion>', 'break')

        self.fifth_frame_entry_name_update_motorista = customtkinter.CTkEntry(self.fifth_frame_update_motorista, placeholder_text="Novo - Nome")
        self.fifth_frame_entry_name_update_motorista.grid(row=4, column=0, pady=5, sticky="n")
        self.fifth_frame_entry_cpf_update_motorista = customtkinter.CTkEntry(self.fifth_frame_update_motorista, placeholder_text="Novo - CPF")
        self.fifth_frame_entry_cpf_update_motorista.grid(row=5, column=0, pady=5, sticky="n")
        self.fifth_frame_entry_cnh_update_motorista = customtkinter.CTkEntry(self.fifth_frame_update_motorista, placeholder_text="Novo - CNH")
        self.fifth_frame_entry_cnh_update_motorista.grid(row=6, column=0, pady=5, sticky="n")

        def display_selected_item_update_motorista(a):
            selected_item = self.fifth_frame_table_search_update_motorista.selection()[0]
            id_select = self.fifth_frame_table_search_update_motorista.item(selected_item)['values'][0]
            global id_final
            id_final = id_select
            print(f'O id selecionado é {id_final}')
        self.fifth_frame_table_search_update_motorista.bind("<<TreeviewSelect>>", display_selected_item_update_motorista)

        self.fifth_frame_button_update_motorista = customtkinter.CTkButton(self.fifth_frame_update_motorista , fg_color="transparent",command=self.button_update_motorista , border_width=2,text="Atualizar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_button_update_motorista.grid(row=7, column=0, pady=(5,23), sticky="n")

        # Administrar - Remover Motorista
        self.fifth_frame_delete_motorista = customtkinter.CTkFrame(self.fifth_frame.tab("Motoristas") , border_width=5, width=400, height=337,)
        self.fifth_frame_delete_motorista.grid_columnconfigure(0, weight=1)

        self.fifth_frame_label_delete_motorista = customtkinter.CTkLabel(self.fifth_frame_delete_motorista , text="""Busque e Selecione o motorista
que deseja remover""",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fifth_frame_label_delete_motorista.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.fifth_frame_entry_delete_motorista = customtkinter.CTkEntry(self.fifth_frame_delete_motorista, placeholder_text="Nome ou Cpf")
        self.fifth_frame_entry_delete_motorista.grid(row=1, column=0, pady=5, sticky="n")
        self.fifth_frame_button_delete_motorista = customtkinter.CTkButton(self.fifth_frame_delete_motorista ,command=self.button_search_motorista_delete, fg_color="transparent", border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_button_delete_motorista.grid(row=2, column=0, pady=5, sticky="n")

        columns_search_update_motorista = ('id', 'nome', 'cpf', 'cnh')
        self.fifth_frame_table_search_delete_motorista = ttk.Treeview(master=self.fifth_frame_delete_motorista,
                                columns=columns_search_update_motorista,
                                height=5,
                                selectmode='browse',
                                show='headings')
        self.fifth_frame_table_search_delete_motorista.column("#1", anchor="c", minwidth=50, width=50)
        self.fifth_frame_table_search_delete_motorista.column("#2", anchor="w", minwidth=165, width=165)
        self.fifth_frame_table_search_delete_motorista.column("#3", anchor="c", minwidth=120, width=120)
        self.fifth_frame_table_search_delete_motorista.column("#4", anchor="c", minwidth=120, width=120)
        self.fifth_frame_table_search_delete_motorista.heading('id', text='ID')
        self.fifth_frame_table_search_delete_motorista.heading('nome', text='Nome')
        self.fifth_frame_table_search_delete_motorista.heading('cpf', text='CPF')
        self.fifth_frame_table_search_delete_motorista.heading('cnh', text='CNH')
        self.fifth_frame_table_search_delete_motorista.grid(row=3, column=0, sticky='nsew', padx=10, pady=(5,5))
        self.fifth_frame_table_search_delete_motorista.bind('<Motion>', 'break')


        def display_selected_item_delete_motorista(a):
            selected_item = self.fifth_frame_table_search_delete_motorista.selection()[0]
            id_select = self.fifth_frame_table_search_delete_motorista.item(selected_item)['values'][0]
            global id_final
            id_final = id_select
            print(f'O id selecionado é {id_final}')
        self.fifth_frame_table_search_delete_motorista.bind("<<TreeviewSelect>>", display_selected_item_delete_motorista)

        self.fifth_frame_delete_checkbox = customtkinter.CTkCheckBox(master=self.fifth_frame_delete_motorista, text='Confirmar exclusão')
        self.fifth_frame_delete_checkbox.grid(row=6, column=0, pady=5)

        self.fifth_frame_delete_button_motorista = customtkinter.CTkButton(self.fifth_frame_delete_motorista , command=self.button_delete_motorista, fg_color="transparent", border_width=2,text="Remover", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_delete_button_motorista.grid(row=7, column=0, pady=(5,23), sticky="n")



        # Administrar - Veiculo - Topbar
        self.fifth_frame_topbar_veiculos = customtkinter.CTkFrame(master=self.fifth_frame.tab("Veiculos"))
        self.fifth_frame_topbar_veiculos.grid_columnconfigure(0, weight=1)
        self.fifth_frame_topbar_veiculos.grid()

        self.fifth_frame_topbar_veiculos_button_1 = customtkinter.CTkButton(master=self.fifth_frame_topbar_veiculos ,command=self.main_button_add_veiculo, text='Adicionar')
        self.fifth_frame_topbar_veiculos_button_1.grid(row=0, column=0, padx=5)
        self.fifth_frame_topbar_veiculos_button_2 = customtkinter.CTkButton(master=self.fifth_frame_topbar_veiculos ,command=self.main_button_update_veiculo, text='Atualizar')
        self.fifth_frame_topbar_veiculos_button_2.grid(row=0, column=1, padx=5)
        self.fifth_frame_topbar_veiculos_button_3 = customtkinter.CTkButton(master=self.fifth_frame_topbar_veiculos ,command=self.main_button_remove_veiculo, text='Remover')
        self.fifth_frame_topbar_veiculos_button_3.grid(row=0, column=2, padx=5)

        # Administrar - Adicionar Veiculo
        self.fifth_frame_add_veiculo = customtkinter.CTkFrame(self.fifth_frame.tab("Veiculos") , border_width=5, width=400, height=337,)
        self.fifth_frame_add_veiculo.grid_columnconfigure(0, weight=1)


        self.fifth_frame_label_add_veiculo = customtkinter.CTkLabel(self.fifth_frame_add_veiculo , text="""Digite os dados do veiculo
que deseja adicionar""",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fifth_frame_label_add_veiculo.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.fifth_frame_entry_placa_add_veiculo = customtkinter.CTkEntry(self.fifth_frame_add_veiculo, placeholder_text="Placa")
        self.fifth_frame_entry_placa_add_veiculo.grid(row=1, column=0,  pady=(5, 5), sticky='n')
        self.fifth_frame_entry_chassi_add_veiculo = customtkinter.CTkEntry(self.fifth_frame_add_veiculo, placeholder_text="Chassi")
        self.fifth_frame_entry_chassi_add_veiculo.grid(row=2, column=0,  pady=5, sticky='n')
        self.fifth_frame_entry_id_motorista_add_veiculo = customtkinter.CTkEntry(self.fifth_frame_add_veiculo, placeholder_text="Id Motorista")
        self.fifth_frame_entry_id_motorista_add_veiculo.grid(row=3, column=0,  pady=5, sticky='n')

        tipo_veiculos_add = ["Carro", "Moto", "Ônibus", "Caminhão"]
        self.fifth_frame_variable_add_veiculo = tkinter.StringVar()
        self.fifth_frame_variable_add_veiculo.set("Escolha o tipo")

        def select_callback_add(choice):
            choice = self.fifth_frame_combobox_add_veiculo.get()
            print("O tipo escolhido foi:", choice)

        self.fifth_frame_combobox_add_veiculo = customtkinter.CTkComboBox(self.fifth_frame_add_veiculo, variable=self.fifth_frame_variable_add_veiculo, values=tipo_veiculos_add, command=select_callback_add)
        self.fifth_frame_combobox_add_veiculo.grid(row=4,pady=5, padx=5)


        self.fifth_frame_button_add_veiculo = customtkinter.CTkButton(self.fifth_frame_add_veiculo , fg_color="transparent",command=self.button_add_veiculo  , border_width=2,text="cadastrar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_button_add_veiculo.grid(row=6, column=0,  pady=(5, 20), sticky='n')


        # Administrar - Atualizar Veiculo
        self.fifth_frame_update_veiculo = customtkinter.CTkFrame(self.fifth_frame.tab("Veiculos") , border_width=5, width=400, height=337,)
        self.fifth_frame_update_veiculo.grid_columnconfigure(0, weight=1)

        self.fifth_frame_label_update_veiculo = customtkinter.CTkLabel(self.fifth_frame_update_veiculo , text="""Busque e Selecione o veiculo
que deseja atualizar""",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fifth_frame_label_update_veiculo.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.fifth_frame_entry_update_veiculo = customtkinter.CTkEntry(self.fifth_frame_update_veiculo, placeholder_text="Placa ou Id")
        self.fifth_frame_entry_update_veiculo.grid(row=1, column=0, pady=5, sticky="n")
        self.fifth_frame_button_update_veiculo = customtkinter.CTkButton(self.fifth_frame_update_veiculo , fg_color="transparent",command=self.button_search_veiculo_update , border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_button_update_veiculo.grid(row=2, column=0, pady=5, sticky="n")

        columns_search_update_veiculo = ('id', 'placa', 'chassi', 'tipo', 'id_motorista')
        self.fifth_frame_table_search_update_veiculo = ttk.Treeview(master=self.fifth_frame_update_veiculo,
                                columns=columns_search_update_veiculo,
                                height=5,
                                selectmode='browse',
                                show='headings')
        self.fifth_frame_table_search_update_veiculo.column("#1", anchor="c", minwidth=20, width=50)
        self.fifth_frame_table_search_update_veiculo.column("#2", anchor="c", minwidth=100, width=100)
        self.fifth_frame_table_search_update_veiculo.column("#3", anchor="c", minwidth=100, width=100)
        self.fifth_frame_table_search_update_veiculo.column("#4", anchor="c", minwidth=100, width=100)
        self.fifth_frame_table_search_update_veiculo.column("#5", anchor="c", minwidth=100, width=100)
        self.fifth_frame_table_search_update_veiculo.heading('id', text='Id')
        self.fifth_frame_table_search_update_veiculo.heading('placa', text='Placa')
        self.fifth_frame_table_search_update_veiculo.heading('chassi', text='Chassi')
        self.fifth_frame_table_search_update_veiculo.heading('tipo', text='Tipo')
        self.fifth_frame_table_search_update_veiculo.heading('id_motorista', text='Id Motorista')
        self.fifth_frame_table_search_update_veiculo.grid(row=3, column=0, sticky='nsew', padx=10, pady=(5,5))
        self.fifth_frame_table_search_update_veiculo.bind('<Motion>', 'break')

        self.fifth_frame_entry_placa_update_veiculo = customtkinter.CTkEntry(master=self.fifth_frame_update_veiculo, placeholder_text="Nova - Placa")
        self.fifth_frame_entry_placa_update_veiculo.grid(row=4, column=0, pady=5, sticky="n")
        self.fifth_frame_entry_chassi_update_veiculo = customtkinter.CTkEntry(master=self.fifth_frame_update_veiculo, placeholder_text="Novo - Chassi")
        self.fifth_frame_entry_chassi_update_veiculo.grid(row=5, column=0, pady=5, sticky="n")

        tipo_veiculos_update = ["Carro", "Moto", "Ônibus", "Caminhão"]
        self.fifth_frame_variable_update_veiculo = tkinter.StringVar()
        self.fifth_frame_variable_update_veiculo.set("Novo - Tipo")

        def select_callback_update_veiculo(choice):
            choice = self.fifth_frame_combobox_update_veiculo.get()
            print("O tipo escolhido foi:", choice)

        self.fifth_frame_entry_id_motorista_update_veiculo = customtkinter.CTkEntry(master=self.fifth_frame_update_veiculo, placeholder_text="Novo - Id Motorista")
        self.fifth_frame_entry_id_motorista_update_veiculo.grid(row=6, column=0, pady=5, sticky="n")

        self.fifth_frame_combobox_update_veiculo = customtkinter.CTkComboBox(self.fifth_frame_update_veiculo, variable=self.fifth_frame_variable_update_veiculo, values=tipo_veiculos_update, command=select_callback_update_veiculo)
        self.fifth_frame_combobox_update_veiculo.grid(row=7,pady=5, padx=5)


        self.fifth_frame_button_update_veiculo = customtkinter.CTkButton(self.fifth_frame_update_veiculo , fg_color="transparent",command=self.button_add_motorista  , border_width=2,text="cadastrar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_button_update_veiculo.grid(row=8, column=0,  pady=(5, 20), sticky='n')



        
        def display_selected_item_update_veiculo(a):
            selected_item = self.fifth_frame_table_search_update_veiculo.selection()[0]
            id_select = self.fifth_frame_table_search_update_veiculo.item(selected_item)['values'][0]
            global id_final
            id_final = id_select
            print(f'O id selecionado é {id_final}')

        self.fifth_frame_table_search_update_veiculo.bind("<<TreeviewSelect>>", display_selected_item_update_veiculo)

        self.fifth_frame_update_main_button_1_veiculo_2 = customtkinter.CTkButton(self.fifth_frame_update_veiculo , fg_color="transparent",command=self.button_update_veiculo , border_width=2,text="Atualizar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_update_main_button_1_veiculo_2.grid(row=8, column=0, pady=(5,23), sticky="n")

        # Administrar - Remover Veiculo
        self.fifth_frame_delete_veiculo = customtkinter.CTkFrame(self.fifth_frame.tab("Veiculos") , border_width=5, width=400, height=337,)
        self.fifth_frame_delete_veiculo.grid_columnconfigure(0, weight=1)

        self.fifth_frame_label_delete_veiculo = customtkinter.CTkLabel(self.fifth_frame_delete_veiculo , text="""Busque e Selecione o veiculo
que deseja remover""",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fifth_frame_label_delete_veiculo.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.fifth_frame_entry_delete_veiculo = customtkinter.CTkEntry(self.fifth_frame_delete_veiculo, placeholder_text="Placa ou Id")
        self.fifth_frame_entry_delete_veiculo.grid(row=1, column=0, pady=5, sticky="n")
        self.fifth_frame_button_delete_veiculo = customtkinter.CTkButton(self.fifth_frame_delete_veiculo,command=self.button_search_veiculo_delete  , fg_color="transparent", border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_button_delete_veiculo.grid(row=2, column=0, pady=5, sticky="n")

        fifth_frame_columns_search_delete_veiculo = ('id', 'placa', 'chassi', 'tipo', 'id_motorista')
        self.fifth_frame_table_search_delete_veiculo = ttk.Treeview(master=self.fifth_frame_delete_veiculo,
                                columns=fifth_frame_columns_search_delete_veiculo,
                                height=5,
                                selectmode='browse',
                                show='headings')
        self.fifth_frame_table_search_delete_veiculo.column("#1", anchor="c", minwidth=20, width=50)
        self.fifth_frame_table_search_delete_veiculo.column("#2", anchor="c", minwidth=100, width=100)
        self.fifth_frame_table_search_delete_veiculo.column("#3", anchor="c", minwidth=100, width=100)
        self.fifth_frame_table_search_delete_veiculo.column("#4", anchor="c", minwidth=100, width=100)
        self.fifth_frame_table_search_delete_veiculo.column("#5", anchor="c", minwidth=100, width=100)
        self.fifth_frame_table_search_delete_veiculo.heading('id', text='Id')
        self.fifth_frame_table_search_delete_veiculo.heading('placa', text='Placa')
        self.fifth_frame_table_search_delete_veiculo.heading('chassi', text='Chassi')
        self.fifth_frame_table_search_delete_veiculo.heading('tipo', text='Tipo')
        self.fifth_frame_table_search_delete_veiculo.heading('id_motorista', text='Id Motorista')
        self.fifth_frame_table_search_delete_veiculo.grid(row=3, column=0, sticky='nsew', padx=10, pady=(5,5))
        self.fifth_frame_table_search_delete_veiculo.bind('<Motion>', 'break')


        
        def display_selected_item_delete_veiculo(a):
            selected_item = self.fifth_frame_table_search_delete_veiculo.selection()[0]
            id_select = self.fifth_frame_table_search_delete_veiculo.item(selected_item)['values'][0]
            global id_final
            id_final = id_select
            print(f'O id selecionado é {id_final}')
        self.fifth_frame_table_search_delete_veiculo.bind("<<TreeviewSelect>>", display_selected_item_delete_veiculo)

        self.fifth_frame_checkbox_delete_veiculo = customtkinter.CTkCheckBox(master=self.fifth_frame_delete_veiculo, text='Confirmar exclusão')
        self.fifth_frame_checkbox_delete_veiculo.grid(row=6, column=0, pady=5)

        self.fifth_frame_button_delete_veiculo = customtkinter.CTkButton(self.fifth_frame_delete_veiculo ,command=self.button_delete_veiculo, fg_color="transparent", border_width=2,text="Remover", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_button_delete_veiculo.grid(row=7, column=0, pady=(5,23), sticky="n")

        # Administrar - Multa - Topbar
        self.fifth_frame_topbar_multas = customtkinter.CTkFrame(master=self.fifth_frame.tab("Multas"))
        self.fifth_frame_topbar_multas.grid_columnconfigure(0, weight=1)
        self.fifth_frame_topbar_multas.grid()

        self.fifth_frame_topbar_multas_button_1 = customtkinter.CTkButton(master=self.fifth_frame_topbar_multas ,command=self.main_button_add_multa, text='Adicionar')
        self.fifth_frame_topbar_multas_button_1.grid(row=0, column=0, padx=5)
        self.fifth_frame_topbar_multas_button_2 = customtkinter.CTkButton(master=self.fifth_frame_topbar_multas ,command=self.main_button_update_multa, text='Atualizar')
        self.fifth_frame_topbar_multas_button_2.grid(row=0, column=1, padx=5)
        self.fifth_frame_topbar_multas_button_3 = customtkinter.CTkButton(master=self.fifth_frame_topbar_multas,command=self.main_button_remove_multa , text='Remover')
        self.fifth_frame_topbar_multas_button_3.grid(row=0, column=2, padx=5)

        # Administrar - Adicionar Multa
        self.fifth_frame_add_multa = customtkinter.CTkFrame(self.fifth_frame.tab("Multas") , border_width=5, width=400, height=337,)
        self.fifth_frame_add_multa.grid_columnconfigure(0, weight=1)


        self.fifth_frame_label_add_multa = customtkinter.CTkLabel(self.fifth_frame_add_multa , text="""Digite os dados do multa
que deseja adicionar""",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fifth_frame_label_add_multa.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.fifth_frame_entry_id_veiculo_add_multa = customtkinter.CTkEntry(self.fifth_frame_add_multa, placeholder_text="Placa")
        self.fifth_frame_entry_id_veiculo_add_multa.grid(row=1, column=0,  pady=(5, 5), sticky='n')
        self.fifth_frame_button_id_veiculo_add_multa = customtkinter.CTkButton(self.fifth_frame_add_multa ,command=self.get_veiculo, fg_color="transparent" , border_width=2,text="buscar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_button_id_veiculo_add_multa.grid(row=2, column=0, sticky='n')
        self.fifth_frame_entry_id_motorista_add_multa = customtkinter.CTkEntry(self.fifth_frame_add_multa, placeholder_text="Motorista")
        self.fifth_frame_entry_id_motorista_add_multa.grid(row=3, column=0,  pady=5, sticky='n')
        self.fifth_frame_entry_data_add_multa = customtkinter.CTkEntry(self.fifth_frame_add_multa, placeholder_text="data (dd/mm/aa)")
        self.fifth_frame_entry_data_add_multa.grid(row=4, column=0,  pady=5, sticky='n')
        self.fifth_frame_entry_valor_add_multa = customtkinter.CTkEntry(self.fifth_frame_add_multa, placeholder_text="valor")
        self.fifth_frame_entry_valor_add_multa.grid(row=5, column=0,  pady=5, sticky='n')
        self.fifth_frame_button_add_multa = customtkinter.CTkButton(self.fifth_frame_add_multa ,command=self.button_add_multa, fg_color="transparent" , border_width=2,text="cadastrar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_button_add_multa.grid(row=6, column=0,  pady=(5, 20), sticky='n')


        # Administrar - Atualizar Multa
        self.fifth_frame_update_multa = customtkinter.CTkFrame(self.fifth_frame.tab("Multas") , border_width=5, width=400, height=337,)
        self.fifth_frame_update_multa.grid_columnconfigure(0, weight=1)

        self.fifth_frame_label_update_multa = customtkinter.CTkLabel(self.fifth_frame_update_multa , text="""Busque e Selecione o multa
que deseja atualizar""",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fifth_frame_label_update_multa.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.fifth_frame_entry_update_multa = customtkinter.CTkEntry(self.fifth_frame_update_multa, placeholder_text="Id ou data")
        self.fifth_frame_entry_update_multa.grid(row=1, column=0, pady=5, sticky="n")
        self.fifth_frame_button_update_multa = customtkinter.CTkButton(self.fifth_frame_update_multa,command=self.button_search_multa_update , fg_color="transparent" , border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_button_update_multa.grid(row=2, column=0, pady=5, sticky="n")

        fifth_frame_colums_search_update_multa = ('id_multa', 'valor', 'data', 'id_motorista', 'id_veiculo')
        self.fifth_frame_table_search_update_multa = ttk.Treeview(master=self.fifth_frame_update_multa,
                                columns=fifth_frame_colums_search_update_multa,
                                height=5,
                                selectmode='browse',
                                show='headings')
        self.fifth_frame_table_search_update_multa.column("#1", anchor="c", minwidth=50, width=50)
        self.fifth_frame_table_search_update_multa.column("#2", anchor="c", minwidth=100, width=100)
        self.fifth_frame_table_search_update_multa.column("#3", anchor="c", minwidth=120, width=120)
        self.fifth_frame_table_search_update_multa.column("#4", anchor="c", minwidth=120, width=120)
        self.fifth_frame_table_search_update_multa.column("#5", anchor="c", minwidth=120, width=120)
        self.fifth_frame_table_search_update_multa.heading('id_multa', text='ID Multa')
        self.fifth_frame_table_search_update_multa.heading('valor', text='Valor')
        self.fifth_frame_table_search_update_multa.heading('data', text='Data')
        self.fifth_frame_table_search_update_multa.heading('id_motorista', text='Id Motorista')
        self.fifth_frame_table_search_update_multa.heading('id_veiculo', text='Id Veiculo')
        self.fifth_frame_table_search_update_multa.grid(row=3, column=0, sticky='nsew', padx=10, pady=(5,5))
        self.fifth_frame_table_search_update_multa.bind('<Motion>', 'break')

  
        self.fifth_frame_entry_id_veiculo_update_multa = customtkinter.CTkEntry(self.fifth_frame_update_multa, placeholder_text="id veiculo")
        self.fifth_frame_entry_id_veiculo_update_multa.grid(row=4, column=0,  pady=(5, 5), sticky='n')
        self.fifth_frame_entry_id_motorista_update_multa = customtkinter.CTkEntry(self.fifth_frame_update_multa, placeholder_text="id motorista")
        self.fifth_frame_entry_id_motorista_update_multa.grid(row=5, column=0,  pady=5, sticky='n')
        self.fifth_frame_entry_data_update_multa = customtkinter.CTkEntry(self.fifth_frame_update_multa, placeholder_text="data")
        self.fifth_frame_entry_data_update_multa.grid(row=6, column=0,  pady=5, sticky='n')
        self.fifth_frame_entry_valor_update_multa = customtkinter.CTkEntry(self.fifth_frame_update_multa, placeholder_text="valor")
        self.fifth_frame_entry_valor_update_multa.grid(row=7, column=0,  pady=5, sticky='n')


        
        def display_selected_item_update_multa(a):
            selected_item = self.fifth_frame_table_search_update_multa.selection()[0]
            id_select = self.fifth_frame_table_search_update_multa.item(selected_item)['values'][0]
            global id_final
            id_final = id_select
            print(f'O id selecionado é {id_final}')
        self.fifth_frame_table_search_update_multa.bind("<<TreeviewSelect>>", display_selected_item_update_multa)

        self.fifth_frame_update_multa_main_button_1_multa_2 = customtkinter.CTkButton(self.fifth_frame_update_multa ,command=self.button_update_multa, fg_color="transparent" , border_width=2,text="Atualizar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_update_multa_main_button_1_multa_2.grid(row=8, column=0, pady=(5,10), sticky="n")

        # Administrar - Remover Multa
        self.fifth_frame_delete_multa = customtkinter.CTkFrame(self.fifth_frame.tab("Multas") , border_width=5, width=400, height=337,)
        self.fifth_frame_delete_multa.grid_columnconfigure(0, weight=1)

        self.fifth_frame_label_delete_multa = customtkinter.CTkLabel(self.fifth_frame_delete_multa , text="""Busque e Selecione o multa
que deseja remover""",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fifth_frame_label_delete_multa.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.fifth_frame_entry_delete_multa = customtkinter.CTkEntry(self.fifth_frame_delete_multa, placeholder_text="Id ou Data")
        self.fifth_frame_entry_delete_multa.grid(row=1, column=0, pady=5, sticky="n")
        self.fifth_frame_button_delete_multa = customtkinter.CTkButton(self.fifth_frame_delete_multa ,command=self.button_search_multa_delete, fg_color="transparent", border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_button_delete_multa.grid(row=2, column=0, pady=5, sticky="n")

        self.fifth_frame_colums_search_delete_multa = ('id_multa', 'valor', 'data', 'id_motorista', 'id_veiculo')
        self.fifth_frame_table_search_delete_multa = ttk.Treeview(master=self.fifth_frame_delete_multa,
                                columns=self.fifth_frame_colums_search_delete_multa,
                                height=5,
                                selectmode='browse',
                                show='headings')
        self.fifth_frame_table_search_delete_multa.column("#1", anchor="c", minwidth=50, width=50)
        self.fifth_frame_table_search_delete_multa.column("#2", anchor="c", minwidth=100, width=100)
        self.fifth_frame_table_search_delete_multa.column("#3", anchor="c", minwidth=120, width=120)
        self.fifth_frame_table_search_delete_multa.column("#4", anchor="c", minwidth=120, width=120)
        self.fifth_frame_table_search_delete_multa.column("#5", anchor="c", minwidth=120, width=120)
        self.fifth_frame_table_search_delete_multa.heading('id_multa', text='ID Multa')
        self.fifth_frame_table_search_delete_multa.heading('valor', text='Valor')
        self.fifth_frame_table_search_delete_multa.heading('data', text='Data')
        self.fifth_frame_table_search_delete_multa.heading('id_motorista', text='Id Motorista')
        self.fifth_frame_table_search_delete_multa.heading('id_veiculo', text='Id Veiculo')
        self.fifth_frame_table_search_delete_multa.grid(row=3, column=0, sticky='nsew', padx=10, pady=(5,5))
        self.fifth_frame_table_search_delete_multa.bind('<Motion>', 'break')



        def display_selected_item_delete_multa(a):
            selected_item = self.fifth_frame_table_search_delete_multa.selection()[0]
            id_select = self.fifth_frame_table_search_delete_multa.item(selected_item)['values'][0]
            global id_final
            id_final = id_select
            print(f'O id selecionado é {id_final}')
        self.fifth_frame_table_search_delete_multa.bind("<<TreeviewSelect>>", display_selected_item_delete_multa)

        self.fifth_frame_checkbox_delete_multa = customtkinter.CTkCheckBox(master=self.fifth_frame_delete_multa, text='Confirmar exclusão')
        self.fifth_frame_checkbox_delete_multa.grid(row=6, column=0, pady=5)

        self.fifth_frame_delete_multa_main_button_1_multa_2 = customtkinter.CTkButton(self.fifth_frame_delete_multa,command=self.button_delete_multa , fg_color="transparent", border_width=2,text="Remover", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_delete_multa_main_button_1_multa_2.grid(row=7, column=0, pady=(5,23), sticky="n")



        # Administrar Logado
        self.sixth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sixth_frame.grid_columnconfigure(0, weight=1)
        self.sixth_frame_large_image_label = customtkinter.CTkLabel(self.sixth_frame, text="", image=self.welcome_image)
        self.sixth_frame_large_image_label.grid(row=2, pady=(90,5))



        # frame padrão
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # Mudar cor do botão
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")

        # Mostrar frame escolhido
        if name == "home" and login == False:
            self.home_frame.grid(row=0, column=1, sticky="nsew")

        elif name == "home" and login == True:
            name = "frame_6"
            self.home_frame.grid_forget()

        else:
            self.home_frame.grid_forget()

        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()

        if name == "frame_5":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifth_frame.grid_forget()
            
        if name == "frame_6":
            self.sixth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sixth_frame.grid_forget()


    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")     

    def frame_6_button_event(self):
        self.select_frame_by_name("frame_6")      

    def login_event(self):
        global login
        login = True
        self.home_frame.grid_forget()  # remover login frame
        self.sixth_frame.grid(row=0, column=1, sticky="nsew")  # mostrar frame logado

        self.frame_2_button.grid(row=2, column=0, sticky="ew")
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        self.frame_4_button.grid(row=4, column=0, sticky="ew")
        self.frame_5_button.grid(row=5, column=0, sticky="ew")

        self.frame_6_button.grid(row=7, column=0, sticky="ew")

    def logout_event(self):
        self.sixth_frame.grid_forget()  # remover frame logado
        self.home_frame.grid(row=0, column=1, sticky="nsew")  # mostrar login frame 
        global login
        login = False

        self.frame_2_button.grid_forget()
        self.frame_3_button.grid_forget()
        self.frame_4_button.grid_forget()
        self.frame_5_button.grid_forget()

        self.frame_6_button.grid_forget()

        self.select_frame_by_name("home")

    def button_search_motorista(self):
        resultados = buscarMotorista(con,self.third_frame_entry_search_motorista.get())
        for item in self.third_frame_table_search_motorista.get_children():
            self.third_frame_table_search_motorista.delete(item)

        for motorista in resultados:
            self.third_frame_table_search_motorista.insert('', tkinter.END, values=motorista)

    def button_search_motorista_update(self):
        resultados = buscarMotorista(con,self.fifth_frame_entry_update_motorista.get())
        for item in self.fifth_frame_table_search_update_motorista.get_children():
            self.fifth_frame_table_search_update_motorista.delete(item)

        for motorista in resultados:
            self.fifth_frame_table_search_update_motorista.insert('', tkinter.END, values=motorista)

#Botão para deletar motorista
    def button_search_motorista_delete(self):
        resultados = buscarMotorista(con,self.fifth_frame_entry_delete_motorista.get())
        for item in self.fifth_frame_table_search_delete_motorista.get_children():
            self.fifth_frame_table_search_delete_motorista.delete(item)

        for motorista in resultados:
            self.fifth_frame_table_search_delete_motorista.insert('', tkinter.END, values=motorista)


    def button_search_veiculo(self):
        resultados = buscarAutomovel(con,self.third_frame_entry_search_veiculo.get())
        for item in self.third_frame_table_search_veiculo.get_children():
            self.third_frame_table_search_veiculo.delete(item)

        for veiculo in resultados:
            self.third_frame_table_search_veiculo.insert('', tkinter.END, values=veiculo)

    def button_search_multa(self):
        resultados = buscarMulta(con, self.third_frame_entry_search_multa.get())
        for item in self.third_frame_table_search_multa.get_children():
            self.third_frame_table_search_multa.delete(item)

        for multa in resultados:
            self.third_frame_table_search_multa.insert('', tkinter.END, values=multa)

    
    def button_add_motorista(self):
        name = self.fifth_frame_entry_name_add_motorista.get()
        cpf = self.fifth_frame_entry_cpf_add_motorista.get()
        cnh = self.fifth_frame_entry_cnh_add_motorista.get()
        inserirMotorista(con,name,cpf,cnh)

        for item in self.table_motorista.get_children():
            self.table_motorista.delete(item)

        motoristas = verMotorista(con)
        for motorista in motoristas:
            self.table_motorista.insert('', tkinter.END, values=motorista)

    def button_update_motorista(self):
        global id_final
        name = self.fifth_frame_entry_name_update_motorista.get()
        cpf = self.fifth_frame_entry_cpf_update_motorista.get()
        cnh = self.fifth_frame_entry_cnh_update_motorista.get()
        updateMotorista(con,id_final, name, cpf, cnh)

        for item in self.table_motorista.get_children():
            self.table_motorista.delete(item)

        motoristas = verMotorista(con)
        for motorista in motoristas:
            self.table_motorista.insert('', tkinter.END, values=motorista)

#Botão remover motorista
    def button_delete_motorista(self):
        global id_final
        deletarMotorista(con,id_final)

        for item in self.table_motorista.get_children():
            self.table_motorista.delete(item)

        motoristas = verMotorista(con)
        for motorista in motoristas:
            self.table_motorista.insert('', tkinter.END, values=motorista)


    def main_button_add_motorista(self):
        self.fifth_frame_update_motorista.grid_forget()
        self.fifth_frame_delete_motorista.grid_forget()
        self.fifth_frame_add_motorista.grid(columnspan=3,pady=10,sticky='ew')

    def main_button_update_motorista(self):
        self.fifth_frame_add_motorista.grid_forget()
        self.fifth_frame_delete_motorista.grid_forget()
        self.fifth_frame_update_motorista.grid(columnspan=3,pady=10,sticky='ew')
    
    def main_button_remove_motorista(self):
        self.fifth_frame_add_motorista.grid_forget()
        self.fifth_frame_update_motorista.grid_forget()
        self.fifth_frame_delete_motorista.grid(columnspan=3,pady=10,sticky='ew')

#--------------------

    def button_add_veiculo(self):
        placa = self.fifth_frame_entry_placa_add_veiculo.get()
        chassi = self.fifth_frame_entry_chassi_add_veiculo.get()
        id_motorista = self.fifth_frame_entry_id_motorista_add_veiculo.get()
        tipo = self.fifth_frame_variable_add_veiculo.get()
        inserirAutomovel(con, placa, chassi, tipo, id_motorista)

        for item in self.table_veiculos.get_children():
            self.table_veiculos.delete(item)

        veiculos = vertodasTabelasVeiculos(con)
        for veiculo in veiculos:
            self.table_veiculos.insert('', tkinter.END, values=veiculo)

    def button_update_veiculo(self):
        global id_final

        placa = self.fifth_frame_entry_placa_update_veiculo.get()
        chassi = self.fifth_frame_entry_chassi_update_veiculo.get()
        id_motorista = self.fifth_frame_entry_id_motorista_update_veiculo.get()
        tipo = self.fifth_frame_variable_update_veiculo.get()
        updateAutomovel(con, id_final, placa, chassi, tipo, id_motorista)

        for item in self.table_veiculos.get_children():
            self.table_veiculos.delete(item)

        veiculos = vertodasTabelasVeiculos(con)
        for veiculo in veiculos:
            self.table_veiculos.insert('', tkinter.END, values=veiculo)

    def  button_search_veiculo_update(self):
        resultados = buscarAutomovel(con,self.fifth_frame_entry_update_veiculo.get())
        for item in self.fifth_frame_table_search_update_veiculo.get_children():
            self.fifth_frame_table_search_update_veiculo.delete(item)

        for veiculo in resultados:
            self.fifth_frame_table_search_update_veiculo.insert('', tkinter.END, values=veiculo)


    def button_delete_veiculo(self):
        global id_final
        deletarAutomovel(con,id_final)

        for item in self.table_veiculos.get_children():
            self.table_veiculos.delete(item)

        veiculos = vertodasTabelasVeiculos(con)
        for veiculo in veiculos:
            self.table_veiculos.insert('', tkinter.END, values=veiculo)


    def  button_search_veiculo_delete(self):
        resultados = buscarAutomovel(con,self.fifth_frame_entry_delete_veiculo.get())
        for item in self.fifth_frame_table_search_delete_veiculo.get_children():
            self.fifth_frame_table_search_delete_veiculo.delete(item)

        for veiculo in resultados:
            self.fifth_frame_table_search_delete_veiculo.insert('', tkinter.END, values=veiculo)



   



#---------------------------------------------------------------------------------

    def main_button_add_veiculo(self):
        self.fifth_frame_update_veiculo.grid_forget()
        self.fifth_frame_delete_veiculo.grid_forget()
        self.fifth_frame_add_veiculo.grid(columnspan=3,pady=10,sticky='ew')

    def main_button_update_veiculo(self):
        self.fifth_frame_add_veiculo.grid_forget()
        self.fifth_frame_delete_veiculo.grid_forget()
        self.fifth_frame_update_veiculo.grid(columnspan=3,pady=10,sticky='ew')
    
    def main_button_remove_veiculo(self):
        self.fifth_frame_add_veiculo.grid_forget()
        self.fifth_frame_update_veiculo.grid_forget()
        self.fifth_frame_delete_veiculo.grid(columnspan=3,pady=10,sticky='ew')
        
#--------------------

    def button_add_multa(self):
        valor = self.fifth_frame_entry_valor_add_multa.get()
        data = self.fifth_frame_entry_data_add_multa.get()
        motorista = self.fifth_frame_entry_id_motorista_add_multa.get()
        automovel = self.fifth_frame_entry_id_veiculo_add_multa.get()
        motorista_id = buscarIdMotorista(con, motorista)
        automovel_id = buscarPlacaAutomovel(con, automovel)
        inserirMulta(con,valor,data,motorista_id[0][0],automovel_id[0][0])

        for item in self.table_multas.get_children():
            self.table_multas.delete(item)

        multas = vertodasTabelas(con)
        for multa in multas:
            self.table_multas.insert('', tkinter.END, values=multa)

    def button_update_multa(self):
        global id_final

        valor = self.fifth_frame_entry_valor_update_multa.get()
        data = self.fifth_frame_entry_data_update_multa.get()
        motorista = self.fifth_frame_entry_id_motorista_update_multa.get()
        automovel = self.fifth_frame_entry_id_veiculo_update_multa.get()
        updateMulta(con,id_final,valor,data,motorista,automovel)

        for item in self.table_multas.get_children():
            self.table_multas.delete(item)

        multas = verMultas(con)
        for multa in multas:
            self.table_multas.insert('', tkinter.END, values=multa)

    def  button_search_multa_update(self):
        resultados = buscarMulta(con,self.fifth_frame_entry_update_multa.get())
        for item in self.fifth_frame_table_search_update_multa.get_children():
            self.fifth_frame_table_search_update_multa.update(item)

        for veiculo in resultados:
            self.fifth_frame_table_search_update_multa.insert('', tkinter.END, values=veiculo)

    def button_delete_multa(self):
        global id_final
        deletarMulta(con,id_final)

        for item in self.table_multas.get_children():
            self.table_multas.delete(item)

        multas = verMultas(con)
        for multa in multas:
            self.table_multas.insert('', tkinter.END, values=multa)


    def  button_search_multa_delete(self):
            resultados = buscarMulta(con,self.fifth_frame_entry_delete_multa.get())
            for item in self.fifth_frame_table_search_delete_multa.get_children():
                self.fifth_frame_table_search_delete_multa.update(item)

            for veiculo in resultados:
                self.fifth_frame_table_search_delete_multa.insert('', tkinter.END, values=veiculo)


    def main_button_add_multa(self):
        self.fifth_frame_update_multa.grid_forget()
        self.fifth_frame_delete_multa.grid_forget()
        self.fifth_frame_add_multa.grid(columnspan=3,pady=10,sticky='ew')


        

    def main_button_update_multa(self):
        self.fifth_frame_add_multa.grid_forget()
        self.fifth_frame_delete_multa.grid_forget()
        self.fifth_frame_update_multa.grid(columnspan=3,pady=10,sticky='ew')
    


    def main_button_remove_multa(self):
        self.fifth_frame_add_multa.grid_forget()
        self.fifth_frame_update_multa.grid_forget()
        self.fifth_frame_delete_multa.grid(columnspan=3,pady=10,sticky='ew')

    def get_veiculo(self):
        self.fifth_frame_entry_id_motorista_add_multa.delete(0, END)
        placa = self.fifth_frame_entry_id_veiculo_add_multa.get()
        motorista=buscarNomeMotorista(con,placa)
        self.fifth_frame_entry_id_motorista_add_multa.insert(END, motorista[0][0])


class AutocompleteEntry(Entry):
    def __init__(self, autocompleteList, *args, **kwargs):

        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            del kwargs['listboxLength']
        else:
            self.listboxLength = 8


        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = re.compile('.*' + re.escape(fieldValue) + '.*', re.IGNORECASE)
                return re.match(pattern, acListEntry)

            self.matchesFunction = matches

        Entry.__init__(self, *args, **kwargs)
        self.focus()

        self.autocompleteList = autocompleteList

        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)

        self.listboxUp = False
    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listboxUp:
                self.listbox.destroy()
                self.listboxUp = False
        else:
            words = self.comparison()
            if words:
                if not self.listboxUp:
                    self.listbox = Listbox(width=self["width"], height=self.listboxLength)
                    self.listbox.bind("<Button-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)
                    self.listbox.place(x=247, y=200)
                    self.listboxUp = True

                self.listbox.delete(0, END)
                for w in words:
                    self.listbox.insert(END, w)
            else:
                if self.listboxUp:
                    self.listbox.destroy()
                    self.listboxUp = False
    def selection(self, event):
        if self.listboxUp:
            self.var.set(self.listbox.get(ACTIVE))
            self.listbox.destroy()
            self.listboxUp = False
            self.icursor(END)
    def moveUp(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != '0':
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)

                self.listbox.see(index)  
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)
    def moveDown(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != END:
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)

                self.listbox.see(index) 
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)
    def comparison(self):
        return [w for w in self.autocompleteList if self.matchesFunction(self.var.get(), w)]


autocompleteList = verNomeMotorista(con)


def matches(fieldValue, acListEntry):
    pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
    return re.match(pattern, acListEntry)
        


app = App()
app.mainloop()