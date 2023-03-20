from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


""" Kişinin doğru giriş yapmadığı bir senaryoyu test edelim. """
#Chrome test yazılımı tarafından kontrol ediliyor ve anlıyor. Manuel müdahalede bulunsak bile reCaptcha yı geçmeye izin vermiyor.
class Test_Sauce:

    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        # en fazla 5 saniye olacak şekilde user-name id'li görünmesini bekle . sleep yapısını buna çevireceğiz.
        usernameInput =driver.find_element(By.ID,"user-name")
        passwordInput= driver.find_element(By.ID,"password")
        sleep(3)
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
       # testResult = errorMessage.text == "HATALI GİRİŞ" burada sonuç False gelir. bize verdiği text farklıdır. Bu testten geçip geçmediğini kontrol edebiliriz.
        print(f"TEST SONUCU : {testResult}")
      
    
        
        

testClass = Test_Sauce()
testClass.test_invalid_login()


