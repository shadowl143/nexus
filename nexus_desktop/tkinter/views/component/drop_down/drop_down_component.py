import ttkbootstrap as tb


class DropDownComponent(tb.Combobox):

    DEFAULT_PADX = 15
    DEFAULT_PADY = 15

    def __init__(self, parent, options, **kwargs):
        super().__init__(**kwargs)
        self.parent = parent
        self.option = options

    def select(self) -> tb.Combobox:
        result = tb.Combobox(self.parent, values=self.option, state="readonly")
        result.current(0)
        return result

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
