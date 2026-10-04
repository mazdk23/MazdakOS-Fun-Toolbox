import ctypes
import random
import time
import threading
import tkinter as tk
from tkinter import messagebox

# ============================================================
# CREEPY v3
# Win32 Horror / Glitch Simulation
#
# SAFE SIMULATION
# ------------------------------------------------------------
# No:
#   - System32 deletion
#   - File deletion
#   - Registry modification
#   - Process termination
#   - Network access
#   - Persistence
#   - Administrator elevation
#
# Win32 APIs are used only for temporary visual effects.
# ============================================================


# ============================================================
# WINDOWS API
# ============================================================

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
kernel32 = ctypes.windll.kernel32

SM_CXSCREEN = 0
SM_CYSCREEN = 1

SRCCOPY = 0x00CC0020
SRCINVERT = 0x00660046


SCREEN_W = user32.GetSystemMetrics(SM_CXSCREEN)
SCREEN_H = user32.GetSystemMetrics(SM_CYSCREEN)


# ============================================================
# UTILITY
# ============================================================

def safe_sleep(seconds):
    time.sleep(seconds)


# ============================================================
# WIN32 SCREEN GLITCH ENGINE
# ============================================================

class ScreenGlitch:

    def __init__(self):
        self.running = False
        self.stop_requested = False

    # --------------------------------------------------------
    # Get desktop device context
    # --------------------------------------------------------

    def get_dc(self):
        return user32.GetDC(0)

    # --------------------------------------------------------
    # Release desktop device context
    # --------------------------------------------------------

    def release_dc(self, dc):
        if dc:
            user32.ReleaseDC(0, dc)

    # --------------------------------------------------------
    # Shift part of screen
    # --------------------------------------------------------

    def shift_region(
        self,
        x,
        y,
        width,
        height,
        dx,
        dy=0
    ):

        if width <= 0 or height <= 0:
            return

        dc = self.get_dc()

        if not dc:
            return

        mem_dc = None
        bitmap = None
        old_bitmap = None

        try:

            mem_dc = gdi32.CreateCompatibleDC(dc)

            if not mem_dc:
                return

            bitmap = gdi32.CreateCompatibleBitmap(
                dc,
                width,
                height
            )

            if not bitmap:
                return

            old_bitmap = gdi32.SelectObject(
                mem_dc,
                bitmap
            )

            # Capture screen section
            gdi32.BitBlt(
                mem_dc,
                0,
                0,
                width,
                height,
                dc,
                x,
                y,
                SRCCOPY
            )

            # Move captured section
            gdi32.BitBlt(
                dc,
                x + dx,
                y + dy,
                width,
                height,
                mem_dc,
                0,
                0,
                SRCCOPY
            )

        except Exception:
            pass

        finally:

            try:
                if old_bitmap and mem_dc:
                    gdi32.SelectObject(
                        mem_dc,
                        old_bitmap
                    )
            except Exception:
                pass

            try:
                if bitmap:
                    gdi32.DeleteObject(
                        bitmap
                    )
            except Exception:
                pass

            try:
                if mem_dc:
                    gdi32.DeleteDC(
                        mem_dc
                    )
            except Exception:
                pass

            self.release_dc(dc)

    # --------------------------------------------------------
    # Random horizontal tear
    # --------------------------------------------------------

    def horizontal_tear(self):

        for _ in range(
            random.randint(2, 8)
        ):

            if self.stop_requested:
                return

            y = random.randint(
                0,
                max(0, SCREEN_H - 5)
            )

            height = random.randint(
                2,
                min(25, SCREEN_H)
            )

            dx = random.randint(
                -120,
                120
            )

            self.shift_region(
                0,
                y,
                SCREEN_W,
                height,
                dx
            )

    # --------------------------------------------------------
    # Small corruption blocks
    # --------------------------------------------------------

    def block_glitch(self):

        for _ in range(
            random.randint(2, 10)
        ):

            if self.stop_requested:
                return

            x = random.randint(
                0,
                max(0, SCREEN_W - 300)
            )

            y = random.randint(
                0,
                max(0, SCREEN_H - 100)
            )

            width = random.randint(
                50,
                min(600, SCREEN_W)
            )

            height = random.randint(
                3,
                min(60, SCREEN_H)
            )

            dx = random.randint(
                -100,
                100
            )

            self.shift_region(
                x,
                y,
                width,
                height,
                dx
            )

    # --------------------------------------------------------
    # Full-width scan distortion
    # --------------------------------------------------------

    def scan_distortion(self):

        for _ in range(
            random.randint(1, 5)
        ):

            if self.stop_requested:
                return

            y = random.randint(
                0,
                max(0, SCREEN_H - 10)
            )

            height = random.randint(
                1,
                min(12, SCREEN_H)
            )

            self.shift_region(
                0,
                y,
                SCREEN_W,
                height,
                random.randint(-50, 50)
            )

    # --------------------------------------------------------
    # Invert random region
    # --------------------------------------------------------

    def invert_region(self):

        dc = self.get_dc()

        if not dc:
            return

        try:

            for _ in range(
                random.randint(1, 4)
            ):

                x = random.randint(
                    0,
                    max(0, SCREEN_W - 200)
                )

                y = random.randint(
                    0,
                    max(0, SCREEN_H - 100)
                )

                width = random.randint(
                    50,
                    min(500, SCREEN_W)
                )

                height = random.randint(
                    5,
                    min(80, SCREEN_H)
                )

                gdi32.BitBlt(
                    dc,
                    x,
                    y,
                    width,
                    height,
                    dc,
                    x,
                    y,
                    SRCINVERT
                )

        except Exception:
            pass

        finally:
            self.release_dc(dc)

    # --------------------------------------------------------
    # Random effect
    # --------------------------------------------------------

    def random_effect(self):

        effects = [
            self.horizontal_tear,
            self.block_glitch,
            self.scan_distortion,
            self.invert_region
        ]

        try:
            random.choice(effects)()
        except Exception:
            pass

    # --------------------------------------------------------
    # Run glitch engine
    # --------------------------------------------------------

    def run(self, duration=5):

        self.running = True
        self.stop_requested = False

        end_time = (
            time.time() + duration
        )

        while (
            time.time() < end_time
            and not self.stop_requested
        ):

            self.random_effect()

            time.sleep(
                random.uniform(
                    0.025,
                    0.12
                )
            )

        self.running = False

    # --------------------------------------------------------
    # Stop
    # --------------------------------------------------------

    def stop(self):

        self.stop_requested = True


