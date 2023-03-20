#Moduller
class Matematik:
    def __init__(self,sayi1,sayi2) : #constructor-yapıcı
        self.s1 = sayi1
        self.s2 = sayi2
        print("Matematik başladı (referans oluştu.)")
        """ bu constructor yapısı aslında referans oluştururken () yaptığımızda kendiliğinden oluşuyor ve bu blok yazmasak da çalışıyor.ekstra bir şey yapmak istersen ( self.s1 = sayi1
        self.s2 = sayi2)
        buraya tanımlayayıp aşağıdaki gibi kullanabilirsin. initialize 
        self classın kendisi pyhtonda bulundurulmak zorundadır."""
    
    def topla(self):
        return self.s1+self.s2

    def cikar(self):
        return self.s1-self.s2
    
    def bol(self):
        return self.s1/self.s2
    
    def carp(self):
        return self.s1*self.s2

#1 tane referans oluştur. İnstance
matematik = Matematik (14,7) 
toplaSonuc = matematik.topla()
print(f"Sonuç : {toplaSonuc}")

# matematik = Matematik(14,7)
# sonuc = matematik.bol()
# print("Sonuc : "+ str(sonuc))


 #burada Matematik'i inheritance ettik. super base aldığı sınıfın ta kendisi...
class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)
    def varyansHesapla(self):
        return self.s1 * self.s2