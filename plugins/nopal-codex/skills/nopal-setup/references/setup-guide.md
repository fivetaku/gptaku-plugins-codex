# nopal Setup Guide for Codex

Use this when `gws` is missing or not authenticated.

## Install

```bash
npm install -g @googleworkspace/cli
gws --version
```

## Auth check

```bash
gws auth status
```

## Interactive setup

If authentication is missing, the user must run:

```bash
gws auth setup
gws auth login
```

If plain credentials are needed for headless execution:

```bash
gws auth export --unmasked 2>/dev/null | grep -v '^Using keyring' > ~/.config/gws/credentials.json
```

## Important rule

Do not pretend the interactive setup can be completed automatically from a non-interactive Codex turn.

