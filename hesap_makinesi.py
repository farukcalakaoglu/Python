import time
class Hesap:
    def __init__(self,say1,say2):
        self.sa1=say1
        self.sa2=say2
    def topla(self):
       return self.sa1+self.sa2
     
    def cikar(self):
       return self.sa1-self.sa2
    def bol(self):
       return self.sa1/self.sa2  
    def carp(self):
       return self.sa1*self.sa2     
t=int(input("1.sayı girin: "))
y=int(input("2.sayı girin: "))
hesap=Hesap(say1=t,say2=y)
while True:
 print("hesap makinesi")
 t = input("Toplama için 1\nÇıkarmak için 2\nBölme için 3\nÇarpma için 4\nÇıkmak için 5\nSeçiminiz: ")
 if t=="5":
    print("cıkılıyor...")
    break
 else:
    if t=="1":
        print(f"toplama sonucu:{hesap.topla()}")
        time.sleep(1)
    elif t=="2":
        print(f"cıkarma sonucu:{hesap.cikar()}")
        time.sleep(1)
    elif t=="3":
        print(f"bölme sonucu:{hesap.bol()}")
        time.sleep(1)   
    elif t=="4":
        print(f"carpma sonucu:{hesap.carp()}")
        time.sleep(1)
    else:
       print("hatalı giriş yaptınız...")
       