#!/usr/bin/env python
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class ESHOT:

    def setup(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.PhantomJS(executable_path='/opt/local/bin/phantomjs')
        self.driver.maximize_window()

    def mainPage(self):
        self.driver.get('http://mobil.eshot.gov.tr/BakiyeSorgulama.aspx')
        self.driver.implicitly_wait(10)
        #print('[+] Main page loaded.')

    def balanceQuery(self, card_no):
        self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtSorgula").send_keys(card_no)
        self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnSorgu").click()
        print(self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblkalanbakiyesonuc").text)
        #print('[+] Balance query completed.')

    def tearDown(self):
        self.driver.close()
