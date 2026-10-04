import tkinter as tk
from tkinter import messagebox
import random
import time
import threading
import sys

try:
    import winsound
except ImportError:
    winsound = None


# ============================================================
# CREEPY - SAFE SIMULATION
# Created by mazdakproninja
# NOTHING IS ACTUALLY DELETED OR MODIFIED.
# ============================================================

APP_NAME = "CREEPY.exe"
CREATOR = "mazdakproninja"

BG = "#050505"
RED = "#ff2020"
GREEN = "#00ff66"
WHITE = "#dddddd"
GRAY = "#555555"


class CreepyApp:

    def __init__(self, root):
        self.root = root
        self.root.title(APP_NAME)
        self.root.configure(bg=BG)
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)

        self.running = True
        self.stage = 0
        self.glitching = False
        self.scan_percent = 0

        # ESC = emergency exit
        self.root.bind("<Escape>", self.emergency_exit)

        self.show_creator_warning()

    # --------------------------------------------------------
    # Initial message box
    # --------------------------------------------------------

    def show_creator_warning(self):
        self.root.withdraw()

        answer = messagebox.askyesno(
            "CREEPY.exe",
            "این برنامه توسط mazdakproninja ساخته شده است.\n\n"
            "این برنامه یک شبیه‌ساز ترسناک و کاملاً فیک است.\n"
            "هیچ فایل سیستمی واقعاً حذف نمی‌شود.\n"
            "هیچ دسترسی Trust Wallet گرفته نمی‌شود.\n\n"
            "آیا می‌خواهید ادامه دهید؟",
            icon="warning"
        )

        if not answer:
            self.root.destroy()
            return

        self.root.deiconify()
        self.build_gui()

        self.root.after(1000, self.start_simulation)

    # --------------------------------------------------------
    # GUI
    # --------------------------------------------------------

    def build_gui(self):

        self.main = tk.Frame(
            self.root,
            bg=BG
        )
        self.main.pack(fill="both", expand=True)

        # Header
        self.header = tk.Label(
            self.main,
            text="C R E E P Y . e x e",
            fg=RED,
            bg=BG,
            font=("Consolas", 28, "bold")
        )
        self.header.pack(pady=(25, 5))

        self.status = tk.Label(
            self.main,
            text="INITIALIZING...",
            fg=GRAY,
            bg=BG,
            font=("Consolas", 12)
        )
        self.status.pack()

        # Fake terminal
        self.terminal = tk.Text(
            self.main,
            bg="#020202",
            fg=GREEN,
            insertbackground=GREEN,
            font=("Consolas", 12),
            relief="flat",
            borderwidth=0
        )
        self.terminal.pack(
            padx=40,
            pady=20,
            fill="both",
            expand=True
        )

        self.terminal.config(state="disabled")

        # Progress
        self.progress = tk.Canvas(
            self.main,
            height=18,
            bg="#151515",
            highlightthickness=0
        )
        self.progress.pack(
            padx=40,
            fill="x"
        )

        self.progress_bar = self.progress.create_rectangle(
            0, 0, 0, 18,
            fill=RED,
            outline=""
        )

        self.percent = tk.Label(
            self.main,
            text="0%",
            fg=RED,
            bg=BG,
            font=("Consolas", 13)
        )
        self.percent.pack(pady=8)

        self.footer = tk.Label(
            self.main,
            text="ESC = EMERGENCY EXIT",
            fg="#444444",
            bg=BG,
            font=("Consolas", 10)
        )
        self.footer.pack(pady=(0, 15))

    # --------------------------------------------------------
    # Terminal
    # --------------------------------------------------------

    def terminal_write(self, text, color=None):

        self.terminal.config(state="normal")

        if color:
            tag = f"tag_{color}"
            self.terminal.tag_config(tag, foreground=color)
            self.terminal.insert("end", text + "\n", tag)
        else:
            self.terminal.insert("end", text + "\n")

        self.terminal.see("end")
        self.terminal.config(state="disabled")

    # --------------------------------------------------------
    # Sound
    # --------------------------------------------------------

    def beep(self, frequency=600, duration=80):

        if winsound:
            try:
                winsound.Beep(frequency, duration)
            except:
                pass

    # --------------------------------------------------------
    # Fake System32 scan
    # --------------------------------------------------------

    def start_simulation(self):

        threading.Thread(
            target=self.simulation_thread,
            daemon=True
        ).start()

    def simulation_thread(self):

        self.safe_print(
            "[CREEPY] Initializing simulation..."
        )

        time.sleep(1)

        self.safe_print(
            "[SYSTEM] Connecting to simulated Windows environment..."
        )

        time.sleep(1)

        self.safe_print(
            "[TRUST] Trust access: SIMULATED"
        )

        time.sleep(1)

        self.safe_print(
            "[WARNING] Administrative privileges: FAKE"
        )

        time.sleep(1)

        self.safe_print(
            ""
        )

        self.safe_print(
            "Scanning C:\\Windows\\System32 ..."
        )

        fake_files = [
            "kernel32.dll",
            "ntdll.dll",
            "user32.dll",
            "advapi32.dll",
            "winlogon.exe",
            "explorer.exe",
            "shell32.dll",
            "cmd.exe",
            "powershell.exe",
            "ntoskrnl.exe",
            "hal.dll",
            "bootres.dll",
            "winload.exe",
        ]

        for file in fake_files:

            if not self.running:
                return

            time.sleep(random.uniform(0.12, 0.4))

            self.safe_print(
                f"[SCAN] C:\\Windows\\System32\\{file}"
            )

            self.scan_percent += random.randint(4, 10)

            if self.scan_percent > 100:
                self.scan_percent = 100

            self.update_progress(
                self.scan_percent
            )

        self.safe_print("")
        self.safe_print(
            "[!]  SYSTEM32 CORRUPTION DETECTED",
            RED
        )

        self.beep(800, 200)

        time.sleep(2)

        self.fake_deletion()

    # --------------------------------------------------------
    # Fake deletion
    # --------------------------------------------------------

    def fake_deletion(self):

        self.safe_print("")
        self.safe_print(
            "STARTING SYSTEM32 CLEANUP..."
        )

        time.sleep(1)

        fake_files = [
            "kernel32.dll",
            "ntdll.dll",
            "user32.dll",
            "winlogon.exe",
            "explorer.exe",
            "csrss.exe",
            "services.exe",
            "lsass.exe",
            "smss.exe",
        ]

        for file in fake_files:

            if not self.running:
                return

            time.sleep(random.uniform(0.2, 0.6))

            self.safe_print(
                f"[SIMULATION] Deleting {file}",
                RED
            )

        self.update_progress(100)

        time.sleep(1)

        self.safe_print("")
        self.safe_print(
            "SYSTEM32 CLEANUP COMPLETE",
            RED
        )

        self.beep(300, 500)

        time.sleep(2)

        self.glitch_sequence()

    # --------------------------------------------------------
    # Glitch
    # --------------------------------------------------------

    def glitch_sequence(self):

        self.glitching = True

        self.status.config(
            text="SYSTEM FAILURE",
            fg=RED
        )

        for i in range(20):

            if not self.running:
                return

            self.root.after(
                0,
                self.random_glitch
            )

            time.sleep(
                random.uniform(0.04, 0.15)
            )

        self.glitching = False

        self.fake_terminal_horror()

    def random_glitch(self):

        if not self.running:
            return

        messages = [
            "SYSTEM FAILURE",
            "YOU SHOULDN'T BE HERE",
            "ACCESS DENIED",
            "DON'T CLOSE THIS",
            "I'M STILL HERE",
            "WHY DID YOU RUN THIS?",
            "0x00000000",
            "CONNECTION LOST",
            "CONNECTION RESTORED",
        ]

        text = random.choice(messages)

        self.header.config(
            text=text,
            fg=random.choice(
                [RED, WHITE, "#ff5555"]
            )
        )

        # random window background flash
        if random.random() < 0.35:
            self.root.configure(
                bg=random.choice(
                    [BG, "#180000", "#001000"]
                )
            )
        else:
            self.root.configure(bg=BG)

    # --------------------------------------------------------
    # Horror terminal
    # --------------------------------------------------------

    def fake_terminal_horror(self):

        self.terminal_write("")
        self.terminal_write(
            "------------------------------------------",
            RED
        )

        creepy = [
            "SYSTEM32 IS GONE.",
            "",
            "BUT YOU ARE STILL HERE.",
            "",
            "PROCESS STATUS: UNKNOWN",
            "USER STATUS: UNKNOWN",
            "EXIT STATUS: DENIED",
            "",
            "YOU CAN'T ESCAPE",
            "",
        ]

        for msg in creepy:

            if not self.running:
                return

            time.sleep(
                random.uniform(0.3, 0.8)
            )

            self.safe_print(
                msg,
                RED if "ESCAPE" in msg else None
            )

            if msg == "YOU CAN'T ESCAPE":
                self.beep(900, 400)

        time.sleep(3)

        self.fake_restart()

    # --------------------------------------------------------
    # Fake restart
    # --------------------------------------------------------

    def fake_restart(self):

        self.main.destroy()

        self.restart_screen = tk.Frame(
            self.root,
            bg="#000000"
        )

        self.restart_screen.pack(
            fill="both",
            expand=True
        )

        self.restart_text = tk.Label(
            self.restart_screen,
            text="Restarting...",
            fg="#dddddd",
            bg="#000000",
            font=("Segoe UI", 22)
        )

        self.restart_text.place(
            relx=0.5,
            rely=0.45,
            anchor="center"
        )

        self.restart_percent = tk.Label(
            self.restart_screen,
            text="0%",
            fg="#888888",
            bg="#000000",
            font=("Segoe UI", 12)
        )

        self.restart_percent.place(
            relx=0.5,
            rely=0.53,
            anchor="center"
        )

        self.root.after(
            500,
            lambda: self.restart_animation(0)
        )

    def restart_animation(self, value):

        if value >= 100:

            time.sleep(1)

            self.restart_screen.destroy()

            self.final_screen()

            return

        self.restart_percent.config(
            text=f"{value}%"
        )

        self.root.after(
            random.randint(40, 100),
            lambda: self.restart_animation(
                value + random.randint(2, 8)
            )
        )

    # --------------------------------------------------------
    # Final screen
    # --------------------------------------------------------

    def final_screen(self):

        frame = tk.Frame(
            self.root,
            bg="#000000"
        )

        frame.pack(
            fill="both",
            expand=True
        )

        title = tk.Label(
            frame,
            text="...",
            fg=RED,
            bg="#000000",
            font=("Consolas", 45, "bold")
        )

        title.place(
            relx=0.5,
            rely=0.35,
            anchor="center"
        )

        msg = tk.Label(
            frame,
            text="",
            fg="#cccccc",
            bg="#000000",
            font=("Consolas", 16)
        )

        msg.place(
            relx=0.5,
            rely=0.50,
            anchor="center"
        )

        def reveal():

            title.config(
                text="SYSTEM RESTORED"
            )

            msg.config(
                text=(
                    "Relax.\n\n"
                    "Everything above was FAKE.\n"
                    "No System32 files were deleted.\n"
                    "No permissions were changed.\n"
                    "No Trust Wallet access was obtained.\n\n"
                    "CREEPY.exe\n"
                    "Created by mazdakproninja"
                )
            )

        self.root.after(
            2500,
            reveal
        )

    # --------------------------------------------------------
    # Safe helpers
    # --------------------------------------------------------

    def safe_print(self, text, color=None):

        if not self.running:
            return

        self.root.after(
            0,
            lambda: self.terminal_write(
                text,
                color
            )
        )

    def update_progress(self, value):

        def update():

            width = self.progress.winfo_width()

            self.progress.coords(
                self.progress_bar,
                0,
                0,
                width * value / 100,
                18
            )

            self.percent.config(
                text=f"{value}%"
            )

        self.root.after(0, update)

    # --------------------------------------------------------
    # Emergency exit
    # --------------------------------------------------------

    def emergency_exit(self, event=None):

        self.running = False

        try:
            self.root.destroy()
        except:
            pass


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = CreepyApp(root)

    root.mainloop()