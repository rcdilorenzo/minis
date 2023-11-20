init:
	@python3.8 -m venv venv
	@./venv/bin/pip install pip-tools

sync-venv:
	@./venv/bin/pip-compile requirements.in --output-file requirements.txt
	@./venv/bin/pip-sync requirements.txt

install:
	@./venv/bin/pip install -r requirements.txt
	@./venv/bin/pip install -e .