import sqlite3 as sql 
import time
con=sql.connect("ders.db")
cursor=con.cursor()
class veritabanı:
    
 def kayit(self):
  try:
   cursor.execute(""" CREATE TABLE IF NOT EXISTS DENE(ad text,soyad text,yas integer)""")
   print("tablo oluşturuldu")
   time.sleep(2)
  except:
    print("tablo oluşturamadı..")
 def bilgiekle(self):
    try:
     b=("INSERT INTO DENE(ad,soyad,yas) VALUES(?,?,?)")
     C=("ALİ","VELİ",22)
     cursor.execute(b,C)
     con.commit()
     time.sleep(2)
     print("kayıt başarılı")
    except:
        print(" kayıt başarısız..")
 def vericek(self):
    cursor.execute("SELECT * FROM DENE")
    ogrenci=cursor.fetchall()
    print("ogrenci: ",ogrenci)
    con.commit()
    time.sleep(2)
 def verisil(self):
    try:
     cursor.execute("DELETE FROM DENE WHERE ad='Ali'")
     print("silme başarılı")   
     con.commit()
     time.sleep(2)
    except:
        print("silme başarısız")
 def veriguncelle(self):
    try: 
     cursor.execute("UPDATE DENE SET ad='Ali' WHERE ad='ALİ'")
     con.commit()
     print("güncelleme başarılı")
     time.sleep(2)
    except:
        print("güncelleme başarısız")
veri=veritabanı()  
while True:
 print("VERİ TABANI")
 a=input("veri eklemek için 1\nveri bakmak için 2\nveri cekmeK için 3\n veri silmek için 4\nveri güncelemek için 5\nseciminiz:")
 if a=="1":
  veri.kayit()
 elif a=="2":
    veri.bilgiekle()
 elif a=="3":
    veri.vericek()
 elif a=="4":
    veri.verisil()
 elif a=="5":
    veri.veriguncelle()
con.close()