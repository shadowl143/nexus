import ttkbootstrap as tb
from ttkbootstrap.constants import *


class DropDownComponent(tb.Combobox):
    def __init__(self, parent, **kwargs):
        super().__init__()
