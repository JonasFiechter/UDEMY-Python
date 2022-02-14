# ('pyuic5 ****.ui -o ****.py') CONVERSOR .ui --> .py no terminal
from app_design import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class ResizeApp(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChooseFile.clicked.connect(self.open_image)
        self.btnResize.clicked.connect(self.resize_img)
        self.btnSave.clicked.connect(self.save)

    def open_image(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Open file',
            r'C:/',
            # options=QFileDialog.DontUseNativeDialog
        )
        self.inputOpenFile.setText(image)
        self.original_img = QPixmap(image)
        self.labelImg.setPixmap(self.original_img)
        self.lineWidth.setText(str(self.original_img.width()))
        self.lineHeight.setText(str(self.original_img.height()))

    def resize_img(self):
        width = int(self.lineWidth.text())
        self.new_image = self.original_img.scaledToWidth(width)
        self.labelImg.setPixmap(self.new_image)
        self.lineWidth.setText(str(self.new_image.width()))
        self.lineHeight.setText(str(self.new_image.height()))

    def save(self):
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Save file',
            r'C:/',
            # options=QFileDialog.DontUseNativeDialog
        )
        self.new_image.save(self.new_image, 'png')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    resize_app = ResizeApp()
    resize_app.show()
    qt.exec()
