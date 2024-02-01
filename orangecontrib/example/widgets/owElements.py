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

    def process_image(self):
        # vzamem input
        return 0
        # self.settings.color -> tuki je ze izbrana barva



if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview

    WidgetPreview(Elements).run()
