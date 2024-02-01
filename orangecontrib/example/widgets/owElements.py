import numpy as np
from AnyQt.QtWidgets import QGridLayout
from AnyQt.QtCore import Qt
from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets import gui
from orangewidget.settings import Setting
from enum import Enum

from orangewidget.utils.signals import summarize, PartialSummary


@summarize.register
def summarize_ndarray(a: np.ndarray):
    return PartialSummary(f"{a.shape[0]}x{a.shape[1]}", f"Image of size {a.shape[0]}x{a.shape[1]}")


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


class Elements(OWWidget):
    name = "GUI Elements"
    description = "GUI Elements"
    icon = "icons/elements.png"

    class Inputs:
        image = Input("Image", np.ndarray)

    class Outputs:
        image = Output("Image", np.ndarray)

    want_main_area = False
    buttons_area_orientation = None
    resizing_enabled = False

    color_channel = Setting(0)
    invert = Setting(False)

    def __init__(self):
        super().__init__()
        self.image_array = None

        self.rgb_combobox = gui.comboBox(self.controlArea, self, "color_channel", box='Color Channels',
                                         items=["R", "G", "B"], sendSelectedValue=True, callback=self.commit)


        self.check_box = gui.checkBox(self.controlArea, self, "invert",
                                      'Invert pixels',
                                      tooltip='Invert pixels',
                                      callback=self.invert)

    @Inputs.image
    def set_image1(self, image):
        self.image_array = image

    def handleNewSignals(self):
        self.commit()
        self.invert()

    def commit(self):
        color = Color(self.rgb_combobox.currentIndex())
        print(f"color {color}")

        temp = self.image_array.copy()
        if color == Color.RED:
            temp[:, :, (1, 2)] = 0
        elif color == Color.GREEN:
            temp[:, :, (0, 2)] = 0
        elif color == Color.BLUE:
            temp[:, :, (0, 1)] = 0

        self.Outputs.image.send(temp)

    def invert(self):
        if not self.check_box.isChecked():
            return
        print("invert")
        temp = self.image_array.copy()
        temp = 255 - temp
        self.Outputs.image.send(temp)


if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview

    WidgetPreview(Elements).run()
