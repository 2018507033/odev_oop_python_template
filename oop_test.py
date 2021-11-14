import oop_assingment;

def test_oop():
    assert oop_assingment.sepet_fiyati(0.15) == 23.91218
    
    class urunler:
name = ""
comments = ""
OTVvergi = 0
KDVvergi = 0
ilk_fiyat = 0
son_fiyat = 0
def __init__(self,qname,qOTVvergi,qKDVvergi,qilk_fiyat)
self.name=qname
self.OTVvergi=qOTVvergi
self.KDVvergi=qKDVvergi
self.ilk_fiyat = qilk_fiyat
self.fiyat()

def fiyat(self)
tmp = self.ilk_fiyat + (self.ilk_fiyat*self.OTVvergi)
self.son_fiyat= tmp + (tmp*self.KDVvergi)

def pprint(self):
    print(f'{self.name}\'ın Fiyatı {self.son_fiyat}TL')
    ekmek = urunler ("Lavaş",0.1,0.2,200)
    peynir = urunler("kaşar",0.2,0.3,300)
    
   ekmek.pprint()

lavaşın fiyatı 264.0TL

peynir.pprint()
Kaşarın Fiyatı 468.0TL
