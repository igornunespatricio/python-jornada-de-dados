.PHONY: quality-classes quality-all check

quality-classes:
	@echo "🔍 Running Ruff on classes_* directories..."
	poetry run ruff check --select E,F,W,I --fix classes_*/ --output-format=concise
	@echo "🎨 Running Black..."
	poetry run black classes_*/
	@echo "✅ Quality checks completed!"

quality-classes-unsafe:
	@echo "🔍 Running Ruff on classes_* directories..."
	poetry run ruff check --select E,F,W,I --fix classes_*/ --unsafe-fixes --output-format=concise
	@echo "🎨 Running Black..."
	poetry run black classes_*/
	@echo "✅ Quality checks completed!"