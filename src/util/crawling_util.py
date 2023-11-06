from selenium import webdriver

def create_driver():
    user_agent_value = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
    options = webdriver.FirefoxOptions()
    options.add_argument(f"user-agent={user_agent_value}")

    driver_instance = webdriver.Firefox(options=options)
    
    return driver_instance 