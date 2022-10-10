from one_hot_encoder import fit_transform
import pytest


def test_cities():
    cities = ["Moscow", "New York", "Moscow", "London"]
    actual = fit_transform(cities)
    expected = [
        ("Moscow", [0, 0, 1]),
        ("New York", [0, 1, 0]),
        ("Moscow", [0, 0, 1]),
        ("London", [1, 0, 0]),
    ]
    assert actual == expected


def test_empty():
    with pytest.raises(TypeError):
        fit_transform()


def test_lotr_races():
    races = ["Elf", "Man", "Dwarf", "Hobbit", "Orc"]
    actual = fit_transform(races)
    expected = [
        ("Elf", [0, 0, 0, 0, 1]),
        ("Man", [0, 0, 0, 1, 0]),
        ("Dwarf", [0, 0, 1, 0, 0]),
        ("Hobbit", [0, 1, 0, 0, 0]),
        ("Orc", [1, 0, 0, 0, 0]),
    ]
    assert actual == expected


def test_output_type():
    answer = "42"
    actual = fit_transform(answer)
    assert isinstance(actual, list)
