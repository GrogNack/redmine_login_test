class Application(object):

    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get("https://task.htc-cs.com/login?back_url=http%3A%2F%2Ftask.htc-cs.com%2F")

    def login(self, user):
        driver = self.driver
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(user.username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(user.password)
        driver.find_element_by_id("login-submit").click()