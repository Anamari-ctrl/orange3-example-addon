import numpy as np
from AnyQt.QtWidgets import QLabel, QVBoxLayout, QWidget
from AnyQt.QtGui import QImage, QPixmap

from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets import gui


class ImageWidget(QWidget):
    def __init__(self):
        super().__init__()


        layout = QVBoxLayout(self)
        self.setLayout(layout)
        self.label = QLabel(self)
        layout.addWidget(self.label)



    def set_image(self, new_image_array):
        image = self.__numpy_array_to_qimage(new_image_array)
        pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)

    def __numpy_array_to_qimage(self, array):
        height, width, channel = array.shape
        bytes_per_line = 3 * width
        qimage = QImage(array.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return qimage

class ShowImage(OWWidget):
    name = "Image Preview"
    description = "Preview uploaded image"
    icon = "icons/showImage.jpg"
    priority = 110
    keywords = ("data", "show", "read", "open", "image")
    category = "Example - documentation"

    label = Setting("")

    class Inputs:
        image = Input("image", np.ndarray)


    want_control_area = False
    buttons_area_orientation = False
    resizing_enabled = False

    def __init__(self):
        super().__init__()

        box = gui.widgetBox(self.mainArea, "")
        self.image_preview = ImageWidget()
        box.layout().addWidget(self.image_preview)

    @Inputs.image
    def show_image(self, image_array):
        self.image_preview.set_image(image_array)


if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview

    WidgetPreview(ShowImage).run()

    main_window = ShowImage()
    main_window.show()

