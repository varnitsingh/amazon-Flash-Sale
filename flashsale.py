from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException,ElementNotInteractableException
from multiprocessing import Process
import time,sys,os

options = Options()
options.headless = False
options.page_load_strategy = 'eager'


def add_to_cart(username, password,item_url):
    driver = webdriver.Firefox(options=options)
    delay = 30
    driver.get(item_url)
    # for logging into amazon
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'nav-link-accountList')))
    except TimeoutException:
        print ("Loading Page took too much time!")
    driver.find_element_by_id('nav-link-accountList').click()
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'ap_email')))
    except TimeoutException:
        print ("Loading Page took too much time!")
    driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys(username + Keys.RETURN)
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'ap_password')))
    except TimeoutException:
        print ("Loading Page took too much time!")
    driver.find_element_by_xpath(
        '//*[@id="ap_password"]').send_keys(password + Keys.RETURN)

    # end of login code
    
    #once the add to cart button is activated, click it
    time.sleep(5)
    checkout = True
    while checkout:
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'goldboxBuyBox')))
        except TimeoutException:
            print ("Loading Page took too much time!")
            driver.refresh()
            continue
        try:
            cart = driver.find_element_by_xpath('//button[text()="\nAdd to Cart\n"]')
            cart.click()
            checkout = False
            continue
        except (NoSuchElementException, ElementClickInterceptedException,ElementNotInteractableException):
            driver.refresh()
        try:
            waitlist = driver.find_element_by_xpath('//button[text()="\nJoin Waitlist\n"]')
            waitlist.click()
            checkout = False
            continue
        except (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException):
            driver.refresh()




if __name__ == '__main__':
    '''
    Example on how to add more accounts.
    add another process name for example third_process
    third_process = Process(target=add_to_cart,args=['account_email@gmail.com','password','product_link'])
    then write
    third_process.start()
    then in the end write
    third_process.join()
    '''
    first_process = Process(target=add_to_cart, args=['test-email@gmail.com','123','https://www.amazon.in/Redmi-Sky-Blue-64GB-Storage/dp/B08697N43N/ref=gbph_tit_m-1_b5c2_591026a7?smid=AQUYM0O99MFUT&pf_rd_p=be9b047d-8b2e-4770-b354-a887418fb5c2&pf_rd_s=merchandised-search-1&pf_rd_t=101&pf_rd_i=22154369031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=XJ59JK96DQBH2917T9BP'])
    first_process.start()
    #second_process = Process(target=add_to_cart, args=['test@fuwamofu.com','6500','https://www.amazon.in/dp/B086978F2L/ref=cm_sw_r_tw_dp_x_pwCuFbYVYFBP2'])
    #second_process.start()
    
    first_process.join()
    #second_process.join()