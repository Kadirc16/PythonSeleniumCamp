from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

""" Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır. """
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.saucedemo.com/")


class hw_test :
   
   
    def test_invalid_just_login(self):
        
        usernameInput = driver.find_element(By.ID,"user-name")  
        usernameInput.send_keys(" ")
       
        sleep(2)

        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()

        errorMessagePassword = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessagePassword.text == "Epic sadface: Password is required"
        print(f"Just Login Test Result : {testResult}")

        sleep(5)
       


    def test_invalid_just_password(self):

        driver.get("https://www.saucedemo.com/")
        passwordInput = driver.find_element(By.ID,"password")

        passwordInput.send_keys(" ")

        sleep(2)

        passwordButton = driver.find_element(By.ID,"login-button")
        passwordButton.click()

        sleep(5)

        errorMessageLogin = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")

        testResult = errorMessageLogin.text == "Epic sadface: Username is required"
        print(f"Just Password Test Result : {testResult}")

    

    def test_invalid_login_locked (self):
        driver.get("https://www.saucedemo.com/")

        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("locked_out_user")

        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")

        sleep(2)

        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()

        sleep(5)

        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Login Locked Test Result : {testResult}")

   

    def test_shut_button(self):
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID,"user-name")  
        usernameInput.send_keys(" ")

        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys(" ")

        sleep(2)

        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()

        sleep(5)

        shutDownButton = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        shutDownButton.click()

        sleep(5)


        print(f"X Button is Shutdown . ")

        sleep(10)


    def test_invalid_succesfull (self):
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID,"user-name")  
        usernameInput.send_keys("standard_user")

        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")

        sleep(2)

        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()

        sleep(5)

        listOfInventory = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"There are {len(listOfInventory)} product in this list ")

      







        



testClass= hw_test ()
testClass.test_invalid_just_login()
testClass.test_invalid_just_password()
testClass.test_invalid_login_locked()
testClass.test_shut_button()
testClass.test_invalid_succesfull()

while True :
    continue








