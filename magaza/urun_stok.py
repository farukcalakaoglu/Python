 #magaza stok otomasyon
def urun_ekle():
    with open("C://users/faruk/desktop/python/magaza/stok.txt","a",encoding="utf-8") as file:
        ukod=input("ürün kodu:")
        uad=input("ürün adı: ")
        ustok=input("ürün stok: ")
        kayit=file.write(ukod+":"+uad+":"+ustok+"\n")
        if kayit>0:
            print("ürün kaydı  başarılı")
        else:
            print("ürün eklenemedi")
def urun_cikar():
   pass
        
                
def urun_kontrol():
        with open("C://users/faruk/desktop/python/magaza/stok.txt","r",encoding="utf-8") as file:
            for i in file:
             urun_bilgileri = i.strip().split(":")  # Satırı ayırıyoruz
             urun_kod=urun_bilgileri[0]
             urun_adi=urun_bilgileri[1]
             urun_stok=int(urun_bilgileri[2])
             
             print("urun kodu:" ,urun_kod, "urun adı:",urun_adi,"urun stok:",urun_stok ,"\n","\n")
            
def stok_kontrol():
    azalan_urunler = []  # Azalan stok ürünleri depolamak için bir liste
    kon = input("Stok 5'ten az olan ürünleri görmek ister misiniz? (E/H): ").lower()
    
    if kon == "e":
        with open("C://users/faruk/desktop/python/magaza/stok.txt", "r", encoding="utf-8") as file:
            for i in file:
                urun_bilgileri = i.strip().split(":")
                
                # Ürün bilgilerini ayrıştırma
                urun_kod = urun_bilgileri[0]
                urun_adi = urun_bilgileri[1]
                urun_stok = int(urun_bilgileri[2])
                
                # Stok 5'ten azsa listeye ekle
                if urun_stok < 5:
                    azalan_urunler.append((urun_kod, urun_adi, urun_stok))

        # Azalan stok ürünlerini göster
        if azalan_urunler:
            print("Dikkat! Stok miktarı 5'ten az olan ürünler:")
            for urun in azalan_urunler:
                print(f"Ürün Kodu: {urun[0]}, Ürün Adı: {urun[1]}, Ürün Stok: {urun[2]}")
        else:
            print("Stok miktarı 5'ten az olan ürün yok.")
    else:
        print("Stok kontrolü iptal edildi.")
def indirim():
        with open("C://users/faruk/desktop/python/magaza/indirim.txt", "r", encoding="utf-8") as file:
         for i in file:
             urun=i.strip().split(":")
             urun_kod=urun[0]
             urun_fiyat=urun[1]
             urun_indirim=urun[2]
             urun_fiyat = float(urun[1])  # Convert price to a float
             urun_indirim = float(urun[2])
             with open("C://users/faruk/desktop/python/stok.txt", "r", encoding="utf-8") as files:
                 for s in files:
                     urun1=s.strip().split(":")
                     urunkod1=urun1[0]
                     urunad=urun1[1]
                     urunstok=urun1[2]
                     if urun_kod==urunkod1:
                          indirim=((urun_fiyat/100)*urun_indirim)

                          print(urunad,":",urun_fiyat,":",urun_indirim,":",indirim)


def giris():
   while True:
        print("ürün eklemek için<1>,ürün çıkarmak için<2>,stok kontrolu için<3>,azalan ürünler için <4>,inirinli ürün için <5> ,,çalışanbilgileri<6>")
        a1=input("ne yapmak istersiniz....")
        if a1=="1":
         urun_ekle()
        elif a1=="2":
         urun_cikar()
        elif a1=="3":
         urun_kontrol()
        
        elif a1=="4":
         stok_kontrol()
        elif a1=="5":
         indirim()
        elif a1=="6":
         pass
        
        else:        
         print("tekrar deneyiniz..")
         giris()
        
giris()