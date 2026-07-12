import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from nexus_desktop.tkinter.views.frame.inicio.inicio_frame import InicioFrame


class TestInicioFrame(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # evita que se abra ventana

        self.language_var = tk.StringVar(value="es_Mx")
        self.dark_var = tk.BooleanVar(value=False)
        self.toggle_callback = MagicMock()

        # Mock de la clase MultiLanguageService
        self.mock_multilanguage_class = MagicMock()

        # Mock de la instancia que devuelve la clase
        self.mock_instance = MagicMock()
        self.mock_instance.load_transaction.return_value = {"welcome": "Hola"}

        self.mock_multilanguage_class.return_value = self.mock_instance

    def test_init_loads_language(self):
        frame = InicioFrame(
            contenedor_principal=self.root,
            language=self.language_var,
            mode=self.dark_var,
            toggle_callback=self.toggle_callback,
            multilanguage_class=self.mock_multilanguage_class,
        )

        # Verifica que se creó el servicio con el idioma correcto
        self.mock_multilanguage_class.assert_called_with(language="es_Mx")

        # Verifica que llamó load_transaction
        self.mock_instance.load_transaction.assert_called_once()

        self.assertEqual(frame.lenguage_value["welcome"], "Hola")

    def test_change_language(self):
        frame = InicioFrame(
            contenedor_principal=self.root,
            language=self.language_var,
            mode=self.dark_var,
            toggle_callback=self.toggle_callback,
            multilanguage_class=self.mock_multilanguage_class,
        )

        frame.change_language("en_US")

        # Verifica que se creó con el nuevo idioma
        self.mock_multilanguage_class.assert_called_with(language="en_US")

        # Verifica actualización del StringVar
        self.assertEqual(self.language_var.get(), "en_US")

    @patch(
        "nexus_desktop.tkinter.views.component.drop_down.drop_down_component.DropDownComponent"
    )
    @patch(
        "nexus_desktop.tkinter.views.component.label.label_tittle_widget.LabelTittleWidget"
    )
    @patch("ttkbootstrap.tb.Checkbutton")
    @patch("ttkbootstrap.tb.Frame")
    @patch("tkinter.tk.StringVar")
    @patch("tkinter.tk.BooleanVar")
    def test_crear_frame_inicio(
        self, mock_frame, mock_checkbutton, mock_label, mock_dropdown
    ):
        mock_frame_instance = MagicMock()
        mock_frame.return_value = mock_frame_instance

        mock_dropdown_instance = MagicMock()
        mock_dropdown.return_value.select.return_value = mock_dropdown_instance

        frame = InicioFrame(
            contenedor_principal=self.root,
            language=self.language_var,
            mode=self.dark_var,
            toggle_callback=self.toggle_callback,
            multilanguage_class=self.mock_multilanguage_class,
        )

        result = frame.crear_frame_inicio()

        # Verifica creación del Frame
        mock_frame.assert_called_once_with(self.root)

        # Verifica creación del dropdown
        mock_dropdown.assert_called_with(
            mock_frame_instance,
            options=["es_Mx", "en_US"],
        )

        # Verifica bind
        mock_dropdown_instance.bind.assert_called_once()

        # Verifica que retorna el frame
        self.assertEqual(result, mock_frame_instance)
