# Development Guide

This document explains the development structure, setup, and workflow for **MazdakOS-Fun-Toolbox**.

## 📁 Project Structure

```text
MazdakOS-Fun-Toolbox/
│
├── apps/
│   ├── gacha/
│   ├── memes/
│   └── sonic/
│
├── core/
│   ├── config.py
│   ├── gui.py
│   └── launcher.py
│
├── docs/
│   └── development.md
│
├── pranks/
│   └── CREEPY/
│
├── tools/
│   └── telegram/
│
├── main.py
├── build.bat
├── requirements.txt
├── README.md
└── LICENSE
```

## 🛠️ Requirements

Recommended environment:

* Windows 10/11
* Python 3.10+
* Git
* PyInstaller

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Toolbox

Run the main application:

```bash
python main.py
```

The launcher automatically scans supported project directories and displays available tools and applications.

## 🧩 Adding a New Application

To add a new application, create a folder inside `apps/`.

Example:

```text
apps/
└── my_app/
    └── my_app.py
```

The launcher can detect Python applications placed inside the supported directories.

## 👻 Adding Pranks

Prank projects should be placed inside:

```text
pranks/
```

For example:

```text
pranks/
└── CREEPY/
    ├── CREEPY.py
    ├── CREEPYv2.py
    └── CREEPYv3.py
```

Pranks should be designed as harmless local experiences and should not damage files, operating-system components, or user data.

## 🔧 Core System

The `core/` directory contains the main toolbox infrastructure.

### `config.py`

Contains configuration values used by the toolbox.

### `gui.py`

Contains the graphical user interface.

### `launcher.py`

Handles discovering and launching supported applications and tools.

## 🏗️ Building the Executable

The project includes a Windows build script:

```bat
build.bat
```

The build process uses **PyInstaller** to create the executable.

You can also run PyInstaller manually when needed:

```bash
python -m PyInstaller
```

Generated build files should remain outside version control.

## 🌿 Git Workflow

Before making changes:

```bash
git pull origin main
```

After modifying the project:

```bash
git status
git add .
git commit -m "Describe your changes"
git push
```

Use clear commit messages whenever possible.

Examples:

```text
Add new Sonic application
Improve toolbox GUI
Fix application launcher
Update documentation
```

## 🧪 Testing

Before pushing changes, make sure that:

1. The toolbox starts correctly.
2. The GUI opens without errors.
3. Applications launch correctly.
4. Required Python dependencies are installed.
5. New files are placed in the correct directory.
6. No unnecessary build files or generated files are committed.

## 📦 Dependencies

Project dependencies are listed in:

```text
requirements.txt
```

When adding a new third-party Python package, update `requirements.txt` so other developers can reproduce the environment.

## 🚀 Development Philosophy

MazdakOS-Fun-Toolbox is intended to be a modular collection of small applications, experiments, tools, and harmless prank projects.

The project prioritizes:

* Modularity
* Simple development
* Experimentation
* Python development
* GUI applications
* Fun projects
* Easy expansion

New projects should be kept as independent as possible so they can be added or removed without breaking the core toolbox.

## ⚠️ Safety

Only include software that you are authorized to run and distribute.

Projects intended to simulate malware or destructive behavior should remain harmless and should never intentionally delete, corrupt, encrypt, or damage user data or operating-system components.

## 📚 Contributing

If you want to experiment with the project:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes locally.
5. Commit your work.
6. Open a Pull Request.

Example:

```bash
git checkout -b feature/my-new-tool
```

Then:

```bash
git add .
git commit -m "Add my new tool"
git push -u origin feature/my-new-tool
```

---

**MazdakOS-Fun-Toolbox**
Built for experimentation, programming, and fun. 💻🔥
