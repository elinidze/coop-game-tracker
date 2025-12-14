import sys
import os

# Добавляем путь к src, чтобы импортировать модули
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_addition():
    """Проверяем, что сложение работает"""
    assert 1 + 1 == 2

def test_list_operations():
    """Проверяем операции со списками"""
    test_list = []
    test_list.append("test")
    assert len(test_list) == 1
    assert test_list[0] == "test"
