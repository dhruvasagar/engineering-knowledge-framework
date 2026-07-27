#!/usr/bin/env python3
"""
Knowledge Graph Generator — Extract cross-references and build a
machine-readable knowledge graph of document relationships.

Outputs:
- knowledge-graph.json: Full graph (nodes + edges) for visualization
- knowledge-graph.dot: Graphviz DOT format for rendering
- capability-report.json: Per-capability document type completeness

Usage:
    python3 tools/build-knowledge-graph.py
    python3 tools/build-knowledge-graph.py --format dot
    python3 tools/build-knowledge-graph.py --format json
"""

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

LINK_PATTERN = re.compile(r'\[\[file:([^\]]+)\]\[([^\]]*)\]\]')
HEADING_PATTERN = re.compile(r'^#\+TITLE:\s*(.*)', re.MULTILINE)
DESCRIPTION_PATTERN = re.compile(r'^#\+DESCRIPTION:\s*(.*)', re.MULTILINE)

# Document types by directory
DOC_TYPE_MAP = {
    'handbooks': 'handbook',
    'guides': 'guide',
    'playbooks': 'playbook',
    'checklists': 'checklist',
    'templates': 'template',
    'learning-paths': 'learning-path',
    'references': 'reference',
    'glossary': 'glossary',
    'prompts': 'ai-workflow',
    'adr': 'adr',
}

# Capability mapping by directory prefix
CAPABILITY_MAP = {
    'engineering': 'Engineering Fundamentals',
    'architecture': 'Software Architecture',
    'rails': 'Rails Engineering',
    'security': 'Security Engineering',
    'ai': 'AI Engineering',
    'quality': 'Engineering Quality',
    'accessibility': 'Accessibility Engineering',
}


def collect_org_files():
    """Collect all .md files."""
    org_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        if '.git' in root.split(os.sep):
            continue
        if 'tools' in root.split(os.sep):
            continue
        for f in files:
            if f.endswith('.md'):
                org_files.append(Path(root) / f)
    return org_files


def classify_file(filepath):
    """Classify a file by capability and document type."""
    rel_path = filepath.relative_to(REPO_ROOT)
    parts = rel_path.parts

    capability = None
    doc_type = None

    # Determine document type from directory
    for dir_name, dtype in DOC_TYPE_MAP.items():
        if dir_name in parts:
            doc_type = dtype
            break

    # Determine capability
    for cap_dir, cap_name in CAPABILITY_MAP.items():
        if cap_dir in parts:
            capability = cap_name
            break

    # Root-level files are governance
    if len(parts) == 1 and parts[0].endswith('.md'):
        capability = 'Governance'
        doc_type = 'governance'

    # ADRs
    if doc_type == 'adr':
        capability = 'Software Architecture'

    return capability, doc_type


def extract_metadata(filepath):
    """Extract title and description from an org file."""
    content = filepath.read_text(encoding='utf-8', errors='ignore')

    title_match = HEADING_PATTERN.search(content)
    desc_match = DESCRIPTION_PATTERN.search(content)

    title = title_match.group(1).strip() if title_match else filepath.stem
    description = desc_match.group(1).strip() if desc_match else ''

    return title, description


def extract_links(filepath):
    """Extract all [[file:...][...]] references from a file."""
    content = filepath.read_text(encoding='utf-8', errors='ignore')
    links = []

    for match in LINK_PATTERN.finditer(content):
        target = match.group(1)
        text = match.group(2)

        # Skip external links
        if target.startswith('http://') or target.startswith('https://'):
            continue

        links.append({'target': target, 'text': text})

    return links


def resolve_link(doc_path, link_target):
    """Resolve a link target to a relative path from repo root."""
    doc_dir = doc_path.parent
    resolved = (doc_dir / link_target).resolve()

    # Try relative to repo root
    if not resolved.exists():
        resolved = (REPO_ROOT / link_target).resolve()

    if resolved.exists():
        try:
            return str(resolved.relative_to(REPO_ROOT))
        except ValueError:
            return None
    return None


