from selenium  import webdriver

browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
browser.get("http://localhost:8000")

assert 	'Django' in browser.title

# driver = webdriver.Chrome("http://localhost:9515", DesiredCapabilities.chrome())
# driver.get("http://www.google.com")