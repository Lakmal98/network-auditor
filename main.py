from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# s = Service(ChromeDriverManager().install())
options = Options()
options.headless = True


def openBrowser():
    url = "https://www.fast.com/"
    # open headless browser

    # driver = webdriver.Chrome(service=s, options=options)
    driver = webdriver.Chrome('./chromedriver', options=options)  # Deprecated
    driver.maximize_window()
    driver.get(url)
    return driver


def saveScreenshot(driver):
    # save screenshot with date and time as name
    driver.save_screenshot(f"{time.strftime('%Y-%m-%d-%H-%M-%S')}.png")


# run function every x seconds
def run(period):
    while True:
        driver = openBrowser()
        time.sleep(40)
        saveScreenshot(driver)
        #  access the page and read a css element
        speedValue = driver.find_element_by_css_selector(
            '#speed-value')  # Deprecated
        speedUnits = driver.find_element_by_css_selector(
            '#speed-units')  # Deprecated
        # append to file
        with open("speed.csv", "a") as f:
            f.write(
                f"{time.strftime('%Y-%m-%d-%H-%M-%S')}, {speedValue.text}, {speedUnits.text}\n")

        driver.quit()
        time.sleep(period)


if __name__ == '__main__':
    # run every 01 hour
    run(3600)
