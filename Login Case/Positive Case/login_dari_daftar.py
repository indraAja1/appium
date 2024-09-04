import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
# import open app
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_daftar import open_app 

# Variable ID
# Di ambil dari APPIUM INSPECTOR
field_email = 'com.nunomics.app.debug:id/etUsernameEmail'
field_pass = 'com.nunomics.app.debug:id/etPassword'
btn_login_page = 'com.nunomics.app.debug:id/btnLogin'
btn_login_id = 'com.nunomics.app.debug:id/btnApply'
btn_notif_id = 'com.android.permissioncontroller:id/permission_allow_button'

# Variable Input
input_email = "usertesting1satu@gmail.com"
input_pass = "Testing1"

class TestLoginValidEmail(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_login_with_valid_email(self):
        try:
            
            print("Step 3: Klik tombol 'Saya Sudah Punya Akun'")            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_login_page))
            ).click()
            
            print(f"Step 4: Masukkan email '{input_email}' ke dalam field Username/ Email/ No Hp")                        
            input_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_email))
            )
            input_field.clear()
            input_field.send_keys(input_email)

            print(f"Step 5: Masukkan password '{input_pass}' ke dalam field Password")            
            input_field_password = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            )
            input_field_password.clear()
            input_field_password.send_keys(input_pass)

            print("Step 6: Klik tombol 'Masuk Sekarang'")
            btn_login = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_login_id))
            )
            btn_login.click()
            
            # Perizinan Notifikasi sistem android            
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, btn_notif_id))
            )
            btn_notif = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_notif_id))
            )
            btn_notif.click()
            
        except Exception as e:
            print(f"Terjadi kesalahan saat login: {e}")

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
