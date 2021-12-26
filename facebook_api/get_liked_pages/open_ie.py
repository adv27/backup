from selenium import webdriver
import time


def main():
    #opening browser
    browser = webdriver.Ie()
    url = 'https://m.facebook.com/profile.php?v=likes&sectionid=9999&lst=100005064335645%3A100005064335645%3A1498576685&startindex=11&refid=17'
    browser.get(url)
    count = 0
    while browser.find_element_by_id("m_more_item") is not None:
        see_more_item = browser.find_element_by_id("m_more_item")
        new_href = see_more_item.find_element_by_tag_name("a").get_attribute("href")
        browser.get(new_href)
        count += 1
        time.sleep(1)
    print(count)
    
if __name__ == "__main__":
    main()
