import numpy as np
from AnyQt.QtWidgets import QLabel, QVBoxLayout, QWidget
from AnyQt.QtGui import QImage, QPixmap

from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets import gui


class ImageWidget(QWidget):
    def __init__(self, image_array):
        super().__init__()

        self.label = QLabel(self)
        self.init_ui()

        # Set the initial image
        self.update_image(image_array)

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def update_image(self, new_image_array):
        image = self.numpy_array_to_qimage(new_image_array)
        pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)

    def numpy_array_to_qimage(self, array):
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

    class Outputs:
        image = Output("image", np.ndarray)

    want_main_area = False
    buttons_area_orientation = False

    def __init__(self):
        super().__init__()

        box = gui.widgetBox(self.controlArea, "")
        self.image_preview = ImageWidget(np.zeros((1, 1, 3), dtype=np.uint8))
        box.layout().addWidget(self.image_preview)

    @Inputs.image
    def show_image(self, image_array):
        self.image_preview.update_image(image_array)


if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview

    WidgetPreview(ShowImage).run()

    main_window = ShowImage()
    main_window.show()

