from selenium import webdriver

import os 
from dotenv import load_dotenv

def create_driver():
    user_agent_value = os.getenv('USER_AGENT')
    options = webdriver.FirefoxOptions()
    options.add_argument(f"user-agent={user_agent_value}")

    driver_instance = webdriver.Firefox(options=options)
    
    return driver_instance 