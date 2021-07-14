from anticaptchaofficial.imagecaptcha import *  # Антикапча
from selenium import webdriver  # селениум
import os  # селениум
import time  # таймер
import numpy as np  # скриншоты
import pyautogui  #
import cv2  #


def capcha(driver):
    # Снимаем капчу
    imgs(383, 159, 170, 64)

    key = str(configini('key'))
    # Подключаемся к антикапче
    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key(key)
    # Отправляем данные капчи
    captcha_text = solver.solve_and_return_solution("pic.png")
    # Если получили ответ
    if captcha_text != 0:
        # Выводим сообщение
        print("captcha text " + captcha_text)
        # Вводим капчу и проходим далее
        driver.find_element_by_xpath('/html/body/div/form/input[1]').send_keys(captcha_text)
        driver.find_element_by_xpath('/html/body/div/form/input[4]').click()
    else:
        # Если капча не распознана выводим ошибку
        print("task finished with error " + solver.error_code)

    # Ждём загрузки страници
    time.sleep(2)
    # Снимаем капчу
    imgs(360, 520, 330, 90)
    # Отправляем данные капчи
    captcha_text = solver.solve_and_return_solution("pic.png")
    # Если получили ответ
    if captcha_text != 0:
        # Выводим сообщение
        print("captcha text " + captcha_text)
        # Вводим капчу, логин и пароль и проходим далее
        # надо получать данные из файла
        login = str(configini('login')).replace("\n","")
        password = str(configini('password')).replace("\n","")
        driver.find_element_by_xpath('/html/body/div/div[2]/div/form/ul/li[1]/input').send_keys(login)
        driver.find_element_by_xpath('/html/body/div/div[2]/div/form/ul/li[2]/input').send_keys(password)
        driver.find_element_by_xpath('/html/body/div/div[2]/div/form/ul/li[4]/input').send_keys(captcha_text)
        driver.find_element_by_xpath('/html/body/div/div[2]/div/form/button').click()

    else:
        # Если капча не распознана выводим ошибку
        print("task finished with error " + solver.error_code)


def main():
    torexe = os.popen(r'C:\spam\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
    PROXY = "socks5://localhost:9050"  # IP:PORT or HOST:PORT

    options = webdriver.ChromeOptions()

    options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\spam\chromedriver.exe')
    driver.get("http://hydraruzxpnew4af.onion/")

    time.sleep(2)
    capcha(driver)

    # n = open('number1.txt', 'r')
    i = 5093
    # f = open('pars.txt', 'w')

    while i <= 10000:
        driver.get("http://hydraruzxpnew4af.onion/market/" + str(i))

        try:
            nameShop = driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/h1')
            n = open('number1.txt', 'w')
            n.write(str(i))
            f = open('pars.txt', 'a')
            f.write(str(i) + '	' + str(nameShop.text) + '\n')
            print(i)
            print(str(nameShop.text))
        except:
            pass
        i += 1
        time.sleep(11)


def imgs(x, y, dx, dy):
    image = pyautogui.screenshot(region=(x, y, dx, dy))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite('pic.png', image)


def configini(name):
    conf = open('config.txt', 'r')
    login = str(conf.readline())
    password = str(conf.readline())
    key = str(conf.read())

    if name == 'login':
        return login
    elif name == 'password':
        return password
    else:
        return key

    conf.close()


if __name__ == '__main__':
    main()
