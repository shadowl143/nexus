import ttkbootstrap as tb 
from nexus_desktop.tkinter.views.component.button_component import WidgetButtons
from nexus_core.design_tokens import TYPOGRAPHY

class WindowsPrincipal():
    def __init__(self, pantallas: dict[str, tb.Frame]):
        self.root = tb.Window(themename="flatly") 
        self.root.title("Ventan Interactiva")
        self.root.minsize(900, 700)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)  
        self.pantallas = pantallas
        self.menu_lateral = tb.Frame(self.root, width= 150, relief="solid")
        # 2. ¡CRUCIAL! Evita que el Frame se encoja al tamaño de los textos
        self.menu_lateral.pack_propagate(False) 
        self.menu_lateral.pack(side= "left", fill="y", padx=(0, 10))
        self.menu_superior()
        self.crear_botones_menu()
        self.mostrar_pantalla("Inicio")

    def menu_superior(self):
        menu_bar = tb.Menu(self.root)
        self.root.config(menu= menu_bar)
        menu_archivo = tb.Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label= "Archivo", menu= menu_archivo)
        menu_archivo.add_command(label="Idioma")
        menu_archivo.add_command(label="Color")

    def crear_botones_menu(self):
        # Crear un botón para cada pantalla disponible
        for nombre_pantalla in self.pantallas.keys():
            boton = tb.Button(
                self.menu_lateral, 
                text=nombre_pantalla, 
                bootstyle="link",
                command=lambda name=nombre_pantalla: self.mostrar_pantalla(name)
            )
            boton.pack(fill="x", padx=15, pady=8, anchor="w") 

    def mostrar_pantalla(self, nombre_pantalla):
        for nombre, creador_frame in self.pantallas.items():
            # Ejecutamos la función fábrica pasando el contenedor adecuado
            self.pantallas[nombre] = creador_frame(self.root)
        
        self.pantallas[nombre_pantalla].pack(fill="both", expand=True)

    def iniciar(self):
        self.root.mainloop()
