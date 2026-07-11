from nexus_desktop.tkinter.views.layout.principal_layout import WindowsPrincipal
import os

if __name__ == "__main__":

    app = WindowsPrincipal()

    os.execl(app.iniciar())
