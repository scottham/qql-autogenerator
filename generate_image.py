import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
from PIL import Image
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

# script

# script
qql_url = 'https://qql.art/create'


driver.get(qql_url)

generate_button = driver.find_element(By.XPATH, '//button[contains(text(), "Generate Art")]')

generate_button.click()
while True:
    try:
        image = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/div[2]/div/div[2]/img').get_attribute('src')
        break
    except:
        continue

image = image.split(',')[1]
image_bytes = base64.b64decode(image)
with open("./qql_current.png", "wb") as img:
    img.write(image_bytes)

img_jpg = Image.open('./qql_current.png')
img_jpg.save('./qql_current.jpg')

