import numpy as np
from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets import gui
from orangewidget.settings import Setting



class ImageProcessing(OWWidget):
    name = "Image Processing"
    description = "Image Processing"
    icon = "icons/imageProcessing.png"
    category = "Example - documentation"

    #class Inputs:
        #image = Input("Image", np.ndarray)

    #class Outputs:
        #image = Output("Image", np.ndarray)






if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview
    WidgetPreview(ImageProcessing).run()