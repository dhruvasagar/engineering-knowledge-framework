#!/usr/bin/env python3
"""
Engineering Knowledge Framework MCP Server

Exposes the framework's knowledge graph, documents, and context pack
generation as MCP resources, tools, and prompts for AI assistants.

Usage:
    # Run as stdio server (for MCP-compatible AI assistants)
    python3 tools/mcp-server/server.py

    # Or with the wrapper script:
    ./tools/mcp-server/run.sh

Resources:
    knowledge://capabilities                    List all capabilities
    knowledge://capability/{name}                Documents in a capability
    knowledge://doc/{encoded-path}              Content of a specific document (use __ for /)
    knowledge://graph/stats                      Knowledge graph statistics
    knowledge://search?q={term}                  Search documents

Tools:
    generate-context-pack                        Generate AI context pack
    find-related-documents                       Find related documents
    search-knowledge                             Search across documents
    capability-report                            Get capability completeness
    read-document                                Read a specific document

Prompts:
    engineering-review                           Code review context pack
    architecture-review                          Architecture review context
    rails-development                            Rails development context
"""

import json
import re
import sys
import urllib.parse
from pathlib import Path

# Add repo root to path
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from mcp.server.fastmcp import FastMCP

# Paths
KG_PATH = REPO_ROOT / 'tools' / 'output' / 'knowledge-graph.json'
CONTEXT_PACK_PATH = REPO_ROOT / 'tools' / 'context-pack.py'

# ── Helpers ──────────────────────────────────────────────────────────


def load_kg():
    """Load the knowledge graph JSON."""
    if not KG_PATH.exists():
        return None
    with open(KG_PATH) as f:
        return json.load(f)


def read_document(path):
    """Read a document from the repo root."""
    filepath = REPO_ROOT / path
    if not filepath.exists():
        return None
    try:
        return filepath.read_text(encoding='utf-8')
    except Exception:
        return None


def extract_front_matter(content):
    """Extract title and description from front matter."""
    fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm_match:
        return None, None
    fm = fm_match.group(1)
    title = None
    description = None
    for line in fm.split('\n'):
        t_match = re.match(r'^title:\s*"?([^"\\n]+)"?\s*$', line)
        if t_match:
            title = t_match.group(1).strip()
        d_match = re.match(r'^description:\s*"?([^"\\n]+)"?\s*$', line)
        if d_match:
            description = d_match.group(1).strip()
    return title, description


def find_capability(term, kg):
    """Match a search term to a capability name."""
    if not kg:
        return None
    term_lower = term.lower().strip()
    for name in kg['capabilities']:
        if term_lower == name.lower():
            return name
        if term_lower in name.lower():
            return name
    return None


# ── Server Setup ──────────────────────────────────────────────────────

mcp = FastMCP(
    "Engineering Knowledge Framework",
    instructions="""Access the Engineering Knowledge Framework — an open-source framework 
for capturing, organizing, evolving and applying engineering knowledge.

Use this server to:
- Browse engineering capabilities (Rails, Security, AI, Architecture, etc.)
- Read framework documents (handbooks, guides, playbooks, checklists)
- Generate context packs for AI-assisted engineering tasks
- Search across all framework knowledge
- Get capability completeness reports""",
)


# ═════════════════════════════════════════════════════════════════════
# RESOURCES
# ═════════════════════════════════════════════════════════════════════


@mcp.resource("knowledge://capabilities")
def list_capabilities() -> str:
    """List all capabilities in the framework with document counts."""
    kg = load_kg()
    if not kg:
        return "Knowledge graph not found. Run `make graph` first."

    lines = ["# Engineering Knowledge Framework — Capabilities", ""]
    for cap, report in sorted(kg['capabilities'].items()):
        missing = report['missing']
        status = '✅ complete' if not missing else f'⚠️  missing: {", ".join(missing)}'
        lines.append(f"## {cap}")
        lines.append(f"- **Documents:** {report['total_documents']}")
        lines.append(f"- **Status:** {status}")
        lines.append("")
        for doc_type, paths in sorted(report['present'].items()):
            lines.append(f"  - {doc_type}: {len(paths)} docs")
        lines.append("")

    lines.append(f"\n*Total: {kg['stats']['total_documents']} documents, "
                 f"{kg['stats']['total_connections']} cross-references*")
    return '\n'.join(lines)


