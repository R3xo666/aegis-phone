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

---

## 🛠️ Comprehensive Troubleshooting Guide

### 1. ⚠️ Device shows `unauthorized` after PC Restart or Cable Reconnect
**Why it happens:** Android 11–14 introduces an automatic authorization revocation timer that clears authorized PC keys every 7 days or after sudden connection drops. If "Always allow from this computer" wasn't ticked, Android drops authorization.

**How Aegis-Phone fixes it permanently:**
Run:
```bash
phone auth-persist
```
This writes `adb_allowed_connection_time = 0` and `stay_on_while_plugged_in = 3` directly into device global settings so the key **never expires**.

**What if the screen is already 100% black/dead when this happens?**
Use the **Blind OTG Rescue Protocol**:
```bash
phone fix-auth
```
- Aegis-Phone switches into pure hardware USB-HID emulation (no ADB authorization required).
- Blind keystroke sequence:
  1. Press `[Tab]` $\rightarrow$ Moves focus to the *"Always allow from this computer"* checkbox.
  2. Press `[Space]` $\rightarrow$ Checks the box.
  3. Press `[Tab]` followed by `[Enter]` $\rightarrow$ Clicks "Allow".
- Your phone is permanently re-authorized without seeing or touching the broken physical display!

---

### 2. 🔌 Device Not Detected (`phone devices` shows empty list)
- Ensure your USB cable supports high-speed data transfer (some cheap charging cables only supply power and lack data lines).
- Plug directly into your computer's motherboard / primary USB port rather than unpowered multi-port USB hubs.
- Ensure your Linux user has permission to access USB devices (if running into permission denied errors):
  ```bash
  sudo adb kill-server && sudo adb start-server
  ```
- Reconnect the USB cable firmly or restart ADB daemon:
  ```bash
  adb kill-server && adb start-server
  ```

---

### 3. 💥 Physical Screen Overheating or Turning On Unexpectedly
- By default, Aegis-Phone launches with `--turn-screen-off` and forces screen brightness to `0` via hardware shell settings.
- If you accidentally turn the screen on, press **`MOD + o`** (`Alt + o` or `Super + o`) inside the scrcpy window to instantly kill the physical display backlight while keeping the PC mirror running.
- Run `phone watch` to monitor internal battery temperature and receive audio alarms if temperatures rise above 42°C.

---

### 4. 🔒 Screen Lock PIN Isn't Registering
- If you have an exotic screen ratio or custom lockscreen widgets, the notification shade might block key events.
- Run:
  ```bash
  phone unlock 1234
  ```
  Aegis-Phone automatically collapses status bar shades, pulses `KEYCODE_MENU`, computes exact vertical midpoint swipe vectors dynamically from `wm size`, and enters numerical keycodes with 80ms debounce.

---

### 5. 🔲 AppLock Overlay Blocking Access (WhatsApp, Gallery, Banking)
- Use `phone app-unlock <PIN>` to inject your AppLock PIN directly.
- Or use `phone bypass-applock` to temporarily suspend vendor security managers (e.g. Transsion PhoneMaster, MIUI SecurityCenter, ColorOS SafeCenter).

---

## ❓ Frequently Asked Questions (FAQ)

<details>
<summary><b>Q1: Can I use Aegis-Phone if my touch screen is 100% dead?</b></summary>
<br>

**Yes, absolutely!** That is the exact reason Aegis-Phone was created. All mouse clicks, gestures, text input, and file drag-and-drops from your PC are sent as software hardware events via ADB and USB-HID. Your physical digitizer does not need to work at all.

</details>

<details>
<summary><b>Q2: Does Aegis-Phone require my phone to be Rooted?</b></summary>
<br>

**No root required!** All capabilities—including display blackout, blind PIN unlock, OTP reading, clipboard synchronization, and call dialing—work on standard unrooted production Android devices.

</details>

<details>
<summary><b>Q3: How do I copy-paste images or files from my PC to my phone?</b></summary>
<br>

You have two easy ways:

1. **Via Floating Controller (`phone gui`):**
   - Click **"🖼️ Paste Image to Phone"** to instantly push any image from your PC clipboard into your phone's Gallery.
   - Click **"📁 Send File / Video..."** to browse and upload files directly.

2. **Via Command Line:**
   ```bash
   phone push ~/Pictures/screenshot.png /sdcard/Pictures/
   ```
   Aegis-Phone automatically triggers Android's MediaScanner so WhatsApp and Gallery recognize the new file immediately.

</details>

<details>
<summary><b>Q4: Will my physical screen light up and show my messages to people around me?</b></summary>
<br>

**No.** Aegis-Phone sends hardware commands to keep the physical backlight completely dark (`0` brightness and powered-off state). Your private activities remain visible only on your Linux computer monitor.

</details>

<details>
<summary><b>Q5: Can I use this wirelessly without keeping the USB cable connected all day?</b></summary>
<br>

**Yes!** While connected via USB, run:

```bash
phone --wifi
```

Aegis-Phone will resolve your device's local Wi-Fi IP address on `wlan0`, bind ADB to port 5555, and launch a wireless mirror session. You can then safely disconnect the USB cable.

</details>

<details>
<summary><b>Q6: What happens if my PC restarts? Will I lose access?</b></summary>
<br>

If you run `phone auth-persist`, your PC's RSA signature is permanently whitelisted in Android's flash memory, and the 7-day auto-revocation timer is set to `0`. Even after 100 PC reboots, your phone will remain authorized.

</details>

---

## 🤝 Contributing & License

Contributions, feature requests, and bug reports are welcome! Feel free to open an issue or pull request.

Distributed under the **MIT License**.

