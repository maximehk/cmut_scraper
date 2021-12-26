from creds import CmutCredentials
from selenium import webdriver
from constants import CmutUrls
from selenium.webdriver.common.by import By


class CmutDriver:
    def __init__(self, credentials: CmutCredentials, driver: webdriver.Remote):
        self.credentials = credentials
        self.driver = driver

    def login(self):
        self.driver.get(CmutUrls.AUTH)
        self.driver.find_element(By.ID, "_userid").send_keys(self.credentials.username)
