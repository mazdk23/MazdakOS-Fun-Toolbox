"""
MazdakOS Fun Toolbox
Graphical User Interface
"""

from pathlib import Path
import shutil
import subprocess
import sys

import customtkinter as ctk


PROJECT_NAME = "MazdakOS Fun Toolbox"
VERSION = "0.1.0"


IGNORED_DIRECTORIES = {
    "__pycache__",
    "build",
    "dist",
    ".git",
    ".venv",
    "venv",
}


class ToolboxGUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        # =====================================================
        # FIND TOOLBOX ROOT
        # =====================================================

        if getattr(sys, "frozen", False):
            self.root_dir = Path(sys.executable).resolve().parent
        else:
            self.root_dir = Path(__file__).resolve().parent.parent

        print("=" * 60)
        print("MAZDAKOS TOOLBOX")
        print(f"Frozen: {getattr(sys, 'frozen', False)}")
        print(f"Executable: {sys.executable}")
        print(f"ROOT: {self.root_dir}")
        print("=" * 60)

        # =====================================================
        # DIRECTORIES
        # =====================================================

        self.categories = {
            "Apps": self.root_dir / "apps",
            "Pranks": self.root_dir / "pranks",
            "Tools": self.root_dir / "tools",
        }

        # =====================================================
        # WINDOW
        # =====================================================

        self.title(
            f"{PROJECT_NAME} v{VERSION}"
        )

        self.geometry("1100x700")
        self.minsize(900, 600)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.current_category = "Apps"

        self.create_interface()

        self.show_category("Apps")

    # =========================================================
    # GUI
    # =========================================================

    def create_interface(self):

        self.header = ctk.CTkFrame(
            self,
            height=75,
            corner_radius=0,
        )

        self.header.pack(
            fill="x"
        )

        self.logo = ctk.CTkLabel(
            self.header,
            text="MAZDAKOS",
            font=ctk.CTkFont(
                size=25,
                weight="bold",
            ),
        )

        self.logo.pack(
            side="left",
            padx=25,
            pady=20,
        )

        self.version = ctk.CTkLabel(
            self.header,
            text=f"FUN TOOLBOX  •  v{VERSION}",
            text_color="#777777",
        )

        self.version.pack(
            side="left"
        )

        self.settings_button = ctk.CTkButton(
            self.header,
            text="⚙",
            width=45,
            command=self.open_settings,
        )

        self.settings_button.pack(
            side="right",
            padx=20,
        )

        # =====================================================
        # MAIN
        # =====================================================

        self.main = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )

        self.main.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20,
        )

        # =====================================================
        # SIDEBAR
        # =====================================================

        self.sidebar = ctk.CTkFrame(
            self.main,
            width=180,
        )

        self.sidebar.pack(
            side="left",
            fill="y",
            padx=(0, 20),
        )

        self.sidebar.pack_propagate(False)

        category_label = ctk.CTkLabel(
            self.sidebar,
            text="CATEGORY",
            text_color="#777777",
            font=ctk.CTkFont(
                size=12,
                weight="bold",
            ),
        )

        category_label.pack(
            pady=(25, 15),
        )

        self.category_buttons = {}

        for category in self.categories:

            button = ctk.CTkButton(
                self.sidebar,
                text=category,
                height=45,
                anchor="w",
                fg_color="transparent",
                command=lambda c=category: self.show_category(c),
            )

            button.pack(
                fill="x",
                padx=15,
                pady=5,
            )

            self.category_buttons[category] = button

        # =====================================================
        # CONTENT
        # =====================================================

        self.content = ctk.CTkFrame(
            self.main
        )

        self.content.pack(
            side="left",
            fill="both",
            expand=True,
        )

        self.title_label = ctk.CTkLabel(
            self.content,
            text="Apps",
            font=ctk.CTkFont(
                size=28,
                weight="bold",
            ),
        )

        self.title_label.pack(
            anchor="w",
            padx=30,
            pady=(25, 5),
        )

        self.subtitle = ctk.CTkLabel(
            self.content,
            text="Select a program to launch.",
            text_color="#777777",
        )

        self.subtitle.pack(
            anchor="w",
            padx=30,
            pady=(0, 20),
        )

        self.program_list = ctk.CTkScrollableFrame(
            self.content
        )

        self.program_list.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20),
        )

    # =========================================================
    # SCAN PROGRAMS
    # =========================================================

    def get_programs(self, category):

        directory = self.categories[category]

        print()
        print("=" * 60)
        print(f"SCANNING: {category}")
        print(f"PATH: {directory}")
        print(f"EXISTS: {directory.exists()}")
        print("=" * 60)

        if not directory.exists():

            print("DIRECTORY DOES NOT EXIST!")

            return []

        programs = []

        for file in directory.rglob("*"):

            # -------------------------------------------------
            # Only Python files
            # -------------------------------------------------

            if not file.is_file():
                continue

            if file.suffix.lower() != ".py":
                continue

            # -------------------------------------------------
            # Ignore __init__.py
            # -------------------------------------------------

            if file.name == "__init__.py":
                continue

            # -------------------------------------------------
            # Ignore build/dist/cache directories
            # -------------------------------------------------

            relative_parts = file.relative_to(
                directory
            ).parts

            if any(
                part in IGNORED_DIRECTORIES
                for part in relative_parts
            ):
                continue

            programs.append(file)

            print(
                f"FOUND: {file}"
            )

        print()
        print(
            f"TOTAL PROGRAMS: {len(programs)}"
        )
        print("=" * 60)

        return sorted(programs)

    # =========================================================
    # SHOW CATEGORY
    # =========================================================

    def show_category(self, category):

        self.current_category = category

        self.title_label.configure(
            text=category
        )

        # -----------------------------------------------------

        for name, button in self.category_buttons.items():

            if name == category:

                button.configure(
                    fg_color="#1f6aa5"
                )

            else:

                button.configure(
                    fg_color="transparent"
                )

        # -----------------------------------------------------
        # Clear list
        # -----------------------------------------------------

        for widget in self.program_list.winfo_children():

            widget.destroy()

        # -----------------------------------------------------

        programs = self.get_programs(
            category
        )

        # -----------------------------------------------------

        if not programs:

            empty = ctk.CTkLabel(
                self.program_list,
                text="No programs found.",
                text_color="#777777",
                font=ctk.CTkFont(
                    size=16
                ),
            )

            empty.pack(
                pady=80
            )

            return

        # -----------------------------------------------------

        for program in programs:

            self.create_card(
                program
            )

    # =========================================================
    # PROGRAM CARD
    # =========================================================

    def create_card(self, program: Path):

        card = ctk.CTkFrame(
            self.program_list,
            height=105,
        )

        card.pack(
            fill="x",
            padx=5,
            pady=7,
        )

        card.pack_propagate(False)

        # -----------------------------------------------------

        name = (
            program.stem
            .replace("_", " ")
            .replace("-", " ")
            .title()
        )

        name_label = ctk.CTkLabel(
            card,
            text=name,
            font=ctk.CTkFont(
                size=17,
                weight="bold",
            ),
        )

        name_label.pack(
            side="left",
            padx=20,
        )

        # -----------------------------------------------------

        folder_label = ctk.CTkLabel(
            card,
            text=program.parent.name,
            text_color="#777777",
        )

        folder_label.pack(
            side="left"
        )

        # -----------------------------------------------------

        launch = ctk.CTkButton(
            card,
            text="LAUNCH",
            width=110,
            command=lambda p=program: self.launch_program(p),
        )

        launch.pack(
            side="right",
            padx=20,
        )

    # =========================================================
    # LAUNCH
    # =========================================================

    def launch_program(self, program: Path):

        if not program.exists():

            self.show_error(
                "Program not found."
            )

            return

        try:

            # =================================================
            # RUNNING FROM PYTHON
            # =================================================

            if not getattr(
                sys,
                "frozen",
                False,
            ):

                subprocess.Popen(
                    [
                        sys.executable,
                        str(program),
                    ],
                    cwd=program.parent,
                )

                return

            # =================================================
            # RUNNING FROM EXE
            # =================================================

            python_executable = shutil.which(
                "python"
            )

            if not python_executable:

                python_executable = shutil.which(
                    "py"
                )

            if not python_executable:

                self.show_error(
                    "Python was not found.\n\n"
                    "Python is required to launch .py programs."
                )

                return

            subprocess.Popen(
                [
                    python_executable,
                    str(program),
                ],
                cwd=program.parent,
            )

        except Exception as error:

            self.show_error(
                f"Could not launch program:\n\n{error}"
            )

    # =========================================================
    # SETTINGS
    # =========================================================

    def open_settings(self):

        window = ctk.CTkToplevel(
            self
        )

        window.title(
            "Settings"
        )

        window.geometry(
            "400x300"
        )

        window.transient(
            self
        )

        title = ctk.CTkLabel(
            window,
            text="Toolbox Settings",
            font=ctk.CTkFont(
                size=22,
                weight="bold",
            ),
        )

        title.pack(
            pady=30
        )

        theme = ctk.CTkOptionMenu(
            window,
            values=[
                "Dark",
                "Light",
                "System",
            ],
            command=self.change_theme,
        )

        theme.set(
            "Dark"
        )

        theme.pack(
            pady=15
        )

    # =========================================================
    # THEME
    # =========================================================

    def change_theme(self, value):

        ctk.set_appearance_mode(
            value.lower()
        )

    # =========================================================
    # ERROR
    # =========================================================

    def show_error(self, message):

        dialog = ctk.CTkToplevel(
            self
        )

        dialog.title(
            "Error"
        )

        dialog.geometry(
            "450x220"
        )

        dialog.transient(
            self
        )

        label = ctk.CTkLabel(
            dialog,
            text=message,
            wraplength=380,
            justify="center",
        )

        label.pack(
            expand=True,
            padx=20,
        )

        button = ctk.CTkButton(
            dialog,
            text="OK",
            command=dialog.destroy,
        )

        button.pack(
            pady=20
        )


# =============================================================
# MAIN
# =============================================================

def main():

    app = ToolboxGUI()

    app.mainloop()


if __name__ == "__main__":

    main()