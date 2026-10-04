"""
MazdakOS Fun Toolbox
CLI Launcher
"""

from pathlib import Path
import subprocess
import sys

from .config import (
    APPS_DIR,
    PRANKS_DIR,
    TOOLS_DIR,
    PROJECT_NAME,
    VERSION,
    IGNORED_DIRECTORIES,
)


class ToolboxLauncher:

    def __init__(self):
        self.categories = {
            "apps": APPS_DIR,
            "pranks": PRANKS_DIR,
            "tools": TOOLS_DIR,
        }

    def is_ignored(self, path: Path) -> bool:
        return any(
            part in IGNORED_DIRECTORIES
            for part in path.parts
        )

    def list_category(self, category: str) -> list[Path]:

        directory = self.categories.get(category)

        if directory is None or not directory.exists():
            return []

        programs = []

        for file in directory.rglob("*.py"):

            if file.name == "__init__.py":
                continue

            if self.is_ignored(file):
                continue

            programs.append(file)

        return sorted(programs)

    def run(self, file_path: Path):

        if not file_path.exists():
            print(f"[ERROR] File not found: {file_path}")
            return

        try:
            subprocess.run(
                [
                    sys.executable,
                    str(file_path),
                ],
                cwd=file_path.parent,
                check=False,
            )

        except KeyboardInterrupt:
            print("\n[INFO] Program stopped.")

        except Exception as error:
            print(f"[ERROR] {error}")

    def interactive(self):

        while True:

            print()
            print("╔══════════════════════════════════════╗")
            print(f"║ {PROJECT_NAME:^36} ║")
            print(f"║ {VERSION:^36} ║")
            print("╚══════════════════════════════════════╝")

            print()
            print("[1] Apps")
            print("[2] Pranks")
            print("[3] Tools")
            print("[0] Exit")

            choice = input("\nSelect: ").strip()

            category_map = {
                "1": "apps",
                "2": "pranks",
                "3": "tools",
            }

            if choice == "0":
                break

            category = category_map.get(choice)

            if category is None:
                print("[ERROR] Invalid option.")
                continue

            programs = self.list_category(category)

            if not programs:
                print("\nNo programs found.")
                continue

            print()

            for index, program in enumerate(programs, 1):

                relative = program.relative_to(
                    self.categories[category]
                )

                print(f"[{index}] {relative}")

            print("[0] Back")

            selected = input("\nSelect: ").strip()

            if selected == "0":
                continue

            try:

                index = int(selected) - 1

                if not 0 <= index < len(programs):
                    raise ValueError

                self.run(programs[index])

            except ValueError:
                print("[ERROR] Invalid selection.")


def main():

    launcher = ToolboxLauncher()
    launcher.interactive()


if __name__ == "__main__":
    main()