# ============================================================
# FULLSCREEN HORROR OVERLAY
# ============================================================

class HorrorOverlay:

    def __init__(self):

        self.root = tk.Toplevel()

        self.root.overrideredirect(True)

        self.root.attributes(
            "-topmost",
            True
        )

        self.root.geometry(
            f"{SCREEN_W}x{SCREEN_H}+0+0"
        )

        self.root.configure(
            bg="black"
        )

        self.root.attributes(
            "-alpha",
            0.0
        )

        self.canvas = tk.Canvas(
            self.root,
            bg="black",
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )

        self.visible = False

    # --------------------------------------------------------
    # Show
    # --------------------------------------------------------

    def show(self, alpha=0.8):

        try:

            self.root.attributes(
                "-alpha",
                alpha
            )

            self.visible = True

            self.root.update()

        except Exception:
            pass

    # --------------------------------------------------------
    # Hide
    # --------------------------------------------------------

    def hide(self):

        try:

            self.root.attributes(
                "-alpha",
                0.0
            )

            self.canvas.delete(
                "all"
            )

            self.root.update()

            self.visible = False

        except Exception:
            pass

    # --------------------------------------------------------
    # Clear
    # --------------------------------------------------------

    def clear(self):

        self.canvas.delete(
            "all"
        )

    # --------------------------------------------------------
    # Flash
    # --------------------------------------------------------

    def flash(
        self,
        color="white",
        duration=0.06
    ):

        try:

            self.canvas.configure(
                bg=color
            )

            self.show(0.85)

            time.sleep(
                duration
            )

            self.hide()

        except Exception:
            pass

    # --------------------------------------------------------
    # Center text
    # --------------------------------------------------------

    def text(
        self,
        text,
        color="white",
        size=40
    ):

        self.clear()

        self.canvas.configure(
            bg="black"
        )

        self.canvas.create_text(
            SCREEN_W // 2,
            SCREEN_H // 2,
            text=text,
            fill=color,
            font=(
                "Consolas",
                size,
                "bold"
            )
        )

        self.show(
            0.85
        )

    # --------------------------------------------------------
    # RGB ghost text
    # --------------------------------------------------------

    def glitch_text(
        self,
        text,
        size=42
    ):

        self.clear()

        self.canvas.configure(
            bg="black"
        )

        x = SCREEN_W // 2
        y = SCREEN_H // 2

        font = (
            "Consolas",
            size,
            "bold"
        )

        # Red channel
        self.canvas.create_text(
            x - 7,
            y,
            text=text,
            fill="#ff0000",
            font=font
        )

        # Cyan channel
        self.canvas.create_text(
            x + 7,
            y,
            text=text,
            fill="#00ffff",
            font=font
        )

        # Main layer
        self.canvas.create_text(
            x,
            y,
            text=text,
            fill="#ffffff",
            font=font
        )

        self.show(
            0.85
        )

    # --------------------------------------------------------
    # Final screen
    # --------------------------------------------------------

    def final_screen(self):

        self.clear()

        self.canvas.configure(
            bg="black"
        )

        lines = [
            (
                "CREEPYv3",
                "#00ff66",
                32
            ),
            (
                "",
                "#aaaaaa",
                18
            ),
            (
                "SIMULATION COMPLETE",
                "#ffffff",
                22
            ),
            (
                "",
                "#aaaaaa",
                18
            ),
            (
                "No files were deleted.",
                "#888888",
                16
            ),
            (
                "No System32 files were modified.",
                "#888888",
                16
            ),
            (
                "No registry changes were made.",
                "#888888",
                16
            ),
            (
                "No processes were terminated.",
                "#888888",
                16
            ),
            (
                "No network connection was made.",
                "#888888",
                16
            ),
            (
                "",
                "#aaaaaa",
                16
            ),
            (
                "Everything you saw was simulated.",
                "#00ff66",
                18
            ),
        ]

        start_y = (
            SCREEN_H // 2
            - 180
        )

        for index, item in enumerate(
            lines
        ):

            text, color, size = item

            self.canvas.create_text(
                SCREEN_W // 2,
                start_y + index * 34,
                text=text,
                fill=color,
                font=(
                    "Consolas",
                    size,
                    "bold" if size >= 22 else "normal"
                )
            )

        self.show(
            0.92
        )


