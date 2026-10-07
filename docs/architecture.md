# Architecture

Providence uses a small set of layers with clear responsibilities.

The domain layer defines validated records for people, projects, time entries, and workspaces. Pydantic validates records before the application can use them.

The repository layer reads and writes a local JSON ledger. It does not make business decisions.

The service layer coordinates repositories and business rules. The rule engine turns validated records into deterministic health signals. The AI insight service processes validated data to answer plain language manager queries without allowing unvalidated output to mutate state.

The presentation layer contains Streamlit views, visual tokens, and interface styles. It consumes prepared data without changing the ledger.

This separation keeps the application understandable. A reader can identify where data is defined, stored, assessed, and presented without tracing unrelated concerns.

## Trade offs

The application uses a file based JSON ledger rather than a database. This choice favours simplicity and auditability over concurrent write performance. The ledger remains small and human readable.

The AI insight service uses deterministic rule based responses rather than a large language model. This choice favours predictability and validation over open ended query support. Supported queries cover budget depletion, capacity alerts, and project risk.

The interface uses Streamlit Cloud for hosting. This choice favours deployment velocity and zero operational overhead over custom infrastructure control.

## Decision records

Decision: Use Pydantic for data validation
Date: October 2026
Rationale: Strong typing, clear validation rules, and automatic documentation through model schemas.

Decision: Use deterministic AI insights
Date: October 2026
Rationale: Predictable responses that can be validated before presentation. No unvalidated model output can mutate application state.

Decision: Use three view structure aligned with Dunkirk narrative
Date: October 2026
Rationale: Clear mental model for managers. Land for weekly health, Sea for project delivery, Air for people capacity.
