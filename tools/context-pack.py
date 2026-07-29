#!/usr/bin/env python3
"""
Context Pack Generator — Generate condensed AI context packs from
Engineering Knowledge Framework documents.

Uses the knowledge graph to find documents and their related
cross-references, extracting key content for AI assistant context.

Usage:
    python3 tools/context-pack.py <capability|path|search-term>
    python3 tools/context-pack.py rails --depth 2 --max-docs 15
    python3 tools/context-pack.py guides/engineering/testing-strategies.md
    python3 tools/context-pack.py "Rails Engineering" --format json
    python3 tools/context-pack.py --list-capabilities

Options:
    --depth N         How deep to follow cross-references (default: 1)
    --max-docs N      Maximum documents in the pack (default: 12)
    --format FMT      Output format: markdown (default) or json
    --output FILE     Write to file instead of stdout
    --include PATH    Additional document paths to include (can repeat)
    --exclude PATH    Document paths to exclude (can repeat)
    --list-capabilities  List all capabilities and exit
"""

import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
KG_PATH = REPO_ROOT / 'tools' / 'output' / 'knowledge-graph.json'

# Section heading pattern for extracting content
HEADING_PATTERN = re.compile(r'^(#{1,6})\s+(.*)', re.MULTILINE)
# Front matter patterns
FM_PATTERN = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)
FM_TITLE_PATTERN = re.compile(r'^title:\s*"?([^"\\n]+)"?\\s*$', re.MULTILINE)
FM_DESC_PATTERN = re.compile(r'^description:\s*"?([^"\\n]+)"?\\s*$', re.MULTILINE)

# Capability names from the knowledge graph
CAPABILITIES = {
    'ai engineering': 'AI Engineering',
    'accessibility engineering': 'Accessibility Engineering',
    'engineering fundamentals': 'Engineering Fundamentals',
    'engineering quality': 'Engineering Quality',
    'rails engineering': 'Rails Engineering',
    'security engineering': 'Security Engineering',
    'software architecture': 'Software Architecture',
    'governance': 'Governance',
}

SKIP_DIRS_IN_PACK = {'tools', 'site', 'docs', 'assets', '.git', '__pycache__', '.org-backup'}


def load_knowledge_graph():
    """Load the knowledge graph JSON."""
    if not KG_PATH.exists():
        print(f"❌ Knowledge graph not found at {KG_PATH}", file=sys.stderr)
        print("   Run: make graph", file=sys.stderr)
        sys.exit(1)
    with open(KG_PATH) as f:
        return json.load(f)


def list_capabilities():
    """Print all capabilities and their document counts."""
    kg = load_knowledge_graph()
    print("Available Capabilities:")
    print()
    for cap, report in sorted(kg['capabilities'].items()):
        missing = report['missing']
        status = '✅ complete' if not missing else f'⚠️  missing: {", ".join(missing)}'
        print(f"  {cap}: {report['total_documents']} docs — {status}")
    print()
    print("Usage: python3 tools/context-pack.py \"<capability name>\"")
    sys.exit(0)


def resolve_capability(term, kg):
    """Resolve a search term to a capability name or None."""
    term_lower = term.lower().strip()
    # Direct match
    if term_lower in CAPABILITIES:
        return CAPABILITIES[term_lower]
    # Fuzzy match
    for key, name in CAPABILITIES.items():
        if term_lower in key or key in term_lower:
            return name
    return None


def find_documents_by_capability(capability_name, kg):
    """Get all document paths for a capability."""
    docs = []
    if capability_name in kg['capabilities']:
        report = kg['capabilities'][capability_name]
        for doc_type, paths in report['present'].items():
            docs.extend(paths)
    return docs


def find_documents_by_search(term, kg):
    """Find documents matching a search term in title or path."""
    term_lower = term.lower()
    matches = []
    for node_id, node in kg['nodes'].items():
        if term_lower in node['title'].lower() or term_lower in node_id.lower():
            matches.append(node_id)
    return matches


def find_related_documents(doc_paths, kg, depth=1, max_docs=12, exclude=None):
    """Find documents related to the given paths via cross-references.

    Uses BFS up to `depth` levels of indirection through the knowledge graph.
    """
    if exclude is None:
        exclude = set()

    visited = set(doc_paths)
    queue = list(doc_paths)
    results = OrderedDict()

    # Build adjacency: for each node, collect outgoing edges
    adjacency = {}
    for edge in kg['edges']:
        src = edge['source']
        tgt = edge['target']
        if src not in adjacency:
            adjacency[src] = []
        adjacency[src].append((tgt, edge['text']))

    # BFS from seed documents
    current_depth = 0
    while queue and len(results) < max_docs:
        level_size = len(queue)
        for _ in range(level_size):
            path = queue.pop(0)
            if path in exclude:
                continue
            if path in results:
                continue
            results[path] = {'depth': current_depth}

            if current_depth < depth and path in adjacency:
                for neighbor, link_text in adjacency[path]:
                    if neighbor not in visited and len(results) < max_docs:
                        visited.add(neighbor)
                        queue.append(neighbor)
        current_depth += 1

    return list(results.keys())


