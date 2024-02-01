import numpy as np
from AnyQt.QtWidgets import QGridLayout
from AnyQt.QtCore import Qt
from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets import gui
from orangewidget.settings import Setting
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class WidgetSettings:
    def __init__(self):
        self.color = Color.RED


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

    def __init__(self):
        super().__init__()
        self.settings = WidgetSettings()
        self.image_array = None

        self.rgb_combobox = gui.comboBox(self.controlArea, self, "color_channel", box='Color Channels',
                                         items=["R", "G", "B"],
                                         sendSelectedValue=True, callback=self.dropdown_changed)

    def dropdown_changed(self):
        print("Dropdown changed")
        print(self.rgb_combobox.currentText())

        if self.rgb_combobox.currentText() == "R":
            self.settings.color = Color.RED
        elif self.rgb_combobox.currentText() == "G":
            self.settings.color = Color.GREEN
        elif self.rgb_combobox.currentText() == "B":
            self.settings.color = Color.BLUE

        self.handleNewSignals()

    @Inputs.image
    def set_image1(self, image):
        self.image_array = image

    def handleNewSignals(self):
        print("Handle new signals")
        print(self.settings.color)
        temp = self.image_array.copy()
        if self.settings.color == Color.RED:
            temp[:, :, (1, 2)] = 0
            print("Here")
        elif self.settings.color == Color.GREEN:
            temp[:, :, (0, 2)] = 0
        elif self.settings.color == Color.BLUE:
            temp[:, :, (0, 1)] = 0

        self.Outputs.image.send(temp)


if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview

    WidgetPreview(Elements).run()
