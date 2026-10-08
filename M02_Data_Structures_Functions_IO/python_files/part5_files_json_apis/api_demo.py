"""Part 5: calling a web API safely.

Needs the requests package:  pip install requests
Run:  python api_demo.py
"""
import requests

URL = "https://jsonplaceholder.typicode.com/todos"

try:
    response = requests.get(URL, timeout=10)    # always set a timeout
    response.raise_for_status()                 # a failed request still returns a response
    todos = response.json()
    print("status :", response.status_code)
    print("records:", len(todos))
    print("first  :", todos[0])
except requests.RequestException as error:
    # Covers timeouts, connection failures and HTTP errors.
    print("Request failed:", error)
    raise SystemExit(1)
