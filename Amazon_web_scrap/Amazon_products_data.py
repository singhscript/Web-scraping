import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

path = r'C:\Users\cygnet\Desktop\Data extract\file3.csv'

name = []
price = []

for i in range(1,14):
    url = 'https://www.amazon.in/s?k=iphone&page=2&crid=LX749TLM37NO&qid=1658221203&sprefix=%2Caps%2C1240&ref=sr_pg_'+str(i)
    driver.get(url)
    phonexpath = '//span[@class="a-size-medium a-color-base a-text-normal"]'
    rows1 = driver.find_elements_by_xpath(phonexpath)
    pricexpath = '//span[@class="a-price-whole"]'
    row2 = driver.find_elements_by_xpath(pricexpath)

    for item in rows1:
        name.append(item.text)
        print(name)

    for prices in row2:
        price.append(prices.text)
        print(price)

    final = {"Item":name,"price":price}
    df = pd.DataFrame.from_dict(final, orient='index')
    df = df.transpose()
    print(df)
    df.to_csv(path, index = False)

# df = pd.DataFrame.from_dict(data, orient='index')
#         df = df.transpose()


