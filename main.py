import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import QTimer

from MovingTextbox import move_window
from LyricReader import LyricReader


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("")
window.resize(600, 300)

lyric = LyricReader('lyric.json')

index = 0

widget = QLabel(lyric[index], window) 

# Function to make the text follow the lyrics
def change_text():
    
    pass

timer = QTimer()
timer.timeout.connect(change_text)
timer.start(2000)

window.show()

move_window(window)

sys.exit(app.exec())

