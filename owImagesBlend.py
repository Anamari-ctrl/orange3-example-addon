import numpy as np
from Orange.data import Table
from Orange.widgets import gui
from orangewidget.widget import settings
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output, Msg
from AnyQt.QtWidgets import \
    QStyle, QComboBox, QMessageBox, QGridLayout, QLabel, \
    QLineEdit, QSizePolicy as Policy, QCompleter
from AnyQt.QtCore import Qt, QTimer, QSize, QUrl, pyqtSignal
from AnyQt.QtGui import QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton
from PyQt5.QtGui import QIcon
from PIL import Image


class ImagesBlend(OWWidget):
    # Widget needs a name, or it is considered an abstract widget
    # and not shown in the menu.
    name = "Blend two images"
    description = "Blending two images"
    icon = "icons/blend.png"
    priority = 100
    keywords = "data, load, read, open, image"
    category = "Example - documentation"

    label = Setting("")

    class Inputs:
        image1 = Input("image1", np.ndarray, auto_summary=False)
        image2 = Input("image2", np.ndarray, auto_summary=False)

    class Outputs:
        image = Output("image", np.ndarray, default=True, auto_summary=False)

    proportion = settings.Setting(50)
    commitOnChange = settings.Setting(0)

    #TODO: Why is important that this is false
    want_main_area = False
    buttons_area_orientation = False

    # TODO: We declare classes for Warning, Information and Errors
    class Information(OWWidget.Information):
        no_file_selected = Msg("No file selected")
        no_file_saved = Msg("No file saved")

    class Warning(OWWidget.Warning):
        file_too_big = Msg("File too big")
        file_upload = Msg("Read error:\n{}")

    class Error(OWWidget.Error):
        missing_file = Msg("No file found")
        error = Msg("This is an error message")
        unknown = Msg("Read error:\n{}")

    def __init__(self):
        super().__init__()
        self.image1 = None
        self.image2 = None

        layout = QGridLayout()
        layout.setSpacing(4)

        self.load_button = QPushButton('Load File', self)
        self.load_button.clicked.connect(self.browse_file)
        layout.addWidget(self.load_button, 0, 0)

    @Inputs.image1
    @Inputs.image2
    def set_images(self, image1, image2):
        self.image1 = image1
        self.image2 = image2




if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview  # since Orange 3.20.0
    WidgetPreview(ImagesBlend).run()