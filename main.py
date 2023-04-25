import customtkinter
import tkinter.ttk as ttk
import tkinter
import tksheet
import os
from PIL import Image
from database import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


login=False
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        # Criar Tela == Frame
        self.title("Gerenciamento de Trânsito.py")
        self.geometry("800x600")


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
        self.search_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "search.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "search.png")), size=(27, 27))
        self.bg_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "bg_gradient.jpg")), size=(480, 450))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.large_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large.png")), size=(311, 243))


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

        self.table = ttk.Treeview(master=self.second_frame.tab("Motoristas"),
                                columns=columns,
                                height=20,
                                selectmode='browse',
                                show='headings')

        self.table.column("#1", anchor="c", minwidth=50, width=50)
        self.table.column("#2", anchor="w", minwidth=165, width=165)
        self.table.column("#3", anchor="c", minwidth=120, width=120)
        self.table.column("#4", anchor="c", minwidth=120, width=120)

        self.table.heading('id', text='ID')
        self.table.heading('nome', text='Nome')
        self.table.heading('cpf', text='CPF')
        self.table.heading('cnh', text='CNH')
        self.table.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.table.bind('<Motion>', 'break')
        motoristas = verMotorista()
        for motorista in motoristas:
            self.table.insert('', tkinter.END, values=motorista)
        
        def display_selected_item(a):
            selected_item = self.table.selection()[0]
            id = self.table.item(selected_item)['values'][0]
            print(f'O id selecionado é {id}')

        self.table.bind("<<TreeviewSelect>>", display_selected_item)

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
        self.table_veiculos.heading('id_motorista', text='Id Motorista')
        self.table_veiculos.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.table_veiculos.bind('<Motion>', 'break')
        veiculos = verAutomoveis()
        for veiculo in veiculos:
            self.table_veiculos.insert('', tkinter.END, values=veiculo)


        columns3 = ('id_multa', 'valor', 'data', 'id_motorista', 'id_automovel')
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
        self.table_multas.heading('id_motorista', text='Id Motorista')
        self.table_multas.heading('id_automovel', text='Id Automovel')
        self.table_multas.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.table_multas.bind('<Motion>', 'break')
        multas = verMultas()
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


        #-----------------------------------------------------------------------------------------------------------------------------------

        self.third_frame_label_motorista = customtkinter.CTkLabel(self.third_frame.tab("Motoristas") , text="Buscas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label_motorista.grid(row=0, column=0, padx=30, pady=(15, 15))
        self.third_frame_label_motorista = customtkinter.CTkLabel(self.third_frame.tab("Motoristas") , text="Realizar busca por Motoristas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label_motorista.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.third_frame_entry_motorista = customtkinter.CTkEntry(self.third_frame.tab("Motoristas"), placeholder_text="Nome ou Cpf")
        self.third_frame_entry_motorista.grid(row=2, column=0, columnspan=1, padx=(10, 0), pady=(10, 10), sticky="nsew")
        self.third_frame_main_button_1_motorista = customtkinter.CTkButton(self.third_frame.tab("Motoristas") , fg_color="transparent",command=self.button_search_motorista , border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.third_frame_main_button_1_motorista.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        columns_search_01 = ('id', 'nome', 'cpf', 'cnh')
        self.table_search_01 = ttk.Treeview(master=self.third_frame.tab("Motoristas"),
                                columns=columns_search_01,
                                height=5,
                                selectmode='browse',
                                show='headings')
        self.table_search_01.column("#1", anchor="c", minwidth=50, width=50)
        self.table_search_01.column("#2", anchor="w", minwidth=165, width=165)
        self.table_search_01.column("#3", anchor="c", minwidth=120, width=120)
        self.table_search_01.column("#4", anchor="c", minwidth=120, width=120)
        self.table_search_01.heading('id', text='ID')
        self.table_search_01.heading('nome', text='Nome')
        self.table_search_01.heading('cpf', text='CPF')
        self.table_search_01.heading('cnh', text='CNH')
        self.table_search_01.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.table_search_01.bind('<Motion>', 'break')




        
        

        #-----------------------------------------------------------------------------------------------------------------------------------

        self.third_frame_label_veiculo = customtkinter.CTkLabel(self.third_frame.tab("Veiculos") , text="Buscas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label_veiculo.grid(row=0, column=0, padx=30, pady=(15, 15))
        self.third_frame_label_veiculo = customtkinter.CTkLabel(self.third_frame.tab("Veiculos") , text="Realizar busca por Veiculos",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label_veiculo.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.third_frame_entry_veiculo = customtkinter.CTkEntry(self.third_frame.tab("Veiculos") , placeholder_text="Placa ou Id")
        self.third_frame_entry_veiculo.grid(row=2, column=0, columnspan=1, padx=(10, 0), pady=(10, 10), sticky="nsew")
        self.third_frame_main_button_1_veiculo = customtkinter.CTkButton(self.third_frame.tab("Veiculos") ,command=self.button_search_veiculo, fg_color="transparent", border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.third_frame_main_button_1_veiculo.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        columns20 = ('id', 'placa', 'chassi', 'tipo', 'id_motorista')
        self.table_search_02 = ttk.Treeview(master=self.third_frame.tab("Veiculos"),
                                columns=columns20,
                                height=5,
                                selectmode='browse',
                                show='headings')

        self.table_search_02.column("#1", anchor="c", minwidth=50, width=50)
        self.table_search_02.column("#2", anchor="c", minwidth=100, width=100)
        self.table_search_02.column("#3", anchor="c", minwidth=120, width=120)
        self.table_search_02.column("#4", anchor="c", minwidth=120, width=120)
        self.table_search_02.column("#5", anchor="c", minwidth=120, width=120)

        self.table_search_02.heading('id', text='ID')
        self.table_search_02.heading('placa', text='Placa')
        self.table_search_02.heading('chassi', text='Chassi')
        self.table_search_02.heading('tipo', text='Tipo')
        self.table_search_02.heading('id_motorista', text='Id Motorista')
        self.table_search_02.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.table_search_02.bind('<Motion>', 'break')

        #-----------------------------------------------------------------------------------------------------------------------------------

        self.third_frame_label_multa = customtkinter.CTkLabel(self.third_frame.tab("Multas") , text="Buscas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label_multa.grid(row=0, column=0, padx=30, pady=(15, 15))
        self.third_frame_label_multa = customtkinter.CTkLabel(self.third_frame.tab("Multas") , text="Realizar busca por Multas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label_multa.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.third_frame_entry_multa = customtkinter.CTkEntry(self.third_frame.tab("Multas") , placeholder_text="Id ou Data")
        self.third_frame_entry_multa.grid(row=2, column=0, columnspan=1, padx=(10, 0), pady=(10, 10), sticky="nsew")
        self.third_frame_main_button_1_multa = customtkinter.CTkButton(self.third_frame.tab("Multas") ,command=self.button_search_multa , fg_color="transparent", border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.third_frame_main_button_1_multa.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        columns30 = ('id_multa', 'valor', 'data', 'id_motorista', 'id_automovel')
        self.table_search_03 = ttk.Treeview(master=self.third_frame.tab("Multas"),
                                columns=columns30,
                                height=5,
                                selectmode='browse',
                                show='headings')

        self.table_search_03.column("#1", anchor="c", minwidth=50, width=50)
        self.table_search_03.column("#2", anchor="c", minwidth=100, width=100)
        self.table_search_03.column("#3", anchor="c", minwidth=120, width=120)
        self.table_search_03.column("#4", anchor="c", minwidth=120, width=120)
        self.table_search_03.column("#5", anchor="c", minwidth=120, width=120)

        self.table_search_03.heading('id_multa', text='Id Multa')
        self.table_search_03.heading('valor', text='Valor')
        self.table_search_03.heading('data', text='Data')
        self.table_search_03.heading('id_motorista', text='Id Motorista')
        self.table_search_03.heading('id_automovel', text='Id Automovel')
        self.table_search_03.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.table_search_03.bind('<Motion>', 'break')





        # Gráficos
        self.fourth_frame = customtkinter.CTkTabview(self, corner_radius=20, border_width=5)
        self.fourth_frame.grid(row=1, column=0, padx=20, pady=10)
        self.fourth_frame.add("Motoristas")
        self.fourth_frame.add("Veiculos")
        self.fourth_frame.add("Multas")
        self.fourth_frame.tab("Motoristas").grid_columnconfigure(0, weight=1) 
        self.fourth_frame.tab("Veiculos").grid_columnconfigure(0, weight=1)
        self.fourth_frame.tab("Multas").grid_columnconfigure(0, weight=1)
        self.fifth_frame_label = customtkinter.CTkLabel(self.fourth_frame.tab("Motoristas") , text="Gráficos",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fifth_frame_label.grid(row=0, column=0, padx=30, pady=(15, 15))


        # Criando figura
        self.figura = plt.figure(figsize=(8,4), dpi=60)
        self.grafico = self.figura.add_subplot(111)
        canva = FigureCanvasTkAgg(self.figura, self.fourth_frame.tab("Motoristas"))
        canva.get_tk_widget().grid(row=1, column=0)


     
        # dados
        np.random.seed(19680801)
        veiculos_lista = ('Carros', 'Motos', 'Caminhões', 'Ônibus')
        y_pos = np.arange(len(veiculos_lista))
        performance = 3 + 10 * np.random.rand(len(veiculos_lista))
        error = np.random.rand(len(veiculos_lista))

        self.grafico.barh(y_pos, performance, xerr=error, align='center')
        self.grafico.set_yticks(y_pos, labels=veiculos_lista)
        self.grafico.invert_yaxis() 
        self.grafico.set_xlabel('24 de Abril - 2023')
        self.grafico.set_title('Número de Multas diárias')





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
        self.fifth_frame_new_add = customtkinter.CTkFrame(self.fifth_frame.tab("Motoristas") , border_width=5, width=400, height=337,)
        self.fifth_frame_new_add.grid_columnconfigure(0, weight=1)


        self.fifth_frame_new_add_label_motorista = customtkinter.CTkLabel(self.fifth_frame_new_add , text="""Digite os dados do motorista
que deseja adicionar""",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fifth_frame_new_add_label_motorista.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.fifth_frame_add_entry_name = customtkinter.CTkEntry(self.fifth_frame_new_add, placeholder_text="Nome Completo")
        self.fifth_frame_add_entry_name.grid(row=1, column=0,  pady=(5, 5), sticky='n')
        self.fifth_frame_add_entry_cpf = customtkinter.CTkEntry(self.fifth_frame_new_add, placeholder_text="CPF")
        self.fifth_frame_add_entry_cpf.grid(row=2, column=0,  pady=5, sticky='n')
        self.fifth_frame_add_entry_cnh = customtkinter.CTkEntry(self.fifth_frame_new_add, placeholder_text="CNH")
        self.fifth_frame_add_entry_cnh.grid(row=3, column=0,  pady=5, sticky='n')
        self.fifth_frame_add_main_button_1 = customtkinter.CTkButton(self.fifth_frame_new_add , fg_color="transparent",command=self.button_add_motorista  , border_width=2,text="cadastrar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_add_main_button_1.grid(row=6, column=0,  pady=(5, 20), sticky='n')

        # self.fifth_frame_checkbox_1 = customtkinter.CTkCheckBox(master=self.fifth_frame_new, text='Aceito os termos de Cadastro')
        # self.fifth_frame_checkbox_1.grid(row=4, column=0, pady=5)


        # Administrar - Atualizar Motorista
        self.fifth_frame_new_update = customtkinter.CTkFrame(self.fifth_frame.tab("Motoristas") , border_width=5, width=400, height=337,)
        self.fifth_frame_new_update.grid_columnconfigure(0, weight=1)

        self.fifth_frame_new_update_label_motorista = customtkinter.CTkLabel(self.fifth_frame_new_update , text="""Busque e Selecione o motorista
que deseja atualizar""",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fifth_frame_new_update_label_motorista.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.fifth_frame_new_update_entry_motorista = customtkinter.CTkEntry(self.fifth_frame_new_update, placeholder_text="Nome ou Cpf")
        self.fifth_frame_new_update_entry_motorista.grid(row=1, column=0, pady=5, sticky="n")
        self.fifth_frame_new_update_main_button_1_motorista = customtkinter.CTkButton(self.fifth_frame_new_update , fg_color="transparent",command=self.button_search_motorista_add , border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_new_update_main_button_1_motorista.grid(row=2, column=0, pady=5, sticky="n")

        columns_search_2000 = ('id', 'nome', 'cpf', 'cnh')
        self.table_search_2000 = ttk.Treeview(master=self.fifth_frame_new_update,
                                columns=columns_search_2000,
                                height=5,
                                selectmode='browse',
                                show='headings')
        self.table_search_2000.column("#1", anchor="c", minwidth=50, width=50)
        self.table_search_2000.column("#2", anchor="w", minwidth=165, width=165)
        self.table_search_2000.column("#3", anchor="c", minwidth=120, width=120)
        self.table_search_2000.column("#4", anchor="c", minwidth=120, width=120)
        self.table_search_2000.heading('id', text='ID')
        self.table_search_2000.heading('nome', text='Nome')
        self.table_search_2000.heading('cpf', text='CPF')
        self.table_search_2000.heading('cnh', text='CNH')
        self.table_search_2000.grid(row=3, column=0, sticky='nsew', padx=10, pady=(5,5))
        self.table_search_2000.bind('<Motion>', 'break')

        self.fifth_frame_update_entry_name = customtkinter.CTkEntry(self.fifth_frame_new_update, placeholder_text="Novo - Nome")
        self.fifth_frame_update_entry_name.grid(row=4, column=0, pady=5, sticky="n")
        self.fifth_frame_update_entry_cpf = customtkinter.CTkEntry(self.fifth_frame_new_update, placeholder_text="Novo - CPF")
        self.fifth_frame_update_entry_cpf.grid(row=5, column=0, pady=5, sticky="n")
        self.fifth_frame_update_entry_cnh = customtkinter.CTkEntry(self.fifth_frame_new_update, placeholder_text="Novo - CNH")
        self.fifth_frame_update_entry_cnh.grid(row=6, column=0, pady=5, sticky="n")

        id_final = 0
        def display_selected_item(a):
            selected_item = self.table_search_2000.selection()[0]
            id_select = self.table_search_2000.item(selected_item)['values'][0]
            global id_final
            id_final = id_select
            print(f'O id selecionado é {id_final}')
        self.table_search_2000.bind("<<TreeviewSelect>>", display_selected_item)

        self.fifth_frame_new_update_main_button_1_motorista_2 = customtkinter.CTkButton(self.fifth_frame_new_update , fg_color="transparent",command=self.button_update_motorista , border_width=2,text="Atualizar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_new_update_main_button_1_motorista_2.grid(row=7, column=0, pady=(5,23), sticky="n")

        # Administrar - Remover Motorista
        self.fifth_frame_new_delete = customtkinter.CTkFrame(self.fifth_frame.tab("Motoristas") , border_width=5, width=400, height=337,)
        self.fifth_frame_new_delete.grid_columnconfigure(0, weight=1)

        self.fifth_frame_new_delete_label_motorista = customtkinter.CTkLabel(self.fifth_frame_new_delete , text="""Busque e Selecione o motorista
que deseja remover""",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.fifth_frame_new_delete_label_motorista.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.fifth_frame_new_delete_entry_motorista = customtkinter.CTkEntry(self.fifth_frame_new_delete, placeholder_text="Nome ou Cpf")
        self.fifth_frame_new_delete_entry_motorista.grid(row=1, column=0, pady=5, sticky="n")
        self.fifth_frame_new_delete_main_button_1_motorista = customtkinter.CTkButton(self.fifth_frame_new_delete , fg_color="transparent", border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_new_delete_main_button_1_motorista.grid(row=2, column=0, pady=5, sticky="n")

        columns_search_3000 = ('id', 'nome', 'cpf', 'cnh')
        self.table_search_3000 = ttk.Treeview(master=self.fifth_frame_new_delete,
                                columns=columns_search_3000,
                                height=5,
                                selectmode='browse',
                                show='headings')
        self.table_search_3000.column("#1", anchor="c", minwidth=50, width=50)
        self.table_search_3000.column("#2", anchor="w", minwidth=165, width=165)
        self.table_search_3000.column("#3", anchor="c", minwidth=120, width=120)
        self.table_search_3000.column("#4", anchor="c", minwidth=120, width=120)
        self.table_search_3000.heading('id', text='ID')
        self.table_search_3000.heading('nome', text='Nome')
        self.table_search_3000.heading('cpf', text='CPF')
        self.table_search_3000.heading('cnh', text='CNH')
        self.table_search_3000.grid(row=3, column=0, sticky='nsew', padx=10, pady=(5,5))
        self.table_search_3000.bind('<Motion>', 'break')


        id_final = 0
        def display_selected_item(a):
            selected_item = self.table_search_3000.selection()[0]
            id_select = self.table_search_3000.item(selected_item)['values'][0]
            global id_final
            id_final = id_select
            print(f'O id selecionado é {id_final}')
        self.table_search_3000.bind("<<TreeviewSelect>>", display_selected_item)

        self.fifth_frame_new_update_main_button_1_motorista_2 = customtkinter.CTkButton(self.fifth_frame_new_delete , fg_color="transparent", border_width=2,text="Remover", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_new_update_main_button_1_motorista_2.grid(row=7, column=0, pady=(5,23), sticky="n")



        # Administrar - Veiculos - Topbar
        self.fifth_frame_topbar_veiculos = customtkinter.CTkFrame(master=self.fifth_frame.tab("Veiculos"))
        self.fifth_frame_topbar_veiculos.grid_columnconfigure(0, weight=1)
        self.fifth_frame_topbar_veiculos.grid()

        self.fifth_frame_topbar_veiculos_button_1 = customtkinter.CTkButton(master=self.fifth_frame_topbar_veiculos , text='Adicionar')
        self.fifth_frame_topbar_veiculos_button_1.grid(row=0, column=0, padx=5)
        self.fifth_frame_topbar_veiculos_button_2 = customtkinter.CTkButton(master=self.fifth_frame_topbar_veiculos , text='Atualizar')
        self.fifth_frame_topbar_veiculos_button_2.grid(row=0, column=1, padx=5)
        self.fifth_frame_topbar_veiculos_button_3 = customtkinter.CTkButton(master=self.fifth_frame_topbar_veiculos , text='Remover')
        self.fifth_frame_topbar_veiculos_button_3.grid(row=0, column=2, padx=5)

        # Administrar - Adicionar Veiculo

        self.fifth_frame_motorista = customtkinter.CTkFrame(self.fifth_frame.tab("Veiculos") , border_width=5, width=400, height=337,)
        self.fifth_frame_motorista.grid_columnconfigure(0, weight=1)
        self.fifth_frame_motorista.grid(columnspan=3,pady=10,sticky='ew')

        self.fifth_frame_add_entry_placa = customtkinter.CTkEntry(self.fifth_frame_motorista, placeholder_text="Placa")
        self.fifth_frame_add_entry_placa.grid(row=0, column=0,  pady=(20, 5), sticky='n')
        self.fifth_frame_add_entry_chassi = customtkinter.CTkEntry(self.fifth_frame_motorista, placeholder_text="Chassi")
        self.fifth_frame_add_entry_chassi.grid(row=1, column=0,  pady=5, sticky='n')
        self.fifth_frame_add_entry_tipo = customtkinter.CTkEntry(self.fifth_frame_motorista, placeholder_text="Tipo")
        self.fifth_frame_add_entry_tipo.grid(row=3, column=0,  pady=5, sticky='n')
        self.fifth_frame_add_main_button_1 = customtkinter.CTkButton(self.fifth_frame_motorista , fg_color="transparent", border_width=2,text="cadastrar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_add_main_button_1.grid(row=6, column=0,  pady=(5, 20), sticky='n')


        # Administrar - Multas - Topbar
        self.fifth_frame_topbar_multas = customtkinter.CTkFrame(master=self.fifth_frame.tab("Multas"))
        self.fifth_frame_topbar_multas.grid_columnconfigure(0, weight=1)
        self.fifth_frame_topbar_multas.grid()

        self.fifth_frame_topbar_multas_button_1 = customtkinter.CTkButton(master=self.fifth_frame_topbar_multas , text='Adicionar')
        self.fifth_frame_topbar_multas_button_1.grid(row=0, column=0, padx=5)
        self.fifth_frame_topbar_multas_button_2 = customtkinter.CTkButton(master=self.fifth_frame_topbar_multas , text='Atualizar')
        self.fifth_frame_topbar_multas_button_2.grid(row=0, column=1, padx=5)
        self.fifth_frame_topbar_multas_button_3 = customtkinter.CTkButton(master=self.fifth_frame_topbar_multas , text='Remover')
        self.fifth_frame_topbar_multas_button_3.grid(row=0, column=2, padx=5)

        # Administrar - Adicionar Multa
        self.fifth_frame_motorista = customtkinter.CTkFrame(self.fifth_frame.tab("Multas") , border_width=5, width=400, height=337,)
        self.fifth_frame_motorista.grid_columnconfigure(0, weight=1)
        self.fifth_frame_motorista.grid(columnspan=3,pady=10,sticky='ew')

        self.fifth_frame_add_entry_veiculo = customtkinter.CTkEntry(self.fifth_frame_motorista, placeholder_text="Veiculo")
        self.fifth_frame_add_entry_veiculo.grid(row=0, column=0,  pady=(20, 5), sticky='n')
        self.fifth_frame_add_entry_motorista = customtkinter.CTkEntry(self.fifth_frame_motorista, placeholder_text="Motorista")
        self.fifth_frame_add_entry_motorista.grid(row=1, column=0,  pady=5, sticky='n')
        self.fifth_frame_add_entry_data = customtkinter.CTkEntry(self.fifth_frame_motorista, placeholder_text="Data")
        self.fifth_frame_add_entry_data.grid(row=3, column=0,  pady=5, sticky='n')
        self.fifth_frame_add_entry_valor = customtkinter.CTkEntry(self.fifth_frame_motorista, placeholder_text="Valor")
        self.fifth_frame_add_entry_valor.grid(row=4, column=0,  pady=5, sticky='n')
        self.fifth_frame_add_main_button_1 = customtkinter.CTkButton(self.fifth_frame_motorista , fg_color="transparent", border_width=2,text="cadastrar", text_color=("gray10", "#DCE4EE"))
        self.fifth_frame_add_main_button_1.grid(row=6, column=0,  pady=(5,20), sticky='n')


        # Administrar Logado
        self.sixth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sixth_frame.grid_columnconfigure(0, weight=1)
        self.sixth_frame_large_image_label = customtkinter.CTkLabel(self.sixth_frame, text="", image=self.large_image)
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
        #print("username:", self.home_frame_username_entry.get(), "password:", self.home_frame_password_entry.get())
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
        resultados = buscarMotorista(self.third_frame_entry_motorista.get())
        for item in self.table_search_01.get_children():
            self.table_search_01.delete(item)

        for motorista in resultados:
            self.table_search_01.insert('', tkinter.END, values=motorista)

    def button_search_motorista_add(self):
        resultados = buscarMotorista(self.fifth_frame_new_update_entry_motorista.get())
        for item in self.table_search_01.get_children():
            self.table_search_2000.delete(item)

        for motorista in resultados:
            self.table_search_2000.insert('', tkinter.END, values=motorista)

    def button_search_motorista_delete(self):
        resultados = buscarMotorista(self.fifth_frame_new_update_entry_motorista.get())
        for item in self.table_search_01.get_children():
            self.table_search_3000.delete(item)

        for motorista in resultados:
            self.table_search_3000.insert('', tkinter.END, values=motorista)


    def button_search_veiculo(self):
        resultados = buscarAutomovel(self.third_frame_entry_veiculo.get())
        for item in self.table_search_02.get_children():
            self.table_search_02.delete(item)

        for veiculo in resultados:
            self.table_search_02.insert('', tkinter.END, values=veiculo)

    def button_search_multa(self):
        resultados = buscarMulta(self.third_frame_entry_veiculo.get())
        for item in self.table_search_03.get_children():
            self.table_search_03.delete(item)

        for veiculo in resultados:
            self.table_search_03.insert('', tkinter.END, values=veiculo)

    
    def button_add_motorista(self):
        name = self.fifth_frame_add_entry_name.get()
        cpf = self.fifth_frame_add_entry_cpf.get()
        cnh = self.fifth_frame_add_entry_cnh.get()
        inserirMotorista(name,cpf,cnh)

        for item in self.table.get_children():
            self.table.delete(item)

        motoristas = verMotorista()
        for motorista in motoristas:
            self.table.insert('', tkinter.END, values=motorista)

    def button_update_motorista(self):
        global id_final
        name = self.fifth_frame_update_entry_name.get()
        cpf = self.fifth_frame_update_entry_cpf.get()
        cnh = self.fifth_frame_update_entry_cnh.get()
        atualizarMotorista(id_final, name, cpf, cnh)

        for item in self.table.get_children():
            self.table.delete(item)

        motoristas = verMotorista()
        for motorista in motoristas:
            self.table.insert('', tkinter.END, values=motorista)


    def main_button_add_motorista(self):
        self.fifth_frame_new_update.grid_forget()
        self.fifth_frame_new_delete.grid_forget()
        self.fifth_frame_new_add.grid(columnspan=3,pady=10,sticky='ew')


        

    def main_button_update_motorista(self):
        self.fifth_frame_new_add.grid_forget()
        self.fifth_frame_new_delete.grid_forget()
        self.fifth_frame_new_update.grid(columnspan=3,pady=10,sticky='ew')
    


    def main_button_remove_motorista(self):
        self.fifth_frame_new_add.grid_forget()
        self.fifth_frame_new_update.grid_forget()
        self.fifth_frame_new_delete.grid(columnspan=3,pady=10,sticky='ew')


        

        


app = App()
app.mainloop()