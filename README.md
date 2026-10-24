# Aegis Phone

Aegis Phone is a Bash command-line wrapper around Android Debug Bridge (ADB) and scrcpy for Linux. It provides commands for screen mirroring, device input, status checks, notifications, calls, screenshots, and file transfer.

## Requirements

- Linux and Bash
- Android Platform Tools (`adb`) and scrcpy; install these separately or place executable copies beside `phone`
- An Android device with USB debugging enabled and authorized for this computer
- Python 3 and Tkinter for the optional `phone gui` control panel
- `bc`, `notify-send`, and `paplay` are used by the optional battery watch command

The script prefers `adb` and `scrcpy` executables in the repository directory, then falls back to those available on `PATH`.

## Install

~~~bash
git clone https://github.com/R3xo666/aegis-phone.git
cd aegis-phone
chmod +x install.sh
./install.sh
~~~

The installer makes the scripts executable and creates `~/.local/bin/phone`. It adds that directory to `~/.bashrc` if it is not already on `PATH`; restart the shell or source the file if needed. It does not install ADB or scrcpy.

## Select a device

By default, Aegis Phone prefers a connected USB device, then a TCP/IP device. Put an explicit selector before the command when several devices are connected:

| Selector | Effect |
| --- | --- |
| `-d` or `--select-usb` | Select a USB-connected device |
| `-e` or `--select-tcpip` | Select a TCP/IP-connected device |
| `-s SERIAL` or `--serial SERIAL` | Select the given ADB serial |

For example, `phone -d status` checks the USB-connected device. Run `phone devices` to see ADB’s device list.

## Mirroring

| Command | Description |
| --- | --- |
| `phone` or `phone --screen-off` | Start the default scrcpy mirror with the device display turned off |
| `phone --hq` | Start the higher-bitrate mirror mode |
| `phone --eco` | Start a 720p, 30 fps lower-bandwidth mode |
| `phone --wifi` | Enable ADB TCP/IP on port 5555, connect over Wi-Fi, and start mirroring |
| `phone disconnect` | Disconnect wireless ADB sessions |
| `phone -b` or `phone --background` | Start the default mirror in the background |
| `phone --otg` | Start scrcpy OTG input mode without a video stream |
| `phone --audio` | Forward audio without opening a video window |
| `phone gui` | Open the optional Tkinter control panel |

## Device commands

| Command | Description |
| --- | --- |
| `phone status` | Show model, Android version, display size, Wi-Fi IP, battery, storage, and ADB state |
| `phone ip` | Print the device’s Wi-Fi IP when available |
| `phone power`, `phone home`, `phone back` | Send the corresponding Android key event |
| `phone volup`, `phone voldn` | Change device volume |
| `phone open APP` | Find and launch an installed app whose package matches `APP` |
| `phone shell` | Open an interactive ADB shell |
| `phone reboot [recovery|bootloader]` | Reboot the device; no argument reboots normally |

### Lock screen and AppLock

| Command | Description |
| --- | --- |
| `phone unlock [PIN]` | Enter a lock-screen PIN and then start the default mirror |
| `phone unlock-only [PIN]` | Enter a lock-screen PIN without starting the mirror |
| `phone app-unlock [PIN]` | Send PIN key events to the currently visible AppLock screen |
| `phone bypass-applock` | Force-stop matching AppLock packages from a built-in package list |
| `phone fix-auth` | Start an interactive OTG workflow for an ADB authorization prompt |

If you omit a PIN, the script prompts for it without echoing input. Avoid putting a real PIN directly in a shell command, where it may be saved in shell history. Device and OEM behavior varies, so these commands are not guaranteed to work on every lock screen or AppLock.

`phone bypass-applock` stops matching package processes and may interrupt the device’s security app. `phone fix-auth` may call `phone auth-persist` after authorization succeeds; see the settings change below.

### Notifications, calls, and clipboard

| Command | Description |
| --- | --- |
| `phone notifs` | Print active notification text and flag likely 4–8 digit codes when nearby text contains terms such as “code” or “verification” |
| `phone calls` | Read and display recent call-log entries |
| `phone dial NUMBER` | Open an outgoing call to the number |
| `phone answer`, `phone hangup` | Send call answer or end-call key events |
| `phone clip TEXT` | Set the phone clipboard text |
| `phone clip` | Request the current clipboard text |

Notifications, one-time codes, call history, and clipboard contents can be sensitive. Use these commands only with permission to access the connected device.

### Screenshots and files

| Command | Description |
| --- | --- |
| `phone shot [PATH]` | Save a screenshot; defaults to a timestamped file in `~/Pictures/` |
| `phone backup [DIR]` | Copy `DCIM`, `Pictures`, `Download`, `Documents`, and `WhatsApp` folders to a local directory |
| `phone push FILE [DEST]` | Copy a local file to the device; destination defaults to `/sdcard/Pictures/` |
| `phone install APK` | Install or replace an APK using `adb install -r -g` |

`phone install` requests that Android grant the APK’s runtime permissions during installation. Review an APK and its requested permissions before installing it.

### Battery and ADB settings

| Command | Description |
| --- | --- |
| `phone watch` | Check battery temperature and charge every five seconds; desktop alerts use fixed thresholds of 42 °C and 85% while charging |
| `phone auth-persist` | Set Android global settings for ADB authorization timeout, stay-awake-while-plugged-in, and developer settings |

`phone auth-persist` changes settings on the connected device: it sets `adb_allowed_connection_time` to `0`, `stay_on_while_plugged_in` to `3`, and `development_settings_enabled` to `1`. Run it only if you intend to keep those settings.

## Troubleshooting

- If `phone devices` lists the device as `unauthorized`, unlock the phone and accept the USB debugging prompt. The `phone fix-auth` OTG workflow is an alternative that requires direct physical input.
- If the device is missing, check the USB cable, enable USB debugging, and confirm `adb devices -l` can see it.
- If mirroring fails, confirm `scrcpy` runs directly and that its version is compatible with the installed ADB tools.
- If `phone gui` fails to start, install Python 3 with Tkinter for your distribution.

## License

MIT. See [LICENSE](LICENSE).