import ttkbootstrap as tb
from ttkbootstrap.constants import *


class DropDownComponent:
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
