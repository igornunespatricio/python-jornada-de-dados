# Default quality check - balanced
quality-classes:
	@echo "🔍 Running Ruff on classes_* directories..."
	poetry run ruff check --select=E,F,W,B,SIM,N8,UP,COM8,PLR,ERA001 --fix classes_*/ --output-format=concise
	@echo "🎨 Running Black..."
	poetry run black classes_*/
	@echo "✅ Quality checks completed!"

# Strict mode - for when you want more comprehensive checks
quality-classes-strict:
	@echo "🔍 Running Ruff on classes_* directories..."
	poetry run ruff check --select=ALL --ignore=D,T20,INP001,ANN,PLC,RSE --fix classes_*/ --output-format=concise
	@echo "🎨 Running Black..."
	poetry run black classes_*/
	@echo "✅ Strict quality checks completed!"

# Quick check - just the essentials
quality-classes-quick:
	@echo "🔍 Running Ruff on classes_* directories..."
	poetry run ruff check --select=E,F,W,B,SIM --fix classes_*/ --output-format=concise
	@echo "🎨 Running Black..."
	poetry run black classes_*/
	@echo "✅ Quick quality checks completed!"