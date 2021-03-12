
from selenium import webdriver
from time import sleep

def loop1():
    sleep(10)
    driver.find_element_by_xpath("//*[@id=\"msg\"]/div/div[3]/div[3]/button").click() #Use
    sleep(10)
    try:
        driver.find_element_by_xpath("//*[@id=\"form1\"]/div/input").send_keys(vidUrl) # Insert video link
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"form1\"]/div/div/button").click() # Find
        sleep(10)
        driver.find_element_by_xpath("//*[@id=\"msg\"]/div/div/div[2]/div/div[2]/button").click() # Send views
        print("Views sent :)")
        sleep(1800) # 30 min
    except:
        print("You already used it, for use again please wait for time is up!\n")
        sleep(180)
    
    driver.refresh()
    loop1()

def loop2():
    sleep(10)
    driver.find_element_by_xpath("//*[@id=\"msg\"]/div/div[3]/div[3]/button").click() #Use
    sleep(10)
    try:
        driver.find_element_by_xpath("//*[@id=\"form1\"]/div/input").send_keys(vidUrl) # Insert profile link
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"form1\"]/div/div/button").click() # Find
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"msg\"]/div/div/p/button").click() # Send views
        sleep(10)
        print("Views sent :)")
        sleep(1800) # 30 min
    except:
        print("You already used it, for use again please wait for time is up!\n")
        sleep(180)
    
    driver.refresh()
    loop2()

print("Author: https://github.com/NoNameoN-A")

vidUrl = "https://www.instagram.com/p/CMT5HZmBIqP/" #Change it

bot = int(input("What do you want to do?\n1 - Auto Views Video\n2 - Auto Views Story\n"))

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path=r'/home/nonameon/Documenti/Alessandro/Instagram-Views-Bot/chromedriver',chrome_options=chrome_options) #Change it

driver.get("https://homedecoratione.com/")

if bot == 1:
    loop1()
elif bot == 2:
    loop2()
else:
    print("You can choose just 1 or 2.\n\nRetry!")