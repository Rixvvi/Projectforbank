from unittest.mock import patch

from src.external_api import get_external_api

'''@patch('requests.get')
def test_external_api(mock_get):
    mock_get.return_value.json.return_value = {}
    assert get_external_api() == 0
    mock_get.assert_called_once_with('https://apilayer.com/marketplace/exchangerates_data-api')'''