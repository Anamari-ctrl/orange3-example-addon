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
    icon = "icons/histogram.png"
    priority = 130
    keywords = ("data", "show", "image", "open", "view")
    category = "Example - documentation"

    label = Setting("")

    class Inputs:
        image1 = Input("image1", np.ndarray, auto_summary=False)

    class Outputs:
        image = Output("image", np.ndarray, auto_summary=False)

    proportion = settings.Setting(50)
    commitOnChange = settings.Setting(0)

    want_main_area = False
    buttons_area_orientation = False


    def __init__(self):
        super().__init__()


        layout = QGridLayout()
        layout.setSpacing(4)

        self.image1_array = None


    @Inputs.image1
    def set_image(self, image1):
        self.image1_array = image1



if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview
    WidgetPreview(ImageHistogram).run()


