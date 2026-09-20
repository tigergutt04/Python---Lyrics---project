import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import QTimer

def move_window(window):
    screen = QApplication.primaryScreen().availableGeometry()

    x = 300
    y = screen.height() - window.height()
    speed = -2

    def move():
        nonlocal y, speed

        y += speed

        if y<= 0:
            window.show()

        window.move(x,y)

    timer = QTimer(window)
    timer.timeout.connect(move)
    timer.start(10)


