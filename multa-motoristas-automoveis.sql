PGDMP         6                {            Multas    15.2    15.2      "           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            #           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            $           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            %           1262    16421    Multas    DATABASE        CREATE DATABASE "Multas" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "Multas";
                postgres    false            �            1259    27590 
   Automoveis    TABLE     �   CREATE TABLE public."Automoveis" (
    id_automovel integer NOT NULL,
    placa character(7) NOT NULL,
    chassi character(17) NOT NULL,
    tipo character varying(255) NOT NULL,
    id_motorista integer NOT NULL
);
     DROP TABLE public."Automoveis";
       public         heap    postgres    false            �            1259    27593    Automoveis_id_automovel_seq    SEQUENCE     �   ALTER TABLE public."Automoveis" ALTER COLUMN id_automovel ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Automoveis_id_automovel_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    214            �            1259    27594    Login    TABLE     �   CREATE TABLE public."Login" (
    id integer NOT NULL,
    login character varying(255) NOT NULL,
    senha character varying(255) NOT NULL,
    data_nascimento character(10),
    email character varying(255)
);
    DROP TABLE public."Login";
       public         heap    postgres    false            �            1259    27599    Login_id_seq    SEQUENCE     �   ALTER TABLE public."Login" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Login_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    216            �            1259    27600 
   Motoristas    TABLE     �   CREATE TABLE public."Motoristas" (
    id_motorista integer NOT NULL,
    nome character varying(255) NOT NULL,
    cpf character(11) NOT NULL,
    cnh character(11) NOT NULL
);
     DROP TABLE public."Motoristas";
       public         heap    postgres    false            �            1259    27603    Motoristas_id_motorista_seq    SEQUENCE     �   ALTER TABLE public."Motoristas" ALTER COLUMN id_motorista ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Motoristas_id_motorista_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    218            �            1259    27604    Multas    TABLE     �   CREATE TABLE public."Multas" (
    id_multa integer NOT NULL,
    valor real NOT NULL,
    data timestamp without time zone DEFAULT CURRENT_TIMESTAMP(0),
    id_motorista integer NOT NULL,
    id_automovel integer NOT NULL
);
    DROP TABLE public."Multas";
       public         heap    postgres    false            �            1259    27608    Multas_id_multa_seq    SEQUENCE     �   ALTER TABLE public."Multas" ALTER COLUMN id_multa ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Multas_id_multa_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    220                      0    27590 
   Automoveis 
   TABLE DATA           W   COPY public."Automoveis" (id_automovel, placa, chassi, tipo, id_motorista) FROM stdin;
    public          postgres    false    214   �%                 0    27594    Login 
   TABLE DATA           K   COPY public."Login" (id, login, senha, data_nascimento, email) FROM stdin;
    public          postgres    false    216   O&                 0    27600 
   Motoristas 
   TABLE DATA           D   COPY public."Motoristas" (id_motorista, nome, cpf, cnh) FROM stdin;
    public          postgres    false    218   �&                 0    27604    Multas 
   TABLE DATA           U   COPY public."Multas" (id_multa, valor, data, id_motorista, id_automovel) FROM stdin;
    public          postgres    false    220   �'       &           0    0    Automoveis_id_automovel_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public."Automoveis_id_automovel_seq"', 12, true);
          public          postgres    false    215            '           0    0    Login_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public."Login_id_seq"', 3, true);
          public          postgres    false    217            (           0    0    Motoristas_id_motorista_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public."Motoristas_id_motorista_seq"', 9, true);
          public          postgres    false    219            )           0    0    Multas_id_multa_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public."Multas_id_multa_seq"', 6, true);
          public          postgres    false    221            v           2606    27610     Automoveis Automoveis_chassi_key 
   CONSTRAINT     a   ALTER TABLE ONLY public."Automoveis"
    ADD CONSTRAINT "Automoveis_chassi_key" UNIQUE (chassi);
 N   ALTER TABLE ONLY public."Automoveis" DROP CONSTRAINT "Automoveis_chassi_key";
       public            postgres    false    214            x           2606    27612    Automoveis Automoveis_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public."Automoveis"
    ADD CONSTRAINT "Automoveis_pkey" PRIMARY KEY (id_automovel);
 H   ALTER TABLE ONLY public."Automoveis" DROP CONSTRAINT "Automoveis_pkey";
       public            postgres    false    214            z           2606    27614    Automoveis Automoveis_placa_key 
   CONSTRAINT     _   ALTER TABLE ONLY public."Automoveis"
    ADD CONSTRAINT "Automoveis_placa_key" UNIQUE (placa);
 M   ALTER TABLE ONLY public."Automoveis" DROP CONSTRAINT "Automoveis_placa_key";
       public            postgres    false    214            |           2606    27616    Login Login_email_key 
   CONSTRAINT     U   ALTER TABLE ONLY public."Login"
    ADD CONSTRAINT "Login_email_key" UNIQUE (email);
 C   ALTER TABLE ONLY public."Login" DROP CONSTRAINT "Login_email_key";
       public            postgres    false    216            ~           2606    27618    Login Login_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public."Login"
    ADD CONSTRAINT "Login_pkey" PRIMARY KEY (id);
 >   ALTER TABLE ONLY public."Login" DROP CONSTRAINT "Login_pkey";
       public            postgres    false    216            �           2606    27620    Motoristas Motoristas_cnh_key 
   CONSTRAINT     [   ALTER TABLE ONLY public."Motoristas"
    ADD CONSTRAINT "Motoristas_cnh_key" UNIQUE (cnh);
 K   ALTER TABLE ONLY public."Motoristas" DROP CONSTRAINT "Motoristas_cnh_key";
       public            postgres    false    218            �           2606    27622    Motoristas Motoristas_cpf_key 
   CONSTRAINT     [   ALTER TABLE ONLY public."Motoristas"
    ADD CONSTRAINT "Motoristas_cpf_key" UNIQUE (cpf);
 K   ALTER TABLE ONLY public."Motoristas" DROP CONSTRAINT "Motoristas_cpf_key";
       public            postgres    false    218            �           2606    27624    Motoristas Motoristas_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public."Motoristas"
    ADD CONSTRAINT "Motoristas_pkey" PRIMARY KEY (id_motorista);
 H   ALTER TABLE ONLY public."Motoristas" DROP CONSTRAINT "Motoristas_pkey";
       public            postgres    false    218            �           2606    27626    Multas Multas_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public."Multas"
    ADD CONSTRAINT "Multas_pkey" PRIMARY KEY (id_multa);
 @   ALTER TABLE ONLY public."Multas" DROP CONSTRAINT "Multas_pkey";
       public            postgres    false    220            �           2606    27627    Multas fk_automovel    FK CONSTRAINT     �   ALTER TABLE ONLY public."Multas"
    ADD CONSTRAINT fk_automovel FOREIGN KEY (id_automovel) REFERENCES public."Automoveis"(id_automovel);
 ?   ALTER TABLE ONLY public."Multas" DROP CONSTRAINT fk_automovel;
       public          postgres    false    220    3192    214            �           2606    27632    Automoveis fk_motorista    FK CONSTRAINT     �   ALTER TABLE ONLY public."Automoveis"
    ADD CONSTRAINT fk_motorista FOREIGN KEY (id_motorista) REFERENCES public."Motoristas"(id_motorista);
 C   ALTER TABLE ONLY public."Automoveis" DROP CONSTRAINT fk_motorista;
       public          postgres    false    214    218    3204            �           2606    27637    Multas fk_motorista    FK CONSTRAINT     �   ALTER TABLE ONLY public."Multas"
    ADD CONSTRAINT fk_motorista FOREIGN KEY (id_motorista) REFERENCES public."Motoristas"(id_motorista);
 ?   ALTER TABLE ONLY public."Multas" DROP CONSTRAINT fk_motorista;
       public          postgres    false    218    220    3204               �   x�u�=�@��:9��e��Tjo`����M��G�b���Xe�g��D�xj A��S.u}Ps����Gp�q��x�ߚs�Z2AI �}��v�񻸨.�֍������IU"${)�YM&ds��EI!;����jfV3O���,�HHv���
�{���ؕ/f�  i^.         K   x�3�LL��̃���@dd``pH�M���K���2�,�L.�/�4426AVFRi̙TT����,��.F��� %�#�         �   x�U�Mn�@���)|���(��n�uՍI5����yz.FP�ΰ�-}z�oz�U���U=8/ʪn�/���)˱�{0c�$��Y��x�M�z+N��}�����O�A����f�"�
�Ō�А�\FX���ۓ�_�LHl��m�����ԭ��:ߚ�\G�b=��ѫ��}z�7Q��.�8z1�/��-���k�e��_^{         U   x�U���0��=�IS����s � E��d[P$�<�e3f��C��(u8k�^v({�ܵ3�1?U����Z����'�8~     