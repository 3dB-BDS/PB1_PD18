# PB1_PD18
**Author:** 3dB-BDS

---

## Description
This project is intended for learning CI.

---

## Files
- **.gitignore** – Config file specifying files Git should ignore
- **kalkulators.py** – Main file, contains function `saskaitit` that summs two numbers together.
- **test_kalkulators.py** – Tests file `kalkulators.py`
- **README.md** – This file

---

## How to Start
1. Install Python 3.8+
2. Copy files to project folder
3. Import `kalkulators.py` to your project and use function `saskaitit(a, b)`

---

## Example

```python
from kalkulators import saskaitit

a = 2
b = 3
result = saskaitit(a, b)
print(f"By summing together {a} and {b} result is {result}")
```

---

## Used Technology

- Python: 3.8+
- Git: 2.53.0.windows.1
- GitHub

---

## Definition of Done

Task is done if:
- function works
- tests passes
- CI is green
- Issue is marked Done