def extract_sections(content, max_sections=20):
    """Extract sections from document content with their heading and text.

    Returns a list of (heading_level, heading_text, body_text) tuples.
    """
    lines = content.split('\n')
    sections = []
    current_heading_level = 0
    current_heading = 'Preamble'
    current_body = []

    # Skip front matter
    body_start = 0
    fm_match = FM_PATTERN.match(content)
    if fm_match:
        body_start = fm_match.end()

    for i, line in enumerate(lines):
        if i < body_start:
            continue
        match = HEADING_PATTERN.match(line)
        if match:
            # Save previous section
            if current_body:
                body = '\n'.join(current_body).strip()
                if body:
                    sections.append((current_heading_level, current_heading, body))
            current_heading_level = len(match.group(1))
            current_heading = match.group(2).strip()
            current_body = []
        else:
            current_body.append(line)

    # Save last section
    if current_body:
        body = '\n'.join(current_body).strip()
        if body:
            sections.append((current_heading_level, current_heading, body))

    return sections[:max_sections]


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
    fm_match = FM_PATTERN.match(content)
    if not fm_match:
        return None, None
    fm = fm_match.group(1)
    title = None
    description = None
    for line in fm.split('\n'):
        t_match = FM_TITLE_PATTERN.match(line)
        if t_match:
            title = t_match.group(1).strip()
        d_match = FM_DESC_PATTERN.match(line)
        if d_match:
            description = d_match.group(1).strip()
    return title, description


def condense_section(heading_level, heading, body, max_lines=15):
    """Condense a section to its essential content."""
    lines = body.split('\n')
    # Remove empty lines at start/end
    while lines and not lines[0].strip():
        lines = lines.pop(0)
    while lines and not lines[-1].strip():
        lines = lines.pop()

    # For lists and checklists, keep all items
    list_items = [l for l in lines if l.strip().startswith('- ') or l.strip().startswith('* [')]
    if list_items and len(list_items) == len([l for l in lines if l.strip()]):
        return '\n'.join(lines)

    # For short content, keep all
    if len(lines) <= max_lines:
        return '\n'.join(lines)

    # For longer content, keep first few lines + summary
    kept = lines[:max_lines]
    kept.append(f'\n*... ({len(lines) - max_lines} more lines)*')
    return '\n'.join(kept)


def generate_context_pack(doc_paths, kg, depth=1, max_docs=12, exclude=None):
    """Generate a context pack for the given documents.

    Returns a structured dict with the context pack content.
    """
    if exclude is None:
        exclude = set()

    # Find related documents
    all_docs = find_related_documents(doc_paths, kg, depth, max_docs, exclude)

    pack = {
        'metadata': {
            'generated_by': 'Engineering Knowledge Framework Context Pack Generator',
            'total_documents': len(all_docs),
            'seed_documents': doc_paths,
            'reference_depth': depth,
        },
        'documents': [],
    }

    for doc_path in all_docs:
        content = read_document(doc_path)
        if content is None:
            continue

        title, description = extract_front_matter(content)
        if not title:
            # Use filename as fallback
            title = Path(doc_path).stem.replace('-', ' ').title()

        node = kg['nodes'].get(doc_path, {})
        capability = node.get('capability', 'Unknown')
        doc_type = node.get('type', 'unknown')

        sections = extract_sections(content)
        condensed_sections = []

        for level, heading, body in sections:
            condensed = condense_section(level, heading, body)
            condensed_sections.append({
                'level': level,
                'heading': heading,
                'content': condensed,
            })

        doc_entry = {
            'path': doc_path,
            'title': title,
            'description': description or node.get('description', ''),
            'capability': capability,
            'type': doc_type,
            'sections': condensed_sections,
        }
        pack['documents'].append(doc_entry)

    return pack


