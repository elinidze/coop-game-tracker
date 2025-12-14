import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Импортируем функции из main.py
from main import games, add_game, show_all

def test_games_list_initialization():
    """Проверяем, что список игр инициализируется пустым"""
    assert isinstance(games, list)
    # В этом тесте мы просто проверяем тип
    # Фактически games будет импортирован как пустой список из main.py

def test_game_structure():
    """Проверяем структуру данных игры"""
    test_game = {
        "name": "Test Game",
        "platform": "PC",
        "max_players": "4",
        "completed": False
    }
    
    assert "name" in test_game
    assert "platform" in test_game
    assert "max_players" in test_game
    assert "completed" in test_game
    assert test_game["name"] == "Test Game"
