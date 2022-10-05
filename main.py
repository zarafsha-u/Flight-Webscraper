import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pprint import pprint


chromedriver_filepath= '/Users/zarafshauzzaman/PycharmProjects/web-scraping-departure-flights/chromedriver-5'
s = Service(chromedriver_filepath)
driver = webdriver.Chrome(service=s)



#google flights url has date and other requirements entered in already
#flight info found based on those requirements
driver.get('https://www.google.com/travel/flights/search?tfs=CBwQAholagwIAhIIL20vMHJoNmsSCjIwMjItMTAtMTNyBwgBEgNZWVooABolagcIARIDWVlaEgoyMDIyLTEwLTE3cgwIAhIIL20vMHJoNmsoAHABggELCP___________wFAAUgBmAEB')
time.sleep(20)



best_depflight_prices = driver.find_elements(By.CLASS_NAME, 'U3gSDe')
best_depflight_times = driver.find_elements(By.CLASS_NAME, 'zxVSec')
company_airport = driver.find_elements(By.CLASS_NAME, 'sSHqwe')



def edit_prices(scraped_price_list):
    prices = [scraped_price_list[i].text for i in range(len(scraped_price_list))]
    edited_price_list = [i.replace('\n', "").replace('round trip', "") for i in prices]
    return edited_price_list

def edit_times(scraped_times_list):
    times = [scraped_times_list[i].text for i in range(len(scraped_times_list))]
    edited_times_list = [i.replace('\n', "") for i in times]
    return edited_times_list

def edit_info(scraped_info):
    extra_info = [scraped_info[i].text for i in range(len(scraped_info))]
    while "" in extra_info:
        extra_info.remove("")
    while "round trip" in extra_info:
        extra_info.remove('round trip')
    extra_info.pop(0)
    edited_info_list = [extra_info[i] + " " +  extra_info[i+1] for i in range(0,len(extra_info)-1, 2)]
    if len(extra_info) % 2 == 1:
        edited_info_list.append(extra_info[len(extra_info)-1])
    return edited_info_list

price = edit_prices(best_depflight_prices)
times= edit_times(best_depflight_times)
info = edit_info(company_airport)



flights = {
    'prices': price,
    'times': times,
    'extra_info': info
}

print(flights['prices'][0])
driver.quit()