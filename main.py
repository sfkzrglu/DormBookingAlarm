import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from playsound import playsound

DROPDOWNMENUXPATH="/html/body/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div[1]/form/div/div[1]/div[1]/div/div/ul"
numberOfUpdates=0
gotResult=False

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('chromedriver',chrome_options=options) 
#the website is not shared publicly
driver.get('website')

time.sleep(2)

def checkElementForAnUpdate():
    dropDownMenu=driver.find_element(By.XPATH,DROPDOWNMENUXPATH)
    children=dropDownMenu.find_elements(By.XPATH,"./child::*")
    length=len(children)
    print(numberOfUpdates," - length is ",length)
    if length>2:
        playsound('alarm.mp3')
        print("ATTENTION!!!")
        gotResult=True

def update():
    global numberOfUpdates
    while gotResult is False:
        checkElementForAnUpdate()
        time.sleep(1200)
        numberOfUpdates+=1
        driver.refresh()

update()
