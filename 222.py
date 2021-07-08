from anticaptchaofficial.imagecaptcha import *
from selenium import webdriver
import os
import time
import numpy as np
import pyautogui
import cv2

def capcha(driver):
    imgs(480, 360, 120, 65)

    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key("750e6dde3083fc28c19a71b57bf4f79c")

    captcha_text = solver.solve_and_return_solution("pic.png")
    if captcha_text != 0:
        print("captcha text " + captcha_text)

        driver.find_element_by_xpath('/html/body/div/form/input[3]').send_keys(captcha_text)
        driver.find_element_by_xpath('/html/body/div/form/input[4]').click()

    else:
        print("task finished with error " + solver.error_code)
    time.sleep(2)

    imgs(310, 460, 100, 60)

    captcha_text = solver.solve_and_return_solution("pic.png")
    if captcha_text != 0:
        print("captcha text " + captcha_text)

        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[2]/form/div[2]/div[1]/div/span/input').send_keys('qazaq123qazaq')
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[2]/form/div[2]/div[2]/div/span/input').send_keys('qazaq123')
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[2]/form/div[2]/div[3]/div/span/input').send_keys(captcha_text)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[2]/form/div[3]/span/input').click()

    else:
        print("task finished with error " + solver.error_code)


def main():
    torexe = os.popen(r'C:\spam\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
    PROXY = "socks5://localhost:9050"  # IP:PORT or HOST:PORT

    options = webdriver.ChromeOptions()

    options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\spam\chromedriver.exe')
    driver.get("http://qmxem5wzk543ppqnyzxsmow2jggexesk2mnzphd5ecnsope4befch5yd.onion/index.php")


    time.sleep(2)
    capcha(driver)

    y = input("Войдите в акаунт и наберите y: ")



def imgs (x, y, dx, dy):
    image = pyautogui.screenshot(region=(x, y, dx, dy))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite('pic.png', image)

if __name__ == '__main__':
    main()


