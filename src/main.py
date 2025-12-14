# Список для хранения информации об играх
#games = []
#
#
#def add_game():
#    """Добавить новую игру"""
#    print("\n--- Добавление новой игры ---")
#
#    name = input("Введите название игры: ")
#    platform = input("Введите платформу (PC, PS4, Xbox и т.д.): ")
#    max_players = input("Введите максимальное количество игроков: ")
#    completed = input("Игра пройдена? (да/нет): ")
#
#    game = {
#        "name": name,
#        "platform": platform,
#        "max_players": max_players,
#        "completed": completed.lower() == "yes",
#    }
#
#    games.append(game)
#    print(f"Игра '{name}' успешно добавлена!")
#
#
#def show_all():
#    """Показать все игры"""
#    print("\n--- Список всех игр ---")
#
#    if not games:
#        print("Игр пока нет.")
#        return
#
#    for i, game in enumerate(games, 1):
#        status = "✓" if game["completed"] else "✗"
#        print(f"{i}. {game['name']} ({game['platform']})")
#        print(f"   Игроков: {game['max_players']}, Пройдена: {status}")
#        print()
#
#
#def main_menu():
#    """Главное меню приложения"""
#    while True:
#        print("\n=== Учет кооперативных игр ===")
#        print("1. Добавить игру")
#        print("2. Показать все игры")
#        print("3. Выйти")
#
#        choice = input("\nВыберите действие (1-3): ")
#
#        if choice == "1":
#            add_game()
#        elif choice == "2":
#            show_all()
#        elif choice == "3":
#            print("До свидания!")
#            break
#        else:
#            print("Неверный выбор. Попробуйте снова.")
#
#
#if __name__ == "__main__":
#    print("Мое приложение для учета кооперативных игр")
#    main_menu()

import json
import os

# Файл для сохранения данных
DATA_FILE = "games_data.json"

def load_games():
    """Загрузить игры из файла"""
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("Ошибка загрузки файла. Будет создан новый список.")
        return []

def save_games():
    """Сохранить игры в файл"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(games, f, ensure_ascii=False, indent=2)
        print("Данные успешно сохранены!")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

# Загружаем игры при старте
games = load_games()

def add_game():
    """Добавить новую игру"""
    print("\n--- Добавление новой игры ---")
    
    name = input("Введите название игры: ")
    platform = input("Введите платформу (PC, PS4, Xbox и т.д.): ")
    max_players = input("Введите максимальное количество игроков: ")
    
    while True:
        completed = input("Игра пройдена? (да/нет): ").lower()
        if completed in ['да', 'нет']:
            break
        print("Пожалуйста, введите 'да' или 'нет'")
    
    game = {
        "name": name,
        "platform": platform,
        "max_players": max_players,
        "completed": completed == "да"
    }
    
    games.append(game)
    save_games()  # Сохраняем после добавления
    print(f"Игра '{name}' успешно добавлена!")

def show_all():
    """Показать все игры"""
    print("\n--- Список всех игр ---")
    
    if not games:
        print("Игр пока нет.")
        return
    
    for i, game in enumerate(games, 1):
        status = "✓" if game["completed"] else "✗"
        print(f"{i}. {game['name']} ({game['platform']})")
        print(f"   Игроков: {game['max_players']}, Пройдена: {status}")
        print()

def delete_game():
    """Удалить игру"""
    if not games:
        print("Список игр пуст.")
        return
    
    show_all()
    
    try:
        index = int(input("\nВведите номер игры для удаления: ")) - 1
        
        if 0 <= index < len(games):
            removed_game = games.pop(index)
            save_games()  # Сохраняем после удаления
            print(f"Игра '{removed_game['name']}' удалена!")
        else:
            print("Неверный номер игры.")
    except ValueError:
        print("Пожалуйста, введите число.")

def main_menu():
    """Главное меню приложения"""
    while True:
        print("\n" + "="*40)
        print("         УЧЕТ КООПЕРАТИВНЫХ ИГР")
        print("="*40)
        print("1. Добавить игру")
        print("2. Показать все игры")
        print("3. Удалить игру")
        print("4. Сохранить данные")
        print("5. Выйти")
        
        try:
            choice = input("\nВыберите действие (1-5): ")
            
            if choice == "1":
                add_game()
            elif choice == "2":
                show_all()
            elif choice == "3":
                delete_game()
            elif choice == "4":
                save_games()
            elif choice == "5":
                print("\nСпасибо за использование приложения!")
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            save_games()
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")

# Основная часть программы
if __name__ == "__main__":
    print("="*50)
    print("ПРИЛОЖЕНИЕ ДЛЯ УЧЕТА КООПЕРАТИВНЫХ ИГР")
    print("="*50)
    print(f"Загружено игр: {len(games)}")
    main_menu()
