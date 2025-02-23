import easyocr, pyautogui, os, time
from selenium import webdriver


def ocr_deny_cookies():
    words_of_denial = ["reject", "deny", "hylkaa", "valttamattomat"]
    reader = easyocr.Reader(["en"])
    # full screenshot so the coordinates match
    pyautogui.screenshot("./temp.jpg")
    result = reader.readtext("./temp.jpg")
    os.remove("./temp.jpg")
    if ("cookie" in str(result).lower()) or ("evaste" in str(result).lower()):
        for word in words_of_denial:
            for (bbox, text, prob) in result:
                if word in text.lower():
                    print(f"EasyOCR found: {word}. Probability: {prob:.2f}")
                    pyautogui.click(bbox[0][0], bbox[0][1])
                    break



# generic version
def ocr_click_word(reader, target_words, condition_words=None):
    # full screenshot so the coordinates match
    pyautogui.screenshot("./temp.jpg")
    result = reader.readtext("./temp.jpg")
    os.remove("./temp.jpg")
    if condition_words:
        if not any(word in str(result).lower() for word in condition_words):
            return False
    for word in target_words:
        for (bbox, text, prob) in result:
            if word in text.lower():
                print(f"EasyOCR found: {word}. Probability: {prob:.2f}")
                pyautogui.click(bbox[0][0], bbox[0][1])
                return True
    return False




if __name__ == "__main__":
    print("\n\n")
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    with open("testpages.txt", encoding="utf-8") as pages:
        for page in pages:
            driver.get(page)
            time.sleep(0.2)
            driver.execute_script("document.body.style.zoom = '80%';")
            ocr_deny_cookies()
            time.sleep(0.2)
        driver.quit()


