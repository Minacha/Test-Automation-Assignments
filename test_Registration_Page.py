from selenium import webdriver
from selenium.webdriver.common.by import By

import random
import string
import time

def generate_unique_email():
    """Generate a unique email using a timestamp and random string."""
    timestamp = int(time.time())
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    email = f"testuser{timestamp}_{random_string}@example.com"
    return email

def test_registration_page():
    # Setup WebDriver
    driver = webdriver.Chrome()

    # Set implicit wait
    driver.implicitly_wait(10)

    # Open the registration page
    driver.get("http://demostore.supersqa.com/my-account/")



    # Generate a unique email address
    unique_email = generate_unique_email()

    # Locate elements
    Email_field= driver.find_element(By.ID, "reg_email")
    Password_field= driver.find_element(By.ID, "reg_password")
    Register_button= driver.find_element(By.XPATH, "//button[@name='register']")

    # Fill out the form
    Email_field.send_keys(unique_email)
    Password_field.send_keys("supersecretpassword")

    # Submit the form
    Register_button.click()


    Logout_button = driver.find_element(By.XPATH, "//a[text()='Log out']")
    assert Logout_button.is_displayed(), "Registration failed."
    print("Registration successful")