# ============================================================
# FAKE TERMINAL
# ============================================================

class FakeTerminal:

    def __init__(self):

        self.root = tk.Toplevel()

        self.root.title(
            "Administrator: C:\\Windows\\System32\\cmd.exe"
        )

        self.root.geometry(
            "900x540"
        )

        self.root.configure(
            bg="#050505"
        )

        self.root.attributes(
            "-topmost",
            True
        )

        self.text = tk.Text(
            self.root,
            bg="#050505",
            fg="#00ff66",
            insertbackground="#00ff66",
            font=(
                "Consolas",
                11
            ),
            borderwidth=0,
            highlightthickness=0
        )

        self.text.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.write(
            "Microsoft Windows [Version 10.0.26200]"
        )

        self.write(
            "(C) Microsoft Corporation."
        )

        self.write("")

    # --------------------------------------------------------
    # Write line
    # --------------------------------------------------------

    def write(self, text):

        try:

            self.text.insert(
                "end",
                text + "\n"
            )

            self.text.see(
                "end"
            )

            self.root.update()

        except Exception:
            pass

    # --------------------------------------------------------
    # Close
    # --------------------------------------------------------

    def close(self):

        try:
            self.root.destroy()
        except Exception:
            pass


# ============================================================
# MAIN CREEPY ENGINE
# ============================================================

