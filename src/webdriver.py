from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from threading import Thread
import logging

class WebDriver:
    __drivers = []
    __driver_manager = ChromeDriverManager(log_level=logging.WARNING, cache_valid_range=15)
    __options = webdriver.ChromeOptions()
    __options.add_argument("--headless")
    __options.add_argument("--disable-dev-shm-usage")
    
    __options.headless = True
    
    
    def __init__(self) -> None:
        for _ in range(2):
            Thread(
                target= lambda: WebDriver.__drivers.append(
                    webdriver.Chrome(
                        executable_path=WebDriver.__driver_manager.install(),
                        options=WebDriver.__options
                    )
                )
            ).start()


    @staticmethod
    def get_driver():
        Thread(
            target= lambda: WebDriver.__drivers.append(
                webdriver.Chrome(
                    service=Service(ChromeDriverManager().install()), 
                    options=WebDriver.__options
                )
            )
        ).start()
        return WebDriver.__drivers.pop()
        
    @staticmethod
    def awaitToGet(driver, url, target):
        driver.get(url)
        try:
            WebDriverWait(
                driver,
                10
            ).until(EC.presence_of_element_located((By.CSS_SELECTOR, target)))
            content = driver.page_source
            driver.close()
            return content
        except TimeoutException:
            return None