def build_graph():
    """Build the complete knowledge graph."""
    org_files = collect_org_files()
    nodes = {}
    edges = []
    capabilities = defaultdict(lambda: defaultdict(list))

    # Create nodes
    for filepath in org_files:
        rel_path = str(filepath.relative_to(REPO_ROOT))
        title, description = extract_metadata(filepath)
        capability, doc_type = classify_file(filepath)

        nodes[rel_path] = {
            'id': rel_path,
            'title': title,
            'description': description,
            'capability': capability,
            'type': doc_type or 'unknown',
            'path': rel_path,
        }

        if capability and doc_type:
            capabilities[capability][doc_type].append(rel_path)

    # Create edges from links
    for filepath in org_files:
        rel_path = str(filepath.relative_to(REPO_ROOT))
        links = extract_links(filepath)

        for link in links:
            resolved = resolve_link(filepath, link['target'])
            if resolved and resolved in nodes:
                edges.append({
                    'source': rel_path,
                    'target': resolved,
                    'text': link['text'],
                })

    # Build capability completeness report
    all_doc_types = set(DOC_TYPE_MAP.values())
    capability_report = {}
    for cap, types in sorted(capabilities.items()):
        present = set(types.keys())
        missing = all_doc_types - present
        capability_report[cap] = {
            'present': dict(types),
            'missing': sorted(missing),
            'total_documents': sum(len(v) for v in types.values()),
        }

    return {
        'nodes': nodes,
        'edges': edges,
        'stats': {
            'total_documents': len(nodes),
            'total_connections': len(edges),
            'capabilities': len(capability_report),
        },
        'capabilities': capability_report,
    }


def export_json(graph, output_path):
    """Export graph as JSON."""
    with open(output_path, 'w') as f:
        json.dump(graph, f, indent=2)
    return output_path


def export_dot(graph, output_path):
    """Export graph as Graphviz DOT format."""
    with open(output_path, 'w') as f:
        f.write('digraph KnowledgeGraph {\n')
        f.write('  rankdir=LR;\n')
        f.write('  node [shape=box, style=rounded];\n\n')

        # Color by capability
        colors = {
            'Governance': '#4A90D9',
            'Engineering Fundamentals': '#7B68EE',
            'Software Architecture': '#2ECC71',
            'Rails Engineering': '#E74C3C',
            'Security Engineering': '#E67E22',
            'AI Engineering': '#9B59B6',
            'Engineering Quality': '#1ABC9C',
            'Accessibility Engineering': '#3498DB',
        }

        for node_id, node in graph['nodes'].items():
            cap = node['capability'] or 'Unknown'
            color = colors.get(cap, '#95A5A6')
            label = node['title'].replace('"', '\\"')
            f.write(f'  "{node_id}" [label="{label}", fillcolor="{color}", style=filled, fontcolor=white];\n')

        f.write('\n')

        for edge in graph['edges']:
            f.write(f'  "{edge["source"]}" -> "{edge["target"]}";\n')

        f.write('}\n')

    return output_path


def main():
    fmt = 'json'
    if '--format' in sys.argv:
        idx = sys.argv.index('--format')
        if idx + 1 < len(sys.argv):
            fmt = sys.argv[idx + 1]

    print("🕸️  Knowledge Graph Generator")
    print(f"   Scanning {REPO_ROOT}...\n")

    graph = build_graph()

    print(f"   Documents: {graph['stats']['total_documents']}")
    print(f"   Connections: {graph['stats']['total_connections']}")
    print(f"   Capabilities: {graph['stats']['capabilities']}")
    print()

    # Print capability completeness
    for cap, report in sorted(graph['capabilities'].items()):
        missing = report['missing']
        status = '✅' if not missing else f'⚠️  missing: {", ".join(missing)}'
        print(f"   {cap}: {report['total_documents']} docs {status}")
    print()

    output_dir = REPO_ROOT / 'tools' / 'output'
    output_dir.mkdir(parents=True, exist_ok=True)

    if fmt == 'json' or fmt == 'all':
        path = export_json(graph, output_dir / 'knowledge-graph.json')
        print(f"   JSON: {path}")

    if fmt == 'dot' or fmt == 'all':
        path = export_dot(graph, output_dir / 'knowledge-graph.dot')
        print(f"   DOT: {path}")

    # Always generate capability report
    report_path = output_dir / 'capability-report.json'
    with open(report_path, 'w') as f:
        json.dump(graph['capabilities'], f, indent=2)
    print(f"   Capability Report: {report_path}")

    print("\n✅ Knowledge graph generated!")


if __name__ == '__main__':
    main()
