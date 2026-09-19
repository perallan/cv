# Oppdater CV-en med Cyberduck

1. Rediger som før i `index.css`, `stack.css` og `print.css`.
2. Kjør `python3 /Users/paj/dev/root/cv/version_css.py`.
3. Last opp CSS-filene kommandoen skriver ut, samt eventuelle nye bilder.
4. Last opp `index.html` til slutt.

HTML-en peker nå på CSS-filer med innholdets fingeravtrykk i navnet.
Endret CSS får et nytt navn; uendret CSS beholder navnet. Ikke rediger de
versjonerte kopiene direkte. Behold gamle versjoner på serveren, slik at
besøkende med eldre HTML fortsatt får fungerende stilark.

Dette fornyer CSS-cachen når nettleseren henter den nye HTML-en. Hvis serveren
også langtidslagrer HTML, bør `index.html` ha `Cache-Control: no-cache` slik at
nettleseren sjekker etter oppdateringer. Serveroppsettet er ikke endret her.
