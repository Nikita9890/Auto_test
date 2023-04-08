from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.CSS_SELECTOR, "#book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element) #скрол страницы до нужного элемента
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button2 = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button2.click()
finally:
    time.sleep(10)
    browser.quit()

