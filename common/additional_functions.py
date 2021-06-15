# import driver_function as df
import time

from whatsapp_automation.common.driver import driver
# driver.implicitly_wait(60)
from random import randint
import string,random

def click_xpath(val):
    driver.find_element_by_xpath(val).click()
def click_access_id(val):
    driver.find_element_by_accessibility_id(val).click()
def click_id(val):
    driver.find_element_by_id(val).click()

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
def random_char_caps(y):
    return ''.join((random.choice(string.ascii_letters)).upper() for x in range(y))
# print(random_char_caps(10))
def random_numbers(length):
    x=''

    for i in range(length):
        random_no = str(randint(1, 9))
        x+=random_no
    return x
# print(random_numbers(10))

def sending_val_xpath(ref,val):
    driver.find_element_by_xpath(ref).send_keys(val)
def sending_val_access_id(ref,val):
    driver.find_element_by_accessibility_id(ref).send_keys(val)

def sending_field_values(ref,values):
    click_access_id(ref)
    sending_val_access_id(ref,values)
    driver.press_keycode(66)
    driver.find_element_by_accessibility_id(ref).clear()
   #second branch

def sending_val_to_field_access_id(ref,field_type):
    if((field_type=="email_field")or(field_type=="input_field")or(field_type=="gst_field")or(field_type=="website_field")):
        sending_field_values(ref,"a")
        time.sleep(5)
        sending_field_values(ref, "abc123")
        sending_field_values(ref, "$%#")
        sending_field_values(ref, "12345")
        sending_field_values(ref, "   ")

    if(field_type=="email_field"):
        sending_field_values(ref, "abc@gmail")
        sending_field_values(ref,"abc.com")
        sending_field_values(ref, "2644@55.5454")

    if (field_type == "website_field"):
        sending_field_values(ref, "www.website")
        sending_field_values(ref, "website.com")
        sending_field_values(ref, "1212.132.com")

    if(field_type=="mobile_number_field"):
        sending_field_values(ref,".,.,")
        sending_field_values(ref, 12536)

    if (field_type == "pincode_field"):
        sending_field_values(ref, ",.,,.,")
        sending_field_values(ref, 12)

    if(field_type=="otp_field"):
        sending_field_values(ref,12)
        click_id(alert_ok_button_id)
        sending_field_values(ref,".,.,")

    if (field_type == "percent_field"):
        sending_field_values(ref, ",.")
        sending_field_values(ref, 120)
        sending_field_values(ref, -10)
        sending_field_values(ref, " ")

    if (field_type == "fee_field"):
        sending_field_values(ref, ",.")
        sending_field_values(ref, 10000000)
        sending_field_values(ref, 100000000)
        sending_field_values(ref, -1)
        sending_field_values(ref, 0)

    if (field_type == "pan_field"):
        sending_field_values(ref, ",.,,.,")
        sending_field_values(ref, 12)
        sending_field_values(ref, "BAPPVJFHSLF")
        sending_field_values(ref, 1226261166)

    if (field_type == "aadhar_field"):
        sending_field_values(ref, ",.,,.,")
        sending_field_values(ref, 12)
        sending_field_values(ref, 1216515446551)
        sending_field_values(ref, 0)

    if (field_type == "gst_field"):
        sending_field_values(ref, "BAUUVKJCCE1234")
        sending_field_values(ref, 1216515446551)
        sending_field_values(ref, 0)

def sending_field_values_xpath(ref,values):
    click_xpath(ref)
    sending_val_xpath(ref,values)
    driver.press_keycode(66)
    driver.find_element_by_xpath(ref).clear()
   #second branch

def sending_val_to_field_xpath(ref,field_type):
    if((field_type=="email_field")or(field_type=="input_field")or(field_type=="gst_field")or(field_type=="website_field")):
        sending_field_values_xpath(ref,"a")
        time.sleep(5)
        sending_field_values_xpath(ref, "abc123")
        sending_field_values_xpath(ref, "$%#")
        sending_field_values_xpath(ref, "12345")
        sending_field_values_xpath(ref, "   ")

    if(field_type=="email_field"):
        sending_field_values_xpath(ref, "abc@gmail")
        sending_field_values_xpath(ref,"abc.com")
        sending_field_values_xpath(ref, "2644@55.5454")

    if (field_type == "website_field"):
        sending_field_values_xpath(ref, "www.website")
        sending_field_values_xpath(ref, "website.com")
        sending_field_values_xpath(ref, "1212.132.com")

    if(field_type=="mobile_number_field"):
        sending_field_values_xpath(ref,".,.,")
        sending_field_values_xpath(ref, 12536)

    if (field_type == "pincode_field"):
        sending_field_values_xpath(ref, ",.,,.,")
        sending_field_values_xpath(ref, 12)

    if(field_type=="otp_field"):
        sending_field_values_xpath(ref,12)
        click_id(alert_ok_button_id)
        sending_field_values_xpath(ref,".,.,")

    if (field_type == "percent_field"):
        sending_field_values_xpath(ref, ",.")
        sending_field_values_xpath(ref, 120)
        sending_field_values_xpath(ref, -10)
        sending_field_values_xpath(ref, " ")

    if (field_type == "fee_field"):
        sending_field_values_xpath(ref, ",.")
        sending_field_values_xpath(ref, 10000000)
        sending_field_values_xpath(ref, 100000000)
        sending_field_values_xpath(ref, -1)
        sending_field_values_xpath(ref, 0)

    if (field_type == "pan_field"):
        sending_field_values_xpath(ref, ",.,,.,")
        sending_field_values_xpath(ref, 12)
        sending_field_values_xpath(ref, "BAPPVJFHSLF")
        sending_field_values_xpath(ref, 1226261166)

    if (field_type == "aadhar_field"):
        sending_field_values_xpath(ref, ",.,,.,")
        sending_field_values_xpath(ref, 12)
        sending_field_values_xpath(ref, 1216515446551)
        sending_field_values_xpath(ref, 0)

    if (field_type == "gst_field"):
        sending_field_values_xpath(ref, "BAUUVKJCCE1234")
        sending_field_values_xpath(ref, 1216515446551)
        sending_field_values_xpath(ref, 0)

def press_key_code_fun(value):
    if(value=="back"):
        driver.press_keycode(4)
    elif(value=="enter"):
        driver.press_keycode(66)

def scroll_up_to_down(times):
    for i in range(times):
        driver.scroll(450,360,450,1600)
def scroll_down_to_up(times):
    for i in range(times):
        driver.scroll(450,1600,450,360)





