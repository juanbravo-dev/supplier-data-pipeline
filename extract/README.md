# Supplier Data Pipeline — Extraction Stage

This project extracts monthly supplier consumption reports from raw CSV files.

## Features

- Read supplier CSV reports with European formatting (semicolon `;` delimiter, comma `,` decimal)

- Dynamic month input via CLI (e.g., `january`, `february`, etc.)

- Month name validation to prevent typos

- Logging all actions to console for traceability

## Folder Structure

```
supplier-data-pipeline/
├── extract/
│   └── extract.py
├── data/
│   └── [location of input CSV files]
├── output/
│   └── [your extracted cleaned CSVs here]
├── README.md
└── .gitignore
```

## How to Run

1. Open your terminal in the project root.
2. Run the extractor script with a valid month name:

```bash
python extract/extract.py january
```

3. If the month is invalid, the script will exit and show a helpful error message.

Example:

```bash
python extract/extract.py Ferbury
# Output: ❌ Invalid month name: 'ferbury'. Valid options: ['april', 'august', ..., 'september']
```

## Requirements

- Python 3.9+
- pandas (install with `pip install pandas`)

## Logging

All actions (reading, saving, success, errors) are logged to the console using Python's built-in `logging` module.

## Author

Juan Bravo — [GitHub Profile](https://github.com/juanbravo-dev)
