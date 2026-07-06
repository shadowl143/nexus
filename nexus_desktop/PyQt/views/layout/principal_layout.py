import ttkbootstrap as tb 
from nexus_desktop.tkinter.views.component.button_component import WidgetButtons
from nexus_core.design_tokens import TYPOGRAPHY

class WindowsPrincipal():
    def __init__(self, pantallas: dict[str, tb.Frame]):
        self.root = tb.Window(themename="flatly") 
        self.root.title("Proyecto integrador")
        self.root.minsize(900, 700)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)  
        self.pantallas = pantallas
        self.menu_lateral = tb.Frame(self.root, width= 150, relief="solid")
        # 2. ¡CRUCIAL! Evita que el Frame se encoja al tamaño de los textos
        self.menu_lateral.pack_propagate(False) 
        self.menu_lateral.pack(side= "left", fill="y", padx=(0, 10))
        self.windows = ""
        self.mostrar_pantalla("Riders")
        self.crear_botones_menu()


    def crear_botones_menu(self):
        # Crear un botón para cada pantalla disponible
        for nombre_pantalla in self.pantallas.keys():
            boton = tb.Button(
                self.menu_lateral, 
                text=nombre_pantalla, 
                bootstyle="link",
                command=lambda name=nombre_pantalla: self.select_frame(name)
            )
            boton.pack(fill="x", padx=15, pady=8, anchor="w") 

    def mostrar_pantalla(self, nombre_pantalla):
        print(self.pantallas)
        for nombre, creador_frame in self.pantallas.items():
            # Ejecutamos la función fábrica pasando el contenedor adecuado
            self.pantallas[nombre] = creador_frame(self.root)
            self.pantallas[nombre].pack_forget()
        self.windows = nombre_pantalla
        self.pantallas[nombre_pantalla].pack(fill="both", expand=True)

    def select_frame(self, name):
        print(self.windows)
        self.pantallas[self.windows].pack_forget()
        self.pantallas[name].pack(fill="both", expand=True)
        self.windows = name


    def iniciar(self):
        self.root.mainloop()
