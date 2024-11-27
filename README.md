poetry add playwright
poetry run playwright install

export PATH="$HOME/.local/bin:$PATH"  # in order to poetry be recognized in terminal


pytest --template=html1/index.html --report=reports/report.html
to run in parallel: pytest -n number_of_workers


linters:
poetry run black .




