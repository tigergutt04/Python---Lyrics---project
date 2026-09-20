# Python---Lyrics---project

A small Python project that displays song lyrics as moving text windows across the screen.

The project is built using **Python** and **PyQt6** and is currently under development.

## Idea

The goal is to read lyrics from a JSON file and display each part of the lyrics in its own moving window.

Each lyric window moves vertically across the screen. New lyric windows are created over time using Qt timers, allowing multiple parts of the lyrics to appear on the screen simultaneously.

## Project Structure

```text
LyricsProject/
├── main.py
├── LyricReader.py
├── MovingTextbox.py
├── lyric.json
└── README.md
```

### `main.py`

Controls the application and connects the different parts of the project.

### `LyricReader.py`

Reads the lyrics from `lyric.json` and returns them to the main program.

### `MovingTextbox.py`

Handles the movement of the lyric windows across the screen.

### `lyric.json`

Contains the lyrics used by the program.

## Requirements

- Python 3
- PyQt6

Install PyQt6 with:

```bash
python -m pip install PyQt6
```

## Running the Project

Run the application from the project directory:

```bash
python main.py
```

## Current Development

The project currently focuses on:

- Reading lyrics from JSON
- Creating lyric windows with `QWidget` and `QLabel`
- Moving windows across the screen
- Using `QTimer` to control timing
- Displaying multiple lyric sections independently

## Planned Features

- Synchronization between lyrics and timing
- Multiple moving lyric windows
- Improved window styling
- Transparent/background-free lyric windows
- Configurable movement speed and positioning
- Song-specific lyric timing