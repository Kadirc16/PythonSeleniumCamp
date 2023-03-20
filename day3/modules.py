#alias
""" from matematik import topla # ---> sadece topla metodunu import ettik. print(topla(10,20)) olarak kullanırız
#import matematik as m ---> tamamını import edip m olarak burada kullandık. print(m.topla(10,20)) olarak kullanırız. """

from matematik import topla as toplamaIslemi # takma ad ile de kullanabiliriz 

from day2 import sayHello
from human import Human

#built- in modules
import random
from selenium import webdriver

#package
#import matematik direkt matematik.topla olarak kullanılabilir. İstersek as ile kendimiz takma isim de ekleyebiliriz.

#random rastgele sayı üreten bir modül
print(toplamaIslemi(10,20))
#print(m.topla(10,20))
print(random.randint(0,100))

# random kaynak kodlarına veya herhangi bir importun ctrl ye basılı tutup üstüne tıkla

human1 = Human("Mirza")
human1.talk("Merhaba")

#packages 
# #daha önceden yazılmış kod paketlerini pypi sitesinden dahil ederiz.
# pypi i terminal kısmında pip yazıp kurulu olup olmadığını kontrol edebiliriz.
#"pip install selenium" terminale yazarak kurabiliriz. ya da pypi sitesinde selenium aratarak koplaya şıkkına basarak direkt terminale yapıştırabiliriz.

chromeDriver = webdriver.Chrome()