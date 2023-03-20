#dosyanın ismi ile modulun ismi aynı olursa modul karmaşası ortaya çıkar
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep



""" Selenium a webdriver tanıtma yolları """
# selenium un kullandığı tarayıcı ile bizim kullandığımız tarayıcı ayrı ona al bunu kullan diyeceğiz.
# buradan sonra bir pencere açılmadıysa selenium kullanacaksın ama selenium a kullanacağı driver vermemişsin.

# -- yöntem 1
#driver = webdriver.Chrome

# --> yöntem 2 (exe dosyası belirtilen yerde olmalı)
#driver = webdriver.Chrome("C:\chromedriver.exe")

# --> yöntem 3 
driver = webdriver.Chrome(ChromeDriverManager().install()) 
#ChromeDriverManager bir class new lemek için () parantezlerini kullanmamız gerek.

#pip install webdriver-manager --> bu komutu çalıştırdığımızda bizim için drivermanager görevini üstlenip bizim için configure edecek. (topluluk ile çalışırken bu tercih edilir.)
driver.maximize_window() # tam ekran yapar.
driver.get("https://www.google.com/") # girdiğimiz linki bize getirir
input = driver.find_element(By.NAME,"q") #istediğimiz elementi bulduk. Selenium a tanıttık.
#print(f"Input : {input} ")
input.send_keys("kodlamaio")
sleep(3)
searchButton = driver.find_element(By.NAME,"btnK") 

#seacrhButton a önce find_element atadıktan sonra istediğimizi bularak işleme başlarız.
#print(searchButton)
sleep(2)
searchButton.click()
sleep(2)
firstResult = driver.find_element (By.XPATH ,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()

listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio sitesinde şu anda {len(listOfCourses)} adet kurs var.")


"""
firstResult =   driver.find_element (By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a ")
 xpath de rso içindeki çift tırnağı tek tırnağa düşürdüğümüz zaman problem çözülecektir.
firstResult.click() 
"""


#  sleep(2) yazdığımızda program 2 sn bekleyecektir. Ancak bu da iyi bir çözüm değildir.
#Herkesin interneti aynı hızda değil . biz send_keys gönderdikten sonra bekleme süresi herkeste farklı old. için defensive programlama ihtiyacı doğar. biz burada seleniuma sen bu element görünene kadar bekle diyebiliyoruz.


# sleep(10) açtığımız sayfa 10 saniye sonra kendiliğinden kapanır.
while True:
    continue   
#açılıp kapanıyor ise bunuda yapabiliriz sonsuz döngüye girer ve kapanmaz.
# input() açılıp kapanıyor ise bunu da kullanabiliriz.Ancak input ilerde hata almamıza neden olabilir.


# HTML LOCATORS
#butonu görüyoruz tıklayabiliyoruz oradaki inputu seleniumun görmesini sağlar. konumunu öğrenme
#tek tek name fln yazıp hata almak yerine from selenium.webdriver.common.by import By modülünü ekleyerek kodları By classından dahil edelim.

# CTRL + C = TERMİNALE TIKLADIKTAN SONRA DURDURUR


""" full xpath
 Ancak ilerde girmemiz gerek yere yeni bir dil eklendiğinde bu divlerin yeri değişebilir(xpath içinde geçerli).En tepeden (html) başlıyor.
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a

xpath 
en yakın unique alandan başlıyor.
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a 

ikisi de By.XPATH ile gönderilebilir.
 """

 #web scraping , data scraping sitelerden veri kazıma (örn.7 adet kurs var gibi veriyi siteden çekebilmek)
 #siber güvenlik durumlarında (reCaptcha) selenium burada takılır.