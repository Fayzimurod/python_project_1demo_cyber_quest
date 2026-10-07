import os
import sys
import time

# Включение поддержки ANSI-цветов в консоли Windows
if os.name == 'nt':
    os.system('')

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_color(text, color=Colors.OKCYAN, delay=0.01):
    """Вывод цветного текста с корректной задержкой печати."""
    sys.stdout.write(color)
    if delay > 0:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write(Colors.ENDC + '\n')
    else:
        sys.stdout.write(text + Colors.ENDC + '\n')
    sys.stdout.flush()

def clear_screen():
    """Очистка терминала."""
    os.system('cls' if os.name == 'nt' else 'clear')
    