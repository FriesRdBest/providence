# Data Contracts

Every workspace record is validated before use.

A person has a name, role, daily capacity, and hours logged today. Capacity and logged hours must remain within zero and twenty four hours.

A project has a name, client, budget, logged hours, and delivery date. Budget must be greater than zero. Logged hours cannot exceed four times the stated budget because such records require review rather than automatic acceptance.

A time entry belongs to one person and one project. It has a start time, duration, and description.

The JSON ledger contains only validated workspace records. The repository validates a workspace before writing it to disk.
