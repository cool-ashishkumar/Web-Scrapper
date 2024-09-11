from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
query = "Books"
file = 0

for i in range(1, 20):

    driver.get(
        "https://www.amazon.in/s?k={query}&page={i}&crid=1P0F954J3XGOI&sprefix=lapt%2Caps%2C198&ref=nb_sb_ss_ts-doa-p_1_4")

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    # print(elems.get_attribute("outerHTML"))
    # locating multiple
    # print(elems.text)
    print(elems)
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1

    time.sleep(2)
driver.close()

