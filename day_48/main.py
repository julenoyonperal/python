# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 18:12:48 2021

@author: JOyon
"""
from selenium import webdriver

chrome_driver_path = 'L:/Analytics/Julen/python/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#driver.get('https://www.amazon.co.uk/')
driver.get('https://www.amazon.co.uk/Professional-Cleaning-SPINCARE-Cleaner-Removes/dp/B076P8BDSS?ref_=Oct_s9_apbd_oup_hd_bw_bH8uf&pf_rd_r=M5GA9F3Z9MNJKCY99CWX&pf_rd_p=73a5db4b-33c9-5fb6-af88-cc267d96065a&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=4085841')
price = driver.find_element_by_id('priceblock_ourprice')
print(price.text)

driver.get('https://www.python.org/')
search_bar = driver.find_element_by_name("q")
print(search_bar.get_attribute('placeholder'))


logo = driver.find_element_by_class_name("python-logo")

# buscar con csss
link = driver.find_element_by_css_selector(".documentation-widget a")
print(link.text)


# buscar con el Xpath - copy by xpath
driver.find_element_by_xpath('')

driver.close()
driver.quit()