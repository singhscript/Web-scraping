import time
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pdb
import pandas as pd
from selenium.webdriver.common.keys import Keys

import xml
import lxml

# driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome(executable_path=r"C:\Users\cygnet\PycharmProjects\pythonProject2\chromedriver.exe")
driver.maximize_window()


file_path = r'D:\My desktop\Data extract\Zauba\Output_Files'
# 13000


def login():
    driver.get("https://www.zauba.com/user")
    user = driver.find_element(By.XPATH,'//input[@id="edit-name"]').send_keys("smshaikh")
    time.sleep(5)
    password = driver.find_element(By.XPATH,'//input[@id="edit-pass"]').send_keys("Admin@123")
    time.sleep(10)
    login = driver.find_element(By.XPATH,'//button[@id="edit-submit"]').click()
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

login()

for count in range(1, 197):
    # https://www.zaubacorp.com/company-list/p-+str(count)-company.html
    driver.get("https://www.zauba.com/import-hsn/p-" + str(count) + "-hs-code.html")
    time.sleep(10)
    tbl = driver.find_element(By.XPATH, '//table[@class="result-table"]').get_attribute('outerHTML')
    df = pd.read_html(tbl)
    df = df[0]
    # pdb.set_trace()
    print(df)
    df.to_csv(file_path + "\\Zauba_page_" + str(count) + "_all_rows.csv", index=False)

driver.quit()


