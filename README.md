<!-- cyber quest
tomorrow will full for whole 
where is my 3rd commit ? 
I wanna know ... --> 

# ⚡️ CyberQuest 2077: Neo-City Escape

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen)
![License](https://img.shields.io/badge/license-MIT-orange)

A terminal-based cyberpunk RPG featuring a typewriter CLI effect, ANSI color coding, turn-based encounters, cyberware trading, procedural exploration events, and persistent JSON save slots.

---

## 📸 Key Features
- **Zero Dependencies**: Built strictly on Python's standard library (`random`, `json`, `os`, `sys`, `time`). Runs out of the box with `0` external `pip` packages.
- **Dynamic CLI UI**: Smooth typewriter text effect paired with non-flickering ANSI color accents.
- **Turn-Based Combat System**: Fight random rogue AI, hunter drones, and scavengers with variable damage calculations and drop rates.
- **Shop & Inventory**: Purchase health pods and upgrade cyber-implants at the local Cyber-Bar.
- **Persistent Save System**: Automatic state serialization to `save_game.json`.

---

## 📁 Project Structure

```text
cyber_quest/
│── src/
│   ├── __init__.py    # Package initializer
│   ├── utils.py       # Typewriter effect, ANSI styling, terminal cleanup
│   ├── player.py      # Player state, inventory, and JSON serialization
│   └── game.py        # Core game engine, combat, shop, and state management
│── main.py            # Application entry point
└── README.md          # Documentation
