from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import time
import imdb



search = input("Enter the the movie you want to see : ")    
ia = imdb.IMDb()
name = ia.search_movie(search)
print("Movie name is :",name[0])
search = name[0]
print("Search: ", search)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension("F:\\python\\add-blocker.crx")
driver = webdriver.Chrome(chrome_options)
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
driver.minimize_window()
driver.get('https://hdmovie2.wine/')
# time.sleep(10)
wait = WebDriverWait(driver , 5)
element = wait.until(EC.presence_of_element_located((By.NAME , "story")))
element.send_keys(f"{search}")
element = driver.find_element(By.CLASS_NAME,"search-btn").click()
time.sleep(3)
try:
    element = driver.find_element(By.ID,"pagination")
    if element.is_displayed():
        for i in range(1,4):
            try:
                page = driver.find_element(By.XPATH,(f"//*[@id='pagination']/div/a[{i}]"))
                page.click()
                try:
                    element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, f"{search}")))
                except:
                    element = wait.until(EC.presence_of_element_located((By.XPATH(f'//img[@alt={search}]')))).click()

                if element.is_displayed():
                    element.click()

                    element= wait.until(EC.presence_of_element_located((By.CLASS_NAME,"ajax-plaer-ico"))).click()
                    time.sleep(1)
                    driver.maximize_window()
                    time.sleep(1)
                    element= wait.until(EC.presence_of_element_located((By.ID,"player"))).click()
                                    
                    keyboard.press_and_release("f")
                    time.sleep(40000000)
                    driver.quit()
                    break
                
            except:
                pass
except:
    try:
        element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, f"{search}"))).click()
    except:
        element = wait.until(EC.presence_of_element_located((By.XPATH(f'//img[@alt={search}]')))).click()

    element= wait.until(EC.presence_of_element_located((By.CLASS_NAME,"ajax-plaer-ico"))).click()
    driver.maximize_window()
    time.sleep(1)
        
    element= wait.until(EC.presence_of_element_located((By.ID,"player"))).click()
        
    keyboard.press_and_release("f")
    time.sleep(4000000)
    driver.quit()

# finally:
#     dynamic_xpath = f'//a[@class="name" and text()="{search}"]'
#     print(dynamic_xpath)
#     driver.get("https://fmovies.ps/")
        
#     element = wait.until(EC.presence_of_element_located((By.NAME,"s"))).send_keys(f"{search}")
#     element = wait.until(EC.presence_of_element_located((By.XPATH,('//*[@id="body-wrapper"]/div/form/button')))).click()
#     element = wait.until(EC.presence_of_element_located((By.CLASS_NAME ,"name")))
#     current_text= element.text
#     lower_text = current_text.lower()
#     print("*************************************",lower_text)
#     print("**********************************************",current_text)
#     driver.execute_script("arguments[0].innerHTML = arguments[1];", element, lower_text)
#     try:

#         element = wait.until(EC.presence_of_element_located((By.XPATH, dynamic_xpath.lower())))
#         element.click()
        
#     except:
#         element = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, search)))
#         element.click()

#     time.sleep(1)
#     driver.maximize_window()
#     element = wait.until(EC.presence_of_element_located((By.XPATH,('/html/body')))).click()
#     keyboard.press_and_release("f") 
#     time.sleep(20000000)
#     driver.quit()
