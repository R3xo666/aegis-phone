# Aegis Phone

Aegis Phone is a Bash command-line tool for controlling and mirroring an Android device from Linux. It wraps Android Debug Bridge (ADB) and scrcpy with commands for display mirroring, connection selection, device status, screenshots, backups, and common device actions.

## Requirements

- Linux and Bash
- Android Platform Tools (`adb`) and scrcpy, installed on your system or available in the repository directory
- An Android device with USB debugging enabled and authorized for the connected computer
- Python 3 and Tkinter for the optional desktop control panel

## Install

~~~bash
git clone https://github.com/R3xo666/aegis-phone.git
cd aegis-phone
chmod +x install.sh
./install.sh
~~~

The installer creates a `phone` command in `~/.local/bin`. It does not install ADB or scrcpy.

## Examples

~~~bash
phone devices
phone                 # Start a scrcpy mirror
phone --eco           # Lower-resolution mirror
phone --wifi          # Connect over ADB TCP/IP and mirror
phone status
phone shot ~/Pictures/phone.png
phone backup ~/PhoneBackup
phone gui             # Optional Tkinter control panel
~~~

Run `phone --help` for the full command list. Commands such as `unlock`, `dial`, `install`, `backup`, and `reboot` send actions to the connected device; review the requested action before using them, and use this tool only on devices you own or are authorized to administer.

## License

MIT. See [LICENSE](LICENSE).