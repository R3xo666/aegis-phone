# 📱 Aegis-Phone: The Ultimate Dead-Screen Android Recovery & Remote Suite

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Fedora%20%7C%20Ubuntu-orange?style=for-the-badge&logo=linux" alt="Linux" />
  <img src="https://img.shields.io/badge/Engine-scrcpy%20v5.0%20%2B%20ADB-blue?style=for-the-badge&logo=android" alt="Scrcpy & ADB" />
  <img src="https://img.shields.io/badge/Security-Zero--Injection%20Hardened-green?style=for-the-badge&logo=shield" alt="Sentinel Hardened" />
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="MIT" />
</p>

```
    ___    ______ _____ _____ _____       ____  __  ______  _   ________
   /   |  / ____// ___// ___// ___/      / __ \/ / / / __ \/ | / / ____/
  / /| | / __/  / / _  \__ \ \__ \ _____/ /_/ / /_/ / / / /  |/ / __/   
 / ___ |/ /___ / /_/ /___/ /___/ /_____/ ____/ __  / /_/ / /|  / /___   
/_/  |_/_____/ \____//____//____/     /_/   /_/ /_/\____/_/ |_/_____/   
```

> **A mission-critical, enterprise-grade Android rescue, mirroring, and remote operations suite designed for broken/dead physical displays, emergency data recovery, and headless automation.**

---

## 📖 The Backstory: Why Aegis-Phone Was Born

One unfortunate morning, my phone took a violent fall onto concrete. The internals were fully alive, vibrating with notifications, alarms buzzing, and calls coming in—**but the physical AMOLED display was completely pitch-black and dead.** The digitizer was unresponsive. No touch, no backlight, no visuals.

I had critical 2FA OTP codes coming in for work, unread client messages on WhatsApp, and urgent phone calls to answer. 

Existing solutions like raw `scrcpy` were frustrating because:
1. When your phone screen is shattered or dead, keeping the display powered draws excess current, causing dangerous thermal runaway while charging.
2. The phone starts in a locked state—you can't swipe up or type your PIN blindly without a screen.
3. Every time an app with **AppLock** opened, everything came to a screeching halt.
4. Launching scrcpy blocked the entire terminal window, leaving zero room to run other ADB commands.

So, I built **Aegis-Phone**: a battle-hardened, zero-hardcode CLI & GUI suite that transforms any Linux PC into a direct physical brain-machine interface for your phone. It unlocks your phone blindly, silences display heating, streams uncompressed native 1080p, parses OTPs directly into your terminal, and gives you a floating desktop remote control deck.

---

## ✨ Enterprise Features at a Glance

- 🖥️ **Dead-Screen Smart Mirroring:** Always mirrors with the physical phone screen **100% powered off** (`--turn-screen-off`). Saves battery, prevents overheating, and keeps your private screen hidden in public.
- 📺 **Ultra-HD Studio Mode (`--hq`):** Streams up to **30Mbps uncompressed 60 FPS** at native resolution (1080x2460) with zero noticeable lag.
- 🔓 **Blind Keypad PIN Injection (`unlock`):** Automatically sends hardware wakeups, collapses intrusive Notification Shades, calculates dynamic screen dimensions, swipes up, and injects your PIN keycodes.
- 📱 **AppLock Breaker (`app-unlock` & `bypass-applock`):** Injects PINs into locked applications or temporarily suspends vendor AppLock overlays (e.g. Transsion PhoneMaster) with one click.
- ⚡ **Floating Desktop Remote Deck (`phone gui`):** An Always-On-Top minimalist dark-mode controller with clickable buttons for Back, Home, Recent Apps, Volume, Power, Call Pickup, and OTP reading.
- 🚀 **Non-Blocking Background Detach (`-b` / `--bg`):** Run scrcpy as a detached background daemon so your terminal prompt stays free for continuous work.
- 📩 **Live Notification & OTP Extractor (`notifs`):** Pulls active notifications directly from Android's notification manager and highlights incoming 2FA / OTP codes (`[🔑 OTP: 839102]`).
- 📞 **Terminal Call Center (`calls`, `dial`, `answer`, `hangup`):** Check call logs, answer incoming phone calls, or dial phone numbers directly via your Linux keyboard.
- 🛡️ **Zero-Injection Hardened:** Audited with `/sentinel-security` rules. Features Base64 binary clipboard piping, preventing shell metacharacter command injection (`CWE-78`).
- 🌐 **Dynamic Wi-Fi IP Discovery:** No hardcoded IPs. Resolves real-time interface IP (`wlan0`) and configures ADB over TCP/IP 5555 automatically.

---

## 🚀 1-Minute Installation

