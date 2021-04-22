.PHONY: help install upgrade clean

.DEFAULT: help
help:
	@echo "make install"
	@echo "       prepare development environment"
	@echo "make upgrade"
	@echo "       pull up the latest code"
	@echo "make clean"
	@echo "       clean python cache files and 'out' folder"

install:
	@bash scripts/install.sh

upgrade:
	@bash scripts/upgrade.sh

clean-pyc:
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -type d | xargs rm -fr
	@find . -name '.pytest_cache' -type d | xargs rm -fr

clean:clean-pyc
	@rm -fr ./out
	@echo "Clean all cache and out folder."