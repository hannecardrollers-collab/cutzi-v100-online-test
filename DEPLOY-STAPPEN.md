# Deploy-stappen — Cutzi v100 Online Shared Test

1. Maak een volledig nieuwe GitHub repository, bijvoorbeeld `cutzi-v100-online-test`.
2. Upload **de inhoud van deze map** naar de root van de repository. Controleer dat `public/index.html`, `functions/api/state.js` en `schema.sql` zichtbaar zijn.
3. Maak in Cloudflare een nieuwe D1 database, bijvoorbeeld `cutzi-v100-test-db`.
4. Open de D1 database > Console, plak de volledige inhoud van `schema.sql` en voer die uit.
5. Maak in Cloudflare een nieuw Pages-project en verbind de nieuwe GitHub repository.
6. Production branch: `main`. Framework preset: None. Build command: leeg of `exit 0`. Build output directory: `public`. Root directory: leeg.
7. Na de eerste deploy: Pages project > Settings > Bindings > Add > D1 database. Variable name: **DB**. Selecteer `cutzi-v100-test-db`.
8. Redeploy de production deployment zodat de binding actief wordt.
9. Open uitsluitend de production `*.pages.dev` URL. Maak daar je nieuwe testaccount aan.
10. Log met exact datzelfde account in op je telefoon via exact dezelfde production URL. Beide toestellen gebruiken dan dezelfde D1 salondata.
11. Test: voeg op desktop één medewerker toe, wacht een seconde, open/ververs Team op mobiel. Voeg daarna op mobiel één klant toe en ververs Klanten op desktop.

Gebruik voor deze test niet twee verschillende Pages-projecten of preview-URL's: dat maakt de login/sessie per hostname verschillend. De database is centraal, maar houd één production URL aan als vaste testomgeving.
