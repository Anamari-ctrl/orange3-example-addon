from AnyQt.QtWidgets import QGridLayout
from AnyQt.QtCore import Qt
from Orange.widgets.widget import OWWidget
from Orange.widgets import gui


class Elements(OWWidget):
    name = "GUI Elements"
    description = "GUI Elements"
    icon = "icons/elements.png"

    want_main_area = False
    buttons_area_orientation = None

    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(3)

        gui.widgetBox(self.controlArea, orientation=layout, box='Color Channels')
        vbox = gui.radioButtonsInBox(None, self, "color_channel", box=True,
                                     callback=self.dropdown_changed, addToLayout=False)

        rc_button = gui.appendRadioButton(vbox, "Channel R", addToLayout=False)
        layout.addWidget(rc_button, 0, 0, Qt.AlignCenter)

        gc_button = gui.appendRadioButton(vbox, "Channel G", addToLayout=False)
        layout.addWidget(gc_button, 0, 1, Qt.AlignCenter)

        bc_button = gui.appendRadioButton(vbox, "Channel B", addToLayout=False)
        layout.addWidget(bc_button, 0, 2, Qt.AlignCenter)

    @staticmethod
    def dropdown_changed():
        print("Dropdown changed")


if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview

    WidgetPreview(Elements).run()
