import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #Gagal SignUp - Data Dikosongi
    def test_a_success_signup(self): 
        # steps
        browser = self.browser #buka web browser
        browser.maximize_window()
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"#signUp").click() # klik tombol sign up
        time.sleep(1)
        response_clickSignup = browser.find_element(By.CSS_SELECTOR,"#registerForm > h1").text #assertion berada di halaman sign up
        time.sleep(1)
        self.assertEqual(response_clickSignup, 'Create Account')
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("") # isi nama by Full XPATH
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='email_register']").send_keys("") # isi email by XPATH, #email tidak boleh sama
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("") # isi password by ID
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#signup_register").click() # klik tombol sign up by CSS Selector
        time.sleep(1)

        #validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    #Sukses SignUp
    def test_a_success_signup(self): 
        # steps
        browser = self.browser #buka web browser
        browser.maximize_window()
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"#signUp").click() # klik tombol sign up
        time.sleep(1)
        response_clickSignup = browser.find_element(By.CSS_SELECTOR,"#registerForm > h1").text #assertion berada di halaman sign up
        time.sleep(1)
        self.assertEqual(response_clickSignup, 'Create Account')
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("Ryukazu") # isi nama by Full XPATH
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='email_register']").send_keys("testasal@gmail.com") # isi email by XPATH, #email tidak boleh sama
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("Testing1234") # isi password by ID
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#signup_register").click() # klik tombol sign up by CSS Selector
        time.sleep(1)

        #validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.maximize_window()
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_a_failed_login_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.maximize_window()
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_a_failed_login_with_empty_email_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.maximize_window()
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('tidak valid', response_data)
        self.assertEqual(response_message, 'Cek kembali email anda')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()