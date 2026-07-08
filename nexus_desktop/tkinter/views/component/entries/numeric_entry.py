import ttkbootstrap as tb

class NumericEntry(tb.Entry):
    """Solo números enteros"""

    def __init__(self, parent, **kwargs):

        validator = parent.register(
            lambda value: value.isdigit() or value == ""
        )

        super().__init__(
            parent,
            font=("Arial", 12),
            validate="key",
            validatecommand=(validator, "%P"),
            **kwargs
        )