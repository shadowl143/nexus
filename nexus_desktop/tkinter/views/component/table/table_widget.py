import ttkbootstrap as tb
import nexus_core.design_tokens as design


class TableFrame(tb.Frame):
    DEFAULT_PADX = 15
    DEFAULT_PADY = 15

    def __init__(self, parent, columns, data, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        style = tb.Style()

        style.configure(
            "Treeview.Heading",
            font=(
                design.TYPOGRAPHY["font.family.sans"],
                design.TYPOGRAPHY["font.size.body"],
                "bold",
            ),  # (familia, tamaño, estilo)
        )
        style.configure(
            "Treeview",
            font=(
                design.TYPOGRAPHY["font.family.sans"],
                design.TYPOGRAPHY["font.size.body"],
            ),
            rowheight=30,
        )
        self.tree = tb.Treeview(self, columns=columns, show="headings")
        self.tree.grid(row=0, column=0, sticky="n")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=220, minwidth=150, stretch=True)

        for row in data:
            self.tree.insert("", "end", values=row)

        self.tree.pack(expand=True, fill="both")

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
