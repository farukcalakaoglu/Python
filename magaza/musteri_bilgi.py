#müstri bilgi
def musteri_bilgi():
    with open("C://users/faruk/desktop/python/magaza/musteri.txt", "r", encoding="utf-8") as file:
        musteri = file.readline()
        print(musteri)
        
        
musteri_bilgi()