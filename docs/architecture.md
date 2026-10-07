# Architecture

Providence uses a small set of layers with clear responsibilities.

The domain layer defines validated records for people, projects, time entries, and workspaces. Pydantic validates records before the application can use them.

The repository layer reads and writes a local JSON ledger. It does not make business decisions.

The service layer coordinates repositories and business rules. The rule engine turns validated records into deterministic health signals.

The presentation layer contains Streamlit views, visual tokens, and interface styles. It consumes prepared data without changing the ledger.

This separation keeps the application understandable. A reader can identify where data is defined, stored, assessed, and presented without tracing unrelated concerns.
