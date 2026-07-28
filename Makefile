.PHONY: validate lint graph context-pack site serve clean all help

validate:
	@echo "🔍 Running all validators..."
	@python3 tools/validate-all.py

lint: validate

graph:
	@echo "🕸️  Building knowledge graph..."
	@python3 tools/build-knowledge-graph.py --format all

context-pack:
	@echo "📦 Generating context pack..."
	@python3 tools/context-pack.py $(filter-out $@,$(MAKECMDGOALS)) --output /tmp/context-pack.md
	@echo "   Output: /tmp/context-pack.md"

site:
	@echo "🌐 Building website..."
	@python3 tools/prepare-site-content.py
	cd site && zola build
	@echo "✅ Site built in site/public/"

serve:
	@echo "🌐 Starting dev server at http://localhost:1111 ..."
	-pkill zola 2>/dev/null; sleep 0.5
	@python3 tools/prepare-site-content.py
	cd site && zola serve --port 1111

clean:
	@echo "🧹 Cleaning..."
	rm -rf site/content site/public

all: validate graph site

help:
	@echo "Engineering Knowledge Framework — Tooling"
	@echo ""
	@echo "Usage:"
	@echo "  make validate          Run all validators"
	@echo "  make graph             Build knowledge graph (JSON + DOT)"
	@echo "  make context-pack TERM Generate context pack for AI assistants"
	@echo "  make mcp-server        Start MCP server (stdio)"
	@echo "  make site              Build the Zola static site"
	@echo "  make serve             Preview site at http://localhost:1111"
	@echo "  make clean             Remove generated content and output"
	@echo "  make all               Run validate + graph + site"
	@echo "  make help              Show this help"
