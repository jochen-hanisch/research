"""Editor-friendly wrapper for the Modellpruefung module.

Purpose:
- Makes `import modellpruefung` resolvable for Pylance by providing a
  top-level module next to `simulation-bildungswirkgefuege.py`.
- For runtime, re-exports everything from the real module located at
  `Modellpruefung/modellpruefung.py`.
"""

from __future__ import annotations

# Prefer a package-relative import (helps static analyzers like Pylance)
try:  # when imported within the package context
    from .Modellpruefung.modellpruefung import *  # type: ignore[F401,F403]
except Exception:
    # Fallback for direct script execution where relative imports may fail
    import importlib.util
    import os
    from types import ModuleType

    _base_dir = os.path.dirname(__file__)
    _real_path = os.path.join(_base_dir, "Modellpruefung", "modellpruefung.py")

    spec = importlib.util.spec_from_file_location("_modellpruefung_impl", _real_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Kann Modul nicht laden: {_real_path}")

    _mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(_mod)  # type: ignore[assignment]

    # Re-export public attributes
    for _name in dir(_mod):
        if not _name.startswith("_"):
            globals()[_name] = getattr(_mod, _name)
