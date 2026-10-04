import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import random
import threading
import time
import math
import sys

try:
    import winsound
except ImportError:
    winsound = None


# ============================================================
# CREEPYv2.exe
# Horror / Creepypasta Simulation
#
# CREATED BY: mazdakproninja
#
# IMPORTANT:
# This program is a PURE SIMULATION.
# It does NOT:
#   - delete System32
#   - modify Windows
#   - modify the registry
#   - access Trust Wallet
#   - obtain administrator privileges
#   - access the network
#
# ESC = Emergency Exit
# ============================================================


APP_TITLE = "CREEPYv2.exe"
CREATOR = "mazdakproninja"

WIDTH = 1200
HEIGHT = 720

BLACK = "#020202"
DARK = "#070707"
RED = "#ff2020"
DARK_RED = "#550000"
GREEN = "#00ff66"
WHITE = "#eeeeee"
GRAY = "#555555"
CYAN = "#00dddd"


class CreepyV2:

    def __init__(self, root):

        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.minsize(900, 600)
        self.root.configure(bg=BLACK)

        self.running = True
        self.glitch = False
        self.stage = 0
        self.restart_count = 0
        self.scan_percent = 0
        self.typing = False

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.emergency_exit
        )

        self.root.bind(
            "<Escape>",
            self.emergency_exit
        )

        self.show_warning()

    # ========================================================
    # INITIAL WARNING
    # ========================================================

    def show_warning(self):

        self.root.withdraw()

        answer = messagebox.askyesno(
            "CREEPYv2.exe",
            "CREEPYv2.exe\n\n"
            "Created by mazdakproninja\n\n"
            "This is a fictional horror simulation.\n"
            "Nothing will actually be deleted or damaged.\n\n"
            "Continue?",
            icon="warning"
        )

        if not answer:
            self.running = False
            self.root.destroy()
            return

        self.root.deiconify()
        self.build_main_gui()

        self.root.after(
            1000,
            self.start
        )

    # ========================================================
    # MAIN GUI
    # ========================================================

    def build_main_gui(self):

        self.container = tk.Frame(
            self.root,
            bg=BLACK
        )

        self.container.pack(
            fill="both",
            expand=True
        )

        # CRT canvas
        self.canvas = tk.Canvas(
            self.container,
            bg=BLACK,
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )

        # Header
        self.header = self.canvas.create_text(
            WIDTH // 2,
            50,
            text="C R E E P Y . e x e",
            fill=RED,
            font=("Consolas", 30, "bold")
        )

        self.status = self.canvas.create_text(
            WIDTH // 2,
            90,
            text="INITIALIZING...",
            fill=GRAY,
            font=("Consolas", 11)
        )

        # Terminal frame
        self.terminal = tk.Text(
            self.container,
            bg="#010101",
            fg=GREEN,
            insertbackground=GREEN,
            font=("Consolas", 11),
            relief="flat",
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="#222222"
        )

        self.terminal.place(
            relx=0.05,
            rely=0.17,
            relwidth=0.90,
            relheight=0.65
        )

        self.terminal.config(
            state="disabled"
        )

        # Progress
        self.progress_bg = tk.Frame(
            self.container,
            bg="#151515",
            height=16
        )

        self.progress_bg.place(
            relx=0.05,
            rely=0.85,
            relwidth=0.90
        )

        self.progress_fill = tk.Frame(
            self.progress_bg,
            bg=RED,
            height=16
        )

        self.progress_fill.place(
            x=0,
            y=0,
            relwidth=0
        )

        self.percent = tk.Label(
            self.container,
            text="0%",
            bg=BLACK,
            fg=RED,
            font=("Consolas", 11)
        )

        self.percent.place(
            relx=0.5,
            rely=0.885,
            anchor="center"
        )

        self.escape_text = tk.Label(
            self.container,
            text="ESC  →  EMERGENCY EXIT",
            bg=BLACK,
            fg="#444444",
            font=("Consolas", 9)
        )

        self.escape_text.place(
            relx=0.5,
            rely=0.94,
            anchor="center"
        )

        self.start_crt()

    # ========================================================
    # CRT EFFECT
    # ========================================================

    def start_crt(self):

        if not self.running:
            return

        try:
            self.draw_crt()
        except:
            pass

        self.root.after(
            80,
            self.start_crt
        )

    def draw_crt(self):

        if not hasattr(self, "canvas"):
            return

        self.canvas.delete("crt")

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if width < 100:
            width = WIDTH

        if height < 100:
            height = HEIGHT

        # Scanlines
        for y in range(0, height, 5):

            self.canvas.create_line(
                0,
                y,
                width,
                y,
                fill="#080808",
                tags="crt"
            )

        # Random static
        if self.glitch:

            for _ in range(80):

                x = random.randint(
                    0,
                    width
                )

                y = random.randint(
                    0,
                    height
                )

                size = random.randint(
                    1,
                    4
                )

                color = random.choice(
                    [
                        "#222222",
                        "#333333",
                        "#550000",
                        "#444444"
                    ]
                )

                self.canvas.create_rectangle(
                    x,
                    y,
                    x + size,
                    y + size,
                    fill=color,
                    outline="",
                    tags="crt"
                )

    # ========================================================
    # START
    # ========================================================

    def start(self):

        threading.Thread(
            target=self.main_sequence,
            daemon=True
        ).start()

    # ========================================================
    # MAIN HORROR SEQUENCE
    # ========================================================

    def main_sequence(self):

        self.log(
            "[CREEPY] Starting environment..."
        )

        time.sleep(1)

        self.log(
            "[SYSTEM] Loading diagnostic interface..."
        )

        time.sleep(1)

        self.log(
            "[SECURITY] Access mode: SIMULATED"
        )

        time.sleep(1)

        self.log(
            "[NETWORK] Offline simulation mode"
        )

        time.sleep(1)

        self.log(
            "[TRUST] Trust access: FAKE"
        )

        time.sleep(1)

        self.fake_scan()

        if not self.running:
            return

        self.fake_cleanup()

        if not self.running:
            return

        self.first_glitch()

        if not self.running:
            return

        self.creepy_messages()

        if not self.running:
            return

        self.fake_restart(1)

        if not self.running:
            return

        self.second_phase()

        if not self.running:
            return

        self.fake_restart(2)

        if not self.running:
            return

        self.third_phase()

        if not self.running:
            return

        self.fake_restart(3)

        if not self.running:
            return

        self.final_reveal()

    # ========================================================
    # FAKE SYSTEM SCAN
    # ========================================================

    def fake_scan(self):

        self.set_status(
            "SCANNING C:\\WINDOWS\\SYSTEM32..."
        )

        self.log("")
        self.log(
            "------------------------------------------",
            RED
        )
        self.log(
            " SYSTEM32 INTEGRITY SCAN",
            RED
        )
        self.log(
            "------------------------------------------",
            RED
        )

        files = [
            "kernel32.dll",
            "ntdll.dll",
            "user32.dll",
            "advapi32.dll",
            "shell32.dll",
            "winlogon.exe",
            "explorer.exe",
            "csrss.exe",
            "services.exe",
            "lsass.exe",
            "smss.exe",
            "ntoskrnl.exe",
            "hal.dll",
            "bootres.dll",
            "winload.exe",
            "conhost.exe",
            "taskhostw.exe",
            "dwm.exe",
            "svchost.exe",
            "RuntimeBroker.exe"
        ]

        self.scan_percent = 0

        for file in files:

            if not self.running:
                return

            time.sleep(
                random.uniform(
                    0.12,
                    0.35
                )
            )

            self.log(
                f"[SCAN] C:\\Windows\\System32\\{file}"
            )

            self.scan_percent += random.randint(
                3,
                7
            )

            if self.scan_percent > 100:
                self.scan_percent = 100

            self.set_progress(
                self.scan_percent
            )

        self.log("")
        self.log(
            "[WARNING] INTEGRITY FAILURE",
            RED
        )

        self.beep(
            900,
            250
        )

        time.sleep(1)

    # ========================================================
    # FAKE CLEANUP
    # ========================================================

    def fake_cleanup(self):

        self.set_status(
            "SYSTEM32 CLEANUP SIMULATION"
        )

        self.log("")
        self.log(
            "BEGINNING CLEANUP...",
            RED
        )

        time.sleep(1)

        files = [
            "kernel32.dll",
            "ntdll.dll",
            "user32.dll",
            "winlogon.exe",
            "explorer.exe",
            "services.exe",
            "lsass.exe",
            "csrss.exe",
            "smss.exe",
            "ntoskrnl.exe"
        ]

        for file in files:

            if not self.running:
                return

            time.sleep(
                random.uniform(
                    0.2,
                    0.55
                )
            )

            self.log(
                f"[SIMULATION] Deleting {file}",
                RED
            )

        self.log("")
        self.log(
            "[SIMULATION] CLEANUP COMPLETE",
            RED
        )

        self.set_progress(100)

        time.sleep(2)

    # ========================================================
    # FIRST GLITCH
    # ========================================================

    def first_glitch(self):

        self.set_status(
            "UNEXPECTED CONDITION"
        )

        self.glitch = True

        for _ in range(35):

            if not self.running:
                return

            self.root.after(
                0,
                self.glitch_frame
            )

            time.sleep(
                random.uniform(
                    0.03,
                    0.12
                )
            )

        self.glitch = False

    def glitch_frame(self):

        if not self.running:
            return

        messages = [
            "SYSTEM FAILURE",
            "ACCESS DENIED",
            "PROCESS UNKNOWN",
            "DON'T CLOSE THIS",
            "WHO ARE YOU?",
            "I'M STILL HERE",
            "CONNECTION LOST",
            "CONNECTION RESTORED",
            "0x00000000",
            "YOU SHOULDN'T BE HERE"
        ]

        message = random.choice(
            messages
        )

        self.canvas.itemconfig(
            self.header,
            text=message,
            fill=random.choice(
                [
                    RED,
                    WHITE,
                    "#ff5555",
                    CYAN
                ]
            )
        )

        self.root.geometry(
            f"{random.randint(1100,1210)}x"
            f"{random.randint(650,730)}"
        )

    # ========================================================
    # CREEPY MESSAGES
    # ========================================================

    def creepy_messages(self):

        self.glitch = False

        messages = [
            "Why are you still watching?",
            "Something is wrong.",
            "The process did not terminate.",
            "I can see the window.",
            "You pressed ESC before.",
            "Don't do it again.",
            "There is something behind this screen.",
            "STOP.",
            "STOP.",
            "STOP.",
            "I'M STILL HERE.",
            "YOU CAN'T ESCAPE."
        ]

        self.log("")
        self.log(
            "UNKNOWN PROCESS DETECTED",
            RED
        )

        time.sleep(1)

        for message in messages:

            if not self.running:
                return

            self.root.after(
                0,
                self.show_center_message,
                message
            )

            self.beep(
                random.randint(300, 1000),
                random.randint(50, 150)
            )

            time.sleep(
                random.uniform(
                    0.5,
                    1.3
                )
            )

        self.root.after(
            0,
            self.clear_center_message
        )

    def show_center_message(self, text):

        self.canvas.delete(
            "creepy"
        )

        width = self.canvas.winfo_width()

        if width < 100:
            width = WIDTH

        self.canvas.create_text(
            width // 2,
            350,
            text=text,
            fill=random.choice(
                [
                    RED,
                    WHITE,
                    "#ff4444"
                ]
            ),
            font=(
                "Consolas",
                random.randint(20, 35),
                "bold"
            ),
            tags="creepy"
        )

    def clear_center_message(self):

        self.canvas.delete(
            "creepy"
        )

    # ========================================================
    # FAKE RESTART
    # ========================================================

    def fake_restart(self, number):

        self.restart_count = number

        self.root.after(
            0,
            self.create_restart_screen,
            number
        )

        time.sleep(4)

    def create_restart_screen(self, number):

        self.clear_all()

        self.restart_frame = tk.Frame(
            self.root,
            bg="#000000"
        )

        self.restart_frame.pack(
            fill="both",
            expand=True
        )

        if number == 1:

            text = "Restarting system..."

        elif number == 2:

            text = "CRITICAL FAILURE\nRestarting..."

        else:

            text = "SYSTEM RECOVERY FAILED"

        self.restart_label = tk.Label(
            self.restart_frame,
            text=text,
            bg="#000000",
            fg="#dddddd",
            font=("Segoe UI", 23)
        )

        self.restart_label.place(
            relx=0.5,
            rely=0.43,
            anchor="center"
        )

        self.restart_percent = tk.Label(
            self.restart_frame,
            text="0%",
            bg="#000000",
            fg="#777777",
            font=("Segoe UI", 11)
        )

        self.restart_percent.place(
            relx=0.5,
            rely=0.52,
            anchor="center"
        )

        self.root.after(
            300,
            lambda: self.restart_animation(
                0,
                number
            )
        )

    def restart_animation(
        self,
        value,
        number
    ):

        if not self.running:
            return

        if value >= 100:

            self.root.after(
                500,
                self.finish_restart
            )

            return

        self.restart_percent.config(
            text=f"{value}%"
        )

        increment = random.randint(
            2,
            8
        )

        self.root.after(
            random.randint(40, 120),
            lambda: self.restart_animation(
                min(100, value + increment),
                number
            )
        )

    def finish_restart(self):

        if hasattr(
            self,
            "restart_frame"
        ):
            self.restart_frame.destroy()

    # ========================================================
    # SECOND PHASE
    # ========================================================

    def second_phase(self):

        self.build_main_gui()

        self.set_status(
            "RECOVERY MODE"
        )

        self.log(
            "SYSTEM RECOVERY STARTED..."
        )

        time.sleep(1)

        self.log(
            "[ERROR] Boot configuration unavailable",
            RED
        )

        time.sleep(1)

        self.log(
            "[ERROR] Kernel response unavailable",
            RED
        )

        time.sleep(1)

        self.log(
            "[UNKNOWN] Process returned..."
        )

        time.sleep(1)

        self.glitch = True

        for _ in range(20):

            if not self.running:
                return

            self.root.after(
                0,
                self.glitch_frame
            )

            time.sleep(
                0.08
            )

        self.glitch = False

        self.root.after(
            0,
            self.show_center_message,
            "DID YOU REALLY THINK IT RESTARTED?"
        )

        time.sleep(2)

        self.root.after(
            0,
            self.clear_center_message
        )

    # ========================================================
    # THIRD PHASE
    # ========================================================

    def third_phase(self):

        self.build_main_gui()

        self.set_status(
            "UNKNOWN SESSION"
        )

        creepy = [
            "[00:00:01] session opened",
            "[00:00:03] user detected",
            "[00:00:05] screen detected",
            "[00:00:08] process detected",
            "[00:00:13] observer detected",
            "",
            "WHO IS WATCHING?",
            "",
            "YOU",
            "",
            "NO",
            "",
            "NOT YOU."
        ]

        for line in creepy:

            if not self.running:
                return

            self.log(
                line,
                RED if "WATCH" in line or
                line == "NOT YOU." else None
            )

            time.sleep(
                random.uniform(
                    0.4,
                    1.0
                )
            )

        self.glitch = True

        for _ in range(30):

            if not self.running:
                return

            self.root.after(
                0,
                self.glitch_frame
            )

            time.sleep(
                0.06
            )

        self.glitch = False

        self.root.after(
            0,
            self.show_center_message,
            "YOU CAN'T ESCAPE"
        )

        self.beep(
            1000,
            500
        )

        time.sleep(2)

    # ========================================================
    # FINAL REVEAL
    # ========================================================

    def final_reveal(self):

        self.clear_all()

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
            text="",
            bg="#000000",
            fg=RED,
            font=("Consolas", 38, "bold")
        )

        title.place(
            relx=0.5,
            rely=0.35,
            anchor="center"
        )

        message = tk.Label(
            frame,
            text="",
            bg="#000000",
            fg="#bbbbbb",
            font=("Consolas", 14),
            justify="center"
        )

        message.place(
            relx=0.5,
            rely=0.52,
            anchor="center"
        )

        self.root.after(
            1500,
            lambda: title.config(
                text="SYSTEM RESTORED"
            )
        )

        self.root.after(
            3000,
            lambda: message.config(
                text=(
                    "Everything you saw was fake.\n\n"
                    "System32 was NOT deleted.\n"
                    "Windows was NOT modified.\n"
                    "No Trust Wallet access occurred.\n"
                    "No network connection was made.\n\n"
                    "This was only a creepypasta simulation.\n\n"
                    "CREEPYv2.exe\n"
                    "Created by mazdakproninja"
                )
            )
        )

    # ========================================================
    # LOGGING
    # ========================================================

    def log(
        self,
        text,
        color=None
    ):

        if not self.running:
            return

        def write():

            try:

                self.terminal.config(
                    state="normal"
                )

                if color:

                    tag = (
                        "tag_" +
                        color.replace(
                            "#",
                            ""
                        )
                    )

                    self.terminal.tag_config(
                        tag,
                        foreground=color
                    )

                    self.terminal.insert(
                        "end",
                        text + "\n",
                        tag
                    )

                else:

                    self.terminal.insert(
                        "end",
                        text + "\n"
                    )

                self.terminal.see(
                    "end"
                )

                self.terminal.config(
                    state="disabled"
                )