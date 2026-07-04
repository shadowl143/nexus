import tkinter as tk
import nexus_core.design_tokens as design
class WidgetButtons(tk.Frame):
    def __init__(self, parent : tk, event_save):
        super().__init__(parent)
        self.event_save = event_save
        self.create_button_save()

    def create_button_save(self):
        self.btn_save = tk.Button(
            self,
            text= "Guardar",
            bg=design.COLORS["bg.primary"],
            fg= design.TYPOGRAPHY["font.family.sans"],
            command= self.event_save
        )
        self.btn_save.pack(padx=5, pady=5)