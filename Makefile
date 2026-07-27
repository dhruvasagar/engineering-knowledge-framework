.PHONY: validate lint graph site serve all clean help

validate:
	@echo "🔍 Running all validators..."
	@python3 tools/validate-all.py

lint: validate

graph:
	@echo "🕸️  Building knowledge graph..."
	@python3 tools/build-knowledge-graph.py --format all

site:
	@echo "🌐 Building website with Hugo..."
	@python3 tools/prepare-hugo-content.py
	cd site && hugo
	@echo "✅ Site built in site/public/"

serve:
	@echo "🌐 Starting Hugo dev server..."
	@python3 tools/prepare-hugo-content.py
	cd site && hugo server --port 1111 --baseURL http://localhost:1111/

clean:
	@echo "🧹 Cleaning..."
	rm -rf site/content site/public site/resources

all: validate graph site

help:
	@echo "Engineering Knowledge Framework — Tooling"
	@echo ""
	@echo "Usage:"
	@echo "  make validate    Run all validators"
	@echo "  make graph       Build knowledge graph (JSON + DOT)"
	@echo "  make site        Build the Hugo static site"
	@echo "  make serve       Preview site at http://localhost:1111"
	@echo "  make clean       Remove generated content and output"
	@echo "  make all         Run validate + graph + site"
	@echo "  make help        Show this help"
