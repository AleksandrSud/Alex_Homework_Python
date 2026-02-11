import pytest
empty_dict = {}

football_stats = {
    "Число стран": 48,
    "Страна": "Катар",
    "Участники": [
        "Австралия", "Англия", "Аргентина",
        "Бельгия", "еще 42 страны", "Эквадор", "Япония"],
    "Награды": {
        "Золотой мяч": "Лионель Месси",
        "Серебряный мяч": "Килиан Мбаппе",
        "Золотая бутса": "Килиан Мбаппе",
        "Серебряная бутса": "Килиан Мбаппе",
        "Больше всего голов": {
            "Игрок": "Килиан Мбаппе - капитан команды",
            "Количество мячей": 8
        }
    }
}


def test_read_value():
    count = football_stats.get("Число стран")
    assert count == 48


def test_empty_dict():
    assert len(empty_dict) == 0


def test_write_value():
    football_stats["Число стран"] = 50
    count = football_stats.get("Число стран")
    assert count == 50


def test_write_new_value():
    len_before = len(football_stats)
    football_stats["Победитель"] = "Аргентина"
    winner = football_stats["Победитель"]
    assert winner == "Аргентина"
    assert len(football_stats) == len_before + 1


def test_read_list():
    participants = football_stats["Участники"]
    assert len(participants) > 0
    assert participants[0] == "Австралия"


def test_read_dict():
    total_goals = football_stats["Награды"]["Больше всего голов"][
        "Количество мячей"]
    assert total_goals == 8


def test_read_error():
    with pytest.raises(KeyError):
        empty_dict["key"]
