# import numpy as np
# from PIL import Image
# from AnyQt.QtWidgets import QLabel, QVBoxLayout, QWidget, QSizePolicy
# from AnyQt.QtGui import QImage, QPixmap
#
# from orangewidget.widget import settings
# from Orange.widgets.settings import Setting
# from Orange.widgets.widget import OWWidget, Input, Output
# from Orange.widgets import gui
#
#
# class ImageWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.image1_array = np.zeros((1, 1, 3), dtype=np.uint8)
#         self.image2_array = np.zeros((1, 1, 3), dtype=np.uint8)
#         self.image_preview = QLabel(self)
#
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.image_preview)
#         self.setLayout(layout)
#
#     def set_images(self, image1_array, image2_array, alpha):
#         self.image1_array = image1_array
#         self.image2_array = image2_array
#         self.resize_blend_images(alpha)
#
#     def resize_blend_images(self, alpha):
#         if not self.image1_array.size or not self.image2_array.size:
#             return  # One or both images not available
#
#         target_size = (
#             min(self.image1_array.shape[0], self.image2_array.shape[0]),
#             min(self.image1_array.shape[1], self.image2_array.shape[1])
#         )
#         img1_resized = Image.fromarray(self.image1_array).resize(target_size)
#         img2_resized = Image.fromarray(self.image2_array).resize(target_size)
#         self.blend_images(img1_resized, img2_resized, alpha)
#
#     def blend_images(self, image1, image2, alpha):
#         # print(f"alpha is: {alpha}")
#         if alpha is None:
#             alpha = 0.5
#
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
#     name = "Image blending Add images to slider"
#     description = "Blend uploaded images"
#     icon = "icons/blend.png"
#     priority = 120
#     keywords = ("data", "show", "read", "open", "image")
#     category = "Example - documentation"
#
#     label = Setting("")
#
#     class Inputs:
#         image1 = Input("image1", np.ndarray, auto_summary=False)
#         image2 = Input("image2", np.ndarray, auto_summary=False)
#
#
#
#     class Outputs:
#         image = Output("image", np.ndarray, auto_summary=False)
#
#     # proportion = settings.Setting(50)
#     # commitOnChange = settings.Setting(0)
#     slider_setting = settings.Setting(50, min=0, max=100)
#
#     want_control_area = False
#     buttons_area_orientation = False
#
#     def __init__(self):
#         super().__init__()
#         show1 = Image.open(r"C:\Users\anama\PycharmProjects\pythonProject3\orange3-example-addon\orangecontrib"
#                            r"\example\widgets\icons\blend.png")
#         show2 = Image.open(r"C:\Users\anama\PycharmProjects\pythonProject3\orange3-example-addon\orangecontrib"
#                            r"\example\widgets\icons\blend.png")
#
#         slider_box = gui.hBox(self.mainArea, "Blend Proportion")
#         self.icon1 = ImageWidget()
#         # slider_box.layout().addWidget(self.icon1)
#         slider_box.layout().addWidget(show1)
#         self.icon2 = ImageWidget()
#         # slider_box.layout().addWidget(self.icon2)
#         slider_box.layout().addWidget(show2)
#         self.slider = gui.hSlider(
#             slider_box, self, "slider_setting",
#             minValue=0, maxValue=100,
#             callback=self._slider_changed, createLabel=False,
#             sizePolicy=(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
#         )
#
#
#         box = gui.widgetBox(self.mainArea, "")
#         self.image_preview = ImageWidget()
#         box.layout().addWidget(self.image_preview)
#
#         self.image1_array = None
#         self.image2_array = None
#
#
#     def _slider_changed(self):
#         self.update_image()
#
#     @Inputs.image1
#     def set_image1(self, image1):
#         self.image1_array = image1
#         self.icon1.set_image(image1)
#
#     @Inputs.image2
#     def set_image2(self, image2):
#         self.image2_array = image2
#         self.icon2.set_image(image2)
#
#     # ko canvas sprocesira signal, ki ga pošljejo vse povezane komponente
#     def handleNewSignals(self):
#         self.update_image()
#
#     def update_image(self):
#         if self.image2_array is not None and self.image1_array is not None:
#             alpha = self.slider_setting / 100.0
#             self.image_preview.set_images(self.image1_array, self.image2_array, alpha)
#
#
#
# if __name__ == "__main__":
#     from Orange.widgets.utils.widgetpreview import WidgetPreview
#     # add code to upload two images
# #    image1 = np.array(Image.open("images/image1.jpg"))
# #    image2 = np.array(Image.open("images/image2.jpg"))
#
#     WidgetPreview(BlendImages().run())
#
#     main_window = BlendImages()
#     main_window.show()
