import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path='chromedriver.exe'
# driver_path = r'C:\Users\TavadarkarHrushikesh\PycharmProjects\pythonProject\chromedriver.exe'
# driver = webdriver.Chrome(executable_path= driver_path)
navigate_url= "https://www.stage-page.chaiport.io/2AZX3ENuQMlYlNBlXfr7dcI5ngS"
# driver.implicitly_wait(30)


# driver.maximize_window()

class Demotesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(driver_path)
        self.driver.maximize_window()
        self.driver.get(navigate_url)
        self.driver.implicitly_wait(30)

    # Testing for all fields in the form
    def test_login(self):
        # Enter name
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/input").send_keys("ching chong")
        # Enter email
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/input[1]").send_keys("chingchong@gmail.com")
        # Enter mob number
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[4]/input[1]").send_keys("9876543210")
        # Click oay now
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div/div[2]/div[5]/button").click()

    def test_without_mob(self):
        # Enter name
        self.driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/input").send_keys("ching chong")
        # Enter email
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/input[1]").send_keys("chingchong@gmail.com")
        # Enter mob number
        self.driver.find_element(By.CLASS_NAME, "selected-flag").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/ul[1]/li[1]").click()
        # Clicks pay now
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/div/div[2]/div[5]/button").click()


if __name__=='__main__':
    unittest.main()
# driver.quit()