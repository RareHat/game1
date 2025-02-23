from PyQt5.QtWidgets import *

import main
from shop import shop_window

app = QApplication([])
window = QWidget()
window.resize(250, 250)
app.setStyleSheet("""
            QWidget{
                background-color: #400000;

            }
            QPushButton
            {
             background-color: #700000 ;
             border-style: outset;
             font-family: Impact;
             min-width: 6em;
             padding: 6px;
             border-width: 5px;
             border-color: #0000e6;
             border-radius 7ox;
            }  
            
            
            
            QLabel
            {
              background-color: #980000;
              border-style: outset;
              font-family: Impact;
              min-width: 6em;
              padding: 6px;
              border-width: 5px;
              border-color: #0000e6;
              border-radius 7px;
              }
""")



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
