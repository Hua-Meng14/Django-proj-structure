# Make sure this file is named 'Makefile' and is placed in the root of your project

.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python3 -m core.manage migrate

.PHONY: migrations
migrations:
	poetry run python3 -m core.manage makemigrations

.PHONY: run-server
run-server:
	poetry run python3 -m core.manage runserver

.PHONY: superuser
superuser:
	poetry run python3 -m core.manage createsuperuser

.PHONY: update
update: install migrate ;
