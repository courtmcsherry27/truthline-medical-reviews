import os
from dataclasses import dataclass, field
DEMO_PASSWORD = os.getenv("SUPERO_PASSWORD", "") or "TruthDemo!2026"
@dataclass
class AppConfig:
    app_name: str = "Truthline Medical Reviews"
    app_emoji: str = "✳"
    app_description: str = "A credibility layer for cross-border care, built on evidence instead of stars."
    domain_name: str = field(default_factory=lambda: os.getenv("SUPERO_DOMAIN", "medto"))
    admin_email: str = field(default_factory=lambda: os.getenv("SUPERO_ADMIN_EMAIL", "admin@medicotourism.example"))
    admin_password: str = field(default_factory=lambda: os.getenv("SUPERO_PASSWORD", "") or DEMO_PASSWORD)
    project_name: str = field(default_factory=lambda: os.getenv("SUPERO_PROJECT", "medicotourism-truth-reviews-e55y"))
    tenants: list = field(default_factory=lambda: [{"name":"default-tenant","display_name":"Truthline Shared Review Platform"}])
    users: list = field(default_factory=lambda: [
        {"email":"admin@medicotourism.example","password":DEMO_PASSWORD,"role":"tenant_admin","full_name":"Truthline Administrator","tenant":"default-tenant"},
        {"email":"patient.one@example.com","password":DEMO_PASSWORD,"role":"tenant_user","full_name":"Amelia Hart","tenant":"default-tenant"},
        {"email":"patient.two@example.com","password":DEMO_PASSWORD,"role":"tenant_user","full_name":"Daniel Reed","tenant":"default-tenant"},
        {"email":"patient.three@example.com","password":DEMO_PASSWORD,"role":"tenant_user","full_name":"Mina Park","tenant":"default-tenant"},
        {"email":"provider.bosphorus@example.com","password":DEMO_PASSWORD,"role":"viewer","full_name":"Bosphorus Renew Clinic","tenant":"default-tenant"},
        {"email":"provider.siam@example.com","password":DEMO_PASSWORD,"role":"viewer","full_name":"Siam Heart & Wellness","tenant":"default-tenant"},
        {"email":"testapp@test.com","password":"Password123!","role":"developer","full_name":"App Tester","tenant":"default-tenant"}])
    services: list = field(default_factory=list)
    public_schemas: list = field(default_factory=lambda: ["provider"])
    public_allow_signup: bool = True
