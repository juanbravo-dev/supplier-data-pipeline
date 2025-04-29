# Supplier Data Pipeline — Extraction Stage

This project extracts monthly supplier consumption reports from raw CSV files.

## Features

- Read supplier CSV reports with European formatting (semicolon `;` delimiter, comma `,` decimal)

- Dynamic month input via CLI (e.g., `january`, `february`, etc.)

- Month name validation to prevent typos

- Logging all actions to both console and 'extractor.log' for traceability

- Safe file management using Pathlib



## Folder Structure

```
supplier-data-pipeline/
├── extract/
│   └── extract.py
├── data/
│   └── [source CSV files go here]
├── output/
│   └── [cleaned files saved here]
├── extractor.log  # (created at runtime)
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

All actions (reading, saving, success, errors) are logged in two places:
    - Console 
    - 'extractor.log' file

## Author

Juan Bravo — [GitHub Profile](https://github.com/juanbravo-dev)
