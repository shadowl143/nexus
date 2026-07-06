import ttkbootstrap as tb

class TableFrame(tb.Frame):
    def __init__(self, parent, columns, data, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.tree = tb.Treeview(self, columns=columns, show='headings')
        self.tree.grid(row=0, column= 0, sticky= 'n')
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        
        for row in data:
            self.tree.insert('', 'end', values=row)
        
        self.tree.pack(expand=True, fill="both")