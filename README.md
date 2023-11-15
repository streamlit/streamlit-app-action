# streamlit-app-action

Github Action for basic validating Streamlit app. This action will:

- Run `pytest` for any tests, including [Streamlit AppTests](https://docs.streamlit.io/library/api-reference/app-testing),
  that are part of your repo.
- Run a smoke test AppTest that runs each page of your app and verifies no exceptions are thrown on the initial run
- Optionally, run [ruff](https://github.com/astral-sh/ruff) for linting and formatting via
  [ruff-action](https://github.com/ChartBoost/ruff-action).

## Usage

```yml
name: Streamlit app

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  streamlit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v3
        with:
          python-version: '3.11'
      - uses: streamlit/streamlit-app-action@v0
        with:
          app-path: streamlit_app.py
          ruff: true
```

### Printing a pretty output of test results

[pytest-results-action](https://github.com/marketplace/actions/pytest-results-actions) is a useful action
to print the output of pytest runs in your GitHub Actions workflow summary view. You can add it as follows:

```yml
# ... setup as above ...
- uses: streamlit/streamlit-app-action@v0
  with:
    app-path: streamlit_app.py
    ruff: true
    # Add pytest-args to output junit xml
    pytest-args: -v --junit-xml=test-results.xml
- if: always()
  uses: pmeier/pytest-results-action@main
  with:
    path: test-results.xml
    summary: true
    display-options: fEX
```
