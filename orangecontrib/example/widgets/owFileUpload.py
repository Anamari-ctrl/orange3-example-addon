import numpy as np
from Orange.data import Table
from orangewidget.widget import settings
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output, Msg
from AnyQt.QtWidgets import QMessageBox, QGridLayout
from PyQt5.QtWidgets import QFileDialog, QPushButton
from PIL import Image

class uploadFile(OWWidget):
    # Widget needs a name, or it is considered an abstract widget
    # and not shown in the menu.
    name = "Upload image"
    description = "Upload image from local directory"
    icon = "icons/uploadImage.png"
    priority = 100
    keywords = "data, load, read, open, image"
    category = "Example - documentation"

    label = Setting("")

    #TODO: We declare output as numpy array
    class Outputs:
        image = Output("image", np.ndarray, default=True, auto_summary=False)

    proportion = settings.Setting(50)
    commitOnChange = settings.Setting(0)

    #TODO: Why is important that this is false
    want_main_area = False
    buttons_area_orientation = False

    # TODO: We declare classes for Warning, Information and Errors
    class Information(OWWidget.Information):
        no_file_selected = Msg("No file selected")
        no_file_saved = Msg("No file saved")

    class Warning(OWWidget.Warning):
        file_too_big = Msg("File too big")
        file_upload = Msg("Read error:\n{}")

    class Error(OWWidget.Error):
        missing_file = Msg("No file found")
        error = Msg("This is an error message")
        unknown = Msg("Read error:\n{}")

    def __init__(self):
        super().__init__()
        self.image = None

        layout = QGridLayout()
        layout.setSpacing(4)

        self.load_button = QPushButton('Load File', self)
        self.load_button.clicked.connect(self.browse_file)
        layout.addWidget(self.load_button, 0, 0)

    def browse_file(self):
        self.image, _ = QFileDialog.getOpenFileName(
            self, 'Open File', '', 'Image Files (*.gif *.jpg *.jpeg *.png *.svg);;All Files (*)'
        )
        # TODO:Preverjanje ce je datoteka izbrana
        msg = QMessageBox()
        msg.setWindowTitle("File Upload")
        msg.setText(f"Do you want to upload the file? {self.image}")
        btn1 = QMessageBox.Yes
        btn2 = QMessageBox.No
        msg.setStandardButtons(btn1 | btn2)
        msg.setDefaultButton(btn1)
        msg.buttonClicked.connect(self.popup_clicked)
        x = msg.exec_()


    def popup_clicked(self, i):
        if i.text() == ("&Yes"):
            img = np.array(Image.open(self.image))
            Image.fromarray(img).save('uploadedFile.jpg')
            self.Outputs.image.send(img)
            self.close()




if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview  # since Orange 3.20.0
    WidgetPreview(uploadFile).run()
