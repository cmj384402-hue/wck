"""Check the core scientific Python environment used by this repository."""

from importlib import import_module

PACKAGES = [
    "numpy",
    "pandas",
    "scipy",
    "matplotlib",
    "openpyxl",
    "xlsxwriter",
    "sklearn",
    "statsmodels",
    "sympy",
    "PIL",
]

failed = []

for package in PACKAGES:
    try:
        module = import_module(package)
        version = getattr(module, "__version__", "installed")
        print(f"[OK] {package}: {version}")
    except Exception as exc:
        failed.append((package, str(exc)))
        print(f"[MISSING] {package}: {exc}")

if failed:
    raise SystemExit(
        "\nEnvironment check failed. Run: python -m pip install -r requirements.txt"
    )

print("\nScientific Python environment ready.")
