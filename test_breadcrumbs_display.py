from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_breadcrumbs_displayed():
    # Setup WebDriver
    driver = webdriver.Chrome()

    # set implicit wait
    driver.implicitly_wait(10)


    # Open the registration page
    driver.get("http://demostore.supersqa.com/product/belt/")


    # Locate the breadcrumbs
    breadcrumbs = driver.find_elements(By.XPATH, "//nav[@aria-label='breadcrumbs']")

    # Check if breadcrumb links are present
    assert len(breadcrumbs) > 0, "No breadcrumbs found."  # Ensure at least one breadcrumb is found
    assert breadcrumbs[0].is_displayed(), "Breadcrumbs are not displayed."
    print("Breadcrumbs are displayed")

    # close the browser
    #driver.quit()