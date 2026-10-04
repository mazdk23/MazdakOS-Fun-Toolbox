# CREEPYv4

> A normal game that slowly stops being normal.

CREEPYv4 is an original retro psychological horror game built with Python
and Pygame.

It begins as a colorful, harmless high-speed platformer with a Gacha
system.

Then something starts going wrong.

The game gradually changes through four stages:

NORMAL → STRANGE → CORRUPTION → NIGHTMARE

The player is never immediately told what is happening.

---

## 🎮 Features

- Original retro platforming
- High-speed movement
- Original characters and enemies
- Collectibles and checkpoints
- In-game Gacha system
- Dynamic corruption system
- Psychological horror events
- CRT / VHS / glitch effects
- Environmental storytelling
- Hidden secrets
- Multiple endings
- Local JSON save system
- Configurable graphics and audio settings
- Windows executable support

---

## 🧠 The Corruption System

CREEPYv4 uses a dynamic corruption system ranging from 0 to 100.

| Level | State |
|---:|---|
| 0–20 | NORMAL |
| 20–40 | STRANGE |
| 40–60 | CORRUPTION |
| 60–80 | HORROR |
| 80–100 | NIGHTMARE |

The higher the corruption level becomes, the more the world begins to
change.

---

## 🎰 Gacha

The game contains a fictional in-game Gacha system.

Possible rarities:

- COMMON
- RARE
- EPIC
- LEGENDARY
- UNKNOWN

The UNKNOWN category is intentionally different from normal rewards.

Some rewards may become relevant to the story later.

There are no real-money purchases.

---

## 👁️ Horror

CREEPYv4 focuses on psychological horror rather than relying exclusively
on jumpscares.

The game uses:

- Glitches
- Distorted audio
- Strange NPC behavior
- Environmental changes
- Corrupted UI
- Fake errors
- Unexpected events
- Visual distortion
- Hidden messages
- Unexplained entities

The goal is to make the player slowly question whether the game is
supposed to behave this way.

---

## 🔐 Endings

CREEPYv4 contains multiple endings:

- ENDING 01 — ESCAPE
- ENDING 02 — CORRUPTION
- ENDING 03 — UNKNOWN

Ending progression depends on player actions, discoveries, corruption,
and Gacha discoveries.

---

## 🗂️ Project Structure

```text
CREEPYv4/
├── main.py
├── requirements.txt
├── README.md
├── build.bat
├── .gitignore
│
├── game/
│   ├── engine.py
│   ├── player.py
│   ├── world.py
│   ├── level.py
│   ├── entities.py
│   ├── gacha.py
│   ├── horror.py
│   ├── events.py
│   ├── corruption.py
│   ├── save.py
│   ├── settings.py
│   ├── audio.py
│   ├── graphics.py
│   └── endings.py
│
├── scenes/
│   ├── menu.py
│   ├── intro.py
│   ├── normal.py
│   ├── strange.py
│   ├── corrupted.py
│   └── nightmare.py
│
├── assets/
├── data/
└── saves/



🛠️ Requirements
Python 3
Pygame
PyInstaller (for building the Windows executable)

Install dependencies:

pip install -r requirements.txt

Run:

python main.py
🪟 Building for Windows

Run:

build.bat

The compiled game will be generated in:

dist/CREEPYv4.exe
⚠️ Safety

CREEPYv4 does not:

Delete system files
Modify System32
Modify the Windows registry
Disable antivirus software
Execute arbitrary system commands
Encrypt user files
Access unrelated user data

Any apparent system errors, corruption, or destructive behavior shown by
the game are purely simulated visual effects.

🎨 Original Content

CREEPYv4 does not use Sonic characters, sprites, music, sounds, logos,
levels, or other copyrighted assets.

All game characters, environments, sounds, UI elements, and horror
elements are original or procedurally generated.

👨‍💻 Developer

mazdakproninja

CREEPYv4 — Version 4.0

A normal game that slowly stops being normal.