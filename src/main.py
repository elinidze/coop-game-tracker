# Список для хранения информации об играх
games = []

def add_game():
    """Добавить новую игру"""
    print("\n--- Добавление новой игры ---")
    
    name = input("Введите название игры: ")
    platform = input("Введите платформу (PC, PS4, Xbox и т.д.): ")
    max_players = input("Введите максимальное количество игроков: ")
    completed = input("Игра пройдена? (да/нет): ")
    
    game = {
        "name": name,
        "platform": platform,
        "max_players": max_players,
        "completed": completed.lower() == "yes"
    }
    
    games.append(game)
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

def main_menu():
    """Главное меню приложения"""
    while True:
        print("\n=== Учет кооперативных игр ===")
        print("1. Добавить игру")
        print("2. Показать все игры")
        print("3. Выйти")
        
        choice = input("\nВыберите действие (1-3): ")
        
        if choice == "1":
            add_game()
        elif choice == "2":
            show_all()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    print("Мое приложение для учета кооперативных игр")
    main_menu()
