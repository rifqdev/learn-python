from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import geckodriver_autoinstaller
from selenium.webdriver.firefox.options import Options
import ssl
import os

PROFILE_PATH = os.getenv("PROFILE_PATH")

# Menonaktifkan verifikasi SSL
ssl._create_default_https_context = ssl._create_unverified_context

# Instal Geckodriver secara otomatis
geckodriver_autoinstaller.install()

# Lokasi profil Firefox
profile_path = PROFILE_PATH

# Konfigurasi opsi Firefox
options = Options()
options.add_argument(f"--profile={profile_path}")
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)

# Inisialisasi WebDriver
driver = webdriver.Firefox(options=options)

try:
    # Buka URL
    driver.get("https://glints.com/id/opportunities/jobs/explore?keyword=javascript&country=ID&locationName=All+Cities%2FProvinces&lowestLocationLevel=1&type=Terakhir+dicari%3A&lastUpdated=PAST_24_HOURS")
    print(driver.title)

    # Tunggu hingga elemen <h2 a> tersedia
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h2 a')))

    # Ambil semua elemen <a> di dalam <h2>
    cards = driver.find_elements(By.CSS_SELECTOR, 'h2 a')

    # Iterasi melalui semua elemen dan ambil properti outerHTML
    for card in cards:
        try:
            print(card.get_property('outerHTML'))  # Mengambil properti outerHTML
        except StaleElementReferenceException:
            # Jika elemen menjadi stale, ambil kembali semua elemen
            cards = driver.find_elements(By.CSS_SELECTOR, 'h2 a')
            print(card.get_property('outerHTML'))  # Coba lagi

finally:
    # Menutup driver setelah selesai
    driver.quit()























