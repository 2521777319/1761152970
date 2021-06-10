from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/s')

input = driver.find_element_by_css_selector('#kw')
input.send_keys('python官网')

button = driver.find_element_by_css_selector('#su')
button.click()
