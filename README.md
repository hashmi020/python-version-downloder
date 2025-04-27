🐍 Python Version Downloader (Tkinter + Selenium)
A simple desktop application to download any specific version of Python for Windows 64-bit directly from the official python.org website.

Built using:

Tkinter (for GUI)

Selenium (for automating web interaction)

webdriver-manager (for automatic ChromeDriver management)

SCREEENSHOT
  
![Screenshot 2025-04-27 161037](https://github.com/user-attachments/assets/c1423f03-4b9f-4ae0-a2a7-11ff301286ab)

✨ Features
Enter any Python version (e.g., 3.12.2).

Automatically finds and downloads the Windows 64-bit installer (.exe) from python.org.

User-friendly GUI with input box and download button.

Success and error pop-up messages.

Non-blocking download (Selenium runs in a background thread).

🚀 Installation
Clone or download the project.

Install the required Python packages:

bash
Copy
Edit
pip install selenium webdriver-manager
✅ Tkinter comes pre-installed with Python, so no need to install separately.

⚙️ Usage
Run the Python script:

bash
Copy
Edit
python automate_tkinter.py
Enter the Python version you want to download (example: 3.12.2).

Click the Download button.

The Windows 64-bit installer .exe will start downloading automatically!

📋 Requirements
Python 3.6+

Google Chrome browser installed

Internet connection

⚠️ Notes
The application currently supports only Windows 64-bit .exe installers.

If the version does not exist or the installer is not available, a proper error message is shown
