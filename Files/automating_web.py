from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import yagmail
from datetime import date
import lxml
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)
try:
    today = date.today()
    day = today.strftime('%d')
    month = str(int(today.month)+1)
    if len(month) < 2:
        month = str(0) + month
    year = today.strftime('%y')
    date = today.strftime(year+month+day)

    DEPARTURE = 'fra'
    DESTINATION = 'kbv'

    def flight_checker():
        url = f"https://www.skyscanner.de/transport/fluge/fra/kbv/{date}/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27543110&inboundaltsenabled=true&infants=0&originentityid=27541706&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=0"
        browser.get(url)
        '''
        html = browser.page_source
        soup = BeautifulSoup(html)

        prices = soup.find_all(class_="BpkText_bpk-text__YWQwM BpkText_bpk-text--lg__ODFjM")
        print(prices)
        '''
        prices = browser.find_element(By.CSS_SELECTOR, 'div span.BpkText_bpk-text__YWQwM.BpkText_bpk-text--lg__ODFjM')
        print(prices)
    flight_checker()




finally:
    browser.quit()