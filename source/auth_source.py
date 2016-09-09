#-*- coding: utf-8 -*-

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class Authorization:

    def __init__(self, app):
        self.app = app

    def login(self, login_name, password):
        wd = self.app.wd
        self.enter_authorization()
        wd.find_element_by_name("login").send_keys(login_name)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_class_name("js-authFormLogin").submit()
        WebDriverWait(self.app.wd, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "user-account")))
        assert "http://irr.ru.stage/account/items" == self.app.wd.current_url

    def enter_authorization(self):
        wd = self.app.wd
        wd.find_element_by_class_name("js-authorizationButton").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_class_name("js-authBlockMenuButton").click()
        WebDriverWait(self.app.wd, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "js-authBlockDropDown")))
        wd.find_element_by_link_text("Выход").click()
        WebDriverWait(self.app.wd, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "js-authorizationButton")))
