import io
import json
import what_is_year_now
import unittest
from mock import patch
from datetime import date


class FakeJsonFile:
    def __init__(self, json):
        self.json = json

    def __enter__(self):
        self.file = io.StringIO(self.json)
        return self.file

    def __exit__(self, *args):
        self.file.close()


@patch("what_is_year_now.urllib.request.urlopen")
class TestCalendar(unittest.TestCase):
    def test_get_datetime(self, mock_datetime):
        date_today = date.today().strftime("%Y-%m-%d")
        fake_response = json.dumps({"currentDateTime": date_today})
        mock_datetime.return_value = FakeJsonFile(fake_response)
        assert what_is_year_now.what_is_year_now() == 2022
        mock_datetime.assert_called_once()

    def test_dot_format(self, mock_datetime):
        date_today = date.today().strftime("%d.%m.%Y")
        fake_response = json.dumps({"currentDateTime": date_today})
        mock_datetime.return_value = FakeJsonFile(fake_response)
        assert what_is_year_now.what_is_year_now() == 2022
        mock_datetime.assert_called_once()

    def test_exception(self, mock_datetime):
        date_today = date.today().strftime("%d/%m/%Y")
        fake_response = json.dumps({"currentDateTime": date_today})
        mock_datetime.return_value = FakeJsonFile(fake_response)
        with self.assertRaises(ValueError):
            what_is_year_now.what_is_year_now()
        mock_datetime.assert_called_once()
