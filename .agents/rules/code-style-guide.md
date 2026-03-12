---
trigger: always_on
glob:
description: Python code style guide based on PEP 8 and App Academy best practices
---

# Python Code Style Guide

> Reference: [8 Python Coding Best Practices — App Academy](https://track.appacademy.io/blog/python-coding-best-practices)

---

## 1. Formatting & Syntax (PEP 8)

### Indentation
- Use **4 spaces** per indentation level — never tabs.
- Be consistent from start to finish.

### Line Length & Spacing
- Keep lines ≤ **79 characters** (up to 99–119 acceptable with team agreement).
- Use parentheses, brackets, or backslashes for line breaks on long statements.
- Separate **top-level** functions/classes with **two** blank lines.
- Separate **methods** within a class with **one** blank line.
- Use blank lines sparingly elsewhere.

### Whitespace
- Use spaces around binary operators (`=`, `==`, `+`, etc.).
- **No** extra spaces inside brackets or before commas/colons.
- **No** trailing whitespace on any line.

### Comments
- Explain **why**, not **what**.
- Keep comments up-to-date; outdated comments are worse than none.
- Use **docstrings** (see §2) for modules, functions, classes, and methods.
- Inline comments: separated by **≥ 2 spaces**, starting with `# `.

### Enforcement Tools
- **Linters:** Pylint, Flake8
- **Auto-formatters:** Black, YAPF

---

## 2. Documentation

- Write **docstrings** for all public modules, functions, classes, and methods ([PEP 257](https://peps.python.org/pep-0257/)).
- Keep docstrings in sync with the code they describe.
- Use **type hints** (Python 3.5+) for function signatures.
- Include usage **examples** for complex functions.
- Don't be redundant — skip docstrings for trivially obvious code.

---

## 3. Testing

- **Write tests early and often**; prefer TDD (test-driven development).
- Each test should verify **a single behavior**.
- Use a **consistent** testing framework across the project (`pytest` or `unittest`).
- **Automate** tests; integrate with CI where possible.
- Test **edge cases and failure modes**, not just the happy path.
- Use **mocks/stubs** to isolate the unit under test.
- Aim for **high coverage** — measure with `coverage.py`.

---

## 4. Naming Conventions

| Element       | Convention                                | Example                |
|---------------|-------------------------------------------|------------------------|
| Variables     | `snake_case`                              | `package_weight`       |
| Functions     | `snake_case`                              | `get_package()`        |
| Classes       | `PascalCase` (CapWords)                   | `PackageHandler`       |
| Constants     | `UPPER_SNAKE_CASE`                        | `MAX_WEIGHT`           |
| Modules       | `lowercase` (underscores if needed)       | `data_model`           |
| Private/Internal | leading underscore                     | `_validate_input()`    |

- Names must be **self-explanatory** and descriptive.
- **Never** use single-character names (except loop counters like `i`, `j`).
- **Never** shadow Python built-ins (`list`, `dict`, `id`, `type`, etc.).

---

## 5. Code Organization

- **Group related code** into modules and packages.
- Use `__init__.py` to mark directories as Python packages.
- **DRY** — extract duplicated logic into reusable functions or classes.
- Use **relative imports** within packages.
- Follow a **defined project structure** for larger projects.

---

## 6. Performance

- Prefer **built-in functions and libraries** — they are already optimized.
- Favor **local variables** over globals.
- Use **list comprehensions** and **generators** over equivalent loops.
- Use `__slots__` in classes when creating many instances.
- Avoid unnecessary or overly complex data structures.

---

## 7. Security

- **Validate and sanitize** all user input (prevent SQL injection, XSS, etc.).
- Use only **well-maintained, reputable** libraries for security-sensitive tasks.
- Always use **HTTPS** for web applications.
- **Limit** use of `exec()` and `eval()`.
- **Never hard-code** secrets — use environment variables or secure config files.

---

## 8. Scalability

- Choose **efficient data structures and algorithms** from the start.
- Leverage **concurrent/parallel execution** (`concurrent.futures`, `multiprocessing`) for CPU-bound work.
- Use **async I/O** (`asyncio`) for I/O-bound tasks.
- **Cache** expensive computations when possible.
- For web apps, plan for **load balancing** across multiple instances.
