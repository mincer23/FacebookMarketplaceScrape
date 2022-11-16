from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from IPython import display
from IPython.display import HTML
from selenium.webdriver.common.by import By
from time import sleep

car = ''
car = input('what car are you looking for? ')

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
options.add_argument('--disable-notifications')

driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)

url = 'https://www.facebook.com/login/?next=%2Fmarketplace%2F'
driver.get(url)

username = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME,"pass")
submit = driver.find_element(By.NAME,"login")
username.send_keys("mehrwan69@gmail.com")
password.send_keys("Center1969$$$")
submit.click()

# url = 'https://www.facebook.com/marketplace/category/vehicles?maxPrice=15000&maxYear=2000&carType=convertible%2Ccoupe%2Cother_body_style&exact=false'
# driver.get(url)

# marketplace_button = driver.find_element(By.XPATH, '//div[contains(text(), "Marketplace")]')
# marketplace_button.click()

vehicles =  driver.find_element(By.XPATH, '//span[contains(text(), "Vehicle")]')
vehicles.click()
sleep(1)


search = driver.find_element(By.XPATH, "//input[@aria-label = 'Search Marketplace']")
search.send_keys(car +"\n")
sleep(5)

# search.submit()


# for i in range(10):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     sleep(2)


# elements = driver.find_elements(By.CLASS_NAME, "rlvdr5c9 qneuxs76 h6ft4zvz ir39z7dx dhod7fyx")
# elements = driver.find_elements(By.XPATH, "//div[@class='a75w6hnp']/a")
elements = driver.find_elements(By.XPATH, '//a[contains(@href,"/marketplace/item")]')

href = []
for elem in elements:
    print("Done")
    href.append(elem.get_attribute('href'))
file_url = 'C:\\Users\\kingm\\Desktop\\FB_PY\\fbm-' + car + '.txt'
f = open(file_url,"x", encoding="utf-8")
for url in href:
    f.write('----------------------------------------------------------------------------------------\n')
    driver.get(url)
    image_elem = driver.find_element(By.XPATH,  "//img[contains(@referrerpolicy, 'origin')]")
    images = [image_elem.get_attribute('src')]
    f.write(images[0] + '\n')
    val = driver.find_element(By.XPATH, "//div[@class = 'x1jx94hy x78zum5 xdt5ytf x1lytzrv x6ikm8r x10wlt62 xiylbte xtxwg39']")
    f.write(val.text)
f.close()

    # print(images)
    # print(val.text)
    

    
    





