# -*- coding: utf-8 -*-
'''
Created in 12/2019
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import os

# input info for bot 
os.system('cls')
print('')
print('\033[0;32mLOGIN INFORMATION\033[m')
print('')
#username = str(input('User: ')) # your user
#password = str(input('Password: ')) # your password
os.system('cls')
print('')
print('Loading...')
print('')
urls = ['https://www.instagram.com/forbesitalia/followers/','https://www.instagram.com/lercio.it/followers/']
# load browser drive in to var and open

driver = webdriver.Firefox() # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
#except:
    #print('\033[0;31mDRIVER ERROR!\033[m Check installed drive or path.')

# function to access the login page and log in
def botlogin (user, pwd):
    username = user # your user
    password = pwd # your password
    driver.get('https://www.instagram.com') # instagram url
    sleep(1)
    driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]').click() # click on the 'connect' button element
    sleep(1)
    userelement = driver.find_element_by_xpath('//input[@name="username"]') # 'username' input element
    userelement.clear()
    userelement.send_keys(username) # user insertion in 'user' element
    pwdelement = driver.find_element_by_xpath('//input[@name="password"]') # 'password 'input element
    pwdelement.clear()
    pwdelement.send_keys(password) # password insertion in 'password' element##/html/body/div[1]/section/main/div/header/section/ul/li[2]/a
    pwdelement.send_keys(Keys.RETURN) # log in to page/html/body/div[1]/section/main/div/header/section/ul/li[2]/a
    sleep(2)
    try:
       stories()
    except KeyboardInterrupt:
            print('\033[0;33mProgram terminated by the user!\033[m')
    except:
            print('\033[0;31mUNEXPECTED ERROR ON STORIES\033[m, please try again and verify your connection!')


# function to view the stories# "//a[@href='/instagram/followers/']"
def stories():
    sleep(1)
    for url in urls:
      driver.get(url)
      driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
      sleep(10)


# execution of functions
'''write below your credentials'''
username = "your_username"
password =  "your_pass"
try:
    botlogin(username, password)
except KeyboardInterrupt:
    print('\033[0;33mProgram terminated by the user!\033[m')
except:
    print('\033[0;31mUNEXPECTED ERROR ON LOGIN\033[m, please try again and verify your connection!')


print('')
print('Finish!')
print('')

'''
# references html
# //a[@href="/accounts/login/?source=auth_switcher"] --> 'connect' page button element
# //input[@name="username"] --> 'username' input element
# //input[@name="password"] --> 'password 'input element
# //button[contains(text(), "Agora não")] --> the notification button
# //div[contains(text(), "Ver tudo")] --> the tab where the stories are
# @class="coreSpriteRightChevron" --> next storie button
'''
