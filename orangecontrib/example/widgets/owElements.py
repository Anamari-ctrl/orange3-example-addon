from AnyQt.QtWidgets import QGridLayout
from AnyQt.QtCore import Qt
from Orange.widgets.widget import OWWidget
from Orange.widgets import gui
from orangewidget.settings import Setting


class Elements(OWWidget):
    name = "GUI Elements"
    description = "GUI Elements"
    icon = "icons/elements.png"

    want_main_area = False
    buttons_area_orientation = None
    resizing_enabled = False

    color_channel = Setting(0)

    def __init__(self):
        super().__init__()

        gui.comboBox(self.controlArea, self, "color_channel", box='Color Channels', items=["R", "G", "B"],
                     sendSelectedValue=True, callback=self.dropdown_changed)

    @staticmethod
    def dropdown_changed():
        print("Dropdown changed")







if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview

    WidgetPreview(Elements).run()
