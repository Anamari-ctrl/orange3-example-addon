import numpy as np
from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets import gui
from orangewidget.settings import Setting


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
    invert = Setting(0)
    brightness = Setting(0)
    contrast = Setting(0)
    binarize = Setting(0)

    def __init__(self):
        super().__init__()
        self.image_array = None

        gui.comboBox(self.controlArea, self, "color_channel", box='Color Channels',
                     items=["None", "R", "G", "B"], callback=self.commit)

        gui.checkBox(self.controlArea, self, "invert",
                     'Invert pixels',
                     tooltip='Invert pixels',
                     callback=self.commit)

        gui.hSlider(self.controlArea, self, "brightness", box='Brightness',
                    callback=self.commit, minValue=-100, maxValue=100, step=1)
        # gui.hSlider(self.controlArea, self, "contrast", box='Contrast',
        # callback=self.commit, minValue=-100, maxValue=100, step=1)
        gui.checkBox(self.controlArea, self, "contrast",
                     'Contrast',
                     tooltip='contrast',
                     callback=self.commit)

        gui.checkBox(self.controlArea, self, "binarize",
                     'Binarize',
                     tooltip='binarize',
                     callback=self.commit)

        gui.spin(self.controlArea, self, "brightness", -100, 100, 1, label="Brightness",
                 callback=self.commit)

        display = gui.widgetBox(self.controlArea, "Display")
        gui.checkBox(display, self, "binarize", "Binarize", callback=self.commit)
        gui.checkBox(display, self, "invert", "Invert", callback=self.commit)


    @Inputs.image
    def set_image1(self, image):
        self.image_array = image

    def handleNewSignals(self):
        self.commit()

    def commit(self):
        temp = self.image_array.copy()

        if self.color_channel == 1:
            temp[:, :, (1, 2)] = 0
        elif self.color_channel == 2:
            temp[:, :, (0, 2)] = 0
        elif self.color_channel == 3:
            temp[:, :, (0, 1)] = 0

        if self.invert:
            temp = 255 - temp

        if self.brightness:
            if self.brightness < 0:
                temp = temp - self.brightness
                temp[temp < 0] = 0
            else:
                temp = temp + self.brightness
                temp[temp > 255] = 255

        if self.contrast:
            temp = temp * 1.5
            temp[temp > 255] = 255

        if self.binarize:
            temp = (temp > 127) * 255

        self.Outputs.image.send(temp)


if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview

    WidgetPreview(Elements).run()
