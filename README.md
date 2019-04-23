# Welcome to my little test server!

---

To get started, we assume that `python3` and `pip3` are both installed and configured. Then:

- `pip3 install pipenv`
- `cd plangrid` (Assuming you checked the repo out to the current directory)
- `pipenv install`

Now we can run the app via one of two methods:

- `pipenv run ./app.py` which will run the app server without debugging enabled, or
- `FLASK_ENV=development pipenv run ./app.py` which will enable debugging, logging requests to `./app.log`

## Tests

To run unit tests, use the following:

- `pipenv run python3 -m pytest`

This will make use of the conftest.py fixture setup and test file in `tests/`.

In order to run manual tests, once the server is running, you can use `curl` as follows:

- `curl -H 'Accept:' localhost:5000` to force the plain response, or
- `curl -H 'Accept: application/json' localhost:5000` to get the JSON response
