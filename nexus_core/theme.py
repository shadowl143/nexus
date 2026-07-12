import ttkbootstrap as tb
import nexus_core.design_tokens as design


def apply_theme(app: tb.Window, colors: dict):
    style = tb.Style()

    # Fondo del window
    app.configure(bg=colors["bg.primary"])

    # Frames
    style.configure("TFrame", background=colors["bg.primary"])

    # Labels
    style.configure(
        "TLabel",
        background=colors["bg.primary"],
        foreground=colors["text.primary"],
    )

    # Labels
    style.configure(
        "TCombobox",
        background=colors["bg.primary"],
        foreground=colors["text.primary"],
    )

    # Checkbutton
    style.configure(
        "TCheckbutton",
        background=colors["bg.surface"],
        foreground=colors["text.primary"],
        indicatorcolor=colors["text.primary"],
    )

    style.map(
        "TCheckbutton",
        background=[
            ("active", colors["bg.surface"]),
            ("selected", colors["bg.surface"]),
        ],
        foreground=[
            ("active", colors["text.primary"]),
            ("selected", colors["text.primary"]),
        ],
    )

    # Botones
    style.configure(
        "TButton",
        font=(
            design.TYPOGRAPHY["font.family.sans"],
            design.TYPOGRAPHY["font.size.body"],
            "bold",
        ),
        background=colors["accent.primary"],
        foreground="white",
    )

    # Entry
    style.configure(
        "TEntry",
        fieldbackground=colors["bg.surface"],
        foreground=colors["text.primary"],
    )

    return style


def mode_dark(app, value: bool):
    if value:
        apply_theme(app, design.COLORS_DARK)
    else:
        apply_theme(app, design.COLORS)
