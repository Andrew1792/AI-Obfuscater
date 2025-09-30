from random import random, choice, uniform
from time import sleep
import pyautogui

class TypingConfig:
    def __init__(self, wpm, wpm_variance, error_rate, pause_chance):
        self.wpm = wpm
        self.wpm_variance = wpm_variance
        self.error_rate = error_rate
        self.word_pause_chance = pause_chance

        min_wpm = self.wpm - self.wpm_variance
        max_wpm = self.wpm + self.wpm_variance
        
        min_word_time = 60 / max_wpm
        max_word_time = 60 / min_wpm
        self.word_time_range = (max(0, min_word_time), max_word_time)

        avg_sec_per_word = 60 / self.wpm
        
        self.word_pause_range = (avg_sec_per_word, avg_sec_per_word * 4)
        
        self.mistake_pause_range = (avg_sec_per_word * 0.4, avg_sec_per_word * 0.8) # time before hitting backspace
        self.correction_pause_range = (avg_sec_per_word * 0.2, avg_sec_per_word * 0.4) # time before typing the correct char
        
        self.error_characters = (' ', '!', '"', '#', '$', '%', '&', "'", '(',
                                 ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
                                 '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
                                 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                                 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',)


def write_word(word: str, config: TypingConfig) -> None:
    total_word_time = uniform(*config.word_time_range)
    avg_letter_time = total_word_time / len(word) if word else 0
    
    # pause BEFORE a word is typed
    if random() <= config.word_pause_chance:
        sleep(uniform(*config.word_pause_range))

    for letter in word:
        sleep(uniform(avg_letter_time * 0.7, avg_letter_time * 1.3))
        
        # make random typo and fix it
        if random() <= config.error_rate:
            mistake = choice(config.error_characters)
            pyautogui.write(mistake)
            sleep(uniform(*config.mistake_pause_range))
            pyautogui.press('backspace')
            sleep(uniform(*config.correction_pause_range))

        pyautogui.write(letter)   