Clone the repository and run the automated universal setup:

```bash
git clone https://github.com/your-username/aegis-phone.git
cd aegis-phone
chmod +x install.sh
./install.sh
```

The installer verifies your dependencies, configures permissions, and sets up a global symlink in `~/.local/bin/phone`.

> **Prerequisites:** Linux (Fedora, Ubuntu, Debian, Arch), `python3`, `tkinter` (optional, for floating GUI deck), and a phone with **USB Debugging** previously authorized.

---

## 🎮 Command Cheatsheet

### 1. Mirroring & Display Control

```bash
# 1. Standard High-Definition Mirror (1080p @ 16Mbps, Physical Screen OFF, Audio ON)
phone

# 2. Ultra-Crisp Uncompressed Studio Mode (30Mbps @ Native Resolution)
phone --hq

# 3. Non-Blocking Mode (Runs mirror in background, keeps terminal free)
phone -b

# 4. Wireless Mirror over Wi-Fi (Auto-detects IP on wlan0)
phone --wifi

# 5. Eco / Low-Battery Recovery Mode (720p @ 4Mbps, 30 FPS cap)
phone --eco

# 6. Hardware OTG Simulation (Direct mouse & keyboard pass-through, no video stream)
phone --otg

# 7. Audio Forwarding Only (Listen to calls/media without opening video window)
phone --audio
```

---

### 2. Dead-Screen Rescue & Lock Management

```bash
# Unlock screen with PIN & immediately launch GUI mirror in one action
phone unlock 1234

# Silently unlock phone without launching scrcpy window
phone unlock-only 1234

# Unlock specific AppLock (WhatsApp, Gallery, Banking apps)
phone app-unlock 1234

# Temporarily suspend AppLock overlay
phone bypass-applock

# Launch Floating Remote Control Deck (GUI)
phone gui
```

---

### 3. Remote Communications Hub

```bash
# View active notifications with auto-extracted OTP verification codes
phone notifs

# View recent call history (Incoming, Outgoing, Missed, Duration)
phone calls

# Dial any phone number directly from CLI
phone dial +919876543210

# Answer incoming phone call
phone answer

# Hang up / terminate call
phone hangup

# Launch any installed application by name
phone open whatsapp
phone open settings
phone open youtube
```

---

### 4. Hardware Controls & System Telemetry

```bash
# View real-time hardware status (Battery %, Temp, Storage, Wi-Fi IP, Screen Dims)
phone status

# Start safe-charging thermal watchdog (Audio alert if temp > 42°C or battery reaches 85%)
phone watch

# Capture direct lossless framebuffer screenshot
phone shot ~/Pictures/phone_screen.png

# Push any file, photo, or video directly to phone (Triggers MediaScanner instantly)
phone push ~/Downloads/document.pdf
phone push ~/Pictures/meme.png /sdcard/Pictures/

# One-click backup of Photos, WhatsApp, Documents & Downloads
phone backup ~/Phone_Emergency_Backup

# Safely inject text to device clipboard (Base64 sanitized)
phone clip "Text to paste into phone"

# Interactive root/ADB terminal shell
phone shell

# Reboot shortcuts
phone reboot
phone reboot recovery
phone reboot bootloader
```

---

## ⌨️ Scrcpy Mirroring Shortcuts (Inside Window)

Use your keyboard `Alt` or `Super` (Windows Key) + key:

| Shortcut | Function |
| :--- | :--- |
| **`MOD + o`** | Turn physical screen **OFF** (PC mirror remains active) |
| **`MOD + Shift + o`** | Turn physical screen back **ON** |
| **`MOD + p`** | Press physical **Power** button |
| **`MOD + h`** | Press **Home** |
| **`MOD + b`** | Press **Back** |
| **`MOD + s`** | Open **App Switcher (Recents)** |
| **`MOD + n`** | Expand **Notification Shade** |
| **`MOD + f`** | Toggle Fullscreen |
| **`MOD + r`** | Rotate display clockwise |

---

## 🔒 Security & Architecture Standards

- **Zero Command Injection (CWE-78):** All clipboard and textual data payloads are converted to Base64 binaries before crossing into the ADB shell context.
- **Dynamic Geometric Calculation:** Coordinates for screen unlock and swipe gestures are dynamically computed relative to `wm size`, preventing failure across different aspect ratios (18:9, 19.5:9, 20:9).
- **Process Memory Sanitization:** Passwords and PIN numbers entered interactively are masked from terminal stdout (`read -rs`) and immediately cleared from shell memory upon transmission.

---

## 🤝 Contributing & License

Contributions, feature requests, and bug reports are welcome! Feel free to open an issue or pull request.

Distributed under the **MIT License**.
