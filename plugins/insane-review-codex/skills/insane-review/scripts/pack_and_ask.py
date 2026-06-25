#!/usr/bin/env python3
"""Skill-local wrapper for the plugin-level pack_and_ask helper."""
from __future__ import annotations

import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
runpy.run_path(str(ROOT / "scripts" / "pack_and_ask.py"), run_name="__main__")
