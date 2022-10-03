from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from IPython import display
from IPython.display import HTML
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")


driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)

url = 'https://www.facebook.com/marketplace/?ref=bookmark'
driver.get(url)

username = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME,"pass")
submit = driver.find_element(By.NAME,"login")
username.send_keys("mehrwan69@gmail.com")
password.send_keys("CENTER1969")
submit.click()

# url = 'https://www.facebook.com/marketplace/category/vehicles?maxPrice=15000&maxYear=2000&carType=convertible%2Ccoupe%2Cother_body_style&exact=false'
# driver.get(url)

# marketplace_button = driver.find_element(By.XPATH, '//div[contains(text(), "Marketplace")]')
# marketplace_button.click()

vehicles =  driver.find_element(By.XPATH, '//span[contains(text(), "Vehicle")]')
vehicles.click()
sleep(1)


search = driver.find_element(By.XPATH, "//input[@aria-label = 'Search Marketplace']")
search.send_keys("bmw e30\n")
sleep(5)

# search.submit()


for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)


# elements = driver.find_elements(By.CLASS_NAME, "rlvdr5c9 qneuxs76 h6ft4zvz ir39z7dx dhod7fyx")
elements = driver.find_elements(By.XPATH, "//div[@class='a75w6hnp']/a")

for elem in elements:
    href  = elem.get_attribute('href')
    print(href)



# item_links = [item.get_attribute('href') for item in elements]




