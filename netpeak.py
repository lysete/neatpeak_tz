import os
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def get_random_string(n):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))


def get_random_digits(n):
    return ''.join((random.choice(string.digits) for _ in range(n)))


browser = webdriver.Firefox()
browser.get('https://netpeak.ua/')

career_element = WebDriverWait(browser, 30) \
    .until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Карьера')]")))

career_element.click()

browser.switch_to.window(browser.window_handles[-1])

i_want_to_work_element = WebDriverWait(browser, 30) \
    .until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Я хочу работать в Netpeak')]")))

i_want_to_work_element.click()

upload_element = WebDriverWait(browser, 30) \
    .until((ec.presence_of_element_located((By.NAME, "up_file"))))

# __file__ == ./netpeak.py
# os.path.abspath(__file__) == C:\Users\Swan\Desktop\Dasha\netpeak.py
# os.path.dirname(os.path.abspath(__file__)) == C:\Users\Swan\Desktop\Dasha
# os.path.dirname(os.path.abspath(__file__)) + '\\test.png' == C:\Users\Swan\Desktop\Dasha\test.png
upload_element.send_keys(os.path.dirname(os.path.abspath(__file__)) + '\\unnamed.jpg')

invalid_file_format_error_element = WebDriverWait(browser, 30) \
    .until(ec.presence_of_element_located((By.XPATH, "//*[@class='form-group has-error']")))

input_first_name = WebDriverWait(browser, 30) \
    .until(ec.presence_of_element_located((By.XPATH, "//*[@id='inputName']")))

input_first_name.send_keys(get_random_string(10))

input_last_name = WebDriverWait(browser, 30) \
    .until(ec.presence_of_element_located((By.XPATH, "//*[@id='inputLastname']"))).send_keys(get_random_string(10))

input_email = WebDriverWait(browser, 30) \
    .until(ec.presence_of_element_located((By.XPATH, "//*[@id='inputEmail']"))) \
    .send_keys(get_random_string(10) + '@' + get_random_string(5) + '.ua')

birth_year = WebDriverWait(browser, 30) \
    .until(ec.element_to_be_clickable((By.XPATH, "//*[@data-error-name='Birth year']")))
all_options = birth_year.find_elements_by_tag_name("option")
random_birth_year = random.choice(all_options).click()

birth_month = WebDriverWait(browser, 30) \
    .until(ec.element_to_be_clickable((By.XPATH, "//*[@data-error-name='Birth month']")))
all_options = birth_month.find_elements_by_tag_name("option")
random_birth_month = random.choice(all_options).click()

birth_day = WebDriverWait(browser, 30) \
    .until(ec.element_to_be_clickable((By.XPATH, "//*[@data-error-name='Birth day']")))
all_options = birth_day.find_elements_by_tag_name("option")
random_birth_day = random.choice(all_options).click()

input_phone = WebDriverWait(browser, 30) \
    .until(ec.presence_of_element_located((By.XPATH, "//*[@id='inputPhone']"))) \
    .send_keys('+380' + get_random_digits(9))

send_button = WebDriverWait(browser, 30) \
    .until(ec.element_to_be_clickable((By.NAME, "difficult")))

send_button.click()

course_element = WebDriverWait(browser, 30) \
    .until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Курсы')]")))

course_element.click()

