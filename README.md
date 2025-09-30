# AI Obfuscater

This Python script uses `pyautogui` to simulate a human typing the contents of a text file. It doesn't just type characters; it mimics a realistic typing rhythm, including variable speeds, "thinking" pauses between words, and typos with a delayed correction mechanism.

## Features

-   **Variable Typing Speed**: Configure a base Words Per Minute (WPM) and a variance range.
-   **Realistic Pauses**: Simulates longer "thinking" pauses between words to break up the monotony.
-   **Human-Like Typos**: Randomly makes mistakes and types a few more characters before noticing, backing up, and fixing the error.
-   **Preserves Formatting**: Accurately reproduces newlines, indentation, and multiple spaces from the source text file.
-   **Highly Configurable**: Easily adjust the typist's "personality" through the `TypingConfig` object.

## Setup and Installation

### Prerequisites

-   Python 3.6+

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```

2.  **Install Dependencies:**
    This project requires the `pyautogui` library. Install it using the provided `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create the Source Text File:**
    Create a file named `AI.txt` in the same directory as the script. Place any text you want the simulator to type inside this file.

## Usage

1.  Open your desired text editor, word processor, or any application with a text field.
2.  Run the script from your terminal:
    ```bash
    python MAIN.py
    ```
3.  The script will print a countdown message. You have **5 seconds** to switch focus to the text field where you want the typing to occur. The simulation will begin automatically.

## Configuration

All of the typist's behaviors are controlled by the `TypingConfig` object, which is created at the start of the script.

```python
# Configure the desired typing personality.
typer_config = TypingConfig(wpm=180, wpm_variance=20, error_rate=0.08, pause_chance=0.5)
```

You can change these parameters to create different typing styles:

| Parameter        | Description                                                                                             | Example Value |
| ---------------- | ------------------------------------------------------------------------------------------------------- | ------------- |
| `wpm`            | **Words Per Minute.** The base speed for the typist. Higher values result in faster typing of each word.  | `120`         |
| `wpm_variance`   | **Speed Variation.** The +/- range around the base `wpm` to make the speed of each word slightly different. | `15`          |
| `error_rate`     | **Typo Chance.** A float from `0.0` (never) to `1.0` (always) representing the chance to make a typo on any given character. | `0.05`        |
| `pause_chance`   | **"Thinking" Pause Chance.** The probability (`0.0` to `1.0`) of a longer, more significant pause occurring before typing a word. | `0.4`         |

### Example "Personalities"

-   **The Professional:** Fast, accurate, and consistent.
    ```python
    TypingConfig(wpm=150, wpm_variance=10, error_rate=0.01, pause_chance=0.1)
    ```

-   **The Deliberate Thinker:** Slow, thoughtful, but makes few mistakes.
    ```python
    TypingConfig(wpm=45, wpm_variance=5, error_rate=0.02, pause_chance=0.8)
    ```

-   **The Sloppy Rusher:** Very fast, but error-prone and erratic.
    ```python
    TypingConfig(wpm=200, wpm_variance=50, error_rate=0.15, pause_chance=0.2)
    ```
