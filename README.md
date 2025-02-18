**README.md**

# arb-xl

arb-xl is a CLI tool that converts translation files between JSON, XLS, and ARB formats. It helps manage localization files efficiently, especially for Flutter projects.

## Installation

```sh
pip install arb-xl
```

## Usage

Convert JSON files to an Excel file:
```sh
arb-xl j2x output.xlsx en.json ar.json
```

Convert an Excel file back to JSON files:
```sh
arb-xl x2j translations.xlsx output_dir/
```

Convert an Excel file to ARB format:
```sh
arb-xl x2j translations.xlsx output_dir/ --arb
```

For help:
```sh
arb-xl --help
```

## Features
- Convert JSON translation files to an XLS file for easy editing.
- Convert XLS files back to JSON or ARB format.
- Handles multiple languages efficiently.
- Logs errors and warnings.

---



