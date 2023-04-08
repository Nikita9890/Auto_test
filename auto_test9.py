from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(int(a)+int(b))

try:
    link = "  https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID,"num1")
    a = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    b = y_element.text
    sum = (int(a)+int(b))
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    import time
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()