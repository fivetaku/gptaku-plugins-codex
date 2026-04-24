# docs-guide Knowledge Base for Codex

This skill is for official documentation retrieval, not general web search.

## Core idea

Use live documentation so answers are grounded in the current official source instead of model memory.

## Preferred retrieval order

1. known `llms.txt` URL
2. official-site `llms.txt`
3. official GitHub docs source
4. `sitemap.xml` or platform-specific search index
5. official-domain search as a last resort

## When to use

- library APIs
- setup or configuration
- migration guides
- version-specific behavior
- official terminology or exact supported syntax

## When not to use

- basic programming syntax
- generic CS explanations with no library/version dependency
- broad architecture advice with no primary-source need

## Citation rule

Always cite the URL used.

If the answer depends on a specific version, say which version you inferred or fetched.

