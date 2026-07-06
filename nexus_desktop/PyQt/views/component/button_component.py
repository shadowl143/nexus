import ttkbootstrap as tb
import nexus_core.design_tokens as design
class WidgetButtons(tb.Frame):
    def __init__(self, parent, event_save, button_text="Guardar"):
        style = tb.Style()
        style.configure("Custom.Button",
                        background=design.COLORS["bg.primary"],  # Color de fondo
                        foreground=design.COLORS["bg.primary"],    # Color del texto
                        font=(design.TYPOGRAPHY["font.family.sans"], design.TYPOGRAPHY["font.size.body"], "bold"))  # Fuente y tamaño)
        super().__init__(parent)
        self.event_save = event_save
        self.button_text = button_text
        self.bootstyle = "Custom.Button"
        self.create_button_save()

    def create_button_save(self):
        # Crear un botón genérico con estilo
        self.btn_save = tb.Button(
            self,
            text=self.button_text,
            bootstyle=self.bootstyle,
            command=self.event_save
        )
        self.btn_save.pack(pady=10)