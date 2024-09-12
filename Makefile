install:
	pip install --upgrade pip &&\
		pip install -r requirement.txt

format:
	black *.py

lint:
	pylint --disable=R,C pandas_test.py


