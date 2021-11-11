from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(15)
driver.get("https://agmarknet.gov.in/")


# to select the dropdown values
def select_dropdown(element_value):
    for i in element_value.keys():
        element = driver.find_element(By.ID, i)
        selection = Select(element)
        selection.select_by_visible_text(element_value[i])
        time.sleep(6)  # required to load the district


# to change the dates
def date_selection(date_list):
    for j in date_list.keys():
        datefield = driver.find_element(By.ID, j)
        datefield.click()
        datefield.send_keys(Keys.CONTROL, "a")
        datefield.send_keys(Keys.BACKSPACE)
        datefield.send_keys(date_list[j])
        datefield.send_keys(Keys.ENTER)
        time.sleep(6)


# values to be passed in form of Dictionaries
values = {
    "ddlCommodity": "Potato",
    "ddlState": "Uttar Pradesh",
    "ddlDistrict": "Agra"
}

Date_range = {
    "txtDate": "01-Jan-2020",
    "txtDateTo": "31-Dec-2020"
}

# calling the functions
select_dropdown(values)
date_selection(Date_range)

time.sleep(10)  # keeping more sleep time to let the browser load the data

download = driver.find_element(By.ID, "cphBody_ButtonExcel")
download.click()