@mcp.resource("knowledge://capability/{name}")
def capability_docs(name: str) -> str:
    """Get all documents in a capability."""
    name = urllib.parse.unquote(name)
    kg = load_kg()
    if not kg:
        return "Knowledge graph not found. Run `make graph` first."

    cap = find_capability(name, kg)
    if not cap:
        available = ', '.join(sorted(kg['capabilities'].keys()))
        return f"Capability '{name}' not found. Available: {available}"

    report = kg['capabilities'][cap]
    lines = [f"# {cap}", ""]
    for doc_type, paths in sorted(report['present'].items()):
        lines.append(f"## {doc_type.replace('-', ' ').title()} ({len(paths)})")
        for p in paths:
            node = kg['nodes'].get(p, {})
            desc = node.get('description', '')
            title = node.get('title', p)
            lines.append(f"- [{title}]({p})")
            if desc:
                lines.append(f"  - {desc}")
        lines.append("")

    return '\n'.join(lines)


@mcp.resource("knowledge://doc/{docpath}")
def document_content(docpath: str) -> str:
    """Read a specific document by path (relative to repo root).
    Encode slashes as double-underscore: handbooks__rails__README.md
    """
    # Decode path: replace __ with /
    docpath = urllib.parse.unquote(docpath)
    clean = docpath.replace('__', '/').lstrip('./').lstrip('/')

    # Try as-is
    content = read_document(clean)
    if content:
        title, desc = extract_front_matter(content)
        if title:
            return f"# {title}\n\n*{desc}*\n\n{content}"
        return content

    # Try with .md extension
    content = read_document(clean + '.md')
    if content:
        title, desc = extract_front_matter(content)
        if title:
            return f"# {title}\n\n*{desc}*\n\n{content}"
        return content

    # Try directory-style path (handbooks/engineering/README/)
    if not clean.endswith('/') and not clean.endswith('.md'):
        for candidate in [clean + '/README.md', clean + '.md']:
            content = read_document(candidate)
            if content:
                title, desc = extract_front_matter(content)
                if title:
                    return f"# {title}\n\n*{desc}*\n\n{content}"
                return content

    # Try as directory path with README
    for candidate in [clean + '/README.md', clean + '/_index.md']:
        content = read_document(candidate)
        if content:
            title, desc = extract_front_matter(content)
            if title:
                return f"# {title}\n\n*{desc}*\n\n{content}"
            return content

    # Search knowledge graph for similar paths
    kg = load_kg()
    if kg:
        clean_lower = clean.lower()
        matches = [n for n in kg['nodes'] if clean_lower in n.lower()]
        if matches:
            suggestions = '\n'.join(f"  - [{n}](knowledge://document/{n})" for n in matches[:10])
            return f"Document '{path}' not found. Did you mean:\n{suggestions}"

    return f"Document '{path}' not found."


@mcp.resource("knowledge://graph/stats")
def graph_stats() -> str:
    """Get knowledge graph statistics."""
    kg = load_kg()
    if not kg:
        return "Knowledge graph not found. Run `make graph` first."

    lines = ["# Knowledge Graph Statistics", ""]
    lines.append(f"- **Total documents:** {kg['stats']['total_documents']}")
    lines.append(f"- **Cross-references:** {kg['stats']['total_connections']}")
    lines.append(f"- **Capabilities:** {kg['stats']['capabilities']}")
    lines.append("")
    lines.append("## Per-Capability Breakdown")
    lines.append("")
    for cap, report in sorted(kg['capabilities'].items()):
        missing = report['missing']
        status = '✅' if not missing else f'⚠️'
        lines.append(f"- **{cap}**: {report['total_documents']} docs {status}")
        if missing:
            lines.append(f"  - Missing types: {', '.join(missing)}")
    lines.append("")
    lines.append("## Most Connected Documents")
    # Count connections per document
    connection_count = {}
    for edge in kg['edges']:
        connection_count[edge['source']] = connection_count.get(edge['source'], 0) + 1
        connection_count[edge['target']] = connection_count.get(edge['target'], 0) + 1
    top_docs = sorted(connection_count.items(), key=lambda x: -x[1])[:10]
    for doc, count in top_docs:
        node = kg['nodes'].get(doc, {})
        title = node.get('title', doc)
        lines.append(f"- **{title}**: {count} connections")

    return '\n'.join(lines)


