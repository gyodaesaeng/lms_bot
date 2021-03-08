import re
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_second(text):
    h, m, s = 0, 0, 0
    index = text.find('시')
    if index > -1:
        h = int(text[:index])
        text = text[index + 1:]
    index = text.find('분')
    if index > -1:
        m = int(text[:index])
        text = text[index + 1:]
    index = text.find('초')
    if index > -1:
        s = int(text[:index])
    return h * 3600 + m * 60 + s


def login():
    driver.get(lms_url + '/ilos/main/member/login_form.acl')
    driver.find_element(By.NAME, 'usr_id').send_keys(usr_id)
    driver.find_element(By.NAME, 'usr_pwd').send_keys(usr_pwd)
    driver.find_element(By.CLASS_NAME, 'btntype').click()


def listen_class():
    sleep(1)
    subjects = driver.find_elements(By.CLASS_NAME, 'sub_open')
    for i in range(len(subjects)):
        sleep(1)
        subjects = driver.find_elements(By.CLASS_NAME, 'sub_open')
        subjects[i].click()
        sleep(1)
        weeks = driver.find_elements(By.CLASS_NAME, 'wb-on')
        for j in range(len(weeks)):
            sleep(1)
            weeks = driver.find_elements(By.CLASS_NAME, 'wb-on')
            weeks[j].find_element(By.CLASS_NAME, 'wb-week-on').click()
            sleep(1)
            elements = driver.find_elements(By.XPATH, '//div/ul/li[1]/ol/li[5]/div/div')
            for k in range(len(elements)):
                elements = driver.find_elements(By.XPATH, '//div/ul/li[1]/ol/li[5]/div/div')
                e = elements[k]
                times = re.split(" / ", e.find_element(By.XPATH, './/div[3]').text)
                last = get_second(times[1]) - get_second(times[0])
                print(e.find_element(By.XPATH, './/div[1]').text)
                print(last)
                if last > 0:
                    sleep(1)
                    e.find_element(By.XPATH, './/span').click()
                    try:
                        sleep(1)
                        alert = driver.switch_to.alert
                        alert.dismiss()
                        print('학습인정기간이 지나 출석시간으로 인정되지 않습니다.')
                    except:
                        sleep(last + 10)
                        driver.find_element(By.ID, 'close_').click()
                        print('출석 완료')
                        try:
                            alert = driver.switch_to.alert
                            alert.dismiss()
                            print('alert occur')
                        except:
                            print('no alert')
            driver.get(lms_url + '/ilos/st/course/submain_form.acl')
        driver.get(lms_url + '/ilos/main/main_form.acl')


driver = webdriver.Chrome('./chromedriver')
with open('userInfo.json', encoding='utf-8') as json_file:
    userInfoJson = json.load(json_file)
    usr_id = userInfoJson['id']
    usr_pwd = userInfoJson['password']
    lms_url = userInfoJson['lms_url']
login()
try:
    listen_class()
    print("every classes are listened.")
finally:
    driver.quit()
