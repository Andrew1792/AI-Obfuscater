import pyautogui
import re
from time import sleep
from src.typer import TypingConfig, write_word, handle_whitespace


if __name__ == "__main__":
    pyautogui.PAUSE = 0
    
    try:
        typer_config = TypingConfig(wpm=100, wpm_variance=20, letter_error_rate=0.03, word_error_rate=0.03, pause_chance=0.3)
        
        print("Starting typing simulation in 5 seconds... Switch to your text editor!")
        sleep(5)

        with open('./AI.txt', 'r', encoding='utf-8') as text_file:
            content = text_file.read()
            tokens = re.split(r'(\s+)', content)

            for token in tokens:
                if not token:
                    continue
                if token.isspace(): 
                    handle_whitespace(token)
                else: 
                    write_word(token, typer_config)
        
        print("\nTyping simulation finished.")

    except FileNotFoundError:
        print("Error: The file 'AI.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