@mcp.resource("knowledge://search?q={query}")
def search_documents(query: str) -> str:
    """Search documents by title, description, or path."""
    query = urllib.parse.unquote(query)
    kg = load_kg()
    if not kg:
        return "Knowledge graph not found. Run `make graph` first."

    q = query.lower()
    results = []

    for node_id, node in kg['nodes'].items():
        score = 0
        if q in node_id.lower():
            score += 3
        if q in node['title'].lower():
            score += 2
        if q in node['description'].lower():
            score += 1
        if score > 0:
            results.append((score, node_id, node))

    results.sort(key=lambda x: (-x[0], x[1]))

    if not results:
        return f"No results for '{query}'."

    lines = [f"# Search Results: '{query}'", ""]
    for score, node_id, node in results[:20]:
        title = node['title']
        desc = node.get('description', '')
        cap = node.get('capability', 'Unknown')
        dtype = node.get('type', 'unknown')
        lines.append(f"## [{title}](knowledge://document/{node_id})")
        lines.append(f"- **Path:** `{node_id}`")
        lines.append(f"- **Capability:** {cap}")
        lines.append(f"- **Type:** {dtype}")
        if desc:
            lines.append(f"- **Description:** {desc}")
        lines.append("")

    if len(results) > 20:
        lines.append(f"*... and {len(results) - 20} more results*")

    return '\n'.join(lines)


# ═════════════════════════════════════════════════════════════════════
# TOOLS
# ═════════════════════════════════════════════════════════════════════


