import requests


class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(base: str, symbol: str, amount: str, api_key: str):
        if base == symbol:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            base_ticker = base
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {base}")

        try:
            symbol_ticker = symbol
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {symbol}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не удалось обработать количество {amount}")

        r = requests.get(f"https://free.currconv.com/api/v7/convert?q={base_ticker}_{symbol_ticker}&compact=ultra&apiKey={api_key}")

        return round(float(r.json()[f'{base_ticker}_{symbol_ticker}']) * amount, 2)
