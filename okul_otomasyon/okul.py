#eokul sistemi
import time

class okul:
 
    def __init__(self):
          self.dizi=[]
    def kayit(self): 
           self.no=int(input("okul no: "))
           self.ad=input("öğrenci ismi ve soyismi:")
           self.ders1=input("1.ders notu:")
           self.ders2=input("2.ders notu: ")
           self.dizi.append(f"{self.no}:{self.ad}:{self.ders1}:{self.ders2}\n")
           with open("okul.txt","a",encoding="utf-8") as file:
              for dizi in self.dizi:
                file.write(dizi)
                print("kayıt başarılı.") 
                
                time.sleep(3)
                break
    def kgör(self):#def gör
      with open("okul.txt","r",encoding="utf-8") as file:
        for i in file:
           a=i.strip().split(":")
           print(f"adı:{a[1]} puan1:{a[2]} puan2:{a[2]}")
           time.sleep(1)
        time.sleep(3)
    def upload(self):
      d = input("Öğrenci;\nAdı ve soyadı değişimi için 1\nPuan1 değişimi için 2\nPuan2 değişimi için 3\nSeçiminiz: ")

      if d == "1":#de1
    # Dosyayı okuma modunda açıyoruz
       with open("okul.txt", "r", encoding="utf-8") as file:
        content = file.readlines()  # Dosyadaki tüm satırları okuyoruz

    # Öğrenci numarasını kullanıcıdan alıyoruz
       de = input("Güncellemek istediğiniz öğrenci numarasını giriniz: ")

    # Dosyayı yeniden yazma işlemi
       updated = False  # Güncelleme yapılıp yapılmadığını kontrol etmek için
       with open("okul.txt", "w", encoding="utf-8") as file:
        for i in content:
            a = i.strip().split(":")  # Satırı ":" ile ayırıyoruz
            if a[0] == de:  # Öğrenci numarası eşleşirse
                f = input("Yeni öğrenci adı ve soyadını giriniz: ")
                a[1] = f  # Öğrencinin adını güncelliyoruz
                file.write(":".join(a) + "\n")  # Güncellenmiş satırı yazıyoruz
                print(f"Öğrenci {de} adlı öğrencinin adı {f} olarak güncellendi.")
                updated = True
            else:
                file.write(i)  # Öğrenci numarası eşleşmediyse mevcut satırı yazıyoruz

    # Eğer öğrenci numarası bulunamadıysa
       if not updated:
           print(f"{de} numaralı öğrenci bulunamadı.")
    
       time.sleep(1)  # 1 saniye bekleyelim
               

      elif d=="2":#de2
          # Dosyayı okuma modunda açıyoruz
       with open("okul.txt", "r", encoding="utf-8") as file:
        content = file.readlines()  # Dosyadaki tüm satırları okuyoruz

    # Öğrenci numarasını kullanıcıdan alıyoruz
       de = input("Güncellemek istediğiniz öğrenci numarasını giriniz: ")

    # Dosyayı yeniden yazma işlemi
       updated = False  # Güncelleme yapılıp yapılmadığını kontrol etmek için
       with open("okul.txt", "w", encoding="utf-8") as file:
        for i in content:
            a = i.strip().split(":")  # Satırı ":" ile ayırıyoruz
            if a[0] == de:  # Öğrenci numarası eşleşirse
                f = input("Yeni öğrenci yeni notu1 giriniz: ")
                a[2] = f  # Öğrencinin adını güncelliyoruz
                file.write(":".join(a) + "\n")  # Güncellenmiş satırı yazıyoruz
                print(f"Öğrenci {de} adlı öğrencinin adı {f} olarak güncellendi.")
                updated = True
            else:
                file.write(i)  # Öğrenci numarası eşleşmediyse mevcut satırı yazıyoruz

    # Eğer öğrenci numarası bulunamadıysa
       if not updated:
           print(f"{de} numaralı öğrenci bulunamadı.")
    
       time.sleep(1)  # 1 saniye bekleyelim
      elif d=="3":#d3
          # Dosyayı okuma modunda açıyoruz
       with open("okul.txt", "r", encoding="utf-8") as file:
        content = file.readlines()  # Dosyadaki tüm satırları okuyoruz

    # Öğrenci numarasını kullanıcıdan alıyoruz
       de = input("Güncellemek istediğiniz öğrenci numarasını giriniz: ")

    # Dosyayı yeniden yazma işlemi
       updated = False  # Güncelleme yapılıp yapılmadığını kontrol etmek için
       with open("okul.txt", "w", encoding="utf-8") as file:
        for i in content:
            a = i.strip().split(":")  # Satırı ":" ile ayırıyoruz
            if a[0] == de:  # Öğrenci numarası eşleşirse
                f = input("Yeni öğrenci yen not2 giriniz: ")
                a[3] = f  # Öğrencinin adını güncelliyoruz
                file.write(":".join(a) + "\n")  # Güncellenmiş satırı yazıyoruz
                print(f"Öğrenci {de} adlı öğrencinin adı {f} olarak güncellendi.")
                updated = True
            else:
                file.write(i)  # Öğrenci numarası eşleşmediyse mevcut satırı yazıyoruz

    # Eğer öğrenci numarası bulunamadıysa
       if not updated:
           print(f"{de} numaralı öğrenci bulunamadı.")
    
       time.sleep(1)  # 1 saniye bekleyelim
      else:
          print("tekrar deneyiniz..")
          time.sleep(1)
      if d=="4":#d44
        # Kullanıcıdan işlem seçimi alıyoruz
           # Dosyayı okuma modunda açıyoruz
       with open("okul.txt", "r", encoding="utf-8") as file:
        content = file.readlines()  # Dosyadaki tüm satırları okuyoruz

    # Öğrenci numarasını kullanıcıdan alıyoruz
       de = input("Güncellemek istediğiniz öğrenci numarasını giriniz: ")

    # Dosyayı yeniden yazma işlemi
       updated = False  # Güncelleme yapılıp yapılmadığını kontrol etmek için
       with open("okul.txt", "w", encoding="utf-8") as file:
        for i in content:
            a = i.strip().split(":")  # Satırı ":" ile ayırıyoruz
            if a[0] == de:  # Öğrenci numarası eşleşirse
                f = input("Yeni öğrenci yen not2 giriniz: ")
                a[3] = f  # Öğrencinin adını güncelliyoruz
                file.write(":".join(a) + "\n")  # Güncellenmiş satırı yazıyoruz
                print(f"Öğrenci {de} adlı öğrencinin adı {f} olarak güncellendi.")
                updated = True
            else:
                file.write(i)  # Öğrenci numarası eşleşmediyse mevcut satırı yazıyoruz

    # Eğer öğrenci numarası bulunamadıysa
       if not updated:
           print(f"{de} numaralı öğrenci bulunamadı.")
    
       time.sleep(1)  # 1 saniye bekleyelim
      else:
          print("tekrar deneyiniz..")
          time.sleep(1)
    def osil(self):
      

    
    # Dosyayı okuma modunda açıyoruz
       with open("okul.txt", "r", encoding="utf-8") as file:
        content = file.readlines()  # Dosyadaki tüm satırları okuyoruz

    # Öğrenci numarasını kullanıcıdan alıyoruz
        de = input("Silmek istediğiniz öğrenci numarasını giriniz: ")

    # Dosyayı yeniden yazma işlemi
        updated = False  # Öğrencinin bulunup silinip silinmediğini kontrol etmek için
        with open("okul.txt", "w", encoding="utf-8") as file:
         for i in content:
            a = i.strip().split(":")  # Satırı ":" ile ayırıyoruz
            if a[0] == de:  # Öğrenci numarası eşleşirse
                print(f"{de} numaralı öğrenci silindi.")
                time.sleep(1)
                updated = True  # Öğrenci bulundu ve silindi
                continue  # Bu satırı dosyaya yazma
            else:
                file.write(i)  # Silinmeyen satırı dosyaya yazıyoruz
                time.sleep(1)
    # Eğer öğrenci numarası bulunamadıysa
        if not updated:
              print(f"{de} numaralı öğrenci bulunamadı.")
    
              time.sleep(1)  # 1 saniye bekleyelim
    
okul=okul()

def oku():
 while True:
  de=input("Ögrenci not girişi için 1\nÖgrenci notları görmek için 2\nÖgrenci not güncellemek için 3\n Ogrenci silmek için 4\nÇıkmak için 5\nSeçiminiz: ")
  if de=="5":
   print("çıkılıyor....")
   break
  else:
   if de=="1":
     okul.kayit()
   elif de=="2":
    okul.kgör()
   elif de=="3":
     okul.upload()
   elif de=="4":
      okul.osil()
   else:
     print("hatalı secim yaptınız . Tekrar deneyiniz")
oku()