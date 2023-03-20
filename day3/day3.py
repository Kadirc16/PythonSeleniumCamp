#Sınıflar --> Classlar
#Modules
#Paket Yönetimi



# instance => örnek 

# Human classından bir nesne, ürün ürettik. Java daki new lemek.
from human import Human


human1 = Human("Enes")
human1.talk("Merhaba")
human1.walk()
print(human1) # __str__ ekleyerek classtan print alabiliyoruz.

human2 = Human("Halit")
human2.talk("Selam")
human2.walk()

Human("Melike").talk("Merhaba") # tek satırda da kullanabiliriz.

