import ttkbootstrap as tb

class DecimalEntry(tb.Entry):
    """Permite números decimales"""

    def __init__(self, parent, **kwargs):

        validator = parent.register(self.validate_decimal)

        super().__init__(
            parent,
            font=("Arial", 12),
            validate="key",
            validatecommand=(validator, "%P"),
            **kwargs
        )

    @staticmethod
    def validate_decimal(value):

        if value == "":
            return True

        try:
            float(value)
            return True
        except ValueError:
            return False