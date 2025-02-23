from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from file_helper_14 import *

def shop_window():
        window = QDialog()
        catalog = [
            {
                "name": "Tier 1",
                "kartinka": "img_3.png",
                "price": 200,
                "gun_attack_speed": 0.25,
                "bullet_speed": 10,
            },
            {
                "name": "Tier 2",
                "kartinka": "images-removebg-preview.png",
                "price": 1000,
                "gun_attack_speed": 0.25,
                "bullet_speed": 25
            },
            {
                "name": "Tier 3",
                "kartinka": "94-947156_terraria-png-terraria-gun-transparent-png-removebg-preview.png",
                "price": 2000,
                "gun_attack_speed": 0.1,
                "bullet_speed": 50,
            }
        ]
        data = read_from_file()
        score_lbl = QLabel("Score: " + str(data['score']))
        main_line = QVBoxLayout()
        main_line.addWidget(score_lbl)

        h1 = QHBoxLayout()

        def buy_func(p, skin, gun_attack_speed, bullet_speed):
            data = read_from_file()
            print(p)
            if data["score"] >= p:
                data["score"] -= p
                data["skin"] = skin
                data["gun_attack_speed"] = gun_attack_speed
                data["bullet_speed"] = bullet_speed
            write_in_file(data)

        for element in catalog:
            v1 = QVBoxLayout()
            name = QLabel(element['name'])
            katinka = QLabel("kartinka")
            pixmap = QPixmap(element['kartinka'])
            pixmap = pixmap.scaledToWidth(100)
            katinka.setPixmap(pixmap)
            price = QLabel(str(element['price']))
            buy_btn = QPushButton("BUY")
            buy_btn.clicked.connect(lambda _,
                                           my_price=element['price'],
                                           skin=element['kartinka'],
                                           gun_attack_speed=element['gun_attack_speed'],
                                           bullet_speed=element['bullet_speed']:
                                    buy_func(my_price, skin,gun_attack_speed, bullet_speed))
            v1.addWidget(name)
            v1.addWidget(katinka)
            v1.addWidget(price)
            v1.addWidget(buy_btn)
            h1.addLayout(v1)
        main_line.addLayout(h1)
        window.setLayout(main_line)
        window.exec()





















        window.exec()