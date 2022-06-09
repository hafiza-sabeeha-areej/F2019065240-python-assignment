from selenium import webdriver
import random
import urllib.request

driver = webdriver.Chrome()
# driver.get("https://unsplash.com/s/photos/nature")
# driver.get("https://unsplash.com/s/photos/beach")
driver.get("https://unsplash.com/s/photos/animals")

data = driver.find_element_by_css_selector(
    "#app > div > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div > div")
image = data.find_elements_by_tag_name("img")
count = 0
for i in image:
    image_link = i.get_attribute("src")
    if i.get_attribute("class") == "YVj9w":
        # image_path = "nature/b" + str(random.random()) + ".jpg"
        # image_path= "beach/b" + str(random.random()) + ".jpg"
        image_path = "animals/b" + str(random.random()) + ".jpg"
        urllib.request.urlretrieve(image_link, image_path)
    if count == 10:
        break
    count = count + 1
