import ttkbootstrap as tb

class DecimalEntry(tb.Entry):
    """Permite números decimales"""

    DEFAULT_PADX = 15
    DEFAULT_PADY = 15
    def __init__(self, parent, **kwargs):

        validator = parent.register(self.validate_decimal)

        super().__init__(
            parent,
            font=("Arial", 12),
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

    @staticmethod
    def validate_decimal(value):

        if value == "":
            return True

        try:
            float(value)
            return True
        except ValueError:
            return False