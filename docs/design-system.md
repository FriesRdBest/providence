# Providence Design System

## Purpose

Providence presents time intelligence as a calm, precise management workspace. The visual system supports quick executive review, detailed project control, and clear people capacity monitoring without making the application feel generic or overly corporate.

The interface uses a light first palette with high elevation ivory surfaces, deep charcoal text, Toggl red for meaningful action and risk, and restrained semantic status colors. Every visual choice exists to improve the clarity of a decision.

## Public language

The public application uses four view names: Overview, Health, Project, and People.

Internal design shorthand is not shown in the application, exports, navigation, headings, or public documentation.

Public copy uses plain sentences. It does not expose implementation language, internal architecture terms, dot point lists, or hyphenated wording.

## Token structure

The design system has three layers.

Primitive tokens define raw values for ivory surfaces, white surfaces, charcoal text, steel neutrals, Toggl red, semantic status colors, spacing, corner radius, and elevation.

Semantic tokens define intent. The principal roles are app surface, primary surface, secondary surface, core text, supporting text, muted text, subtle border, default border, primary action, healthy status, watch status, risk status, neutral status, and keyboard focus.

Component rules consume semantic roles. Components do not use scattered raw color values. This keeps the application consistent and allows controlled visual changes.

## Color and meaning

High elevation ivory provides the application background. White provides primary content surfaces. Deep charcoal gives core text and visual structure. Steel and slate carry supporting information and boundaries.

Toggl red is reserved for primary action, urgent attention, critical risk, and decision support emphasis. It is not used as general decoration.

Green represents healthy conditions. Amber represents a watch condition or limited remaining capacity. Red represents a risk condition or overbooked capacity. Blue represents neutral information and missing time conditions.

Status is always communicated through language and color together.

## Type and spacing

Typography uses the system sans serif stack with a strong hierarchy. Page titles are editorial and spacious. Section titles are compact and structural. Metric labels are small uppercase utility labels. Data values use tight letter spacing for fast scanning.

The spacing scale begins at four pixels and grows through eight, twelve, sixteen, twenty, twenty four, thirty two, forty, and forty eight pixels. Cards use generous internal space. Dense operational views use disciplined row rhythm rather than compressed clutter.

## Surfaces and elevation

Primary surfaces use white with subtle borders, rounded corners, and restrained elevation. Shadows remain soft and low contrast. The application avoids heavy glass effects, large blur fields, decorative gradients, and exaggerated motion.

The Overview and Health views use more whitespace and larger value hierarchy. Project and People use denser rows while keeping the same surface treatment and typography.

## View density

Overview is the executive decision surface. It uses one clear delivery story, a concise metric row, focused project and health previews, decision support, and a quiet export action.

Health is the weekly strategic surface. It presents utilization, budget pace, delivery exposure, decision support, and project health without gauges or traffic light dashboards.

Project is the daily operational workspace. It uses status and sort controls, compact metrics, decision support, and responsive project rows that show budget pace and delivery timing.

People is the current capacity workspace. It uses capacity controls, concise metrics, decision support, and stable ledger rows for logged time, capacity, remaining hours, and people status.

## Accessibility

Text must maintain strong contrast against its surface. Keyboard focus boundaries remain visible on controls. Status never relies on color alone. Labels remain visible and direct. Rows and controls preserve logical scan order.

The application supports wide and narrow viewports. At narrow widths, Streamlit columns stack naturally and shared CSS preserves readable spacing, type hierarchy, and surface edges.

## Streamlit boundaries

The visual system is implemented through Streamlit containers, columns, metrics, select controls, progress tracks, download controls, and focused presentation markup.

Shared styling lives in `src/ui/styles.py`. Tokens live in `src/ui/tokens.py`. Reusable presentation helpers live in `src/ui/components.py`.

Custom presentation markup is limited to stable text, status, identity, header, and surface elements. It does not replace Streamlit interaction or application behavior. No custom JavaScript or fragile frontend framework is required.

## Review standard

A Providence screen must make its most important management decision clear within a short scan. Every card, color, label, and piece of emphasis must have a defined purpose.

The application should feel intentional at first glance and robust under closer review. It should read as a serious product built with Streamlit, not a default Streamlit interface that has been decorated.
