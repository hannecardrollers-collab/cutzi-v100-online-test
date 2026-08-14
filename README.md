# Cutzi v100 — Online Shared Test

Dit is de nieuwe gedeelde testomgeving voor Cutzi.

- `public/index.html` — dezelfde responsive Cutzi-interface voor desktop en mobiel.
- `functions/api/*` — Cloudflare Pages Functions voor online login en synchronisatie.
- `schema.sql` — Cloudflare D1 schema voor accounts, sessies en gedeelde salondata.
- D1 bindingnaam in Cloudflare: **DB**.

## Belangrijk
Dit is een testarchitectuur, niet de definitieve productie-authenticatie. Wachtwoorden worden wel met PBKDF2 gehasht en sessies gebruiken een HttpOnly-cookie, maar e-mailverificatie, rate limiting, recovery en auditlogging zijn nog niet toegevoegd.

Desktop en mobiel delen dezelfde data wanneer je dezelfde Pages production URL en hetzelfde Cutzi-account gebruikt.
