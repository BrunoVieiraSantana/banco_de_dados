import customtkinter
import tkinter.ttk as ttk
import tkinter
import tksheet
import os
from PIL import Image
from back import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


login=False
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        # Criar Tela == Frame
        self.title("Gerenciamento de Trânsito.py")
        self.geometry("700x450")






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
Trânsito""", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
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
        self.home_frame_label = customtkinter.CTkLabel(self.home_frame , text="Página de Login",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.home_frame_label.grid(row=0, column=1, padx=170, pady=(110, 15))
        self.home_frame_username_entry = customtkinter.CTkEntry(self.home_frame , width=200, placeholder_text="login")
        self.home_frame_username_entry.grid(row=1, column=1, padx=30, pady=(15, 15))
        self.home_frame_password_entry = customtkinter.CTkEntry(self.home_frame , width=200, show="*", placeholder_text="password")
        self.home_frame_password_entry.grid(row=2, column=1, padx=30, pady=(0, 15))
        self.home_frame_login_button = customtkinter.CTkButton(self.home_frame , text="Login", command=self.login_event, width=200)
        self.home_frame_login_button.grid(row=3, column=1, padx=30, pady=(15, 15))



        # Visualizar
        self.second_frame = customtkinter.CTkTabview(self, corner_radius=20, border_width=5)
        self.second_frame.grid(row=1, column=0, padx=20, pady=10)
        self.second_frame.add("Motoristas")
        self.second_frame.add("Veiculos")
        self.second_frame.add("Multas")
        self.second_frame.tab("Motoristas").grid_columnconfigure(0, weight=1) 
        self.second_frame.tab("Veiculos").grid_columnconfigure(0, weight=1)
        self.second_frame.tab("Multas").grid_columnconfigure(0, weight=1)

        columns = ('id', 'nome', 'cpf', 'rg')

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
        self.table.heading('rg', text='RG')
        self.table.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.table.bind('<Motion>', 'break')
        motoristas = []
        for n in range(1, 100):
            motoristas.append((f'{n}', f'Motorista {n}', f'rg - {n}', f'cpf - {n}'))
        for motorista in motoristas:
            self.table.insert('', tkinter.END, values=motorista)


        columns2 = ('id', 'nome', 'placa', 'chassi')
        self.table_veiculos = ttk.Treeview(master=self.second_frame.tab("Veiculos"),
                                columns=columns2,
                                height=20,
                                selectmode='browse',
                                show='headings')

        self.table_veiculos.column("#1", anchor="c", minwidth=50, width=50)
        self.table_veiculos.column("#2", anchor="w", minwidth=165, width=165)
        self.table_veiculos.column("#3", anchor="c", minwidth=120, width=120)
        self.table_veiculos.column("#4", anchor="c", minwidth=120, width=120)

        self.table_veiculos.heading('id', text='ID')
        self.table_veiculos.heading('nome', text='Nome')
        self.table_veiculos.heading('placa', text='Placa')
        self.table_veiculos.heading('chassi', text='Chassi')
        self.table_veiculos.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.table_veiculos.bind('<Motion>', 'break')
        veiculos = []
        for n in range(1, 100):
            veiculos.append((f'{n}', f'Veiculo {n}', f'placa - {n}', f'chassi - {n}'))
        for veiculo in veiculos:
            self.table_veiculos.insert('', tkinter.END, values=veiculo)




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

        self.third_frame_label = customtkinter.CTkLabel(self.third_frame.tab("Motoristas") , text="Buscas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label.grid(row=0, column=0, padx=30, pady=(15, 15))
        self.third_frame_label = customtkinter.CTkLabel(self.third_frame.tab("Motoristas") , text="Realizar busca por Motoristas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.third_frame_entry = customtkinter.CTkEntry(self.third_frame.tab("Motoristas"), placeholder_text="Nome ou Cpf")
        self.third_frame_entry.grid(row=2, column=0, columnspan=1, padx=(10, 0), pady=(10, 10), sticky="nsew")
        self.third_frame_main_button_1 = customtkinter.CTkButton(self.third_frame.tab("Motoristas") , fg_color="transparent", border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.third_frame_main_button_1.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        columns_search_01 = ('id', 'nome', 'cpf', 'rg')
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
        self.table_search_01.heading('rg', text='RG')
        self.table_search_01.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.table_search_01.bind('<Motion>', 'break')

        #-----------------------------------------------------------------------------------------------------------------------------------

        self.third_frame_label = customtkinter.CTkLabel(self.third_frame.tab("Veiculos") , text="Buscas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label.grid(row=0, column=0, padx=30, pady=(15, 15))
        self.third_frame_label = customtkinter.CTkLabel(self.third_frame.tab("Veiculos") , text="Realizar busca por Veiculos",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.third_frame_entry = customtkinter.CTkEntry(self.third_frame.tab("Veiculos") , placeholder_text="Placa ou Chassi")
        self.third_frame_entry.grid(row=2, column=0, columnspan=1, padx=(10, 0), pady=(10, 10), sticky="nsew")
        self.third_frame_main_button_1 = customtkinter.CTkButton(self.third_frame.tab("Veiculos") , fg_color="transparent", border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.third_frame_main_button_1.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        columns20 = ('id', 'nome', 'placa', 'chassi')
        self.table_veiculos_b = ttk.Treeview(self.third_frame.tab("Veiculos") ,
                                columns=columns20,
                                height=5,
                                selectmode='browse',
                                show='headings')

        self.table_veiculos_b.column("#1", anchor="c", minwidth=50, width=50)
        self.table_veiculos_b.column("#2", anchor="w", minwidth=165, width=165)
        self.table_veiculos_b.column("#3", anchor="c", minwidth=120, width=120)
        self.table_veiculos_b.column("#4", anchor="c", minwidth=120, width=120)

        self.table_veiculos_b.heading('id', text='ID')
        self.table_veiculos_b.heading('nome', text='Nome')
        self.table_veiculos_b.heading('placa', text='Placa')
        self.table_veiculos_b.heading('chassi', text='Chassi')
        self.table_veiculos_b.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.table_veiculos_b.bind('<Motion>', 'break')

        #-----------------------------------------------------------------------------------------------------------------------------------

        self.third_frame_label = customtkinter.CTkLabel(self.third_frame.tab("Multas") , text="Buscas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label.grid(row=0, column=0, padx=30, pady=(15, 15))
        self.third_frame_label = customtkinter.CTkLabel(self.third_frame.tab("Multas") , text="Realizar busca por Multas",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_label.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.third_frame_entry = customtkinter.CTkEntry(self.third_frame.tab("Multas") , placeholder_text="Id ou Data")
        self.third_frame_entry.grid(row=2, column=0, columnspan=1, padx=(10, 0), pady=(10, 10), sticky="nsew")
        self.third_frame_main_button_2 = customtkinter.CTkButton(self.third_frame.tab("Multas") , fg_color="transparent", border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.third_frame_main_button_2.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")



        # Gráficos
        self.four_frame = customtkinter.CTkTabview(self, corner_radius=20, border_width=5)
        self.four_frame.grid(row=1, column=0, padx=20, pady=10)
        self.four_frame.add("Motoristas")
        self.four_frame.add("Veiculos")
        self.four_frame.add("Multas")
        self.four_frame.tab("Motoristas").grid_columnconfigure(0, weight=1) 
        self.four_frame.tab("Veiculos").grid_columnconfigure(0, weight=1)
        self.four_frame.tab("Multas").grid_columnconfigure(0, weight=1)
        self.five_frame_label = customtkinter.CTkLabel(self.four_frame.tab("Motoristas") , text="Gráficos",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.five_frame_label.grid(row=0, column=0, padx=30, pady=(15, 15))


        # Criando figura
        self.figura = plt.figure(figsize=(8,4), dpi=60)
        self.grafico = self.figura.add_subplot(111)
        canva = FigureCanvasTkAgg(self.figura, self.four_frame.tab("Motoristas"))
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
        

        self.five_frame = customtkinter.CTkTabview(self, corner_radius=20, border_width=5)
        self.five_frame.grid(row=1, column=0, padx=0, pady=0)
        self.five_frame.add("Motoristas")
        self.five_frame.add("Veiculos")
        self.five_frame.add("Multas")
        self.five_frame.tab("Motoristas").grid_columnconfigure(0, weight=1) 
        self.five_frame.tab("Veiculos").grid_columnconfigure(0, weight=1)
        self.five_frame.tab("Multas").grid_columnconfigure(0, weight=1)

        self.five_frame_admin_button_1 = customtkinter.CTkButton(master=self.five_frame.tab("Motoristas"), text='Adicionar')
        self.five_frame_admin_button_1.grid(row=0, column=0, padx=5, pady=0)
        self.five_frame_admin_button_2 = customtkinter.CTkButton(master=self.five_frame.tab("Motoristas"), text='Atualizar')
        self.five_frame_admin_button_2.grid(row=0, column=1, padx=5, pady=0)
        self.five_frame_admin_button_3 = customtkinter.CTkButton(master=self.five_frame.tab("Motoristas"), text='Remover')
        self.five_frame_admin_button_3.grid(row=0, column=2, padx=5, pady=0)

        self.five_frame_new = customtkinter.CTkFrame(self.five_frame.tab("Motoristas") , border_width=5, width=400, height=337,)
        self.five_frame_new.grid(columnspan=3,pady=10,sticky='ew')


        # self.five_frame_add_label = customtkinter.CTkLabel(self.five_frame_add.tab("Motoristas") , text="Cadastro",
        #                                           font=customtkinter.CTkFont(size=15, weight="bold"))
        # self.five_frame_add_label.grid(row=0, column=0, padx=30, pady=(15, 15))
        # self.five_frame_add_label = customtkinter.CTkLabel(self.five_frame_add.tab("Motoristas") , text="Realizar busca por Motoristas",
        #                                           font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.five_frame_add_label.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.five_frame_add_entry = customtkinter.CTkEntry(self.five_frame_new, placeholder_text="Nome Completo")
        self.five_frame_add_entry.grid(row=0, column=0, padx=120, pady=(30, 10), sticky="n")
        self.five_frame_add_entry = customtkinter.CTkEntry(self.five_frame_new, placeholder_text="RG")
        self.five_frame_add_entry.grid(row=1, column=0, padx=120, pady=(10, 10), sticky="n")
        self.five_frame_add_entry = customtkinter.CTkEntry(self.five_frame_new, placeholder_text="CPF")
        self.five_frame_add_entry.grid(row=3, column=0, padx=120, pady=(10, 10), sticky="n")
        self.five_frame_checkbox_1 = customtkinter.CTkCheckBox(master=self.five_frame_new, text='Aceito os termos de Cadastro')
        self.five_frame_checkbox_1.grid(row=4, column=0, padx=120, pady=(10, 10), sticky="n")
        self.five_frame_add_main_button_1 = customtkinter.CTkButton(self.five_frame_new , fg_color="transparent", border_width=2,text="cadastrar", text_color=("gray10", "#DCE4EE"))
        self.five_frame_add_main_button_1.grid(row=6, column=0, padx=120, pady=50, sticky="nsew")




        self.five_frame_admin_button_1 = customtkinter.CTkButton(master=self.five_frame.tab("Veiculos"), text='Adicionar')
        self.five_frame_admin_button_1.grid(row=0, column=0, padx=5, pady=0)
        self.five_frame_admin_button_2 = customtkinter.CTkButton(master=self.five_frame.tab("Veiculos"), text='Atualizar')
        self.five_frame_admin_button_2.grid(row=0, column=1, padx=5, pady=0)
        self.five_frame_admin_button_3 = customtkinter.CTkButton(master=self.five_frame.tab("Veiculos"), text='Remover')
        self.five_frame_admin_button_3.grid(row=0, column=2, padx=5, pady=0)

        self.five_frame_new = customtkinter.CTkFrame(self.five_frame.tab("Veiculos") , border_width=5, width=400, height=337,)
        self.five_frame_new.grid(columnspan=3,pady=10,sticky='ew')



        self.five_frame_admin_button_1 = customtkinter.CTkButton(master=self.five_frame.tab("Multas"), text='Adicionar')
        self.five_frame_admin_button_1.grid(row=0, column=0, padx=5, pady=0)
        self.five_frame_admin_button_2 = customtkinter.CTkButton(master=self.five_frame.tab("Multas"), text='Atualizar')
        self.five_frame_admin_button_2.grid(row=0, column=1, padx=5, pady=0)
        self.five_frame_admin_button_3 = customtkinter.CTkButton(master=self.five_frame.tab("Multas"), text='Remover')
        self.five_frame_admin_button_3.grid(row=0, column=2, padx=5, pady=0)


        # Administrar Logado
        self.six_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.six_frame_large_image_label = customtkinter.CTkLabel(self.six_frame, text="", image=self.large_image)
        self.six_frame_large_image_label.grid(row=2, column=2, padx=105, pady=60)



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
            self.four_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.four_frame.grid_forget()

        if name == "frame_5":
            self.five_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.five_frame.grid_forget()
            
        if name == "frame_6":
            self.six_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.six_frame.grid_forget()


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
        print("username:", self.home_frame_username_entry.get(), "password:", self.home_frame_password_entry.get())
        global login
        login = True
        self.home_frame.grid_forget()  # remover login frame
        self.six_frame.grid(row=0, column=1, sticky="nsew")  # mostrar frame logado

        self.frame_2_button.grid(row=2, column=0, sticky="ew")
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        self.frame_4_button.grid(row=4, column=0, sticky="ew")
        self.frame_5_button.grid(row=5, column=0, sticky="ew")

        self.frame_6_button.grid(row=7, column=0, sticky="ew")

    def logout_event(self):
        self.six_frame.grid_forget()  # remover frame logado
        self.home_frame.grid(row=0, column=1, sticky="nsew")  # mostrar login frame 
        global login
        login = False

        self.frame_2_button.grid_forget()
        self.frame_3_button.grid_forget()
        self.frame_4_button.grid_forget()
        self.frame_5_button.grid_forget()

        self.frame_6_button.grid_forget()

        self.select_frame_by_name("home")




app = App()
app.mainloop()