class CreepyEngine:

    def __init__(self):

        self.glitch = ScreenGlitch()

        self.overlay = None

        self.terminal = None

        self.stopped = False

    # --------------------------------------------------------
    # Create overlay
    # --------------------------------------------------------

    def create_overlay(self):

        self.overlay = HorrorOverlay()

    # --------------------------------------------------------
    # Fake system scan
    # --------------------------------------------------------

    def scan_system(self):

        self.terminal = FakeTerminal()

        files = [
            "ntdll.dll",
            "kernel32.dll",
            "KernelBase.dll",
            "user32.dll",
            "gdi32.dll",
            "gdi32full.dll",
            "advapi32.dll",
            "combase.dll",
            "ole32.dll",
            "shell32.dll",
            "winlogon.exe",
            "explorer.exe",
            "dwm.exe",
            "csrss.exe",
            "services.exe",
            "lsass.exe",
            "wininit.exe",
            "smss.exe",
            "conhost.exe",
            "bootmgr",
        ]

        self.terminal.write(
            "[CREEPY] Starting diagnostic scan..."
        )

        self.terminal.write(
            "[CREEPY] Target: "
            "C:\\Windows\\System32"
        )

        self.terminal.write(
            "----------------------------------------"
        )

        time.sleep(
            0.8
        )

        for filename in files:

            if self.stopped:
                return

            self.terminal.write(
                "[SCAN] "
                f"C:\\Windows\\System32\\{filename}"
            )

            time.sleep(
                random.uniform(
                    0.08,
                    0.22
                )
            )

        self.terminal.write("")
        self.terminal.write(
            "[OK] Scan completed."
        )

        self.terminal.write(
            "[OK] No actual system files were touched."
        )

        time.sleep(
            1
        )

    # --------------------------------------------------------
    # Fake deletion phase
    # --------------------------------------------------------

    def fake_deletion(self):

        if not self.terminal:
            return

        fake_files = [
            "kernel32.dll",
            "user32.dll",
            "advapi32.dll",
            "explorer.exe",
            "dwm.exe",
            "winlogon.exe",
            "shell32.dll",
        ]

        self.terminal.write("")
        self.terminal.write(
            "[WARNING] Integrity mismatch."
        )

        time.sleep(
            0.5
        )

        for filename in fake_files:

            if self.stopped:
                return

            self.terminal.write(
                "[SIMULATION] "
                f"Deleting {filename}..."
            )

            time.sleep(
                random.uniform(
                    0.15,
                    0.35
                )
            )

        self.terminal.write("")
        self.terminal.write(
            "[SIMULATION] Operation complete."
        )

    # --------------------------------------------------------
    # Corruption phase
    # --------------------------------------------------------

    def corruption(self):

        if self.terminal:

            self.terminal.write("")
            self.terminal.write(
                "[ERROR] Explorer.exe response lost."
            )

            self.terminal.write(
                "[ERROR] Desktop rendering unstable."
            )

        # Close terminal after a moment
        time.sleep(
            1
        )

        if self.terminal:
            self.terminal.close()
            self.terminal = None

        # Real visual Win32 effects
        self.glitch.run(
            duration=5
        )

    # --------------------------------------------------------
    # Horror messages
    # --------------------------------------------------------

    def horror_sequence(self):

        messages = [
            (
                "SYSTEM ERROR",
                "#ff2020",
                42
            ),
            (
                "EXPLORER.EXE",
                "#ffffff",
                40
            ),
            (
                "WHO ARE YOU?",
                "#ff2020",
                46
            ),
            (
                "DON'T LOOK AWAY",
                "#ff2020",
                38
            ),
            (
                "I SEE YOU",
                "#ffffff",
                50
            ),
            (
                "STOP",
                "#ff0000",
                70
            ),
        ]

        for text, color, size in messages:

            if self.stopped:
                return

            self.overlay.glitch_text(
                text,
                size
            )

            self.glitch.run(
                duration=0.7
            )

            time.sleep(
                random.uniform(
                    0.2,
                    0.6
                )
            )

    # --------------------------------------------------------
    # Fake reboot
    # --------------------------------------------------------

    def fake_reboot(self):

        self.overlay.text(
            "RESTARTING...",
            "#ffffff",
            34
        )

        time.sleep(
            1.8
        )

        self.overlay.text(
            ":(",
            "#ff2020",
            80
        )

        time.sleep(
            1.2
        )

        self.overlay.text(
            "Your PC ran into a problem.",
            "#ffffff",
            26
        )

        time.sleep(
            1.5
        )

        self.overlay.text(
            "Collecting diagnostic information...",
            "#bbbbbb",
            16
        )

        time.sleep(
            1.5
        )

        self.overlay.text(
            "RECOVERY MODE",
            "#ffffff",
            38
        )

        time.sleep(
            2
        )

        self.overlay.hide()

    # --------------------------------------------------------
    # Second corruption
    # --------------------------------------------------------

    def second_corruption(self):

        self.overlay.glitch_text(
            "RECOVERY FAILED",
            38
        )

        time.sleep(
            1
        )

        self.glitch.run(
            duration=3
        )

        self.overlay.glitch_text(
            "KERNEL STATE UNKNOWN",
            32
        )

        time.sleep(
            1
        )

        self.glitch.run(
            duration=3
        )

    # --------------------------------------------------------
    # Final horror
    # --------------------------------------------------------

    def final_horror(self):

        messages = [
            "WHO IS WATCHING?",
            "NOT YOU.",
            "DON'T CLOSE THIS.",
            "I KNOW YOU ARE THERE.",
            "...",
        ]

        for message in messages:

            self.overlay.glitch_text(
                message,
                random.randint(
                    28,
                    48
                )
            )

            self.glitch.run(
                duration=0.7
            )

            time.sleep(
                0.25
            )

    # --------------------------------------------------------
    # Final reveal
    # --------------------------------------------------------

    def final_reveal(self):

        self.overlay.final_screen()

        time.sleep(
            5
        )

    # --------------------------------------------------------
    # Main sequence
    # --------------------------------------------------------

    def run(self):

        try:

            self.create_overlay()

            time.sleep(
                1
            )

            # Phase 1
            self.scan_system()

            time.sleep(
                1
            )

            # Phase 2
            self.fake_deletion()

            time.sleep(
                1
            )

            # Phase 3
            self.corruption()

            time.sleep(
                1
            )

            # Phase 4
            self.fake_reboot()

            time.sleep(
                1
            )

            # Phase 5
            self.second_corruption()

            time.sleep(
                1
            )

            # Phase 6
            self.horror_sequence()

            time.sleep(
                1
            )

            # Phase 7
            self.fake_reboot()

            time.sleep(
                1
            )

            # Phase 8
            self.final_horror()

            time.sleep(
                1
            )

            # Reveal
            self.final_reveal()

        except Exception as error:

            print(
                "[CREEPYv3 ERROR]",
                repr(error)
            )

        finally:

            self.cleanup()

    # --------------------------------------------------------
    # Cleanup
    # --------------------------------------------------------

    def cleanup(self):

        self.stopped = True

        try:
            self.glitch.stop()
        except Exception:
            pass

        try:
            if self.terminal:
                self.terminal.close()
        except Exception:
            pass


# ============================================================
# APPLICATION
# ============================================================

def main():

    root = tk.Tk()

    root.withdraw()

    # --------------------------------------------------------
    # Warning
    # --------------------------------------------------------

    answer = messagebox.askyesno(
        "CREEPYv3",
        "CREEPYv3 is a fictional Windows horror simulation.\n\n"
        "The program will display temporary visual "
        "glitches and fake system errors.\n\n"
        "It will NOT:\n"
        "• delete files\n"
        "• modify System32\n"
        "• modify the Registry\n"
        "• terminate processes\n"
        "• access the network\n"
        "• change Windows configuration\n\n"
        "Continue?"
    )

    if not answer:

        root.destroy()
        return

    root.destroy()

    # --------------------------------------------------------
    # Start engine
    # --------------------------------------------------------

    engine = CreepyEngine()

    try:

        engine.run()

    except KeyboardInterrupt:

        print(
            "CREEPYv3 interrupted."
        )

    except Exception as error:

        print(
            "Fatal error:",
            repr(error)
        )

    finally:

        try:
            engine.cleanup()
        except Exception:
            pass


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()