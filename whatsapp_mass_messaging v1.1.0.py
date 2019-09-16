"""
whatsapp_mass_messaging v1.1.0.py :
A Python code to to automate sending mass whatsapp messages.
The list of phone numbers is stored in moblie_no_list in list
 format.
The phone numbers are imported from test_numbers.csv file.
To automate web processes selenium is used. Make sure to install
 chrome web drivers to allow selenium to automate the web proces.
"""

__author__ = "Rishit Dagli"
__copyright__ = ""
__credits__ = ["Rishit Dagli"]
__license__ = "Apache License 2.0"
__version__ = "1.1.0"
__maintainer__ = "Rishit Dagli"
__email__ = "rishit.dagli@gmail.com"
__status__ = "Development"

from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import csv

message_text = 'Rishit Dagli'
# message you want to send

no_of_message = 1
# no. of time you want the message to be send

moblie_no_list = []
# list of phone number can be of any length

with open('test_numbers.csv', 'r') as csvfile:
    moblie_no_list = [int(row[0])
                      for row in csv.reader(csvfile, delimiter=';')]


# get mobile no from csv file

def element_presence(by, xpath, time):
    '''
    @author Rishit Dagli
    Determines presence of web drivers.
    '''
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


def is_connected():
    '''
    @author Rishit Dagli
    Returns True if ping to www.google.com
    on port 80 is succesfull
    '''
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except BaseException:
        is_connected()


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://web.whatsapp.com")
sleep(10)


# wait time to scan the code in second


def send_whatsapp_msg(phone_no, text):
    '''
    @author Rishit Dagli
    send_whatsapp_msg() accepts 2 arguments - phone_no and text integer and string respectively.
    For keyword arguments use send_whatsapp_msg(phone_no= ,test='').
    Connects to whatsapp web and takes precautions for wrong mobile numbers.
    Call the isConnected method before this function.
    '''

    driver.get(
        "https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no)
    )

    try:
        driver.switch_to_alert().accept()

    except Exception as e:
        pass

    try:
        element_presence(
            By.XPATH,
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',
            30)
        txt_box = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("Invailid phone no :" + str(phone_no))


def main():
    '''
    @author Rishit Dagli
    Iterates through mobile number and sends them
    to send_whatsapp_msg function
    '''

    for moblie_no in moblie_no_list:
        try:
            send_whatsapp_msg(phone_no=moblie_no, text=message_text)

        except Exception as e:

            sleep(10)
            is_connected()


'''
print("functions- main, element_presence, is_connected, send_whatsapp_msg")
print("Docs")
print(main.__doc__)
print(element_presence.__doc__)
print(is_connected.__doc__)
print(send_whatsapp_msg.__doc__)
'''

if __name__ == '__main__':
    main()
