#!/usr/bin/env python

from selenium import webdriver
import os
import time

 
def sign_me_up():
    chrome_options = webdriver.ChromeOptions()
    driver_path = os.getcwd() + '/bin/chromedriver'
    chrome_options.binary_location = os.getcwd() + '/bin/headless-chromium'
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
   
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    
    """
    Example code start
    
    

    driver.get("gym-adress-here")
    time.sleep(1)  # Obligatory for waiting to load page
    driver.find_element_by_xpath("//div/input[@name='Login']") \
        .send_keys('your-gym-login')
    driver.find_element_by_xpath("//div/input[@name='Password']") \
        .send_keys('your-gym-password')
    time.sleep(0.2)  # Just to see results no need in headless mode
    driver.find_element_by_class_name('auth-form-actions').click()
    time.sleep(1)  # Next page waiting
    # Diffrent gym classes calender view
    list_url = 'gym-adress-here'
    driver.get(list_url)
    time.sleep(1)

    # Find date string
    date = driver.find_element_by_css_selector(".cp-class-container > div:nth-of-type(2) \
                                                .class-list-day-title").text.lower()
    # List all activities in one day
    list_all = []
    list_all_day_act = driver.find_elements_by_css_selector(".cp-class-container > div:nth-of-type(2) \
                                                             .calendar-item-name")
    for element in list_all_day_act:
        list_all.append((element.text).lower())
    # list all bookable activities and their start time
    list_bookable = []
    list_all_bookable_act = driver.find_elements_by_css_selector(".cp-class-container > div:nth-of-type(2) \
                                                                  .is-bookable .calendar-item-name")
    for element in list_all_bookable_act:
        list_bookable.append((element.text).lower())
    # List all activities' start time
    list_all_start = []
    list_hours = driver.find_elements_by_css_selector(".cp-class-container > div:nth-of-type(2) \
                                                       .calendar-item-start")
    for element in list_hours:
        list_all_start.append(element.text)

    # Combine date & start hour strings, then list parsed
    date_hour = []
    for hour in list_all_start:
        date_hour.append(date + ' ' + hour)

    user_training = "example_training_name"
    if user_training not in list_bookable:
        pass
    else:
        # Find index of desirable workout and book
        workout_index = list_all.index("example_training_name".lower())
        web_index = str(workout_index + 2)  # From gym website
        driver.find_element_by_css_selector(".cp-class-container > div:nth-of-type(2) > div:nth-of-type(" + web_index + ") \
                                             .class-item-actions").click()
    driver.close()
    return {'user_trainig' : user_training}


    
    Example code end
    """

def lambda_handler(event, context):
    result = sign_me_up()
    return result


if __name__ == '__main__':
    lambda_handler(None, None)