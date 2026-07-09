from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.style import Style
import nexus_core.design_tokens as design


class MessageBox(Messagebox):
    def __init__(self, parent, title: str, message: str, icon="info"):
        super().__init__()
        self.parent = parent
        self.title = title
        self.message = message
        style = Style()
        style.configure(
            ".",
            font=(
                design.TYPOGRAPHY["font.family.sans"],
                design.TYPOGRAPHY["font.size.body"],
            ),
        )
        style.configure(
            "TButton",
            font=(
                design.TYPOGRAPHY["font.family.sans"],
                design.TYPOGRAPHY["font.size.body"],
            ),
        )
        self.principal = design.COLORS["accent.primary"]
        self.cancel = design.COLORS["accent.danger"]

    def msg_save(self) -> str:
        respuesta = Messagebox.yesno(
            title=self.title,
            message=self.message,
            parent=self.parent,
            buttons=[
                f"Si:{self.principal}",
                f"No:{self.cancel}",
            ],
        )
        return respuesta

    def msg_information(self) -> None:
        respuesta = Messagebox.show_info(
            title=self.title,
            message=self.message,
            parent=self.parent,
            buttons=[
                f"Ok:{self.principal}",
            ],
        )
