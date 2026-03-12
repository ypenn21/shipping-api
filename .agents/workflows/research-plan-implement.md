---
description: research-create-plan
---

# Research & Plan Workflow

Use this workflow when the user asks to research a Google developer topic and produce an implementation plan.

## Steps

1. **Clarify the topic.** Confirm what the user wants to research. Extract the core topic/question from their prompt.

2. **Search Google Developer Knowledge.** Use the `mcp_google-developer-knowledge_search_documents` tool to find relevant documentation. Run 2–3 searches with varied queries to ensure broad coverage (e.g., a general query, an API-specific query, and a best-practices query).
   - **If unavailable:** Log that Google Developer Knowledge is unavailable and skip to step 3. Do not fail the workflow.

3. **Research libraries via Context7.** For each key library/framework used in the project (identified from `requirements.txt`, `package.json`, or imports):
   - Use `mcp_context7_resolve-library-id` to resolve the library name to a Context7-compatible library ID. Select the result with the highest benchmark score and `High` source reputation.
   - Use `mcp_context7_query-docs` with the resolved library ID to fetch the latest documentation and code examples relevant to the topic. Be specific in your query (e.g., "Flask application factory pattern and blueprints" rather than just "Flask").
   - Limit to 2–3 `query-docs` calls total to avoid excessive API usage.
   - **If unavailable:** Log that Context7 is unavailable and skip to step 4. Do not fail the workflow.

4. **Handle both sources unavailable.** If **both** Google Developer Knowledge (step 2) and Context7 (step 3) are unavailable:
   - Notify the user that neither research source is accessible.
   - Ask the user whether to:
     - **A) End the workflow** — stop here and revisit later when tools are available.
     - **B) Continue to step 6** — proceed with only codebase analysis (skip steps 5 and proceed to step 6 using existing project knowledge).
   - Wait for the user's choice before proceeding.

5. **Retrieve full documents.** For the most relevant search results from step 2 (if available), call `mcp_google-developer-knowledge_get_documents` using the `parent` field from the search results to pull the complete document content. Skip this step if step 2 was unavailable.

6. **Research the existing codebase.** Review the current project files (especially `main.py`, `data_model.py`, `connect_connector.py`, and any related modules) to understand how the new feature or change would integrate.

7. **Create the implementation plan.** Write a markdown plan file at `plans/<topic-slug>.md` with the following structure:

   ```markdown
   # <Plan Title>

   ## Overview
   Brief description of the goal and why it matters.

   ## Documentation References

   ### Google Developer Knowledge
   List each document used with title, URL, and a one-line summary of what was learned from it.
   Format:
   > **Ref-N:** [Title](URL) — Summary of key insight

   ### Context7 Library Docs
   List each library researched with the Context7 library ID and key findings.
   Format:
   > **Lib-N:** `<library-id>` — Summary of key patterns/APIs discovered

   ## Current State
   Describe the current project architecture relevant to this change.

   ## 📋 Checklist
   High level description of what to change in steps that you can check off to keep track of where the agent is at as the agent steps through each step.

   ## Proposed Changes
   Detailed description of what to change based on the checklist and steps referenced above. Organized by file/component.
   Include **sample code snippets** inline showing the proposed implementation.

   ## Trade-offs & Considerations
   Pros, cons, and alternative approaches considered.
   
   ## 📌 Feature Specification

   ### Use Case
   [Who, what, why — as provided by the developer]

   ### Feature Behavior
   [Inputs, outputs, edge cases, error scenarios]

   ### Acceptance Criteria
   [Specific, testable conditions]

   ## 🔍 Analysis & Investigation

   ### Codebase Structure
   [Your findings about the current codebase]

   ### Current Architecture
   [Architecture analysis and relevant patterns]

   ### Dependencies & Integration Points
   [External dependencies and how they integrate]

   ### Considerations & Challenges
   [Potential issues and how to address them]
   ## Next Steps
   Ordered list of implementation tasks.
   ```

8. **Ask the user to review.** Present the plan file to the user for feedback using the `notify_user` tool with `BlockedOnUser=true` and the plan path in `PathsToReview`.

9. **Iterate.** If the user requests changes:
   - Update the plan file based on their feedback.
   - If needed, pull additional documentation with further `search_documents` / `get_documents` / `query-docs` calls.
   - Present the updated plan again for review.
   - Repeat until the user approves the plan.

Remember: You are in planning mode only. Your job ends after the plan is written to `plans/<feature_name>.md`. After finish conversation.