from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

class MonkeyTypeBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def accept_cookies(self):
        self.driver.get("https://monkeytype.com")
        accept_all_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "active.acceptAll"))
        )
        accept_all_button.click()

    def type_sentences(self):
        previous_sentence = ""
        try:
            while True:
                time.sleep(1)
                sentence_element = self.driver.find_element(By.XPATH, '//*[@id="words"]')
                sentence_text = sentence_element.text
                sentence_text = ' '.join(sentence_text.split())
                # Check if the current sentence is different from the previous one
                # if sentence_text != previous_sentence:
                print(sentence_text)
                pyautogui.typewrite(sentence_text, 0.01)
                

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def close_browser(self):
        time.sleep(500)
        self.driver.quit()

if __name__ == "__main__":
    monkey_type_bot = MonkeyTypeBot()
    monkey_type_bot.accept_cookies()
    monkey_type_bot.type_sentences()
    monkey_type_bot.close_browser()
