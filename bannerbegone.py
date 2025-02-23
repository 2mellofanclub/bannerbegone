import easyocr, pyautogui, sys, os, time
from selenium import webdriver


def ocr_deny_cookies():
    words_of_denial = ["reject", "deny", "hylkaa", "valttamattomat"]
    reader = easyocr.Reader(["en"])
    pyautogui.hotkey('ctrl', '1')
    # full screenshot so the coordinates match
    pyautogui.screenshot("./temp.jpg")
    result = reader.readtext("./temp.jpg")
    if ("cookie" in str(result).lower()) or ("evaste" in str(result).lower()):
        for word in words_of_denial:
            for (bbox, text, prob) in result:
                if word in text.lower():
                    print(f"EasyOCR found: {word}")
                    pyautogui.click(bbox[0][0], bbox[0][1])
    os.remove("./temp.jpg")




if __name__ == "__main__":
    print("\n\n")
    #if len(sys.argv) < 2:
    #    print("\033[91m\nPlease provide a list of pages to check as a txt-file.\033[00m")
    #    print("Example:     python3 bannerbegone.py pages.txt\n")
    #    quit()
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    with open("pages.txt", encoding="utf-8") as pages:
        for page in pages:
            driver.get(page)
            time.sleep(0.2)
            driver.execute_script("document.body.style.zoom = '85%';")
            ocr_deny_cookies()
            time.sleep(0.2)
        driver.quit()


