import ttkbootstrap as tb


class WidgetButtons(tb.Button):
    DEFAULT_PADX = 15
    DEFAULT_PADY = 15

    def __init__(self, parent, button_text: str = "Guardar", command=None, **kwargs):
        super().__init__(
            parent,
            text=button_text,
            command=command,
            **kwargs,
        )

    # Defaults para pack
    def pack(self, **kwargs):
        kwargs.setdefault("padx", self.DEFAULT_PADX)
        kwargs.setdefault("pady", self.DEFAULT_PADY)
        return super().pack(**kwargs)

    # Defaults para grid
    def grid(self, **kwargs):
        kwargs.setdefault("padx", self.DEFAULT_PADX)
        kwargs.setdefault("pady", self.DEFAULT_PADY)
        return super().grid(**kwargs)
