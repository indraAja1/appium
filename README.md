# <img src="https://brandslogos.com/wp-content/uploads/images/large/appium-logo.png" alt="Appium Logo" width="39" style ="display: block;, margin-top: 10px;"/> Automation Appium

## Selector Android

1. **[AppiumBy.ID]
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

6. **[AppiumBy.NAME]
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

