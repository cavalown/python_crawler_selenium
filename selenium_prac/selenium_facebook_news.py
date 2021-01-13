from selenium import webdriver
from read_file import read_yaml as ryaml
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

webdriver_path = '/Users/huangyiling/python_work/side_project/webdriver/chromedriver'
facebook_url = 'https://www.facebook.com/'
yaml_path = '/Users/huangyiling/python_work/side_project/credential/.test_user.yaml'
target_url = 'https://www.facebook.com/pnnpts'

# set driver
options = Options()
prefs = {'profile.default_content_setting_values': {'notifications': 2}}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(webdriver_path, chrome_options=options)

driver.get(facebook_url)

# log in facebook
email = driver.find_element_by_id("email")
email.send_keys(ryaml.read_yaml(yaml_path)['facebook']['email'])
time.sleep(2)
password = driver.find_element_by_id("pass")
password.send_keys(ryaml.read_yaml(yaml_path)['facebook']['password'])
time.sleep(2)
driver.find_element_by_class_name("_6ltg").click()

# after log in , use sleep to assure that log_in finished
time.sleep(3)

# go to the target page
driver.get(target_url)

# 模擬滑鼠滾動
for i in range(10):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')
titles = soup.find_all('div', {'class': "ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a"})
for title in titles:
    print(title.text)

driver.close()
