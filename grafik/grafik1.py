import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import squarify
 
class grafik:
 def __init__(self,x=False,y=False):
   self.x=x
   self.y=y
 
 def cizgi(self,x,y):
   
  plt.plot(x,y,marker="*",linestyle="-",color="b",label="veri1")
  plt.xlabel("x ekseni")
  plt.ylabel("y exsen")
  plt.title("basit grafik")
  plt.legend()
  plt.grid(True, linestyle="--", linewidth=0.5, color="red", alpha=0.7)
  plt.show()
 
 def cubuk(self,x,y):
 
  plt.bar(x,y,color=["red","blue","green"])
  plt.xlabel("kategori")
  plt.ylabel("degerler")
  plt.title("cubuk grafik")
  plt.show()

  
 def yataycubuk(self,x,y):
 
    plt.barh(x,y,color=["red","blue"])
    plt.xlabel("x label")
    plt.ylabel("y label")
    plt.title("yatay cubuk grafil")
    plt.show()
 def histogram():
    veri=np.random.randn(1000)
    plt.hist(veri,bins=30,color="red",edgecolor='black',alpha=0.1)
    plt.xlabel("deger")
    plt.ylabel("frekans")
    plt.title("histogram")
    plt.show()
 @staticmethod
 def dagilim():
    x=np.random.randn(50)
    y=np.random.randn(50)
    plt.scatter(x,y,color="red",marker="x")
    plt.xlabel("x label")
    plt.ylabel("y label")
    plt.title("dagilim")
    plt.show()
 
 def pasta(self,x,y):
    
    renk=["red","pink","purple","blue","yellow"]
    plt.pie(x,labels=y,colors=renk,autopct="%1.1f%%",startangle=100,shadow=True,wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
    plt.title("pasta grafik")
    plt.show()
 @staticmethod
 def alan():
    x=range(1,6)
    y1=[3,4,5,6,7,8]
    y2=[1,2,3,4,5,6]
    plt.fill_between(x,y1,color="blue",alpha=0.5,label="veri1")
    plt.fill_between(x,y2,color="red",alpha=0.5,label="veri2" )
    plt.xlabel("x eksen")
    plt.ylabel=("y label")
    plt.legend()
    plt.show()
 @staticmethod
 def kutu():
    veri=[np.random.rand(10)*100 for _ in range(4)]
    plt.boxplot(veri,labels=["a","b","c","d"],patch_artist=True)
    plt.xlabel("kategori")
    plt.ylabel("deger")
    plt.title("kutu")
    plt.show()
 @staticmethod
 def radar():
    etiket=["hız","güc","dayanıklık","zeka","çevik"]
    deger=[80,60,70,90,95]
    N=len(etiket)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    deger+=deger[:1]
    angles+=angles[:1]
    plt.figure(figsize=(6,6))
    ax = plt.subplot(111, polar=True)
    ax.fill(angles,deger,color="red",alpha=0.4)
    ax.plot(angles,deger,color="red",linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(etiket)
    plt.title("radar grafik")
    plt.show()

 def cokgrafik(self,x,y1,y2):
 
    plt.plot(x,y1,marker="o",linestyle="-",color="blue",label="seri1")
    plt.plot(x,y2,marker="s",linestyle="--",color="red",label="seri2")
    plt.xlabel("x eksen")
    plt.ylabel("y label")
    plt.title("coklu cizgi")
    plt.grid()
    plt.legend()
    plt.show()
 @staticmethod
 def boncuk():
    x=np.random.rand(20)*100
    y=np.random.rand(20)*100
    boyut=np.random.rand(20)*100
    plt.scatter(x,y,s=boyut,alpha=0.5,color="red",edgecolors="black")
    plt.xlabel("x eksen")
    plt.ylabel("y label")
    plt.title("boncuk grafik")
    plt.show()
 @staticmethod
 def akis():
   x = range(1, 6)
   y1 = [3, 6, 9, 12, 15]
   y2 = [2, 5, 8, 11, 14]
   y3 = [1, 4, 7, 10, 13]

   plt.stackplot(x, y1, y2, y3, labels=["Kategori 1", "Kategori 2", "Kategori 3"], alpha=0.6)
   plt.xlabel("Zaman")
   plt.ylabel("Değer")
   plt.title("Akış Diyagramı")
   plt.legend()
   plt.show()
 @staticmethod
 def isi():
   theta = np.linspace(0, 2*np.pi, 10)
   r = np.abs(np.sin(theta))

   plt.polar(theta, r, marker="o")
   plt.title("Kutup Grafiği")
   plt.show()
 @staticmethod
 def agac():

  değerler = [500, 300, 200, 100]
  etiketler = ["Kategori A", "Kategori B", "Kategori C", "Kategori D"]
  renkler = ["red", "blue", "green", "orange"]
  squarify.plot(sizes=değerler, label=etiketler, color=renkler, alpha=0.7)
  plt.axis("off")
  plt.title("Ağaç Haritası")
  plt.show()
grafik=grafik()
#grafik.cizgi()
#grafik.cubuk()
#grafik.yataycubuk()
#grafik.histogram()
#grafik.dagilim()
#grafik.pasta()
#grafik.kutu()
#grafik.radar()
#grafik.cokgrafik()
#grafik.boncuk()
#grafik.akis()
#grafik.isi()
#grafik.agac()