# automate_tkinter.py

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading
import sys

def download_python(version):
    # Setup Chrome browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Step 1: Open Python downloads page
        driver.get('https://www.python.org/downloads/')

        # Step 2: Search for the given version
        link = driver.find_element(By.PARTIAL_LINK_TEXT, version)
        link.click()
        print(f"Opened download page for Python {version}")

        time.sleep(2)

        # Step 3: Find the 64-bit Windows installer (.exe)
        file_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Windows installer (64-bit)')
        download_url = file_link.get_attribute('href')

        # Open the download URL directly
        driver.get(download_url)
        print(f"Downloading from: {download_url}")
        time.sleep(10)

        messagebox.showinfo("Success", f"Downloading Python {version} (64-bit Windows installer)!")
    
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"Version {version} not found or installer missing!")
    finally:
        driver.quit()

def start_download():
    version = entry.get().strip()
    if not version:
        messagebox.showwarning("Input Error", "Please enter a Python version (e.g., 3.12.2)")
        return
    
    # Run Selenium in a new thread so Tkinter doesn't freeze
    threading.Thread(target=download_python, args=(version,), daemon=True).start()

# --- Tkinter UI setup ---
root = tk.Tk()
root.title("Python Version Downloader")
root.geometry("400x200")
root.resizable(False, False)

label = tk.Label(root, text="Enter Python Version:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

button = tk.Button(root, text="Download", font=("Arial", 14), command=start_download)
button.pack(pady=20)

root.mainloop()
