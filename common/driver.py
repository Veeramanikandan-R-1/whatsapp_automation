from appium import webdriver
# importing desired capabalities json from appium
desired_capabilites_redmi_whatsapp={
  "platformName": "Android",
  "deviceName": "e81ad2c19804",
  # "app": "F:\\mani\\GURUKUL\\apk\\app-release (1).apk",  not needed
  "appPackage": "com.whatsapp",
  "appActivity": "com.whatsapp.HomeActivity}"
}
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilites_redmi_whatsapp)