@mcp.tool(
    name="generate-context-pack",
    description="Generate a condensed AI context pack from selected framework documents. "
                "Provide a capability name, document path, or search term.",
)
def generate_context_pack(
    term: str,
    max_docs: int = 10,
    depth: int = 1,
) -> str:
    """Generate a context pack for AI assistant consumption.

    Args:
        term: Capability name, document path, or search term
        max_docs: Maximum number of documents to include (default: 10)
        depth: How deep to follow cross-references (0 = seed docs only, default: 1)
    """
    kg = load_kg()
    if not kg:
        return "Knowledge graph not found. Run `make graph` first."

    # Resolve the term to document paths
    doc_paths = []

    # 1. Try as capability
    cap = find_capability(term, kg)
    if cap:
        report = kg['capabilities'][cap]
        for doc_type, paths in report['present'].items():
            doc_paths.extend(paths)
        header = f"📚 Capability: {cap} ({len(doc_paths)} documents)"
    else:
        # 2. Try as file path
        clean = term.lstrip('./')
        if clean in kg['nodes']:
            doc_paths = [clean]
            header = f"📄 Document: {clean}"
        else:
            # 3. Search
            q = term.lower()
            matches = [(n, n['title']) for n, node in kg['nodes'].items()
                       if q in n.lower() or q in node['title'].lower()]
            doc_paths = [m[0] for m in matches[:5]]
            if doc_paths:
                header = f"🔍 Search '{term}': {len(matches)} matches, using {len(doc_paths)}"
            else:
                return f"No documents found for '{term}'."

    if not doc_paths:
        return f"No documents found for '{term}'."

    # Follow cross-references if depth > 0
    if depth > 0:
        visited = set(doc_paths)
        queue = list(doc_paths)
        results = list(doc_paths)
        current_depth = 0

        # Build adjacency
        adj = {}
        for edge in kg['edges']:
            adj.setdefault(edge['source'], []).append(edge['target'])

        while queue and len(results) < max_docs:
            level_size = len(queue)
            for _ in range(level_size):
                path = queue.pop(0)
                if path in adj:
                    for neighbor in adj[path]:
                        if neighbor not in visited and len(results) < max_docs:
                            visited.add(neighbor)
                            results.append(neighbor)
                            queue.append(neighbor)
            current_depth += 1
            if current_depth >= depth:
                break

        doc_paths = results[:max_docs]

    # Build the context pack
    lines = [f"# Context Pack — {header}", ""]
    lines.append("> Auto-generated context for AI assistant consumption.")
    lines.append("")

    for doc_path in doc_paths:
        content = read_document(doc_path)
        if not content:
            continue

        node = kg['nodes'].get(doc_path, {})
        title = node.get('title', Path(doc_path).stem.replace('-', ' ').title())
        cap_name = node.get('capability', 'Unknown')
        doc_type = node.get('type', 'unknown')
        description = node.get('description', '')

        lines.append(f"## {title}")
        lines.append(f"- **Path:** `{doc_path}`")
        lines.append(f"- **Capability:** {cap_name}")
        lines.append(f"- **Type:** {doc_type}")
        if description:
            lines.append(f"- **Description:** {description}")
        lines.append("")

        # Extract key sections
        fm_match = re.match(r'^---\n.*?\n---\n', content, re.DOTALL)
        body_start = fm_match.end() if fm_match else 0
        body = content[body_start:]

        # Split by headings, keep first 100 lines max per doc
        heading_match = re.finditer(r'^(#{1,4})\s+(.*)', body, re.MULTILINE)
        sections = []
        prev_end = 0
        prev_level = 0
        prev_heading = "Preamble"

        for m in heading_match:
            if prev_heading and body[prev_end:m.start()].strip():
                sections.append((prev_level, prev_heading, body[prev_end:m.start()].strip()))
            prev_level = len(m.group(1))
            prev_heading = m.group(2).strip()
            prev_end = m.end()

        if prev_heading and body[prev_end:].strip():
            sections.append((prev_level, prev_heading, body[prev_end:].strip()))

        for level, heading, text in sections[:8]:
            if heading in ('Purpose', 'Preamble', 'Related Documents', 'Capability Map',
                           'Long-term Goal', 'Definition of Success'):
                continue
            # Truncate long sections
            text_lines = text.split('\n')
            if len(text_lines) > 20:
                text = '\n'.join(text_lines[:20]) + f'\n*... ({len(text_lines) - 20} more lines)*'
            lines.append(f"{'#' * (level + 2)} {heading}")
            lines.append("")
            lines.append(text)
            lines.append("")

    lines.append("---")
    lines.append(f"*Generated context pack: {len(doc_paths)} documents, "
                 f"{kg['stats']['total_connections']} cross-references available*")
    return '\n'.join(lines)


