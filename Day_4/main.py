import sys

from PyQt6.QtWidgets import QApplication
from HangManWindow import HangManWindow

app = QApplication(sys.argv)
mainWindow = HangManWindow()
mainWindow.show()
app.exec()