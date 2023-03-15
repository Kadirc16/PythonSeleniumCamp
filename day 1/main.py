print("Kodlama.io")
 # print() fonksiyonu ekrana yazı yazdırmak için kullanılır.

# Değişkenler
""" 
Değişkenler, programlama dillerinde verileri saklamak için kullanılan isimlendirilmiş yer tutuculardır. Ayrıca print() ile yazdırmaktansa ileride güncellemek daha kolaydır. 
Değişken değerlerini değiştirebiliriz.
"""
baslik = "Taşıt Kredisi" # baslik değişkenine "Taşıt Kredisi" değerini atadık.
print(baslik)

# Veri Türleri

#string => metinsel ifade 
baslik = "İhtiyaç Kredisi"
print(baslik) 

#int , integer => tam sayı
vade = 36 #numeric bir ifade matematiksel işlemler yapabiliriz.
ekVade = 6
vade2 = "36" #metinsel bir ifade ""

# float,decimal,double  ondalıklı ifade tutanlar
aylikOdeme = 200.50 

#bool , boolean => True veya False karar yapılarında python da büyük harfle başlar
yukselisteMi = True

# Matematiksel İşlemler
# Toplama + 
# Çıkarma -
# Çarpma *
# Bölme /
# Üs alma **
# Mod alma %
# Tam Bölme //
print(36 + 6)
print(vade + 12 )
print(vade + ekVade)



# -
print(8 - 2)
print(vade - ekVade)

# *
print(5*5)
print(vade * ekVade)

# / sonucu float getirir 
print( 12/6 )


yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operatörü =bir sayının bir sayıya bölümünden kalanı

print(10%2)
print(vade %  5 )
print(vade % ekVade)
print (40 % 10 )

# mantıksal operatörler karşılaştırma operatörleri

"""
Belirli bir koşulu kontrol etmek için kullanılır.
== => eşitse
!= => eşit değilse
> => büyükse
< => küçükse
<= => küçük veya eşitse
>= => büyük veya eşitse
"""

# eşit eşittir ==
print(1 == 1) #boolean true ya da false verir
print(1 == 2)

# CTRL K + CTRL C yorum satırı oluşturur ya da editten de yapılabilir
# print(3 > 1)
# print(1 > 1)
# print(1 >= 1)

print (3 < 1)
print (1 < 2)
print(1 < 1)
print (1 <= 1)

print (1 != 1)
print (1 != 2)

# and => ve her iki koşul da doğruysa True diğer durumlarda False
# or => veya her iki koşuldan biri doğruysa True diğer durumlarda False

print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)
print(2 > 1 and 5 > 2 and 3 > 2)

# Karar Yapıları
"""
if => eğer
elif => eğer değilse
else => değilse
if koşul:
    koşul sağlandığında yapılacak işlemler
elif koşul2:
    koşul2 sağlanmadığında yapılacak işlemler
else:
    koşullar sağlanmadığında yapılacak işlemler
"""

sayi1 = 15
sayi2 = 15
# sayi1 sayi2'den büyükse ekrana sayi 1 daha büyük yazdır
#condition karar doğru olduğunda çalıştırılacak

"""indent mantığı pyhton çalışmasında bir bloğu , boşluğu ifade eder.
  if in içerisinde altındaki boşluklar if bloğunun içinde olduğunu gösterir
 """
 # if den sonra elif yerine if devam etseydik yeni bir karar bloğu oluşturmuş olurduk.
 #​ilki doğruysa diğerlerini okumaz. 
if sayi1 >= sayi2 :
    print("sayi 1 sayi 2'den büyüktür.")

elif sayi1 == sayi2 :
    print("iki sayı eşittir.")
# eğer if ve else if bloklarından hiçbirine girmez ise 
else :
    print("sayi1 sayi2'den küçüktür")
    print("Burası if bloğunun dışındadır.")


