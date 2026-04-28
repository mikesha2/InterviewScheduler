# Interview Scheduler

An optimal interview scheduling tool using the Hungarian algorithm to match candidates to available dates, with support for priority weighting and duplicate-date detection.

## Features

- **Optimal Matching**: Uses the Hungarian algorithm (`scipy.optimize.linear_sum_assignment`) to find the globally optimal assignment of interviews to dates
- **Priority Weighting**: Each interview can have an optional priority score (defaults to 1) to influence matching preference
- **Duplicate-Date Detection**: Automatically alerts when multiple interviews are assigned to the same date
- **Dual Interface**: 
  - CLI (`schedule.py`) for command-line usage
  - Web UI (`index.html`) with browser-based Pyodide Python runtime

## Usage

### CLI

```bash
python schedule.py < input.csv
```

Format: `name, date1, date2, ..., priority (optional)`

Example:
```csv
A,1/23,1/28,2
B,1/8,1/22,1/30
C,1/7,1/9,1/12,1/13
```

### Web UI

Open `index.html` in a browser. Paste CSV data or upload a file, then click **Run Scheduler**.

## CSV Format

| Column | Description | Required |
|--------|-------------|----------|
| Name | Interview identifier | Yes |
| Dates | Comma-separated available dates | Yes (≥1) |
| Priority | Numeric weight (higher = more important) | No (defaults to 1) |

## Output

- **Assigned**: Each interview matched to a preferred date
- **Unassigned**: Interviews with no matching date
- **Notes**: Alerts if multiple interviews share the same date

## License

CC BY 4.0 — Copyright (c) 2026 Congzhou M Sha (consha@sas.upenn.edu)