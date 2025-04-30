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

⚠️ Again, this is only for lab simulation — do not enable this on real machines or without permission.

📬 Contact
Created by Sarwar ilyas feel free to contribute, fork, or contact for collaborations in cybersecurity research.
