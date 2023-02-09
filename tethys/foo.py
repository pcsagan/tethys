import requests


def bar() -> str:
    return 'foo'


def fetch() -> int:
    return requests.get('https://github.com').status_code
