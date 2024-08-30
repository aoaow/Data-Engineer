install:
	pip install --upgrade pip &&\
		pip install -r requirement.txt

format:
	black *.py

lint:
	pylint --disable=R,C hello.py
# which would only give me warning and error messages
# and run pylint on hello py file

test:
	python -m pytest -vv --cov=hello test_hello.py