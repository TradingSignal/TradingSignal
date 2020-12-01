JOBS ?= 2

help:
	@echo "make"
	@echo "    clean"
	@echo "        Remove Python/build artifacts."
	@echo "    install"
	@echo "        Install tradingsignal."
	@echo "    install-full"
	@echo "        Install tradingsignal with all extras."
	@echo "    formatter"
	@echo "        Apply black formatting to code."
	@echo "    lint"
	@echo "        Lint code with flake8, and check if black formatter should be applied."
	@echo "    types"
	@echo "        Check for type errors using mypy."
	@echo "    prepare-tests-macos"
	@echo "        Install system requirements for running tests on macOS."
	@echo "    test"
	@echo "        Run pytest on tests/."
	@echo "        Use the JOBS environment variable to configure number of workers (default: 1)."

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +

install:
	poetry run python -m pip install -U pip
	poetry install

install-full:
	poetry run python -m pip install -U pip
	poetry install -E full

formatter:
	poetry run black tradingsignal tests

lint:
	poetry run flake8 tradingsignal tests
	poetry run black --check tradingsignal tests

types:
	poetry run mypy tradingsignal --disable-error-code arg-type \
	--disable-error-code assignment \
	--disable-error-code var-annotated \
	--disable-error-code return-value \
	--disable-error-code union-attr \
	--disable-error-code override \
	--disable-error-code operator \
	--disable-error-code attr-defined \
	--disable-error-code index \
	--disable-error-code misc \
	--disable-error-code return \
	--disable-error-code call-arg \
	--disable-error-code type-var \
	--disable-error-code list-item \
	--disable-error-code has-type \
	--disable-error-code valid-type \
	--disable-error-code dict-item \
	--disable-error-code no-redef \
	--disable-error-code func-returns-value

prepare-install-macos:
	brew install ta-lib

test: clean
	poetry run pytest tests -n=$(JOBS) --cov=./ --cov-report=xml