from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/invoice/app/index.php?signIn=1")
driver.find_element_by_class_name("form-control").send_keys("admin")
driver.find_element_by_id("password").send_keys("admin")
driver.find_element_by_id("submit").click()
Title = driver.title
ExpectedTitle = "Online Inovicing System | Homepage"
assert Title == ExpectedTitle

