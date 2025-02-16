from PyQt5.QtWidgets import *

import main
from shop import shop_window

app = QApplication([])
window = QWidget()



play_btn = QPushButton("Почати Гру")
shop_btn = QPushButton("Магазин")


play_btn.clicked.connect(main.game)
shop_btn.clicked.connect(shop_window)


main_line = QVBoxLayout()
main_line.addWidget(play_btn)
main_line.addWidget(shop_btn)

window.setLayout(main_line)















window.show()
app.exec()
