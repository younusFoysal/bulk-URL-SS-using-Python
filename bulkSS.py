import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from tqdm import tqdm

lines = []
Links_File = r'Y:\Projects\AFFIX\Affix IT Solutions\Python\bulkSS\links.txt'
OP_DIR = r'Y:\Projects\AFFIX\Affix IT Solutions\Python\bulkSS\op'
i = 1

S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)

with open(Links_File, "r") as f:
    lines = f.readlines()
lines = [line.rstrip() for line in lines]

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
print(driver.execute_script("return navigator.userAgent;"))
for link in tqdm(lines, ncols=65):
    try:
        driver.get(link)
        time.sleep(5)
        driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
        driver.find_element(By.TAG_NAME,'body').screenshot(f'{OP_DIR}\{i}.png')
        i = i + 1
    except WebDriverException:
        print(link)
        continue
driver.quit()
