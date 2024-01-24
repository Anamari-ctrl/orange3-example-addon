# import numpy as np
# from Orange.data import Table
# from Orange.widgets import gui
# from orangewidget.widget import settings
# from Orange.widgets.settings import Setting
# from Orange.widgets.widget import OWWidget, Input, Output, Msg
# from AnyQt.QtWidgets import (
#     QStyle, QComboBox, QMessageBox, QGridLayout, QLabel,
#     QLineEdit, QSizePolicy as Policy, QCompleter, QVBoxLayout
# )
# from AnyQt.QtCore import Qt, QSize
# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QFileDialog, QPushButton
# from PIL import Image
# class ImageWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         # Initialize with default images
#         self.image1_array = np.zeros((1, 1, 3), dtype=np.uint8)
#         self.image2_array = np.zeros((1, 1, 3), dtype=np.uint8)
#         self.image_preview = QLabel(self)
#
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.image_preview)
#         self.setLayout(layout)
#
#         # Resize and blend default images
#         self.resize_blend_images()
#
#     def set_images(self, image1_array, image2_array):
#         self.image1_array = image1_array
#         self.image2_array = image2_array
#         self.resize_blend_images()
#
#     def resize_blend_images(self):
#         if not self.image1_array.size or not self.image2_array.size:
#             return  # One or both images not available
#
#         target_size = (
#             min(self.image1_array.shape[0], self.image2_array.shape[0]),
#             min(self.image1_array.shape[1], self.image2_array.shape[1])
#         )
#         img1_resized = Image.fromarray(self.image1_array).resize(target_size)
#         img2_resized = Image.fromarray(self.image2_array).resize(target_size)
#         self.blend_images(img1_resized, img2_resized)
#
#     def blend_images(self, image1, image2):
#         alpha = 0.5
#         blended_img = alpha * np.array(image1) + (1 - alpha) * np.array(image2)
#         blended_image = np.clip(blended_img, 0, 255).astype(np.uint8)
#         self.display_image(blended_image)
#
#     def display_image(self, array):
#         image = self.numpy_array_to_qimage(array)
#         pixmap = QPixmap.fromImage(image)
#         self.image_preview.setPixmap(pixmap)
#
#     def numpy_array_to_qimage(self, array):
#         height, width, channel = array.shape
#         bytes_per_line = 3 * width
#         qimage = QImage(array.data, width, height, bytes_per_line, QImage.Format_RGB888)
#         return qimage
#
# class BlendImages(OWWidget):
#     name = "Blend two images - working version"
#     description = "Blend uploaded images"
#     icon = "icons/blend.png"
#     priority = 100
#     keywords = ("data", "show", "read", "open", "image")
#     category = "Example - documentation"
#
#     label = Setting("")
#
#     class Inputs:
#         image1 = Input("image1", np.ndarray, auto_summary=False)
#         image2 = Input("image2", np.ndarray, auto_summary=False)
#
#     class Outputs:
#         image = Output("image", np.ndarray, auto_summary=False)
#
#     proportion = settings.Setting(50)
#     commitOnChange = settings.Setting(0)
#
#     want_main_area = False
#     buttons_area_orientation = False
#
#     def __init__(self):
#         super().__init__()
#
#         box = gui.widgetBox(self.controlArea, "")
#         self.image_preview = ImageWidget()
#         box.layout().addWidget(self.image_preview)
#
#         self.image1_array = None
#         self.image2_array = None
#
#     @Inputs.image1
#     def set_image1(self, image1):
#         self.image1_array = image1
#         self.image_preview.set_images(self.image1_array, self.image2_array)
#
#     @Inputs.image2
#     def set_image2(self, image2):
#         self.image2_array = image2
#         self.image_preview.set_images(self.image1_array, self.image2_array)
#
# if __name__ == "__main__":
#     from Orange.widgets.utils.widgetpreview import WidgetPreview
#
#     WidgetPreview(BlendImages).run()
#
#     main_window = BlendImages()
#     main_window.show()
