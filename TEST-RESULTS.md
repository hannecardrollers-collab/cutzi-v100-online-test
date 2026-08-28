# Testresultaten — Cutzi MASTER

Gecontroleerd op 28 augustus 2026 op de huidige mastercode.

## Pakket en live-codegelijkheid
- `public/index.html` is byte-identiek aan de huidige GitHub `main`-versie (Git blob `fe32738b77ae59a960b6f825dc1155f521cdf965`).
- `public/_headers` is byte-identiek aan GitHub `main`.
- Alle Cloudflare Pages Functions in `functions/_lib` en `functions/api` zijn byte-identiek aan GitHub `main`.
- `schema.sql` en `package.json` zijn aanwezig.

## Syntax
- Alle 8 Cloudflare Pages Function JavaScript-bestanden: syntax OK.
- Alle 5 inline JavaScript-blokken in `public/index.html`: syntax OK.

## Login/authenticatie
- Front-end login gebruikt één autoritatieve online handler.
- Login gaat naar `/api/login` met `credentials: include` en `cache: no-store`.
- Verkeerd wachtwoord: HTTP 401.
- Correct testwachtwoord: HTTP 200 en accountpayload correct.
- Sessiecooky: `HttpOnly`, `SameSite=Lax`, `Secure` op HTTPS; `remember` zet `Max-Age=2592000`.
- `/api/me` leest de actieve sessie correct.
- Uitloggen verwijdert de sessie en wist de cookie; daarna geeft `/api/me` HTTP 401.
- Wachtwoorden worden met PBKDF2 / SHA-256 / 100000 iteraties gehasht.

## D1 / clouddata
- De Pages Functions verwachten de D1-binding exact als `DB`.
- `schema.sql` bevat `salons`, `users`, `sessions` en `salon_state` plus de nodige indexen en foreign keys.
- De live D1-database en bestaande account-/salondata zitten bewust niet in deze code-ZIP; die staan extern in Cloudflare D1 en moeten apart worden geback-upt voor volledige data-disaster-recovery.

## Opmerking
De buildcontainer kan `*.pages.dev` niet via DNS bereiken. Daarom is de actuele live-accountlogin niet met echte gebruikersgegevens opnieuw uitgevoerd; de actuele frontend/backend-code, sessiestroom en loginlogica zijn wel volledig statisch en met een lokale D1-harness gecontroleerd.
