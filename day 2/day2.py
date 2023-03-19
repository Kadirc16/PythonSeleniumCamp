faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

#Girdiğimiz değer veya metnin hangi tipte olduğunu görebilmek için "type" kullanırız.
print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12) # bu yapıda string ifadeyi integere çevirerek işlem yapabiliriz. 
# print(int(krediAdi)) karakter içerdiği için çeviremez.

faiz = str(faiz)  # string e çevirdik .
print(type(faiz))

# input kullanıcı girdisi almamızı sağlayan bir fonksiyon 
vade = 36 # int(input("Lütfen istediğiniz vade sayısını giriniz : ")) 
print(type(vade)) # kullanıcıdan alınan input pyhtonda default olarak string olur.
#print(int(vade) + 12)  burada int çevirdik
vade = vade + 12
# string interpolation 

# yukarıda vadeyi int çevirdik. ancak aşağıda string + int hata verir o yüzden str ye çevirmiş olduk.str+str oldu.
print("Seçtiğiniz vade sonucu ortaya çıkan vade : " + str(vade)) # yöntem - 1

#format fonksiyonu 
#  burada solda verdiğimiz takma isme sağda değerini belirtiyoruz. 
print("Seçtiğiniz vade sonucu ortaya çıkan vade :  {vadeSayisi}".format(vadeSayisi=vade)) # yöntem 2


print(f"Seçtiğiniz vade sonucu ortaya çıkan vade : {vade}") # yöntem 3


isim = "Kadir"
metin = "Merhaba {name}".format(name=isim)
print(metin)

# f-string
# metin içinde python kodu yazıyormuşuz gibi düşüneceğiz.

metin = f"Hoşgeldiniz {1+1}" # içini kod gibi gördüğü için burada toplama işlemi yapar
print(metin)

#listeler -->verilerin liste grup olarak saklanmasını sağlar. Array
#Pyhtonda farklı data tipinde elemanlar tanımlanabilir
#fonksiyonlar
# index mantığı vardır. Saymaya 0 dan başlar. #liste dışında verirsek out of range hatası verir.
krediler  = ["İhtiyaç Kredisi","Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))
print(krediler[0]) 
print(len(krediler)) # length

dizi = ["İhtiyaç Kredisi" , 10 , 5.2 , True ]
print(dizi)

krediler.append("Özel Kredi") # append bir objenin listenin sonuna eklemeyi sağlar.
print(krediler)

print("********")

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0) # verdiğin indexteki objeyi siler . vermezsen son objeyi siler.
print(krediler)

krediler.remove("Taşıt Kredisi")  #index değil de değer bazlı çalışır. ilk bulduğu değeri siler.
print(krediler)

krediler.extend(["Y Kredisi","Z Kredisi"]) #diziye birden çok ekleme yapmak istersek .extend
print(krediler)

# Döngüler ---> for , foreach , while
# Döngü = bir condition vererek bu condition sağlandığı sürece tekrar tekrar çalıştır demek

# for 
# i 0 dan başladı 10 a kadar çalışır. 10 dahil değil
for i in range(10):
    print("xx")
    print(i)

print("************")

for i in range(5,10):
    print (i)

print("************")
for i in range(0,51,10) :# ilk başlangıç,iki son , üçüncü eleman kaçar kaçar arttırmamız gerektiğini gösterir.
    print (i)

print("************")
"""     for i in range(0.1,0.5): integer ister kod çalışmaz.
        print(i) """

krediler  = ["İhtiyaç Kredisi","Taşıt Kredisi", "Konut Kredisi","X Kredisi"]
for kredi in krediler :  #yöntem 1
    print(kredi)

print("************")

for i in range(len(krediler)): # yöntem 2 bunda hangi indexte çalıştığımız sınırı belirliyoruz.len(3) desekte aynı çıktı olacaktı
    print(krediler[i])

    # While
i=0 
while i <10 : #yanındaki condition True old. sürece içindeki bloğu çalıştırır.
        print("x")
        i = i + 1
print("y")

print("************")

while True : 
     print("X")
     break #break komutu ile döngüyü durdurduk.

print("************")

i= 0

while i < len(krediler):
     print(krediler[i])
     i +=1 #bu kısmı yazmazsak arraydeki ilk değer sınırsız döngüde kalacak 1 arttır i = i + 1 ile aynı

print("*****")
i = 0
while i < len(krediler):
    print(i)
    print(krediler[i])
    i += 1              # 1.indexten başlattık. İhtiyaç Kredisi 0. index haliyle yazmadı.
    if krediler[i] == "Konut Kredisi" :
        break # burada ise Konut Kredisine kadar olan kısmı yazacak Konut Kredisi ve sonrasını yazmayacak.

# Fonksiyonlar (methodlar) --- def ---> definition define

fiyat = 100
indirim = 20

yeniFiyat = fiyat - indirim

def calculate():            #burada bir fonksiyon tanımladık. calculate()
     print(100-20)

def calculateWithParams( fiyat,indirim) :# burada 2 parametreli tanımladık.
     print(fiyat-indirim)

def sayHello(name):
     print(f"Merhaba {name}")

calculate()
calculateWithParams(50,10)
calculateWithParams(80,30)
sayHello("Ahmet")
sayHello("Esin")

print("*****")
# Fonksiyonun geriye değer döndürme

def calculateAndReturn(price,discount):
     return price-discount    

yeniFiyat = calculateAndReturn (200,50)
print(yeniFiyat )

# java daki void = return
def calculatePrice (price , discount):
     print(price-discount)

def calculatePriceAndReturn (price , discount):
     return price-discount

print("*********")

fonk1 = calculatePrice (150,50)
fonk2 = calculatePriceAndReturn(200,100)

print(f"174.satır : {fonk1}")
print(f"175.satır : {fonk2}")
#174.satır print olarak girilmiş . haliyle değer döndürmüyor (none). fonks. kendi içinde kullanıyor.
#175.satır return old. için değer döndürür.

print("*********")
