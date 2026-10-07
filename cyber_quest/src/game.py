import random
import json
import os
import time
from src.utils import Colors, print_color, clear_screen
from src.player import Player

SAVE_FILE = "save_game.json"

class Game:
    def __init__(self):
        self.player = None

    def start(self):
        clear_screen()
        print_color("=" * 55, Colors.HEADER, delay=0)
        print_color("      CYBER-QUEST 2077: ПОБЕГ ИЗ НЕОНОВОГО ГОРОДА", Colors.BOLD + Colors.OKCYAN, delay=0.02)
        print_color("=" * 55, Colors.HEADER, delay=0)
        print()
        
        if os.path.exists(SAVE_FILE):
            print_color("Найдено сохранение!", Colors.WARNING, delay=0)
            choice = input("Загрузить игру? (y/n): ").strip().lower()
            if choice == 'y':
                self.load_game()
            else:
                self.new_game()
        else:
            self.new_game()

        self.main_loop()

    def new_game(self):
        name = input("\nВведите имя твоего героя: ").strip()
        if not name:
            name = "Кибер-Странник"
        self.player = Player(name)
        print_color(f"\nДобро пожаловать в неоновые трущобы, {self.player.name}!", Colors.OKGREEN)
        time.sleep(1)

    def main_loop(self):
        while self.player.is_alive():
            clear_screen()
            self.show_status()
            print_color("\nЧто будешь делать?", Colors.HEADER, delay=0)
            print("1. Исследовать заброшенный сектор")
            print("2. Зайти в кибер-бар (Магазин / Лечение)")
            print("3. Инвентарь")
            print("4. Сохранить игру")
            print("5. Выйти")

            choice = input("\nВыберите действие (1-5): ").strip()

            if choice == "1":
                self.explore()
            elif choice == "2":
                self.visit_bar()
            elif choice == "3":
                self.show_inventory()
            elif choice == "4":
                self.save_game()
            elif choice == "5":
                print_color("\nДо связи, сетевой странник!", Colors.WARNING)
                break
            else:
                print_color("Неверный ввод, попробуй снова.", Colors.FAIL, delay=0)
                time.sleep(1)

        if not self.player.is_alive():
            print_color("\n[GAME OVER] Твои системы отключились...", Colors.FAIL)

    def show_status(self):
        print_color(f"--- [ ГЕРОЙ: {self.player.name} ] ---", Colors.BOLD + Colors.OKBLUE, delay=0)
        print_color(f"Здоровье: {self.player.hp}/{self.player.max_hp} HP | Кредиты: {self.player.credits} ₵ | Атака: {self.player.attack}", Colors.OKGREEN, delay=0)

    def explore(self):
        clear_screen()
        print_color("Вы проникаете в затенённый сектор...", Colors.OKCYAN)
        time.sleep(1)

        event = random.choice(["fight", "treasure", "empty", "trap"])

        if event == "fight":
            self.fight_event()
        elif event == "treasure":
            found = random.randint(20, 60)
            self.player.credits += found
            print_color(f"\nВы нашли взломанный терминал с {found} кредитами!", Colors.OKGREEN)
        elif event == "trap":
            damage = random.randint(10, 25)
            self.player.hp -= damage
            print_color(f"\nВы попали под токовый разряд! Потеряно {damage} HP.", Colors.FAIL)
        else:
            print_color("\nЗдесь тихо... Лишь шум серверов на заднем плане.", Colors.WARNING)

        input("\nНажмите Enter для продолжения...")

    def fight_event(self):
        enemies = [
            {"name": "Дрон-Охотник", "hp": 40, "attack": 10, "reward": 30},
            {"name": "Кибер-Мусорщик", "hp": 60, "attack": 14, "reward": 50},
            {"name": "Сбойный Боевой ИИ", "hp": 85, "attack": 18, "reward": 80}
        ]
        enemy = random.choice(enemies)
        e_hp = enemy["hp"]

        print_color(f"\n⚠ ВРАГ ОБНАРУЖЕН: {enemy['name']} (HP: {e_hp})!", Colors.FAIL)

        while e_hp > 0 and self.player.is_alive():
            print(f"\nВаше HP: {self.player.hp} | HP врага: {e_hp}")
            print("1. Атаковать")
            print("2. Использовать Энергоячейку (+30 HP)")
            print("3. Сбежать")

            action = input("Выберите действие: ").strip()

            if action == "1":
                dmg = random.randint(self.player.attack - 3, self.player.attack + 5)
                e_hp -= dmg
                print_color(f"Вы нанесли {dmg} урона!", Colors.OKGREEN, delay=0)
            elif action == "2":
                if "Энергоячейка" in self.player.inventory:
                    self.player.inventory.remove("Энергоячейка")
                    self.player.heal(30)
                    print_color("Вы восстановили 30 HP!", Colors.OKGREEN, delay=0)
                else:
                    print_color("У вас нет Энергоячеек!", Colors.FAIL, delay=0)
                    continue
            elif action == "3":
                if random.random() > 0.4:
                    print_color("Вам удалось успешно сбежать!", Colors.OKCYAN, delay=0)
                    return
                else:
                    print_color("Побег не удался!", Colors.FAIL, delay=0)
            else:
                continue

            if e_hp > 0:
                e_dmg = random.randint(enemy["attack"] - 2, enemy["attack"] + 4)
                self.player.hp -= e_dmg
                print_color(f"{enemy['name']} атаковал вас и нанес {e_dmg} урона!", Colors.FAIL, delay=0)

        if self.player.is_alive() and e_hp <= 0:
            print_color(f"\nВраг уничтожен! Вы получили {enemy['reward']} кредитов.", Colors.OKGREEN)
            self.player.credits += enemy["reward"]

    def visit_bar(self):
        clear_screen()
        print_color("--- [ КИБЕР-БАР 'БИТ & БАЙТ' ] ---", Colors.HEADER)
        print(f"Ваш баланс: {self.player.credits} ₵\n")
        print("1. Купить Энергоячейку (+30 HP) — 25 ₵")
        print("2. Улучшить кибер-имплант (+5 к атаке) — 60 ₵")
        print("3. Полная диагностика и ремонт (+50 HP) — 40 ₵")
        print("4. Уйти")

        choice = input("\nВаш выбор: ").strip()
        if choice == "1" and self.player.credits >= 25:
            self.player.credits -= 25
            self.player.inventory.append("Энергоячейка")
            print_color("Вы купили Энергоячейку!", Colors.OKGREEN)
        elif choice == "2" and self.player.credits >= 60:
            self.player.credits -= 60
            self.player.attack += 5
            print_color("Атака увеличена!", Colors.OKGREEN)
        elif choice == "3" and self.player.credits >= 40:
            self.player.credits -= 40
            self.player.heal(50)
            print_color("Здоровье восстановлено!", Colors.OKGREEN)
        elif choice == "4":
            return
        else:
            print_color("Недостаточно кредитов или неверный выбор!", Colors.FAIL)

        time.sleep(1)

    def show_inventory(self):
        clear_screen()
        print_color("--- [ ИНВЕНТАРЬ ] ---", Colors.HEADER)
        if not self.player.inventory:
            print("Инвентарь пуст.")
        else:
            for item in set(self.player.inventory):
                print(f"- {item} x{self.player.inventory.count(item)}")
        input("\nНажмите Enter...")

    def save_game(self):
        try:
            with open(SAVE_FILE, "w", encoding="utf-8") as f:
                json.dump(self.player.to_dict(), f, ensure_ascii=False, indent=4)
            print_color("\nИгра успешно сохранена!", Colors.OKGREEN)
        except Exception as e:
            print_color(f"\nОшибка сохранения: {e}", Colors.FAIL)
        time.sleep(1)

    def load_game(self):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.player = Player.from_dict(data)
            print_color(f"\nСохранение загружено. С возвращением, {self.player.name}!", Colors.OKGREEN)
        except Exception as e:
            print_color(f"\nОшибка загрузки: {e}. Создается новая игра.", Colors.FAIL)
            self.new_game()
        time.sleep(1)
