import ttkbootstrap as tb


class NumericEntry(tb.Entry):
    """Solo números enteros"""

    DEFAULT_PADX = 15
    DEFAULT_PADY = 15

    def __init__(self, parent, **kwargs):

        validator = parent.register(lambda value: value.isdigit() or value == "")

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
