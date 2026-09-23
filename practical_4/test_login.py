import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Read test data from CSV file
def read_test_data():
    data = []

    with open("test_data.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(
                (
                    row["username"],
                    row["password"],
                    row["expected"]
                )
            )

    return data


# Data-driven test
@pytest.mark.parametrize(
    "username,password,expected",
    read_test_data()
)
def test_login(username, password, expected):

    # Start Chrome
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        # Demo login page
        driver.get(
            "https://the-internet.herokuapp.com/login"
        )

        # Enter username
        username_box = driver.find_element(
            By.ID, "username"
        )
        username_box.send_keys(username)

        # Enter password
        password_box = driver.find_element(
            By.ID, "password"
        )
        password_box.send_keys(password)

        # Click Login
        login_button = driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        )
        login_button.click()

        # Check result
        if expected == "success":

            message = driver.find_element(
                By.ID, "flash"
            ).text

            assert "You logged into a secure area!" in message

        else:

            message = driver.find_element(
                By.ID, "flash"
            ).text

            assert "Your username is invalid!" in message or \
                   "Your password is invalid!" in message

    finally:
        # Close browser
        driver.quit()