from unittest.mock import patch

from All_home_works.hw4.task2 import count_dots_on_i

URL = "https://example.com/"


class Data:
    def __init__(self, data: list):
        self.data = data

    def __enter__(self):
        return map(lambda x: x.encode(), self.data)

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None


@patch("urllib.request.urlopen")
def test_urlopen_got__path(urlopen):
    count_dots_on_i(URL)
    urlopen.assert_called_with(URL)


@patch("urllib.request.urlopen")
def test_count_dots_on_i__check_valid_data(urlopen):
    expect = 2
    urlopen.return_value = Data(["<div></div>"])
    res = count_dots_on_i(URL)
    assert expect == res
