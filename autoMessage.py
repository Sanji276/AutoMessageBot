from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui


def handle_notification():
    notification_x = 957
    notification_y = 677
    pyautogui.click(notification_x, notification_y)


class MessageBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        lines = []
        self.driver.get("https://facebook.com")
        self.driver.implicitly_wait(5)
        file_path = 'C:/Users/bibek/OneDrive/Desktop/userId.txt'
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            second_line = file.readline().strip()
        if second_line:
            lines.append(first_line)
            lines.append(second_line)
        pyautogui.typewrite(lines[0], 0.01)
        pyautogui.press('tab')
        pyautogui.typewrite(lines[1], 0.01)
        self.login_button()

    def login_button(self):
        login_button = self.driver.find_element(By.NAME, 'login')
        sentence_element_username = self.driver.find_element(By.NAME, 'email')
        sentence_element_password = self.driver.find_element(By.NAME, 'pass')

        username = sentence_element_username.get_attribute('value')
        password = sentence_element_password.get_attribute('value')
        login_button.click()
        time.sleep(10)
        handle_notification()
        time.sleep(10000)


def close_browser(self):
    time.sleep(1)
    self.driver.quit()


if __name__ == "__main__":
    message_bot = MessageBot()
    message_bot.login()
    # message_bot.close_browser()
