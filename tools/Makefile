REPO_ROOT = ..

.PHONY: validate lint graph site serve all help

validate:
	@echo "🔍 Running all validators..."
	@cd $(REPO_ROOT) && python3 tools/validate-all.py

lint: validate

graph:
	@echo "🕸️  Building knowledge graph..."
	@cd $(REPO_ROOT) && python3 tools/build-knowledge-graph.py --format all

site:
	@echo "🌐 Building website..."
	@cd $(REPO_ROOT) && python3 tools/org-to-md.py
	@cd $(REPO_ROOT)/site && zola build
	@echo "✅ Site built in site/public/"

serve:
	@echo "🌐 Starting dev server..."
	@cd $(REPO_ROOT)/site && zola serve --port 1111

all: validate graph site

help:
	@echo "Engineering Knowledge Framework — Tooling"
	@echo ""
	@echo "Usage:"
	@echo "  make validate    Run all validators"
	@echo "  make graph       Build knowledge graph (JSON + DOT)"
	@echo "  make site        Build the Zola static site"
	@echo "  make serve       Build and serve the site locally"
	@echo "  make all         Run validate + graph + site"
	@echo "  make help        Show this help"