def format_markdown(pack):
    """Format context pack as a markdown document."""
    lines = []
    lines.append(f"# Context Pack — {pack['metadata']['total_documents']} documents")
    lines.append('')
    lines.append('> Auto-generated context pack for AI assistant consumption.')
    lines.append('> Use this to provide focused, relevant context from the')
    lines.append('> Engineering Knowledge Framework.')
    lines.append('')
    lines.append(f"- **Seed documents:** {', '.join(pack['metadata']['seed_documents'])}")
    lines.append(f"- **Reference depth:** {pack['metadata']['reference_depth']}")
    lines.append(f"- **Total documents:** {pack['metadata']['total_documents']}")
    lines.append('')

    for doc in pack['documents']:
        lines.append(f"## {doc['title']}")
        lines.append('')
        lines.append(f"- **Path:** `{doc['path']}`")
        lines.append(f"- **Capability:** {doc['capability']}")
        lines.append(f"- **Type:** {doc['type']}")
        if doc['description']:
            lines.append(f"- **Description:** {doc['description']}")
        lines.append('')

        for section in doc['sections']:
            if section['heading'] in ('Purpose', 'Preamble', 'Related Documents'):
                # Skip boilerplate sections to save space
                continue
            if section['heading'] == doc['title']:
                continue

            lines.append(f"{'#' * (section['level'] + 2)} {section['heading']}")
            lines.append('')
            lines.append(section['content'])
            lines.append('')

    return '\n'.join(lines)


def main():
    args = sys.argv[1:]

    if not args or '--help' in args or '-h' in args:
        print(__doc__.strip())
        sys.exit(0)

    if '--list-capabilities' in args:
        list_capabilities()

    # Parse options
    depth = 1
    max_docs = 12
    fmt = 'markdown'
    output = None
    include = []
    exclude = []

    # Parse options — collect all positional args at end
    remaining = []
    i = 0
    while i < len(args):
        if args[i] == '--depth' and i + 1 < len(args):
            depth = int(args[i + 1])
            i += 2
        elif args[i] == '--max-docs' and i + 1 < len(args):
            max_docs = int(args[i + 1])
            i += 2
        elif args[i] == '--format' and i + 1 < len(args):
            fmt = args[i + 1]
            i += 2
        elif args[i] == '--output' and i + 1 < len(args):
            output = args[i + 1]
            i += 2
        elif args[i] == '--include' and i + 1 < len(args):
            include.append(args[i + 1])
            i += 2
        elif args[i] == '--exclude' and i + 1 < len(args):
            exclude.append(args[i + 1])
            i += 2
        else:
            # Positional argument: the search term / capability / path
            remaining.append(args[i])
            i += 1

    if not remaining:
        print("❌ Missing search term. Use --help for usage.", file=sys.stderr)
        sys.exit(1)

    term = remaining[0]

    # Load knowledge graph
    kg = load_knowledge_graph()

    # Resolve the term
    doc_paths = []

    # 1. Try as a capability name
    capability = resolve_capability(term, kg)
    if capability:
        doc_paths = find_documents_by_capability(capability, kg)
        print(f"📚 Capability: {capability} ({len(doc_paths)} documents)", file=sys.stderr)
    else:
        # 2. Try as a file path
        # Strip leading ./ if present
        clean_term = term[2:] if term.startswith('./') else term
        if clean_term in kg['nodes']:
            doc_paths = [clean_term]
            print(f"📄 Document: {clean_term}", file=sys.stderr)
        else:
            # 3. Try as a partial path
            matches = [n for n in kg['nodes'] if clean_term in n]
            if matches:
                doc_paths = matches[:5]  # Limit to 5 matches
                print(f"🔍 Found {len(matches)} matches, using top {len(doc_paths)}", file=sys.stderr)
                for m in doc_paths:
                    print(f"   - {m}", file=sys.stderr)
            else:
                # 4. Try as a search term
                doc_paths = find_documents_by_search(term, kg)
                if doc_paths:
                    doc_paths = doc_paths[:5]
                    print(f"🔍 Search '{term}': {len(doc_paths)} matches", file=sys.stderr)
                    for m in doc_paths:
                        print(f"   - {m}", file=sys.stderr)
                else:
                    print(f"❌ No documents found for '{term}'", file=sys.stderr)
                    sys.exit(1)

    # Add included documents
    for inc in include:
        clean_inc = inc[2:] if inc.startswith('./') else inc
        if clean_inc in kg['nodes']:
            if clean_inc not in doc_paths:
                doc_paths.append(clean_inc)
                print(f"➕ Included: {clean_inc}", file=sys.stderr)
        else:
            print(f"⚠️  Include path not found: {clean_inc}", file=sys.stderr)

    # Generate context pack
    pack = generate_context_pack(
        doc_paths,
        kg,
        depth=depth,
        max_docs=max_docs,
        exclude=set(exclude),
    )

    if fmt == 'json':
        output_content = json.dumps(pack, indent=2)
    else:
        output_content = format_markdown(pack)

    if output:
        out_path = Path(output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output_content, encoding='utf-8')
        print(f"\n✅ Context pack written to {out_path}", file=sys.stderr)
        print(f"   {pack['metadata']['total_documents']} documents in pack", file=sys.stderr)
    else:
        print(output_content)


if __name__ == '__main__':
    main()
