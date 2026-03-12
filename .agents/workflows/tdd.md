---
description: Test-Driven Development — write failing tests first, then implement just enough code to pass them, refactor, and repeat.
---

# Test-Driven Development (TDD) Workflow

This workflow follows the **Red-Green-Refactor** cycle. The developer provides a detailed feature/use-case description, and the agent drives development test-first.

---

## Phase 1 — Understand the Feature

1. **Gather requirements.** Ask the developer to describe:
   - The **use case** (who, what, why)
   - The **feature behavior** in detail (inputs, outputs, edge cases, error scenarios)
   - Any **acceptance criteria** or constraints
   - The **scope boundary** — what is explicitly *out* of scope

2. **Analyze the codebase.** Research existing code, models, and test infrastructure to understand:
   - Where the new feature fits architecturally
   - Which modules/files will be affected
   - Existing test patterns and frameworks in use (`pytest`, `unittest`, etc.)

3. **Document the test plan.** Create `plans/tdd_plan.md` listing:
   - A numbered list of **test cases** derived from the requirements, ordered from simplest to most complex
   - For each test case: a short description, expected input, expected output/behavior
   - Group tests logically (happy path → edge cases → error handling)

// turbo
4. **Present the plan for review.** Use `notify_user` to share `plans/tdd_plan.md` and ask the developer to confirm, adjust, or add test cases before any code is written.

---

## Phase 2 — Red: Write Failing Tests

Work through the test plan **one test at a time**, starting with the simplest.

5. **Write a single test.** Add exactly one test function that asserts the expected behavior for the current test case.
   - Keep the test small and focused on a single behavior
   - Use descriptive test names (e.g., `test_create_package_returns_201_with_valid_data`)
   - Include meaningful assertions — never write a test without an `assert`

// turbo
6. **Run the test suite.** Execute the tests and confirm the new test **fails** (Red). This proves the feature is not yet implemented.
   ```bash
   pytest -v
   ```
   - If the test passes unexpectedly, the test may be trivial or the feature already exists — revisit
   - Capture and note the failure output

---

## Phase 3 — Green: Write Minimal Implementation

7. **Write just enough code** to make the failing test pass.
   - Do **not** add functionality beyond what the test requires
   - Prefer the simplest possible implementation (even if it looks naive)
   - Avoid premature optimization or abstraction

// turbo
8. **Run the test suite.** Execute all tests and confirm:
   - The new test **passes** (Green) ✅
   - All previously passing tests **still pass** (no regressions) ✅
   ```bash
   pytest -v
   ```
   - If any test fails, fix the implementation (not the test) and re-run

---

## Phase 4 — Refactor

9. **Refactor the code** while keeping all tests green.
   - Improve naming, reduce duplication, extract functions/methods
   - Apply SOLID principles and project conventions
   - Do **not** change behavior — only improve structure and clarity

// turbo
10. **Run the test suite again** to confirm refactoring introduced no regressions.
    ```bash
    pytest -v
    ```

---

## Phase 5 — Repeat (Accumulate Tests)

11. **Loop back to Step 5** for the next test case in the plan.
    - Each iteration adds one test and the minimal code to pass it
    - The test suite grows incrementally and always stays green
    - Continue until all test cases from the plan are implemented and passing

---

## Phase 6 — Final Verification & Walkthrough

// turbo
12. **Run the full test suite** one final time to confirm everything passes.
    ```bash
    pytest -v
    ```

13. **Create a walkthrough.** Summarize:
    - What was implemented
    - How many tests were written and their coverage
    - Any design decisions or trade-offs made during refactoring
    - Present the walkthrough to the developer for final review

---

## Anti-Pattern Guardrails

> [!CAUTION]
> **Avoid these common TDD mistakes during this workflow:**
> - ❌ Writing multiple tests before implementing any code
> - ❌ Writing implementation code before a failing test exists
> - ❌ Writing tests without assertions
> - ❌ Writing tests for trivial accessors/getters
> - ❌ Making tests too large or testing multiple behaviors at once
> - ❌ Modifying tests to make them pass instead of fixing the implementation
> - ❌ Skipping the refactor phase
