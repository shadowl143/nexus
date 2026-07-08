import ttkbootstrap as tb
import nexus_core.design_tokens as design

class LettersEntry(tb.Entry):
    """Solo letras y espacios"""

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
