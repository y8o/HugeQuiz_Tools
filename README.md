# HugeQuiz Text Entry Tool

This project is an automated Selenium script that interacts with hugequiz.com by logging into the site and submitting city names or whatever is inputted in response to a quiz challenge. The script mimics human-like behavior, including handling the login process and inputting city names into the quiz form.

**Note:** This script is not intended for cheating or bypassing the challenge. It is designed to assist with entering city names and typing responses quickly, especially for hard quizzes. It also helps with easily going back to where you left off in the quiz.


## Features
- Automated login process
- Submits city names to a quiz based on a predefined list
- Mimics human behavior by pausing between actions to avoid detection by anti-bot systems
- Supports interaction with dynamic web elements

## Requirements
- Python 3.x
- Selenium WebDriver
- Firefox WebDriver (Geckodriver)

## Setup

### 1. Install Python Dependencies
Make sure you have Python 3.x installed. Then, you need to install the required packages using `pip`.

```bash
pip install selenium
```

### 2. Download WebDriver
- Firefox: Download the latest version of Geckodriver from [here](https://github.com/mozilla/geckodriver/releases)
- Ensure that geckodriver is accessible in your system's PATH

### 3. Configure Credentials and URLs
Open the script (`quiz_bot.py`) and replace the following placeholders with your actual credentials and URLs:
- `USERNAME`: Your login username
- `PASSWORD`: Your login password
- `QUIZ_URL`: The quiz page URL

### 4. Add City List
You can customize the list of cities in the `city_list` variable with the cities you want to use for the quiz.
An example is shown below:
```python
city_list = [
    "London","Paris","Amsterdam","Hamburg"
]
```
**Note:** This is what is being inputted into the quiz, if the quiz requires a period after every name then add periods, or if it needs the country, like 'losangelesus' for Los Angeles in the US.

### 5. Run the Script
To start the automation, simply run the script using Python:

```bash
python quiz_bot.py
```
## How It Works
1. The script first logs into the quiz site using the provided credentials
2. After logging in, it navigates to the quiz page
3. The script then enters a series of cities from the `city_list` variable into the quiz form, submitting each one sequentially
4. After completing the quiz, the script waits for 1 second between each input to mimic human-like behavior and avoid anti-bot detection mechanisms

## Notes
- This script is designed for educational purposes and to automate tasks on web-based quizzes
- Make sure to not share your login credentials or sensitive information in a public repository

## License
This project is open-source. Feel free to fork, clone, or use it for personal projects.
