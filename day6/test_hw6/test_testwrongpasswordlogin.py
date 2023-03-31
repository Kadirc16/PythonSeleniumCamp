# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constants import globalConstants
from pathlib import Path
from datetime import date
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class TestTestwrongpasswordlogin():
  def setup_method(self):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.folderPath =str (date.today())
    Path(self.folderPath).mkdir(exist_ok=True)
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  @pytest.mark.parametrize("username,password",[("standard_user","1"),("Kadir","sauce_secret"),("performance_glitch_user","locked_out_user")])
  def test_testwrongpasswordlogin(self,username,password):
    self.driver.get(globalConstants.URL)
    self.driver.maximize_window()
    self.waitForElementVisible((By.ID, globalConstants.idButton))
    self.driver.find_element(By.ID, globalConstants.idButton).click()
    self.driver.find_element(By.ID, globalConstants.idButton).send_keys(username)
    self.waitForElementVisible((By.ID, globalConstants.passwordButton))
    self.driver.find_element(By.ID, globalConstants.passwordButton).click()
    self.driver.find_element(By.ID, globalConstants.passwordButton).send_keys(password)
    self.waitForElementVisible((By.ID, globalConstants.loginButton))
    self.driver.find_element(By.ID, globalConstants.loginButton).click()
    self.waitForElementVisible((By.XPATH, "//div[@id=\'login_button_container\']/div/form/div[3]/h3"))

    self.driver.save_screenshot(f"{self.folderPath}/test-wrong-login-with{username}-{password}.png")
    assert self.driver.find_element(By.XPATH, "//div[@id=\'login_button_container\']/div/form/div[3]/h3").text == globalConstants.textNotMatchAnything

  
  def waitForElementVisible(self,locator,timeout=5):
    WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located(locator))