@mcp.tool(
    name="find-related-documents",
    description="Find documents related to a given document path via cross-references.",
)
def find_related_documents(path: str, max_results: int = 10) -> str:
    """Find documents related to the given path via knowledge graph cross-references.

    Args:
        path: Document path relative to repo root
        max_results: Maximum number of related documents (default: 10)
    """
    kg = load_kg()
    if not kg:
        return "Knowledge graph not found. Run `make graph` first."

    clean = path.lstrip('./').lstrip('/').rstrip('/')
    # Try with .md extension
    if not clean.endswith('.md'):
        candidates = [clean + '.md', clean + '/README.md']
    else:
        candidates = [clean]

    matched_path = None
    for c in candidates:
        if c in kg['nodes']:
            matched_path = c
            break

    if not matched_path:
        # Try partial match
        for n in kg['nodes']:
            if clean in n:
                matched_path = n
                break

    if not matched_path:
        return f"Document '{path}' not found in knowledge graph."

    node = kg['nodes'].get(matched_path, {})
    lines = [f"# Documents Related to: {node.get('title', matched_path)}", ""]
    lines.append(f"- **Path:** `{matched_path}`")
    lines.append(f"- **Capability:** {node.get('capability', 'Unknown')}")
    lines.append(f"- **Type:** {node.get('type', 'unknown')}")
    lines.append("")

    # Find outgoing edges
    outgoing = [e for e in kg['edges'] if e['source'] == matched_path][:max_results]
    if outgoing:
        lines.append("## References To")
        lines.append("")
        for edge in outgoing:
            target = kg['nodes'].get(edge['target'], {})
            title = target.get('title', edge['target'])
            desc = target.get('description', '')
            cap = target.get('capability', '')
            lines.append(f"- [{title}](knowledge://document/{edge['target']})")
            if desc:
                lines.append(f"  - {desc}")
            if cap:
                lines.append(f"  - *{cap}*")
            lines.append("")

    # Find incoming edges
    incoming = [e for e in kg['edges'] if e['target'] == matched_path][:max_results]
    if incoming:
        lines.append("## Referenced By")
        lines.append("")
        for edge in incoming:
            source = kg['nodes'].get(edge['source'], {})
            title = source.get('title', edge['source'])
            desc = source.get('description', '')
            cap = source.get('capability', '')
            lines.append(f"- [{title}](knowledge://document/{edge['source']})")
            if desc:
                lines.append(f"  - {desc}")
            if cap:
                lines.append(f"  - *{cap}*")
            lines.append("")

    if not outgoing and not incoming:
        lines.append("No cross-references found for this document.")

    return '\n'.join(lines)


@mcp.tool(
    name="search-knowledge",
    description="Search across all framework documents by title, description, and path.",
)
def search_knowledge(query: str, max_results: int = 10) -> str:
    """Search across all framework documents.

    Args:
        query: Search term to match against document titles, descriptions, and paths
        max_results: Maximum number of results (default: 10)
    """
    return search_documents(query)


@mcp.tool(
    name="capability-report",
    description="Get the capability completeness report showing which document types each capability has and is missing.",
)
def capability_report() -> str:
    """Get the capability completeness report."""
    kg = load_kg()
    if not kg:
        return "Knowledge graph not found. Run `make graph` first."

    lines = ["# Capability Completeness Report", ""]
    lines.append("| Capability | Docs | Status | Missing Types |")
    lines.append("|---|---|---|---|")
    for cap, report in sorted(kg['capabilities'].items()):
        missing = report['missing']
        status = '✅' if not missing else '⚠️'
        missing_str = ', '.join(missing) if missing else '—'
        lines.append(f"| {cap} | {report['total_documents']} | {status} | {missing_str} |")

    lines.append("")
    lines.append("## Document Types")
    lines.append("")
    lines.append("The framework defines 9 document types per capability:")
    lines.append("- **handbook**: Core principles and philosophy")
    lines.append("- **glossary**: Terminology definitions")
    lines.append("- **guide**: Practical how-to guidance")
    lines.append("- **playbook**: Repeatable workflows")
    lines.append("- **checklist**: Verification checklists")
    lines.append("- **template**: Reusable templates")
    lines.append("- **learning-path**: Structured learning progressions")
    lines.append("- **reference**: Quick-reference material")
    lines.append("- **ai-workflow**: AI-assisted workflow prompts")

    return '\n'.join(lines)


@mcp.tool(
    name="read-document",
    description="Read a specific document from the framework. Provide a path like 'handbooks/rails/README.md' or 'guides/engineering/testing-strategies'.",
)
def read_document_tool(path: str) -> str:
    """Read a specific document from the framework.

    Args:
        path: Document path relative to repo root (e.g., 'handbooks/rails/README.md', 'guides/engineering/testing-strategies')
    """
    return document_content(path)


# ═════════════════════════════════════════════════════════════════════
# PROMPTS
# ═════════════════════════════════════════════════════════════════════


