from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Placeholder for login credentials and URLs
USERNAME = 'your_username_here'
PASSWORD = 'your_password_here'
LOGIN_URL = 'https://hugequiz.com/wp-login.php'
QUIZ_URL = 'your_quiz_page_url_here'

# Initialize Firefox with Selenium
driver = webdriver.Firefox()

# Navigate to the login page
driver.get(LOGIN_URL)

# Explicitly wait for the username and password fields to be visible
wait = WebDriverWait(driver, 10)

# Wait for the username field to be present
username_box = wait.until(EC.presence_of_element_located((By.ID, "user_login")))

# Wait for the password field to be present
password_box = wait.until(EC.presence_of_element_located((By.ID, "user_pass")))

# Enter login credentials (replace with actual credentials)
username_box.send_keys(USERNAME)
password_box.send_keys(PASSWORD)

# Wait for the login button to be clickable, then click it
login_button = wait.until(EC.element_to_be_clickable((By.ID, "wp-submit")))
login_button.click()

# Wait for login to complete and redirect
time.sleep(5)

# Now that you're logged in, navigate to the quiz page
driver.get(QUIZ_URL)

# Wait for the page to load
time.sleep(5)

# Locate the correct input field for the quiz (ID = "guess")
input_box = wait.until(EC.presence_of_element_located((By.ID, "guess")))

# Locate the `.quiz-inner` element (ensure this element is correct by inspecting the page)
quiz_inner_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".quiz-inner")))

# List of cities to input in the quiz
city_list = [
    "city1", "city2", "city3", # Replace with actual city names
    # Add the rest of the cities from your original list
]

# Loop through the list and input each city name
for city in city_list:
    input_box.clear()  # Clear any previous input
    input_box.send_keys(city)  # Type the city name
    input_box.send_keys('\n')  # Simulate pressing ENTER after each input

    # Use JavaScript to scroll to the .quiz-inner element
    driver.execute_script("arguments[0].scrollIntoView();", quiz_inner_element)

    # Wait a bit between each input to mimic human behavior and avoid potential anti-bot measures
    time.sleep(1)

# Close the browser after finishing
# driver.quit()
