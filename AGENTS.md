# AGENTS.md — Codex rules for this research repository

## Repository purpose
This repository is a reproducible research workspace for scientific data processing, ICP/Excel analysis, plotting, statistical analysis, and manuscript-support tasks.

## Core working principles
1. Preserve raw data. Never overwrite files under `data/raw/`.
2. Prefer reproducible scripts over manual editing.
3. Put cleaned/intermediate data under `data/interim/` or `data/processed/`.
4. Put publication figures under `results/figures/`.
5. Put result tables under `results/tables/`.
6. Put export-ready files for Origin, Excel, Word, or collaborators under `results/exports/`.
7. Keep manuscript notes, methods, and interpretation separate from raw numerical data.

## Python environment
Before analysis, use the repository environment:

```bash
python -m pip install -r requirements.txt
```

If a required package is missing, first check whether it belongs in `requirements.txt`. For common reusable research packages, add it there instead of relying only on a one-off `pip install`.

For environment verification:

```bash
python scripts/check_environment.py
```

## Excel / ICP data rules
- Read Excel files with `pandas` / `openpyxl`.
- Preserve original worksheets and raw values.
- Do not silently change units, sample names, decimal separators, or detection-limit notation.
- When calculating concentrations, dilution factors, recoveries, means, standard deviations, or RSD, make formulas explicit in code or output notes.
- Keep a traceable mapping from source columns to processed columns.
- If a value is missing, below detection limit, or ambiguous, flag it instead of inventing a value.
- Export processed datasets to a new file; never replace the original workbook unless explicitly requested.

## Plotting rules
- Use `matplotlib` by default.
- Figures should be publication-oriented: readable labels, explicit units, sensible aspect ratios, and vector output when possible.
- Save editable/vector figures as PDF or SVG when appropriate and high-resolution PNG for preview.
- Never smooth, fit, interpolate, or remove outliers unless explicitly justified.
- Preserve non-monotonic trends in experimental data.
- Keep source data for every final figure in `results/exports/` when practical.

## Statistical analysis
- State the sample size and statistical method.
- Distinguish descriptive statistics from inferential statistics.
- Do not claim significance without an appropriate test.
- Preserve replicate-level data whenever available.
- Report assumptions and limitations when they materially affect interpretation.

## Manuscript-support workflow
- Numerical claims in manuscript text must trace back to processed data or analysis outputs.
- Do not fabricate references, experimental conditions, uncertainty values, or instrument information.
- Keep interpretation separate from direct observation.
- For draft figures/tables intended for publication, use concise English labels unless instructed otherwise.
- Store manuscript-oriented notes in `docs/manuscript/`, methods in `docs/methods/`, and working notes in `docs/notes/`.

## Directory conventions
```text
data/
  raw/          original files; read-only in normal workflows
  external/     third-party/reference datasets
  interim/      temporary but meaningful transformed data
  processed/    analysis-ready datasets

scripts/
  data_processing/
  plotting/
  statistics/
  utils/

notebooks/      exploratory notebooks

results/
  figures/      final or near-final figures
  tables/       analysis tables
  exports/      Origin/Excel/CSV/other handoff files
  tmp/          disposable generated files

docs/
  methods/
  manuscript/
  notes/
```

## Coding style
- Prefer small, reusable scripts and functions.
- Use clear variable names and comments for scientific assumptions.
- Use relative paths based on the repository root.
- Avoid hard-coded machine-specific absolute paths.
- When possible, make scripts rerunnable from a clean checkout.
- Validate inputs before writing outputs.

## Change discipline
- Make minimal, task-focused changes.
- Do not delete or rename user data without explicit instruction.
- Summarize important generated files and assumptions after completing a task.
