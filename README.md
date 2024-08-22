# ![Appium Logo](https://brandslogos.com/wp-content/uploads/images/large/appium-logo.png) Automation Appium

## Selector Android

1. **[AppiumBy.ID](http://appiumby.id/)**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan resource-id Android.
    - **Contoh:**
      ```python
      driver.find_element(AppiumBy.ID, "com.example.app:id/username_input")
      ```

2. **AppiumBy.CLASS_NAME**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan nama kelas Android.
    - **Contoh:**
      ```python
      driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
      ```

3. **AppiumBy.ACCESSIBILITY_ID**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan content-description Android.
    - **Contoh:**
      ```python
      driver.find_element(AppiumBy.ACCESSIBILITY_ID, "login_button")
      ```

4. **AppiumBy.ANDROID_UIAUTOMATOR**
    - **Deskripsi:** Menggunakan UiAutomator string untuk mengidentifikasi elemen.
    - **Contoh:**
      ```python
      driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
      driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.example.app:id/login_button")')
      ```

5. **AppiumBy.XPATH**
    - **Deskripsi:** Menggunakan XPath untuk mengidentifikasi elemen.
    - **Contoh:**
      ```python
      driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Login']")
      ```

6. **[AppiumBy.NAME](http://appiumby.name/)**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan atribut "name" (biasanya sama dengan teks yang ditampilkan).
    - **Contoh:**
      ```python
      driver.find_element(AppiumBy.NAME, "Login")
      ```

7. **AppiumBy.TAG_NAME**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan jenis widget Android.
    - **Contoh:**
      ```python
      driver.find_element(AppiumBy.TAG_NAME, "android.widget.Button")
      ```

## Contoh Penggunaan dengan WebDriverWait

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Menunggu dan menemukan elemen menggunakan ID
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((AppiumBy.ID, "com.example.app:id/username_input"))
)

# Menunggu dan menemukan elemen menggunakan UiAutomator
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")'))
)

# Menunggu dan menemukan elemen menggunakan XPath
password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_lo
