from unittest.mock import MagicMock, mock_open, patch

from src.utils import read_json


@patch("builtins.open", new_callable=mock_open, read_data="[]")
@patch("json.load")
def test_read_json(mock_json_load: MagicMock, mock_open: MagicMock) -> None:
    mock_json_load.return_value = []
    result = read_json("test_file.json")
    assert result == []
    mock_open.assert_called_once_with("test_file.json", "r", encoding="utf-8")
    mock_json_load.assert_called_once_with(mock_open())
