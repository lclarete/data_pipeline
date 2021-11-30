from selenium import webdriver
import time
from datetime import datetime
import pandas as pd

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class InstagramBot:
    def __init__(self, username, password, hashtag, startDate, endDate=datetime.today()):
        self.username = username
        self.password = password
        self.hashtag = hashtag
        self.startDate = self.textToDate(startDate)
        self.endDate = self.textToDate(endDate)

        self.driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.by = By
        self.ec = ec
        self.webDriverWait = WebDriverWait


        time.sleep(10)
        self.login()
        time.sleep(5.5)
        self.explore_hashtags()
        time.sleep(2)
        self.get_post_data()

    def textToDate(self, text):
        try:
            datetime_object = datetime.strptime(text, "%b %d, %Y")
        except:
            return text
        return datetime_object


    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        self.webDriverWait(self.driver, 20).until(self.ec.presence_of_element_located((self.by.NAME, "username")))
        self.webDriverWait(self.driver, 20).until(self.ec.presence_of_element_located((self.by.NAME, "password")))
        self.webDriverWait(self.driver, 20).until(self.ec.element_to_be_clickable((self.by.XPATH, "//*[contains(text(), 'Log In')]")))

        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_element_by_xpath("//*[contains(text(), 'Log In')]").click()

    def explore_hashtags(self):
        self.driver.get("https://www.instagram.com/explore/tags/"+self.hashtag)


    def get_post_data(self):
        self.webDriverWait(self.driver, 5).until(self.ec.element_to_be_clickable((self.by.CLASS_NAME, "_9AhH0")))
        self.driver.find_element_by_class_name("_9AhH0").click()
        pageIdx = 0
        data_list = []
        postDatetime = datetime.now()

        while (self.endDate >= postDatetime >= self.startDate) or (pageIdx <= 9):
            data = {}
            self.webDriverWait(self.driver, 100).until(self.ec.presence_of_element_located((self.by.TAG_NAME, "time")))
            self.webDriverWait(self.driver, 100).until(self.ec.presence_of_element_located((self.by.CSS_SELECTOR, "a.sqdOP")))
            self.webDriverWait(self.driver, 100).until(self.ec.presence_of_element_located((self.by.CSS_SELECTOR, ".C4VMK span")))
            self.webDriverWait(self.driver, 100).until(self.ec.presence_of_element_located((self.by.CLASS_NAME, "JF9hh")))
            time.sleep(2)

            # gettting date
            try: 
                timeText = self.driver.find_element_by_tag_name("time").get_attribute("title")
                postDatetime = self.textToDate(timeText)
            except Exception as e:
                print("DATE")
                print(f"ERROR: {e}")
                continue           
            else:
                data["date"] = timeText
                

            # getting post id
            try:
                currentUrl = self.driver.current_url
                postId = currentUrl.split("/")[-2]
            except Exception as e:
                print("POST ID")
                print(f"ERROR: {e}")
            else:
                data["post_id"] = postId


            # getting author
            try:
                user_name = self.driver.find_element_by_css_selector("a.sqdOP").text
            except Exception as e:
                print("AUTHOR")
                print(f"ERROR: {e}")
            else:
                data["author"] = user_name


            # getting text
            try: 
                postText = self.driver.find_elements_by_css_selector(".C4VMK span")[1].text
                if postText == "Verified":
                    postText = self.driver.find_elements_by_css_selector(".C4VMK span")[2].text
            except Exception as e:
                print("TEXT")
                print(f"ERROR: {e}")          
            else:
                data["text"] = postText


            # getting location
            try: 
                postLocation = self.driver.find_element_by_class_name("JF9hh").text
            except Exception as e:
                print("LOCATION")
                print(f"ERROR: {e}")                
            else:
                data["location"] = postLocation


            pageIdx += 1
            data_list.append(data)
            self.driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()

            df = pd.DataFrame(data_list[10:])
            json_name = self.hashtag+".json"
            df.to_json(json_name, orient="records", indent=4)
        print("SCRAPED ALL", len(df))

# date format should be: %b %d, %Y. ex. Jun 15, 2020
# if you don't enter the endDate it is set to current date
ig = InstagramBot("escuteocorpo", "datadata2021!", "hardseltzer", "Oct 15, 2021")

