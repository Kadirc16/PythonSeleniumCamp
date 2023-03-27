from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


""" Kişinin doğru giriş yapmadığı bir senaryoyu test edelim. """
#Chrome test yazılımı tarafından kontrol ediliyor ve anlıyor. Manuel müdahalede bulunsak bile reCaptcha yı geçmeye izin vermiyor.
class Test_Sauce:

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        #her seferinde newlemek (driver=self.initializeDriver) yerine init ile parametre olarak göndereceğiz.ilgili alanları classın kendi içine taşımış olduk.
    
    
    def test_invalid_login(self):
     
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name"))) # maks 5 sn ilgili şartın sağlanmasını until.(visibility_of_element_located)bekleyecek. 
        # en fazla 5 saniye olacak şekilde user-name id'li görünmesini bekle . sleep yapısını buna çevireceğiz.çift parantezin sebebi iki parametre göndermemiz gerekiyor. ancak üstteki fonksiyon tek parametre istiyor.burada tek parametre içinde göndererek çözdük.alttaki defensive oldu
  

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
       
        usernameInput =self.driver.find_element(By.ID,"user-name")
        passwordInput= self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        
        loginBtn = self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
       # testResult = errorMessage.text == "HATALI GİRİŞ" burada sonuç False gelir. bize verdiği text farklıdır. Bu testten geçip geçmediğini kontrol edebiliriz.
        print(f"TEST SONUCU : {testResult}")

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name"))) 
        usernameInput =self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        passwordInput= self.driver.find_element(By.ID,"password")

        
        
        #bu aksiyon zincirleme şeklinde çalışacak ama hangi driver üzerinde çalışacağını buradan (self.driver) belirtiyoruz.
        actions = ActionChains(self.driver) 
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform() 
        #bunları perform ettiğimizde birbiri ardına çalışacak. perform demezsek zinciri oluşturur ama hiçbir zaman çalıştırmaz.
      
       
        #usernameInput.send_keys("standard_user")
        #passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

     
      


        

     
        
        
      
    
        
        

testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()


"""  Action Chains 
         bizim aksiyonları zincir misali birbirine bağlamaları ve bu sıralamada kullanabilmemizi sağlayan yapı 
         
         
         
         """
""" self.driver.execute_script("window.scrollTo(0,500)") javascript bilmemize gerek yok bu işlemlerin çoğunluğu seleniumda mevcut sadece js ile de yapabileceğimiz gösterdi.


!!!BU ÖRNEK PYTEST KULLANILMADAN YAPILMIŞTIR.!!!
 """


