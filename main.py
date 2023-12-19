from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_to_linkedin(driver, username, password):
    while True:
        # Get the LinkedIn login page
        driver.get("https://www.linkedin.com/uas/login?session_redirect=%2Fsales&_f=navigator&fromSignIn=true&trk=sales-home-page_nav-header-signin&src=or-search&veh=www.google.com%7Cor-search")

        # Wait until the username input field is loaded
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )

        # Enter username
        username_input.send_keys(username)

        # Find the password input field and enter password
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)

        # Find the login button and click it
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()

        # Check if login was successful
        if "feed" in driver.current_url:
            break
        else:
            print("Login unsuccessful. Retrying...")
            time.sleep(2)

def get_url():
    # LinkedIn URL is given
    LinkedIn_URL = "https://www.linkedin.com/sales/search/people?savedSearchId=50587557&sessionId=eALNsr3mQWO3ZsCS9kWtJA%3D%3D"

    # Setup WebDriver to use Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Read username and password from files
    with open('username.txt', 'r') as file:
        username = file.readline().strip()
    with open('password.txt', 'r') as file:
        password = file.readline().strip()

    # Log in to LinkedIn
    login_to_linkedin(driver, username, password)

    # Get the LinkedIn page
    driver.get(LinkedIn_URL)

    try:
        # Wait until the boxes are loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='search-results__result-item']"))
        )

        # Fetch the boxes
        boxes = driver.find_elements(By.XPATH, "//div[@class='search-results__result-item']")

        for box in boxes:
            try:
                # Fetch the name within the box
                name_element = box.find_element(By.XPATH, ".//span[@data-anonymize='person-name']")
                name = name_element.text

                # Click on the name
                name_element.click()

                time.sleep(2)  # Wait for the profile to load

                # Perform the necessary actions on the profile page

                # Go back to the search results
                driver.back()

                time.sleep(2)  # Wait for the search results to load

            except Exception as e:
                print(f"An error occurred while processing a box: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

# call get_url function
get_url()
