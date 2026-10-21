#!/usr/bin/env python3
"""
Aegis-Phone Floating Remote Control Deck (GUI)
Minimalist Dark-Mode Clickable Controller for Dead-Screen Android Mirroring.
"""

import sys
import os
import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog

import shutil

SCRCPY_DIR = os.path.dirname(os.path.abspath(__file__))
local_adb = os.path.join(SCRCPY_DIR, "adb")
ADB = local_adb if os.path.isfile(local_adb) and os.access(local_adb, os.X_OK) else (shutil.which("adb") or "adb")

def run_adb(cmd_list):
    try:
        subprocess.run([ADB] + cmd_list, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Error running adb: {e}", file=sys.stderr)

def get_screen_size():
    try:
        proc = subprocess.run([ADB, "shell", "wm", "size"], stdout=subprocess.PIPE, text=True)
        for line in proc.stdout.splitlines():
            if "Physical size" in line:
                dims = line.split(":")[-1].strip()
                w, h = dims.split("x")
                return int(w), int(h)
    except Exception:
        pass
    return 1080, 2460

class PhoneDeck(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("⚡ Aegis Deck")
        self.geometry("260x520")
        self.resizable(False, False)
        self.attributes("-topmost", True)  # Always stay on top of scrcpy window
        self.configure(bg="#121214")

        self.create_widgets()

    def create_widgets(self):
        # Header
        header = tk.Label(self, text="AEGIS CONTROLLER", font=("Helvetica", 11, "bold"), fg="#a855f7", bg="#121214")
        header.pack(pady=(12, 6))

        # Status text
        self.lbl_status = tk.Label(self, text="● Device Ready", font=("Helvetica", 8), fg="#22c55e", bg="#121214")
        self.lbl_status.pack(pady=(0, 10))

        # Button Factory
        def btn(parent, text, cmd, bg="#27272a", fg="#f4f4f5", active_bg="#3f3f46"):
            b = tk.Button(parent, text=text, command=cmd, font=("Helvetica", 9, "bold"),
                          bg=bg, fg=fg, activebackground=active_bg, activeforeground=fg,
                          relief="flat", bd=0, padx=8, pady=5, cursor="hand2")
            return b

        # Section 1: Locks & Security
        sec_lock = tk.LabelFrame(self, text=" Lock & App Security ", font=("Helvetica", 8, "bold"),
                                 fg="#a1a1aa", bg="#121214", bd=1, relief="solid")
        sec_lock.pack(fill="x", padx=12, pady=4)

        b_unlock = btn(sec_lock, "🔓 Unlock Phone", self.unlock_phone, bg="#3b82f6", fg="#ffffff")
        b_unlock.pack(fill="x", padx=6, pady=3)

        b_applock = btn(sec_lock, "📱 Unlock AppLock (PIN)", self.unlock_applock, bg="#8b5cf6", fg="#ffffff")
        b_applock.pack(fill="x", padx=6, pady=3)

        b_bypass = btn(sec_lock, "⚡ Bypass AppLock", self.bypass_applock, bg="#1e293b", fg="#94a3b8")
        b_bypass.pack(fill="x", padx=6, pady=3)

        # Section 2: Hardware Navigation
        sec_nav = tk.LabelFrame(self, text=" System Navigation ", font=("Helvetica", 8, "bold"),
                                fg="#a1a1aa", bg="#121214", bd=1, relief="solid")
        sec_nav.pack(fill="x", padx=12, pady=4)

        nav_row1 = tk.Frame(sec_nav, bg="#121214")
        nav_row1.pack(fill="x", padx=6, pady=2)
        btn(nav_row1, "🔙 Back", lambda: run_adb(["shell", "input", "keyevent", "KEYCODE_BACK"])).pack(side="left", expand=True, fill="x", padx=2)
        btn(nav_row1, "🏠 Home", lambda: run_adb(["shell", "input", "keyevent", "KEYCODE_HOME"])).pack(side="left", expand=True, fill="x", padx=2)
        btn(nav_row1, "🔲 Apps", lambda: run_adb(["shell", "input", "keyevent", "KEYCODE_APP_SWITCH"])).pack(side="left", expand=True, fill="x", padx=2)

        nav_row2 = tk.Frame(sec_nav, bg="#121214")
        nav_row2.pack(fill="x", padx=6, pady=2)
        btn(nav_row2, "🔊 Vol +", lambda: run_adb(["shell", "input", "keyevent", "KEYCODE_VOLUME_UP"])).pack(side="left", expand=True, fill="x", padx=2)
        btn(nav_row2, "🔉 Vol -", lambda: run_adb(["shell", "input", "keyevent", "KEYCODE_VOLUME_DOWN"])).pack(side="left", expand=True, fill="x", padx=2)
        btn(nav_row2, "⚡ Power", lambda: run_adb(["shell", "input", "keyevent", "KEYCODE_POWER"])).pack(side="left", expand=True, fill="x", padx=2)

        # Section 3: Communications & Fast Actions
        sec_comm = tk.LabelFrame(self, text=" Quick Actions ", font=("Helvetica", 8, "bold"),
                                 fg="#a1a1aa", bg="#121214", bd=1, relief="solid")
        sec_comm.pack(fill="x", padx=12, pady=4)

        call_row = tk.Frame(sec_comm, bg="#121214")
        call_row.pack(fill="x", padx=6, pady=2)
        btn(call_row, "📞 Answer", lambda: run_adb(["shell", "input", "keyevent", "KEYCODE_CALL"]), bg="#15803d", fg="#ffffff").pack(side="left", expand=True, fill="x", padx=2)
        btn(call_row, "🛑 Hangup", lambda: run_adb(["shell", "input", "keyevent", "KEYCODE_ENDCALL"]), bg="#b91c1c", fg="#ffffff").pack(side="left", expand=True, fill="x", padx=2)

        btn(sec_comm, "📩 Read OTP & Notifs", self.view_notifs, bg="#1e293b", fg="#38bdf8").pack(fill="x", padx=6, pady=3)
        btn(sec_comm, "📋 Paste Text Clipboard", self.paste_clipboard, bg="#1e293b", fg="#cbd5e1").pack(fill="x", padx=6, pady=3)

        # Section 4: File & Image Drop Box
        sec_file = tk.LabelFrame(self, text=" File & Image Transfer ", font=("Helvetica", 8, "bold"),
                                 fg="#a1a1aa", bg="#121214", bd=1, relief="solid")
        sec_file.pack(fill="x", padx=12, pady=4)

        btn(sec_file, "🖼️ Paste Image to Phone", self.paste_clipboard_image, bg="#0284c7", fg="#ffffff").pack(fill="x", padx=6, pady=3)
        btn(sec_file, "📁 Send File / Video...", self.pick_and_send_file, bg="#334155", fg="#f8fafc").pack(fill="x", padx=6, pady=3)

    def unlock_phone(self):
        pin = simpledialog.askstring("Device Lock", "Enter Device PIN:", show="*")
        if not pin:
            return
        subprocess.run([os.path.join(SCRCPY_DIR, "phone"), "unlock-only", pin])
        self.lbl_status.config(text="● Device Unlocked", fg="#22c55e")

    def unlock_applock(self):
        pin = simpledialog.askstring("AppLock PIN", "Enter AppLock PIN:", show="*")
        if not pin:
            return
        subprocess.run([os.path.join(SCRCPY_DIR, "phone"), "app-unlock", pin])
        self.lbl_status.config(text="● AppLock Keycodes Sent", fg="#22c55e")

    def bypass_applock(self):
        subprocess.run([os.path.join(SCRCPY_DIR, "phone"), "bypass-applock"])
        self.lbl_status.config(text="● AppLock Overlay Dismissed", fg="#eab308")

    def view_notifs(self):
        terminals = [
            ["ptyxis", "--", "bash", "-c"],
            ["konsole", "-e", "bash", "-c"],
            ["foot", "bash", "-c"],
            ["kitty", "bash", "-c"],
            ["gnome-terminal", "--", "bash", "-c"],
            ["xterm", "-e", "bash", "-c"]
        ]
        phone_cmd = f"{os.path.join(SCRCPY_DIR, 'phone')} notifs; echo ''; read -p 'Press Enter to close...'"
        
        launched = False
        for term in terminals:
            if shutil.which(term[0]):
                try:
                    subprocess.Popen([term[0]] + term[1:] + [phone_cmd])
                    launched = True
                    break
                except Exception:
                    continue
        if not launched:
            # Fallback to direct output popup in tkinter
            res = subprocess.run([os.path.join(SCRCPY_DIR, "phone"), "notifs"], stdout=subprocess.PIPE, text=True)
            messagebox.showinfo("Notifications & OTP", res.stdout or "No active notifications")

    def paste_clipboard(self):
        try:
            clip = self.clipboard_get()
            if clip:
                subprocess.run([os.path.join(SCRCPY_DIR, "phone"), "clip", clip])
                self.lbl_status.config(text="● Text Injected to Phone", fg="#22c55e")
        except Exception as e:
            messagebox.showerror("Clipboard Error", str(e))

    def paste_clipboard_image(self):
        try:
            from PIL import ImageGrab
            import tempfile
            im = ImageGrab.grabclipboard()
            if im is not None:
                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tf:
                    tmp_img = tf.name
                im.save(tmp_img, "PNG")
                subprocess.run([os.path.join(SCRCPY_DIR, "phone"), "push", tmp_img, "/sdcard/Pictures/"])
                if os.path.exists(tmp_img):
                    os.remove(tmp_img)
                self.lbl_status.config(text="● Image Sent to Gallery!", fg="#22c55e")
                messagebox.showinfo("Success", "Copied image transferred directly into phone's Pictures/Gallery!")
            else:
                messagebox.showwarning("No Image", "No image found in clipboard! Copy an image first.")
        except Exception as e:
            messagebox.showerror("Image Error", str(e))

    def pick_and_send_file(self):
        from tkinter import filedialog
        filepath = filedialog.askopenfilename(title="Select File to Send to Phone")
        if filepath:
            subprocess.run([os.path.join(SCRCPY_DIR, "phone"), "push", filepath, "/sdcard/Download/"])
            self.lbl_status.config(text=f"● Sent: {os.path.basename(filepath)[:15]}...", fg="#22c55e")
            messagebox.showinfo("File Sent", f"File '{os.path.basename(filepath)}' saved to phone's Download folder!")

if __name__ == "__main__":
    app = PhoneDeck()
    app.mainloop()
