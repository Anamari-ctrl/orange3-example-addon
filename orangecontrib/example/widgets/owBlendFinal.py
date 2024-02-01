import numpy as np
from PIL import Image
from AnyQt.QtWidgets import QLabel, QVBoxLayout, QWidget, QSizePolicy
from AnyQt.QtGui import QImage, QPixmap

from orangewidget.widget import settings
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets import gui


class ImageWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.image_preview = QLabel(self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.image_preview)
        self.setLayout(layout)

    def set_image(self, image):
        image = ImageWidget._numpy_array_to_qimage(image)
        pixmap = QPixmap.fromImage(image)
        self.image_preview.setPixmap(pixmap)

    @staticmethod
    def _numpy_array_to_qimage(array):
        height, width, channel = array.shape
        bytes_per_line = 3 * width
        qimage = QImage(array.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return qimage

class ImageBlend:
    @staticmethod
    def _resize_images(image1, image2):
        target_size = (
            min(image1.shape[0], image2.shape[0]),
            min(image1.shape[1], image2.shape[1])
        )
        img1_resized = Image.fromarray(image1).resize(target_size)
        img2_resized = Image.fromarray(image2).resize(target_size)

        return img1_resized, img2_resized

    @staticmethod
    def blend_images(image1, image2, alpha):
        if alpha is None:
            alpha = 0.5

        image1,image2 = ImageBlend._resize_images(image1, image2)

        blended_img = alpha * np.array(image1) + (1 - alpha) * np.array(image2)
        blended_image = np.clip(blended_img, 0, 255).astype(np.uint8)

        return blended_image


class BlendImages(OWWidget):
    name = "Image blending"
    description = "Blend uploaded images"
    icon = "icons/blend.png"
    priority = 120
    keywords = ("data", "show", "read", "open", "image")
    category = "Example - documentation"

    label = Setting("")

    class Inputs:
        image1 = Input("image1", np.ndarray, auto_summary=False)
        image2 = Input("image2", np.ndarray, auto_summary=False)

    class Outputs:
        image = Output("image", np.ndarray, auto_summary=False)

    # proportion = settings.Setting(50)
    # commitOnChange = settings.Setting(0)
    slider_setting = settings.Setting(50, min=0, max=100)

    want_control_area = False
    buttons_area_orientation = False

    def __init__(self):
        super().__init__()

        slider_box = gui.hBox(self.mainArea, "Blend Proportion")

        self.image1_preview = ImageWidget()
        self.image2_preview = ImageWidget()

        self.slider = gui.hSlider(
            slider_box, self, "slider_setting",
            minValue=0, maxValue=100,
            callback=self._slider_changed, createLabel=False,
            sizePolicy=(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        )

        slider_box.layout().addWidget(self.image2_preview)
        slider_box.layout().addWidget(self.slider)
        slider_box.layout().addWidget(self.image1_preview)

        box = gui.widgetBox(self.mainArea, "")
        self.image_preview = ImageWidget()
        box.layout().addWidget(self.image_preview)

        self.image1_array = None
        self.image2_array = None


    def _slider_changed(self):
        self.update_image()

    @Inputs.image1
    def set_image1(self, image1):
        self.image1_array = image1

    @Inputs.image2
    def set_image2(self, image2):
        self.image2_array = image2

    # ko canvas sprocesira signal, ki ga pošljejo vse povezane komponente
    def handleNewSignals(self):
        self.update_image()

    def update_image(self):
        if self.image2_array is None or self.image1_array is None:
            return

        image1_thumbnail = np.array(Image.fromarray(self.image1_array).resize((32, 32)))
        image2_thumbnail = np.array(Image.fromarray(self.image2_array).resize((32, 32)))

        self.image1_preview.set_image(image1_thumbnail)
        self.image2_preview.set_image(image2_thumbnail)


        alpha = self.slider_setting / 100.0
        blended = ImageBlend.blend_images(self.image1_array, self.image2_array, alpha)
        self.image_preview.set_image(blended)

if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview

    WidgetPreview(BlendImages).run()

    main_window = BlendImages()
    main_window.show()
