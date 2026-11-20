# Test First Water: next steps (all need Gabe's OK where noted)
Preview: https://betrnames.github.io/water-treatment-guide/ (GitHub Pages, free; noindex,nofollow + robots Disallow)
Repo: https://github.com/betrnames/water-treatment-guide (source in src/, output docs/)

1. Domain (costs ~$12/yr, needs Gabe's yes). RDAP-open on Nov 19, 2026: testfirstwater.com/.org/.net, watertestfirst.com,
   testyourwaterfirst.com, nopitchwater.com/.org, hardwaterhonest.com, plainwaterguide.com. Taken: knowyourtap.com, testbeforeyoutreat.com.
2. Affiliate approvals (free, needs Gabe's OK; see research/AFFILIATES.md): SpringWell, US Water Systems, Aquasana (Rakuten), iSpring (GoAffPro).
   Then swap hrefs on every data-affiliate link and add rel="sponsored".
3. Go live: PREVIEW_NOINDEX=0 SITE_ORIGIN=https://<domain> BASE_PATH=/ python3 build.py ; push; Search Console verify + submit sitemap (Gabe signs in).
4. Content backlog (quality over volume): chloramine filters, lead at the tap (NSF 53/58), iron filter sizing, softener salt/potassium, "how much does a water softener cost" (installed).
