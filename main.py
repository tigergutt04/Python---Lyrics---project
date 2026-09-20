import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import QTimer

from MovingTextbox import move_window
from LyricReader import LyricReader


app = QApplication(sys.argv)

lyric = LyricReader('lyric.json')

window = QWidget()
window.setWindowTitle("Lyrics Project")
window.resize(300, 300)


widget = QLabel(lyric[0], window) 
window.show()

move_window(window)

sys.exit(app.exec())

