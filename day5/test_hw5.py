from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path 
from datetime import date


class Test_Hw5:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath =str (date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()
    
    @pytest.mark.parametrize("username,",[(" ")])
    def test_invalid_just_login(self,username):
        self.waitForElementVisibility((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")  
        usernameInput.send_keys(username)

        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        errorMessagePassword = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-just-login-with-{username}.png")
        assert errorMessagePassword.text == "Epic sadface: Password is required"   

    
    @pytest.mark.parametrize("password",[(" ")])
    def test_invalid_just_password(self,password):
        self.waitForElementVisibility((By.ID,"password"),5)
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys(password)

        passwordButton = self.driver.find_element(By.ID,"login-button")
        passwordButton.click()

        errorMessageLogin = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")

        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-just-password-with-{password}.png")
        assert errorMessageLogin.text == "Epic sadface: Username is required"
        

    
    @pytest.mark.parametrize("username, password", [("standard_user", "1"), ("locked_out_user", "60"), ("Kadir", "sauce_secret"), ("performance_glitch_user", "sauce_secret")])
    def test_wrong_password_login(self, username, password):
        self.waitForElementVisibility((By.ID, 'user-name'))

        usernameInput = self.driver.find_element(By.ID, 'user-name')
        passwordInput = self.driver.find_element(By.ID, 'password')
        loginBtn = self.driver.find_element(By.ID, 'login-button')

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput, username)
        actions.send_keys_to_element(passwordInput, password)
        actions.perform()

        loginBtn.click()

        errorMessage = self.driver.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

        self.driver.save_screenshot(
            f"{self.folderPath}/test-wrong-password-{username}-{password}-login.png")
        
        assert errorMessage.text == 'Epic sadface: Username and password do not match any user in this service'
    
    
    
    
    
    @pytest.mark.parametrize("username,password,",[("locked_out_user","secret_sauce")])
    def test_invalid_login_locked (self,username,password):
        
        self.waitForElementVisibility((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys(username)

        self.waitForElementVisibility((By.ID,"password"),5)
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys(password)

        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")

        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-locked-with-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        

   
    @pytest.mark.parametrize("username,password,",[(" "," ")])
    def test_shut_button(self,username,password):
        self.waitForElementVisibility((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys(username)
        
        self.waitForElementVisibility((By.ID,"password"),5)
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys(password)

        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        shutDownButton = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        shutDownButton.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-shut-button-with-{username}-{password}.png")

        assert True

    
    def test_valid_succesfull_login(self):
        
        self.waitForElementVisibility((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        
        
        self.waitForElementVisibility((By.ID,"password"),5)
        passwordInput = self.driver.find_element(By.ID,"password")
        

        actions = ActionChains(self.driver) 
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform() 

        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        products = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-valid-succesfull.png")

        assert len(products) == 6


   
    def test_add_to_card_button(self):

        self.waitForElementVisibility((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        
        
        self.waitForElementVisibility((By.ID,"password"),5)
        passwordInput = self.driver.find_element(By.ID,"password")

        actions = ActionChains(self.driver) 
        actions.send_keys_to_element(usernameInput,"problem_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform() 
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        self.waitForElementVisibility((By.CLASS_NAME,"inventory_item"))
        addToCardButtons = self.driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        
        
        
        self.driver.save_screenshot(f"{self.folderPath}/test-add-to-card-button.png")


        assert len(addToCardButtons) == 6
        
        


    def waitForElementVisibility(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located(locator))


