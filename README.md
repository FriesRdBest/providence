# Providence

Providence is a time intelligence application for managers who need a clear view of capacity, project health, and delivery risk.

It turns simulated workspace records into practical decisions across three connected views. Land presents weekly organisational health. Sea presents project delivery status. Air presents current people capacity.

## Live application

The application will be available through Streamlit Cloud after deployment.

## Purpose

Providence demonstrates thoughtful product engineering through accessible language, validated data, predictable rules, and a carefully structured interface.

## Architecture

The application separates domain models, data access, business rules, presentation components, and persistent records. Each layer has a narrow responsibility so that changes remain understandable and safe.

## Documentation

Read `docs/architecture.md` for the application structure.

Read `docs/design-system.md` for visual language decisions.

Read `docs/data-contracts.md` for data validation rules.

Read `docs/operating-plan.md` for the ninety day operating plan.

## Local use

Install the dependencies listed in `requirements.txt`, then run `streamlit run app.py`.

## Licence

This project is licensed under the Apache License, Version 2.0. See `LICENSE` for the complete licence text.
