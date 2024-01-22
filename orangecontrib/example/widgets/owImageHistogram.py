import numpy as np
from Orange.data import Table
from Orange.widgets import gui
from orangewidget.widget import settings
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output, Msg
from AnyQt.QtWidgets import (
    QStyle, QComboBox, QMessageBox, QGridLayout, QLabel,
    QLineEdit, QSizePolicy as Policy, QCompleter, QVBoxLayout
)
from AnyQt.QtCore import Qt, QSize
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QFileDialog, QPushButton
from PIL import Image
from Orange.widgets import gui


class ImageHistogram(OWWidget):
    name = "Image Histogram"
    description = "Make histogram from image"
    icon = ""
    priority = 100
    keywords = ("data", "show", "image", "open", "view")
    category = "Example - documentation"

    label = Setting("")

    class Inputs:
        image1 = Input("image1", np.ndarray, auto_summary=False)

    class Outputs:
        image = Output("image", np.ndarray, auto_summary=False)

    want_main_area = False
    buttons_area_orientation = False


    def __init__(self):
        super().__init__()
        self.image = None

        layout = QGridLayout()
        layout.setSpacing(4)

if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview
    WidgetPreview(ImageHistogram).run()


