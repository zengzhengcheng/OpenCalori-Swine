# OpenCalori-Swine

OpenCalori-Swine is a desktop GUI tool for pig heat-production calculation.

## What It Does

- Loads indoor and outdoor chamber `.xls` data
- Computes heat-production outputs from paired gas-exchange records
- Exports highlighted `.xlsx` result files and `.txt` warning summaries
- Supports a redesigned UI with Chinese / English switching

## Main Entrypoint

Run:

```bash
python newhello.py
```

`newhello.py` keeps the calculation workflow, while the UI is loaded dynamically from `mainwindow.ui`.

## Dependencies

- Python 3.8+
- PySide6
- pandas
- numpy
- xlsxwriter
- xlrd