@mcp.prompt(
    name="engineering-review",
    description="Generate a context pack for reviewing engineering work — code, design, or documentation.",
)
def engineering_review_prompt(review_type: str = "code", focus_area: str = "") -> str:
    """Template for engineering review context.

    Args:
        review_type: Type of review — 'code', 'design', or 'documentation' (default: code)
        focus_area: Optional specific area of focus (e.g., 'security', 'performance', 'testing')
    """
    return f"""I need you to review a {review_type} change.

First, use the knowledge://capabilities resource to find relevant engineering standards,
then use generate-context-pack with the appropriate capability to get focused context.

**Review type:** {review_type}
{f'**Focus area:** {focus_area}' if focus_area else ''}

**For code reviews**, consider:
- Engineering principles (clarity, separation of concerns, error handling)
- Code organization patterns
- Testing strategy and coverage
- Security implications

**For design reviews**, consider:
- Architectural principles and patterns
- Quality attributes (performance, scalability, maintainability)
- Trade-off analysis
- ADR documentation

**For documentation reviews**, consider:
- Writing principles (timeless, opinionated, practical)
- Style guide compliance
- Cross-referencing completeness
- AI-first readability

After the review, provide:
1. Summary of findings
2. Specific issues with suggested fixes
3. What was done well
4. Recommendations for follow-up
"""


@mcp.prompt(
    name="architecture-review",
    description="Generate a context pack for reviewing architectural decisions or system designs.",
)
def architecture_review_prompt(context: str = "") -> str:
    """Template for architecture review context.

    Args:
        context: Description of the architectural decision or system to review
    """
    return f"""I need you to review an architectural decision or system design.

Use the knowledge:// resources to load the Software Architecture capability,
including the handbook, ADR writing guide, and architectural patterns guide.

**Context:**
{context if context else '(Describe the system, decision, or design to review)'}

**Review against:**
1. **Architectural Principles**: Are the right patterns being applied?
2. **Quality Attributes**: How are performance, scalability, security, and maintainability addressed?
3. **Trade-offs**: Are trade-offs explicitly identified and documented?
4. **Documentation**: Is the architecture documented at the appropriate C4 level?
5. **Decision Records**: Are significant decisions captured as ADRs?

**Output format:**
- Architecture review summary
- Identified risks and concerns
- Recommendations prioritized by impact
- Suggested next steps
"""


@mcp.prompt(
    name="rails-development",
    description="Generate a context pack for Rails development tasks — building features, debugging, or reviewing.",
)
def rails_development_prompt(task: str = "", framework_version: str = "Rails 7.1+") -> str:
    """Template for Rails development context.

    Args:
        task: Description of the Rails development task
        framework_version: Rails version being used (default: Rails 7.1+)
    """
    return f"""I need help with a Rails development task.

Use the knowledge:// resources to load the Rails Engineering capability,
including the handbook, guides, and templates.

**Framework:** {framework_version}

**Task:**
{task if task else '(Describe the Rails development task)'}

**Before starting, check:**
1. **Rails conventions**: Follow Rails naming and structure conventions
2. **Service objects**: Extract complex operations from controllers/models
3. **Testing patterns**: Follow the Rails testing guide
4. **API design**: Use consistent versioning, serialization, and error formats
5. **Security**: Apply Brakeman-recommended patterns

**Provide:**
- Clean, convention-following code
- Tests following the project's testing patterns
- Documentation of any design decisions
- Migration strategy if applicable
"""


# ═════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════

def main():
    """Run the MCP server over stdio."""
    # Quick sanity check
    kg = load_kg()
    if not kg:
        print("⚠️  Knowledge graph not found. Run `make graph` first.", file=sys.stderr)
        print("   Server will start but some features may not work.", file=sys.stderr)

    print("🚀 Engineering Knowledge Framework MCP Server", file=sys.stderr)
    print(f"   Documents: {kg['stats']['total_documents'] if kg else 'N/A'}", file=sys.stderr)
    print(f"   Connections: {kg['stats']['total_connections'] if kg else 'N/A'}", file=sys.stderr)
    print("   Running over stdio...", file=sys.stderr)

    mcp.run(transport="stdio")


if __name__ == '__main__':
    main()
