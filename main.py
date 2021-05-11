import csv
from selenium import webdriver
import pandas
from pandas import DataFrame
import requests

test_url = "https://downtowndallas.com/experience/stay/"

chrome_driver_path = "F:\software/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(test_url)

driver.find_element_by_xpath("/html/body").click()

driver.back()

driver.find_element_by_xpath("/html/body/main/div/section[2]/div[1]/div[3]/a").click()

place_name = driver.find_element_by_css_selector(".place-header h1").text
print(place_name)

address = driver.find_element_by_xpath("/html/body/main/article/div/div[1]/div[1]/a").text
print(address)

phone = driver.find_element_by_xpath("/html/body/main/article/div/div[1]/div[2]/div/a").text
print(phone)

area = driver.find_element_by_xpath("/html/body/main/article/div/div[1]/div[3]/a").text
print(area)

logo = driver.find_element_by_css_selector(".place-info-image img")
logo_src = logo.get_attribute("src")
print(logo_src)

driver.get(logo_src)
driver.save_screenshot("AC-Marriot.png")

my_dict = [
    {
        'Name': place_name,
        'Address': address,
        'Phone': phone,
        'Area': area,
        'Image-url': logo_src,
    }
]
print(my_dict)

data = pandas.DataFrame(my_dict)
data.to_csv('record.csv')