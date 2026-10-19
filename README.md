# Truthline - Medical Tourism Truth Reviews

A credibility layer for medical travel: patients score providers on 7
objective truth metrics (1-10, where 1 = hype/false claims, 10 = fully
substantiated), with a mandatory written justification per score.
Stars tell you nothing in cross-border care - this measures
substantiation, not sentiment.

Built entirely via AI-driven development on Supero over MCP (GitHub
Copilot agent in VS Code) - no hand-written code. This repo contains
the Supero-generated application source (Python backend + `ui/app.js`);
the app runs on Supero's platform.

## The 7 truth metrics
Clinical Competency · Health Improvement · Recovery Time ·
Cost Transparency · Staff Professionalism · Travel & Accommodation ·
Referral Likelihood

## Roles
- **Patient** - creates/edits own reviews (7 scores + justifications each)
- **Provider** - sees only reviews about itself + aggregate truth profile
- **Admin** - full cross-provider view + low-score follow-up queue

## Demo accounts (password: `TruthDemo!2026`)
- Admin: `admin@medicotourism.example`
- Providers: `provider.bosphorus@example.com`, `provider.siam@example.com`
- Patients: `patient.one@example.com`, `patient.two@example.com`, `patient.three@example.com`

## Known issues / v2 list
See the submission write-up. Highlights: tenant isolation is enforced
via server-side record filters within a shared tenant (full per-provider
platform tenancy is the v2 fix); admin/provider can currently open the
patient review form (role restriction needed); follow-up queue items
lack provider attribution.
