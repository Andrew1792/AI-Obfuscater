from random import random, choice, uniform, randrange
from time import sleep
import pyautogui
import nltk
import os


class TypingConfig:
  def __init__(self, wpm: int, wpm_variance: int, letter_error_rate: float, word_error_rate: float, pause_chance: float):
    self.wpm = wpm
    self.wpm_variance = wpm_variance
    self.letter_error_rate = letter_error_rate
    self.word_error_rate = word_error_rate
    self.word_pause_chance = pause_chance

    min_wpm = self.wpm - self.wpm_variance
    max_wpm = self.wpm + self.wpm_variance
    
    min_word_time = 60 / max_wpm
    max_word_time = 60 / min_wpm
    self.word_time_range = (max(0, min_word_time), max_word_time)

    avg_sec_per_word = 60 / self.wpm
    
    self.word_pause_range = (avg_sec_per_word, avg_sec_per_word * 4)
    
    self.mistake_pause_range = (avg_sec_per_word * 0.4, avg_sec_per_word * 0.8)    # time before hitting backspace
    self.correction_pause_range = (avg_sec_per_word * 0.2, avg_sec_per_word * 0.4) # time before correcting error
    
    self.error_characters = (' ', '!', '"', '#', '$', '%', '&', "'", '(',
                              ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
                              '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
                              'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',)


def ensure_nltk_data():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    local_data_dir = os.path.join(project_root, 'nltk_data')
    
    wordnet_dir = os.path.join(local_data_dir, 'corpora', 'wordnet')
    words_file = os.path.join(local_data_dir, 'corpora', 'words.zip')

    if not os.path.isdir(wordnet_dir) or not os.path.exists(words_file):
        print("First-time setup for 'typer' module: Downloading NLTK data...")
        print(f"Data will be stored in: {local_data_dir}")
        nltk.download('wordnet', download_dir=local_data_dir)
        nltk.download('words', download_dir=local_data_dir)
        print("Download complete.")
    
    nltk.data.path.append(local_data_dir)


def word_error(word: str) -> None:
  # find synonym

  # type out synonym

  # delete synonym

  pass


def letter_error(word: str, pos: int, avg_letter_time: float, config: TypingConfig) -> None:
  extra_letters = min(randrange(1, 5), len(word)-pos)
  mistake = choice(config.error_characters)
  mistake_text = mistake + word[pos:pos+extra_letters]

  for letter in mistake_text:
    sleep(uniform(avg_letter_time * 0.7, avg_letter_time * 1.3))
    pyautogui.write(letter)
  
  sleep(uniform(*config.mistake_pause_range))
  for letter in mistake_text:
    sleep(uniform(avg_letter_time * 0.7, avg_letter_time * 1.3))
    pyautogui.press('backspace')
          

def handle_whitespace(whitespace: str) -> None:
    for char in whitespace:
        if char == '\n':
            pyautogui.press('enter')
        elif char == '\t':
            pyautogui.press('tab')
        else:
            pyautogui.write(char)


def write_word(word: str, config: TypingConfig) -> None:
  total_word_time = uniform(*config.word_time_range)
  avg_letter_time = total_word_time / min(len(word), 10)
  
  # random long pause before a word is typed
  if random() <= config.word_pause_chance:
    sleep(uniform(*config.word_pause_range))
  
  # use random wrong word
  if random() <= config.word_error_rate:
    word_error()

  for pos, letter in enumerate(word):
    sleep(uniform(avg_letter_time * 0.7, avg_letter_time * 1.3))
      
    # make random typo and fix it
    if random() <= config.letter_error_rate:
      letter_error(word, pos, avg_letter_time, config)
      sleep(uniform(*config.correction_pause_range))
    pyautogui.write(letter)


ensure_nltk_data()