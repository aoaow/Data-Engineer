install:
	pip install --upgrade pip &&\
		pip install -r requirement.txt

format:
	black *.py

lint:
	pylint --disable=R,C pandas_test.py


generate_and_push:
	# Create the markdown file (assuming it's generated from the plot)
	python pandas_test.py  # Replace with the actual command to generate the markdown

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add egrid.png egrid_summary.md; \
		git commit -m "Add generated plot and report"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi
