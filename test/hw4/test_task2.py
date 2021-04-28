from unittest.mock import patch

import pytest

from All_home_works.hw4.task2 import count_dots_on_i

URL = "https://example.com/"


class Response:
    def __init__(self, data: str):
        self.data = data.split(" ")

    def __enter__(self):
        return map(lambda x: x.encode(), self.data)

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None


@patch("urllib.request.urlopen")
def test_urlopen__with_right_url(urlopen):
    count_dots_on_i(URL)
    urlopen.assert_called_with(URL)


@patch("urllib.request.urlopen", side_effect=ValueError("BAD URL"))
def test_urlopen__with_invalid_url(urlopen):
    with pytest.raises(ValueError, match="BAD URL"):
        count_dots_on_i("BAD URL")


@patch("urllib.request.urlopen")
def test_count_dots_on_i__check_valid_data(urlopen):
    expect = 2
    urlopen.return_value = Response("<div> </div>")
    res = count_dots_on_i(URL)
    assert expect == res
