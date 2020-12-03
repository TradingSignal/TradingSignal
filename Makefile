JOBS ?= 2

help:
	@echo "make"
	@echo "    clean"
	@echo "        Remove Python/build artifacts."
	@echo "    install"
	@echo "        Install tradingsignal."
	@echo "    formatter"
	@echo "        Apply black formatting to code."
	@echo "    lint"
	@echo "        Lint code with flake8, and check if black formatter should be applied."
	@echo "    types"
	@echo "        Check for type errors using mypy."
	@echo "    prepare-install-macos"
	@echo "        Install system requirements for running on macOS."
	@echo "    prepare-install-ubuntu"
	@echo "        Install system requirements for running on ubuntu."
	@echo "    test"
	@echo "        Run pytest on tests/."
	@echo "        Use the JOBS environment variable to configure number of workers (default: 1)."

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +

prepare-install-macos:
	brew install ta-lib

prepare-install-ubuntu:
	cd lib/ \
	&& tar -xzf ta-lib-0.4.0-src.tar.gz \
	&& cd ta-lib \
    && ./configure --prefix=/usr \
    && make \
    && which sudo && sudo make install || make install \
    && cd ..

install:
	poetry run python -m pip install -U pip
	poetry install

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

test: clean
	poetry run pytest tests -n=$(JOBS) --cov=./ --cov-report=xml