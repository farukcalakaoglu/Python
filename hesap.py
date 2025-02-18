from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys

class Hesapmakine(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(100, 100, 300, 300)
        self.hesap()

    def hesap(self):
        # 1. Sayı Girişi
        self.sa1 = QLabel(self)
        self.sa1.setText("1. Sayı: ")
        self.sa1.move(20, 20)
        self.sa1a = QLineEdit(self)
        self.sa1a.move(80, 20)
        self.sa1a.resize(100, 30)

        # 2. Sayı Girişi
        self.sa2 = QLabel(self)
        self.sa2.setText("2. Sayı: ")
        self.sa2.move(20, 70)
        self.sa2a = QLineEdit(self)
        self.sa2a.move(80, 70)
        self.sa2a.resize(100, 30)

        # İşlem Türü
        self.isl = QLabel(self)
        self.isl.setText("İşlem (+, -, *, /):")
        self.isl.move(20, 120)
        self.islem = QLineEdit(self)
        self.islem.move(120, 120)
        self.islem.resize(60, 30)

        # Buton
        self.bt = QPushButton(self)
        self.bt.setText("Sonucu Göster")
        self.bt.move(50, 170)
        self.bt.resize(150, 40)
        self.bt.clicked.connect(self.click)

        # Sonuç Ekranı
        self.so = QLabel(self)
        self.so.setText("Sonuç: ")
        self.so.move(20, 230)
        self.so.resize(200, 30)

    def click(self):
        islem = self.islem.text().strip()
        try:
            sayi1 = float(self.sa1a.text())
            sayi2 = float(self.sa2a.text())

            if islem == "+":
                sonuc = sayi1 + sayi2
            elif islem == "-":
                sonuc = sayi1 - sayi2
            elif islem == "*":
                sonuc = sayi1 * sayi2
            elif islem == "/":
                if sayi2 == 0:
                    self.so.setText("Hata: Sıfıra bölünemez!")
                    return
                sonuc = sayi1 / sayi2
            else:
                self.so.setText("Hata: Geçersiz işlem!")
                return

            self.so.setText(f"Sonuç: {sonuc}")

        except ValueError:
            self.so.setText("Hata: Geçersiz sayı girişi!")

def window():
    app = QApplication(sys.argv)
    win = Hesapmakine()
    win.show()
    sys.exit(app.exec_())

window()
        