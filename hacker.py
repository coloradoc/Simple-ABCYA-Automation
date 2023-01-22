#selenium imports
from re import search
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create the webdriver object. Here the 
# chromedriver is present in the driver 
# folder of the root directory.

PATH = "C:\Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)


options = webdriver.ChromeOptions() 
options.add_experimental_option("detach", True)
# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 
 
# Setting the driver path and requesting a page 
driver = webdriver.Chrome(options=options, executable_path=PATH) 
 
# Changing the property of the navigator value for webdriver to undefined 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

# get https://www.geeksforgeeks.org/
driver.get("https://www.abcya.com/games/jet_ski_addition")



# Maximize the window and let code stall 
# for 10s to properly maximise the window.
time.sleep(5)
wait = WebDriverWait(driver, 15)
#switch to game frame
wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#desktopGame > iframe")))

time.sleep(1)
#find the button 
driver.find_element(By.XPATH, "//*[name()='svg']//*[local-name()='g' and @id='main']//*[local-name()='g' and @cursor='pointer']").click()


# find the button by xpath
#driver.find_element(By.XPATH, "//*[name()='svg']//*[local-name()='g' and @id='main']//*[local-name()='g' and @cursor='pointer']").click()


#this element will get the text on the object
email_txt = driver.find_element(By.XPATH, "//*[name()='svg']//*[local-name()='g' and @id='main']//*[local-name()='text' and @transform='translate(20, 52.629629135131836) scale(1, 1) rotate(0 140 9.259259223937988)']").text

email_txt = driver.find_element(By.XPATH, "//*[name()='svg']//*[local-name()='g' and @id='main']//*[local-name()='input' and @spellcheck='false']")

#enter game with name
# necessary imports
import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# fix password length
pwd_length = 12

# generate a password string
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))
pwd = pwd[0:4]
print(pwd)

gamertext= f"Furry{pwd}"
email_txt.send_keys(gamertext)
email_txt.send_keys(Keys.RETURN)

  
print(email_txt)



print("nah")

#join game
while True:
    try:
        email_txt = driver.find_element(By.XPATH, "//*[name()='svg']//*[local-name()='g' and @id='main']//*[local-name()='rect' and @fill='#FFE98E']").click()
        print("found game")
        time.sleep(1)
        print("join complete")
        break
    except:
       time.sleep(.5)
        



while True:
    try:
        #get equation
        theEqu = driver.find_element(By.XPATH, "//*[name()='svg']//*[local-name()='g' and @id='main']//*[local-name()='text' and @font-size='34']").text
        print(theEqu)
        
        #theNum1 = driver.find_element(By.XPATH, "//*[name()='svg']//*[local-name()='g' and @id='main']//*[@dy='1em']//*[contains(text(),'3')]").text
        #theNum1 = driver.find_element(By.XPATH, "//*[name()='svg']//*[local-name()='g' and @id='main']//*[local-name()='text' and @font-size='30']").text

        #see which has it
        equ = eval(theEqu)
        print(equ)
        theNum1 = driver.find_element(By.XPATH, f"//*[name()='svg']//*[local-name()='g' and @id='main']//*[@font-size='30' and contains(text(),{equ})]")

        
        t= theNum1.find_element_by_xpath("..")
        t.click() 
    except:
        time.sleep(.5)
        print("expect act")
        try:
            driver.find_element(By.XPATH, "//*[name()='svg']//*[local-name()='g' and @id='main']//*[local-name()='g' and @transform='translate(440, 349) scale(1, 1) rotate(0 0 0)']").click()
        except:
            pass
        try:
            email_txt = driver.find_element(By.XPATH, "//*[name()='svg']//*[local-name()='g' and @id='main']//*[local-name()='rect' and @fill='#FFE98E']").click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, f"//*[name()='svg']//*[local-name()='g' and @id='main']//*[@text-anchor='middle' and contains(text(),{equ})]").click()
        except:
            pass
       # for i in theNum1:
        #    print(i)
        #break

#<text dy="1em" fill="#FFFFFF" font-family="Arial" font-size="14" style="white-space: pre;" font-weight="bold" transform="translate(242.323486328125, 2) scale(1, 1) rotate(0 16.8382568359375 7.870370388031006)">JOIN</text>








#button = driver.find_element_by_css_selector("g[cursor='pointer'][role='button']")
#button = driver.find_elements_by_xpath("//g[@role = 'button']") works
#frame = driver.find_element_by_id('desktopGame')
#frame = driver.find_element_by_xpath("//iframe[@title='jet-ski']")

    # Store iframe web element
#iframe = driver.find_element(By.CSS_SELECTOR, "#desktopGame > iframe")

    # switch to selected iframe
#driver.switch_to.frame(iframe)

    # Now click on button
#driver.find_element(By.TAG_NAME, 'PlayChevrons').click()

#driver.find_element(By.ID, "main").click()


#d = driver.find_element(By.TAG_NAME, "use")





#button = driver.find_element_by_xpath("//use[@href='#PlayChevrons']")
#button.click()




#button = driver.find_element_by_xpath("//use[@href='#PlayChevrons']")
#button.click()
# simulate a click on the button

