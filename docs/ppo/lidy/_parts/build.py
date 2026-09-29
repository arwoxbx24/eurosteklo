#!/usr/bin/env python3
"""Сборка «Лидов» теперь общая: docs/ppo/build_all.py (код — docs/ppo/_common/build_proc.py)."""
import runpy
from pathlib import Path

runpy.run_path(str(Path(__file__).resolve().parents[2] / "build_all.py"), run_name="__main__")
