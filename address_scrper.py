"""
For running the chrome in debugging mode, since selenium is running on the same window.:
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:/selenum/ChromeProfile"
"""
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=options)

def extract_address():
    try:
        print("Attempting to locate the iframe containing the Google My Map...")
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//iframe[contains(@src, "google.com/maps/d/embed")]'))
        )
        print("Iframe located. Switching to the iframe...")
        driver.switch_to.frame(iframe)
        print("Switched to iframe. Waiting for the address to appear in the side panel...")
        address_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="featurecardPanel"]/div/div/div[4]/div[1]/div[5]'))
        )
        address = address_element.text
        print(f"Address: {address}")
        return f'{address}'
    except Exception as e:
        print(f"Error: Could not extract the address. {e}")
        return None
    finally:
        driver.switch_to.default_content()
        print("Switched back to main content.")

if __name__ == "__main__":
    extract_address()
