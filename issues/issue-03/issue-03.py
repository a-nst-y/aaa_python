from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_cities(self):
        cities = ["Moscow", "New York", "Moscow", "London"]
        actual = fit_transform(cities)
        expected = [
            ("Moscow", [0, 0, 1]),
            ("New York", [0, 1, 0]),
            ("Moscow", [0, 0, 1]),
            ("London", [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_lotr_races(self):
        races = ["Elf", "Man", "Dwarf", "Hobbit", "Orc"]
        actual = fit_transform(races)
        expected = [
            ("Orc", [1, 0, 0, 0, 0]),
            ("Hobbit", [0, 1, 0, 0, 0]),
            ("Dwarf", [0, 0, 1, 0, 0]),
            ("Man", [0, 0, 0, 1, 0]),
            ("Elf", [0, 0, 0, 0, 1]),
        ]
        self.assertCountEqual(actual, expected)

    def test_output_type(self):
        answer = "42"
        actual = fit_transform(answer)
        self.assertIsInstance(actual, list)
