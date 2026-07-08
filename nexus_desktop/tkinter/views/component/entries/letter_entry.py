import ttkbootstrap as tb
import nexus_core.design_tokens as design

class LettersEntry(tb.Entry):
    """Solo letras y espacios"""

    DEFAULT_PADX = 15
    DEFAULT_PADY = 15

    def __init__(self, parent, **kwargs):
        validator = parent.register(
            lambda value: value.replace(" ", "").isalpha() or value == ""
        )
        super().__init__(
            parent,
            font=(design.TYPOGRAPHY["font.family.sans"], design.TYPOGRAPHY["font.size.body"]),
            validate="key",
            validatecommand=(validator, "%P"),
            **kwargs
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