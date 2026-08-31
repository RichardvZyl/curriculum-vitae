# AGENTS.md

Canonical agent entry for the public CV/portfolio repo.

- How an AI should collaborate with Richard: `AI-CONTEXT.md`
- Public profile / CV / skills: `PROFILE.md`, `CV.md`, `SKILLSMATRIX.md`
- Public project list: `PROJECTS.md` (public remotes only)
- Private inventory: `PROJECTS.private.md` (git-ignored). Never copy private/client detail into public files.

This repository is PUBLIC. Other agent files in this folder (`CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`) reference this file rather than duplicating it.

## Memory and workspace context (Perseus)

- **Vault** (shared across clients on this machine): `perseus_vault_*` MCP tools. Session start: `perseus_vault_context`. Durable facts: `perseus_vault_remember`. No secrets. Never remember anything that cannot appear in a public repo.
- **Context Engine** (this repo only): `perseus` MCP tools and `.perseus/context.md`. Do not reuse another project's briefing.