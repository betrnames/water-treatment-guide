"""Page content for Test First Water. Every price, policy, rating and certification below was opened on
Nov 19, 2026 (America/Los_Angeles). Sources are listed in ../research/SOURCES.md and cited inline."""
import html

# ---- verified URLs (opened Nov 19, 2026) ----
SW = "https://www.springwellwater.com/product/"
U = {
 "sw_cf": SW + "water-filters/whole-house-water-filters/",
 "sw_ss": SW + "water-softeners/salt-water-softeners/",
 "sw_fs": SW + "water-softeners/salt-free-water-softeners/",
 "sw_ws": SW + "well-water/whole-house-iron-filter/",
 "sw_css": SW + "dual-systems/water-filter-salt-softener/",
 "sw_wsss": SW + "well-water/well-water-filter-and-salt-based-water-softener/",
 "sw_uv": SW + "uv-systems/uv-water-purification-system/",
 "sw_welltest": SW + "water-testing/well-water-test-kit/",
 "sw_returns": "https://www.springwellwater.com/shipping/",
 "sw_warranty": "https://www.springwellwater.com/warranty/",
 "aq_rhino": "https://www.aquasana.com/whole-house-water-filters/rhino-100365488.html",
 "aq_sf": "https://www.aquasana.com/whole-house-water-filters/salt-free-water-conditioner-100365583.html",
 "isp_wgb32b": "https://www.ispringfilter.com/products/ispring-whole-house-water-filtration-system-sediment-carbon-big-blue",
 "isp_ksnc": "https://www.ispringfilter.com/products/ispring-chloramine",
 "isp_wgb32bm": "https://www.ispringfilter.com/products/ispring-whole-house-water-filtration-system-sediment-carbon-iron-manganese-big-blue",
 "usw_matrixx": "https://uswatersystems.com/products/matrixx-smart-metered-water-softener",
 "usw_flexx": "https://uswatersystems.com/products/flexx-pro-series-smart-metered-water-softener",
 "usw_bodyguard": "https://uswatersystems.com/products/bodyguard-whole-house-water-filter-system",
 "usw_infusion": "https://uswatersystems.com/products/flexx-infusion-iron-and-sulfur-system",
 "usw_oxigen": "https://uswatersystems.com/products/flexx-oxi-gen-aeration-iron-and-sulfur-filter-by-us-water-systems",
 # authorities
 "epa_ccr": "https://www.epa.gov/ccr/ccr-information-consumers",
 "epa_labs": "https://www.epa.gov/dwlabcert/contact-information-certification-programs-and-certified-laboratories-drinking-water",
 "epa_wells": "https://www.epa.gov/privatewells/protect-your-homes-water",
 "epa_lead": "https://www.epa.gov/ground-water-and-drinking-water/basic-information-about-lead-drinking-water",
 "epa_use": "https://www.epa.gov/watersense/how-we-use-water",
 "cdc_wells": "https://www.cdc.gov/drinking-water/safety/guidelines-for-testing-well-water.html",
 "usgs_hard": "https://www.usgs.gov/water-science-school/science/hardness-water",
 "nsf_std": "https://www.nsf.org/consumer-resources/articles/standards-water-treatment-systems",
 "nsf_list": "https://info.nsf.org/Certified/DWTU/",
 "wqa": "https://wqa.org/",
 "unl_saltfree": "https://extensionpubs.unl.edu/publication/g2275/2026/pdf/view/g2275-2026.pdf",
 "mdh_soft": "https://www.health.mn.gov/communities/environment/water/factsheet/softening.html",
 "mdh_scams": "https://www.health.mn.gov/communities/environment/water/factsheet/beware.html",
 "fl_ag": "https://www.myfloridalegal.com/consumer-protection/how-to-protect-yourself-water-treatment-devices",
 "cfr_4290": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-429/section-429.0",
 "cfr_4291": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-429/section-429.1",
 "bbb_sw": "https://www.bbb.org/us/fl/daytona-beach/profile/water-purification-equipment/springwell-water-filtration-systems-0733-90638942/complaints?page=1",
 "reddit_sw": "https://www.reddit.com/r/WaterTreatment/comments/1q81pce/psa_about_springwell_if_youre_researching_whole/",
}

CALC_JS = r"""
(function(){
  var SIZES=[24000,32000,40000,48000,64000,80000,96000,110000];
  function $(id){return document.getElementById(id);}
  function fmt(n){return Math.round(n).toLocaleString('en-US');}
  function calc(){
    var h=parseFloat($('hard').value), unit=$('unit').value, fe=parseFloat($('iron').value)||0,
        ppl=parseFloat($('people').value), gpd=parseFloat($('gpd').value), days=parseFloat($('days').value);
    var out=$('out');
    if(!(h>=0)||!(ppl>0)||!(gpd>0)||!(days>0)){out.innerHTML='<p>Enter your hardness, household size, gallons per person, and days between regenerations.</p>';return;}
    var gpg = unit==='mgl' ? h/17.1 : h;
    var comp = gpg + 4*fe;
    var daily = comp*ppl*gpd;
    var need = daily*days;
    var pick=null; for(var i=0;i<SIZES.length;i++){ if(need<=SIZES[i]*0.75){pick=SIZES[i];break;} }
    var cls = gpg<1?'soft':gpg<3.5?'slightly hard':gpg<7?'moderately hard':gpg<10.5?'hard':'very hard';
    var html='<p class="big">'+fmt(need)+' grains</p><p>to remove between regenerations ('+days+' days).</p>'+
      '<ul><li>Your water: <strong>'+gpg.toFixed(1)+' gpg</strong> ('+cls+')'+(fe>0?', <strong>'+comp.toFixed(1)+' gpg</strong> after adding iron':'')+'</li>'+
      '<li>Daily load: '+fmt(comp)+' gpg × '+ppl+' people × '+gpd+' gal = <strong>'+fmt(daily)+' grains/day</strong></li>';
    if(pick){html+='<li>Rule-of-thumb size: <strong>'+(pick/1000)+',000-grain</strong> softener (your need is '+Math.round(need/pick*100)+'% of its rated capacity), about '+(pick/32000).toFixed(1)+' cu ft of resin</li>';}
    else{html+='<li>Your need is above common single-tank sizes. Shorten the days between regenerations, or ask about a larger or twin-tank system.</li>';}
    html+='</ul>';
    if(gpg<3.5){html+='<p class="small"><strong>Note:</strong> under 3.5 gpg is soft to slightly hard. Many homes at this level skip a softener entirely.</p>';}
    if(fe>0){html+='<p class="small"><strong>Iron:</strong> check the softener spec sheet for its iron limit. Higher iron usually means a dedicated iron filter first. See our well water guide.</p>';}
    out.innerHTML=html;
  }
  ['hard','unit','iron','people','gpd','days'].forEach(function(id){var el=$(id);el.addEventListener('input',calc);el.addEventListener('change',calc);});
  $('calc-form').addEventListener('submit',function(e){e.preventDefault();calc();});
  calc();
})();
"""

def register(add, href, url, link, cite, DISCLOSURE, CHECKED, article_schema, faq_schema, faq_html, SITE_NAME, EMAIL):
    import datetime
    d = datetime.date.today()
    dstr = d.strftime("%b %-d, %Y")

    def meta(minutes):
        return (f'<p class="meta">By the {SITE_NAME} team · Updated <time datetime="{d.isoformat()}">{dstr}</time> · '
                f'{minutes} min read · No hands-on testing claimed: we compare published specs, policies, and certifications.</p>')

    def answer(text):
        return f'<p class="note"><strong>Short answer:</strong> {text}</p>'

    def p(text):  # price tag
        return f'<span class="price">(price checked {CHECKED} on the maker\'s site; prices change often)</span>'

    def related(*items):
        lis = "".join(f'<li><a href="{href(pp)}">{html.escape(t)}</a></li>' for pp, t in items)
        return f'<h2>Keep going</h2><ul>{lis}</ul>'

    def sources(*items):
        lis = "".join(f'<li>{cite(t, u)}</li>' for t, u in items)
        return f'<h2>Sources</h2><ul class="small">{lis}</ul><p class="small">All sources opened {CHECKED}.</p>'

    def art(path, title, desc, h1, body, crumbs, faqs=None, minutes=7, money=False, extra_head=""):
        schema = [article_schema(path, h1, desc)]
        if faqs:
            schema.append(faq_schema(faqs))
            body = body + faq_html(faqs)
        top = meta(minutes) + (DISCLOSURE if money else "")
        add(path, title=title, desc=desc, h1=h1, body=top + body, crumbs=crumbs, schema=schema, extra_head=extra_head)

    # =========================================================== HOME
    home = f'''
<p class="lede"><strong>Don't buy a $2,000 water system from someone who knocked on your door.</strong> Test your water first, find out what is actually in it, and then pick a system that fixes that problem. It's usually cheaper, and you'll know it's working.</p>
{DISCLOSURE}
<h2>The three-step plan</h2>
<div class="grid">
<div class="card"><h3>1. Test</h3><p>Read your city's free annual water report, or send well water to a state-certified lab. <a href="{href('test-your-water/')}">How to test your water</a></p></div>
<div class="card"><h3>2. Match</h3><p>Hardness needs a softener. Chlorine taste needs carbon. Bacteria needs disinfection. <a href="{href('softener-vs-salt-free/')}">Softener vs salt-free</a></p></div>
<div class="card"><h3>3. Size and buy</h3><p>Size it with real numbers, then compare the return policy as hard as the price. <a href="{href('softener-size-calculator/')}">Sizing calculator</a></p></div>
</div>
<h2>Pick your situation</h2>
<div class="card"><h3><a href="{href('whole-house-water-filter/')}">I'm on city water</a></h3><p>Whole-house filter shortlist for chlorine and chloramine taste, plus when you don't need one at all.</p></div>
<div class="card"><h3><a href="{href('well-water/')}">I'm on a private well</a></h3><p>Test for bacteria and nitrate first, then iron, sulfur, and hardness. Systems by problem.</p></div>
<div class="card"><h3><a href="{href('door-to-door-water-sales/')}">A salesperson is coming over (or just left)</a></h3><p>The red flags, the "free water test" trick, and your federal three-day right to cancel.</p></div>
<div class="card"><h3><a href="{href('springwell-review/')}">I'm looking at SpringWell</a></h3><p>A skeptical read of its prices, return policy, warranty, and public complaints.</p></div>
<h2>Why trust this site?</h2>
<p>We don't sell equipment and we don't do home visits. We don't claim to have lab-tested anything. Instead, we send you to the sources that matter, like the EPA, the CDC, state health departments, NSF certification listings, and each maker's own return policy. We show every price with the date we checked it. Read more <a href="{href('about/')}">about us</a>.</p>
<p class="small">Hard water is a nuisance, not a health risk, according to {cite('Nebraska Extension', U['unl_saltfree'])}. Health problems like bacteria, nitrate, or lead are a different job with different equipment, and testing is how you tell them apart.</p>
'''
    add("", title=f"{SITE_NAME}: Test Your Water Before You Buy a Filter or Softener",
        desc="Skip the door-to-door water pitch. Test your water first, learn salt vs salt-free, size a softener, and compare whole-house systems with dated prices.",
        h1="Test your water first. Then buy the right system.", body=home, og_type="website",
        schema=[{"@context": "https://schema.org", "@type": "WebSite", "name": SITE_NAME, "url": url("")}])

    # =========================================================== TEST YOUR WATER
    body = f'''
{answer(f"On city water, start with your utility's free annual Consumer Confidence Report and ask the utility for your hardness number. On a private well, the CDC says to test at least once a year for total coliform bacteria, nitrates, total dissolved solids, and pH, using a state-certified lab.")}
<p>Every good water decision starts with a number. Without one, you're buying based on a sales pitch or a scary demo. Here's how to get real numbers for little or no money.</p>

<h2>If you're on city water: read your Consumer Confidence Report</h2>
<p>The EPA requires community water systems to send customers a Consumer Confidence Report, an annual drinking water quality report, by July 1 each year ({cite('EPA', U['epa_ccr'])}). If you can't find yours, the EPA has an online search tool on that page, or you can call your water supplier.</p>
<p>What to look for:</p>
<ul>
<li><strong>Disinfectant type.</strong> Chlorine or chloramine? It matters when you pick a carbon filter, because some filters are sold in separate chloramine versions.</li>
<li><strong>Hardness.</strong> Often listed in mg/L or grains per gallon (gpg). If it isn't in the report, call the utility and ask. Divide mg/L by 17.1 to get gpg.</li>
<li><strong>Any violations</strong> and the contaminants detected, compared with the legal limit.</li>
</ul>
<div class="warn"><strong>Lead is the big exception.</strong> The EPA says the most common sources of lead in drinking water are lead pipes, faucets, and fixtures, and that lead service lines are typically the most significant source in homes that have them ({cite('EPA', U['epa_lead'])}). Your utility's report can't tell you what your own pipes add. If your home is older, test water from your own tap through a certified lab.</div>

<h2>If you're on a private well: test every year</h2>
<p>EPA rules for public water systems don't apply to private wells, so the owner is responsible for testing. The {cite('CDC', U['cdc_wells'])} and {cite('EPA', U['epa_wells'])} both say to test at least once a year for:</p>
<ul><li>Total coliform bacteria</li><li>Nitrates</li><li>Total dissolved solids</li><li>pH</li></ul>
<p>The CDC also says to ask your local health department what else is common in your area. That could be arsenic, lead, radium, VOCs, or pesticides. Test again after flooding or well repairs, if the taste, color, or smell changes, or if someone in the home becomes pregnant or a child moves in.</p>
<p>For equipment sizing, add these to the lab order: <strong>hardness, iron, manganese, and hydrogen sulfide</strong> (rotten-egg smell). Those decide which filter or softener you need. They're also the conditions some makers exclude from warranty coverage, as you'll see in our <a href="{href('springwell-review/')}">SpringWell review</a>.</p>

<h2>Where to get a real test</h2>
<ol>
<li><strong>Your local or state health department.</strong> Many test well water for bacteria and nitrate, or keep a list of certified labs.</li>
<li><strong>A state-certified drinking water lab.</strong> The EPA keeps a page linking every state's certification program and certified lab list ({cite('EPA', U['epa_labs'])}).</li>
<li><strong>Mail-in kits sold by water companies.</strong> These are convenient, but you're asking a seller to diagnose a problem it sells the fix for. For example, SpringWell lists a well water test (Level 1 + Bacteria) at $169 {p(1)}. Compare it with a certified lab before you buy.</li>
<li><strong>Hardness test strips.</strong> Fine for a ballpark hardness number, but not for health contaminants.</li>
</ol>

<h2>What a "free in-home water test" really is</h2>
<p>Florida's Attorney General warns that sellers offering "free home water testing" may add tablets or drops to your water. When the water changes color, they say it's polluted. The AG says that in almost all of these cases, any water, even spring water, would "fail" the test ({cite('Florida AG', U['fl_ag'])}). Minnesota's Department of Health describes the same tactic. The "tests" may only show normal minerals ({cite('MDH', U['mdh_scams'])}). More in our <a href="{href('door-to-door-water-sales/')}">sales red flags guide</a>.</p>

<h2>Reading hardness</h2>
<div class="table-wrap"><table><tr><th>Classification</th><th>mg/L as CaCO₃</th><th>grains per gallon</th></tr>
<tr><td>Soft</td><td>0 to 17.1</td><td>0 to 1</td></tr><tr><td>Slightly hard</td><td>17.1 to 60</td><td>1 to 3.5</td></tr>
<tr><td>Moderately hard</td><td>60 to 120</td><td>3.5 to 7</td></tr><tr><td>Hard</td><td>120 to 180</td><td>7 to 10.5</td></tr>
<tr><td>Very hard</td><td>180 and over</td><td>10.5 and over</td></tr></table></div>
<p class="small">Table from {cite('Nebraska Extension G2275', U['unl_saltfree'])}. The {cite('USGS', U['usgs_hard'])} uses similar bands.</p>
<p>Got your number? Plug it into the <a href="{href('softener-size-calculator/')}">softener sizing calculator</a>.</p>
{related(("softener-vs-salt-free/", "Salt softener vs salt-free conditioner"), ("well-water/", "Well water systems by problem"), ("whole-house-water-filter/", "Whole-house filters for city water"))}
{sources(("EPA: CCR information for consumers", U['epa_ccr']), ("EPA: certified drinking water labs", U['epa_labs']), ("EPA: Protect your home's water (private wells)", U['epa_wells']), ("CDC: Guidelines for testing well water", U['cdc_wells']), ("EPA: Basic information about lead in drinking water", U['epa_lead']), ("Florida Attorney General: water treatment devices", U['fl_ag']), ("Minnesota Department of Health: water treatment scams", U['mdh_scams']), ("Nebraska Extension G2275", U['unl_saltfree']))}
'''
    faqs = [("How often should I test well water?", "The CDC and EPA say at least once a year for total coliform bacteria, nitrates, total dissolved solids, and pH, and again after flooding, repairs, or any change in taste, color, or smell."),
            ("Does my city water report show lead from my pipes?", "No. The EPA says lead usually comes from lead service lines, faucets, and fixtures, so test water from your own tap if your home might have them."),
            ("How do I convert mg/L hardness to grains per gallon?", "Divide mg/L (as calcium carbonate) by 17.1. For example, 171 mg/L is 10 gpg.")]
    art("test-your-water/", "How to Test Your Water (City or Well) Before Buying a Filter",
        "Read your Consumer Confidence Report, use an EPA/state-certified lab, and know what to test a well for. Plain steps, with EPA and CDC sources.",
        "How to test your water before you buy anything", body, [("test-your-water/", "Test your water")], faqs, minutes=7)

    # =========================================================== SOFTENER VS SALT-FREE
    body = f'''
{answer("A salt-based (ion exchange) softener removes the calcium and magnesium that make water hard. A salt-free conditioner doesn't remove them. It changes their form to reduce scale. If you want soft-feeling water, fewer spots, and better soap lather, you want a real softener. If you mostly want less scale and can't or won't use salt, a conditioner is an option, but test results won't show softer water.")}
{DISCLOSURE}
<h2>How a real softener works</h2>
<p>A softener is a tank of resin beads. The beads trap calcium and magnesium and swap them for sodium or potassium. When the beads fill up, the unit "regenerates": it flushes them with a strong salt (or potassium) brine and sends the waste down the drain ({cite('Minnesota Department of Health', U['mdh_soft'])}). The certification standard for these units is <strong>NSF/ANSI 44</strong> ({cite('NSF', U['nsf_std'])}).</p>
<p><strong>The tradeoffs</strong>, per MDH: added sodium in the water, salt and brine going into the environment, and a unit that needs regular testing and maintenance to keep working. Some areas restrict brine-discharging softeners, so check local rules before you buy.</p>

<h2>How a salt-free conditioner works (and what it doesn't do)</h2>
<p>Nebraska Extension calls salt-free units "descalant devices as opposed to hardness removing devices, since they do not remove the hardness from the water." Template-assisted crystallization (TAC), the most common type sold for whole homes, uses treated beads to "convert (not remove)" hardness minerals ({cite('Nebraska Extension G2275', U['unl_saltfree'])}).</p>
<p>The same guide adds that:</p>
<ul>
<li>salt-free units don't remove iron or manganese, so they often need pretreatment;</li>
<li>they don't handle bacteria, hydrogen sulfide, sediment, lead, nitrate, or pesticides;</li>
<li>few conclusive studies confirm how well they work in homes, and no independent studies confirm the "use less soap" claims.</li>
</ul>
<div class="warn"><strong>This is where people get burned.</strong> In a 2026 Reddit post, a buyer said a sales rep recommended a salt-free combo for hard water and skin problems. After five months the water spots hadn't changed, and he was then told salt-free systems "don't actually remove minerals" ({cite('r/WaterTreatment', U['reddit_sw'])}). That's one person's account, not a lab result. But it matches exactly what the extension guide says these units do.</div>

<h2>Side by side</h2>
<div class="table-wrap"><table>
<tr><th></th><th>Salt-based softener</th><th>Salt-free conditioner (TAC)</th></tr>
<tr><td>Removes hardness minerals?</td><td>Yes</td><td>No, it changes their form</td></tr>
<tr><td>Hardness test after install</td><td>Reads soft</td><td>Reads about the same as before</td></tr>
<tr><td>Soap lather, "slippery" feel</td><td>Yes</td><td>No independent evidence</td></tr>
<tr><td>Scale reduction</td><td>Yes</td><td>Claimed; results vary by water</td></tr>
<tr><td>Salt bags, drain line, power</td><td>Yes</td><td>Usually no</td></tr>
<tr><td>Iron and manganese</td><td>Some, within the unit's limits</td><td>No, needs pretreatment</td></tr>
<tr><td>Standard to look for</td><td>NSF/ANSI 44</td><td>Ask what test backs the scale claim</td></tr>
</table></div>

<h2>What they cost (maker list prices)</h2>
<ul>
<li>SpringWell salt-based softener: {link("SS1 listed at $1,512", U['sw_ss'], "springwell")} (regular $1,890) {p(1)}</li>
<li>SpringWell salt-free FutureSoft conditioner: {link("FS1 listed at $1,680", U['sw_fs'], "springwell")} (regular $2,100) {p(1)}</li>
<li>Aquasana salt-free conditioner: {link("listed at $703.20", U['aq_sf'], "aquasana")} (MSRP $1,758) {p(1)}</li>
<li>US Water Systems Matrixx metered softener: {link("$1,094 to $1,694 by size", U['usw_matrixx'], "uswatersystems")} {p(1)}</li>
</ul>
<p>Notice that at SpringWell, the salt-free conditioner costs <em>more</em> than the real softener. Don't assume "salt-free" means "cheaper" or "better."</p>

<h2>How to choose</h2>
<ol>
<li>Get your hardness number (see <a href="{href('test-your-water/')}">how to test</a>).</li>
<li>Under about 3.5 gpg: many homes don't need either.</li>
<li>Want soft water: buy a salt-based softener and size it with the <a href="{href('softener-size-calculator/')}">calculator</a>.</li>
<li>Can't use salt (local ban, health reasons, no drain): a conditioner is a scale-control compromise. Know what you're getting, and read the return policy before buying.</li>
</ol>
{related(("softener-size-calculator/", "Softener sizing calculator"), ("springwell-review/", "SpringWell review (salt-free return complaint)"), ("well-water/", "Best options for well water"))}
{sources(("Nebraska Extension G2275: Salt-free water 'softener' options", U['unl_saltfree']), ("Minnesota Department of Health: home water softening", U['mdh_soft']), ("NSF: standards for water treatment systems", U['nsf_std']), ("r/WaterTreatment PSA about SpringWell (2026)", U['reddit_sw']))}
'''
    faqs = [("Do salt-free water softeners actually soften water?", "No. Nebraska Extension describes them as descalers that change the form of hardness minerals without removing them, so a hardness test reads about the same afterward."),
            ("Which certification should a water softener have?", "NSF/ANSI 44 covers cation exchange (salt or potassium) water softeners. Check the exact model on NSF's or WQA's listing."),
            ("Is hard water bad for my health?", "Nebraska Extension says hard water is not a health risk. It is a nuisance that causes scale, spots, and poor soap performance.")]
    art("softener-vs-salt-free/", "Water Softener vs Salt-Free Conditioner: An Honest Comparison",
        "Salt-free conditioners don't remove hardness. Here's what each system really does, what they cost, and how to choose, with extension and NSF sources.",
        "Salt softener vs salt-free conditioner, honestly explained", body, [("softener-vs-salt-free/", "Softener vs salt-free")], faqs, minutes=8, money=True)

    # =========================================================== CITY WATER FILTERS
    body = f'''
{answer("On city water that already meets EPA limits, a whole-house filter is mostly a comfort upgrade: less chlorine taste and smell at every tap. Check your utility's report first. If it uses chloramine, buy a filter sold for chloramine. If lead is your worry, a whole-house carbon tank isn't the answer. Test your tap and look at a point-of-use filter certified for lead.")}
{DISCLOSURE}
<h2>Do you need one?</h2>
<p>Minnesota's health department says most residents on public water don't need home treatment to protect their health, and treatment should be bought only to fix a specific water issue ({cite('MDH', U['mdh_scams'])}). Good reasons to buy a whole-house filter: you dislike the chlorine taste or smell, or you want sediment out before it reaches appliances. Bad reason: a salesperson's color-change demo.</p>

<h2>Certifications, decoded</h2>
<p>From {cite('NSF', U['nsf_std'])}:</p>
<ul>
<li><strong>NSF/ANSI 42</strong>: aesthetic effects, like chlorine, taste, and odor. Covers whole-house (point-of-entry) systems too.</li>
<li><strong>NSF/ANSI 53</strong>: a contaminant with a health effect, like lead.</li>
<li><strong>NSF/ANSI 58</strong>: reverse osmosis, usually under-sink.</li>
<li><strong>NSF/ANSI 401</strong>: up to 15 "emerging" contaminants.</li>
</ul>
<p>Watch the wording. <em>"Tested to"</em> a standard is not the same as <em>"certified to"</em> it, and a certified tank or housing material (NSF/ANSI 61) doesn't mean the filter's performance is certified. Look up the exact model on {cite("NSF's listings", U['nsf_list'])} or {cite("WQA's Gold Seal directory", U['wqa'])}.</p>

<h2>Shortlist for city water</h2>
<p>These are options to compare, not tested rankings. All prices are list prices on each maker's site {p(1)}.</p>

<div class="card"><h3>Budget cartridge system: iSpring WGB32B</h3>
<p>{link("iSpring WGB32B, $516.99", U['isp_wgb32b'], "ispring")}. A 3-stage "Big Blue" cartridge housing (sediment plus carbon). You swap cartridges yourself. iSpring also sells a {link("chloramine version (WGB32B-KSNC), $639.99", U['isp_ksnc'], "ispring")}.</p>
<p><strong>Certification:</strong> on NSF's listing (checked {CHECKED}), iSpring's certified products are under-sink reverse osmosis units under NSF/ANSI 58. We didn't find the WGB32B whole-house line listed. <strong>Check certification</strong> before relying on performance claims.</p></div>

<div class="card"><h3>Mid-price tank filter: Aquasana Rhino</h3>
<p>{link("Aquasana Rhino, listed at $799.20", U['aq_rhino'], "aquasana")} (MSRP $1,998, shown with a "60% off" banner). A large carbon tank with a 10-year limited warranty, per the product page.</p>
<p><strong>Certification:</strong> the page says the Rhino is "independently tested to NSF/ANSI Standard 42" for chlorine and that its tanks are WQA certified to NSF/ANSI/CAN 61, which is a materials-safety standard. On NSF's own listing we found only two Aquasana UV units. <strong>Check certification</strong> for the filter itself. And when the "sale" is permanent, compare the real price, not the MSRP.</p></div>

<div class="card"><h3>Premium tank filter: SpringWell CF</h3>
<p>{link("SpringWell CF1 listed at $1,092", U['sw_cf'], "springwell")} (regular $1,365); CF4 $1,218; CF+ $2,016. It's marketed with a lifetime warranty and a "6-month money-back guarantee." Read our <a href="{href('springwell-review/')}">SpringWell review</a> before buying, because the return policy is narrower than that headline.</p>
<p><strong>Certification:</strong> NSF's listing returned no SpringWell products when we searched on {CHECKED}. <strong>Check certification.</strong></p></div>

<div class="card"><h3>American-made backwashing filter: US Water Systems Bodyguard</h3>
<p>{link("US Water Systems Bodyguard, $945 to $1,399 by size", U['usw_bodyguard'], "uswatersystems")}. A whole-house filter sold for chlorine and chemical removal.</p>
<p><strong>Certification:</strong> NSF lists some US Water Systems filter cartridges under NSF/ANSI 42, but marked "conforms to the material requirements only," which is not a performance certification. <strong>Check certification.</strong></p></div>

<h2>Before you click buy</h2>
<ul>
<li><strong>Match flow to your home.</strong> Bigger homes need higher flow ratings, or you'll feel the pressure drop.</li>
<li><strong>Budget for install.</strong> The Reddit buyer in our SpringWell review paid about $800 for a plumber on top of the equipment. Ask for a written quote.</li>
<li><strong>Read the return policy.</strong> Many "money-back" promises exclude installed systems.</li>
<li><strong>Price the replacement filters,</strong> not just the system.</li>
</ul>
{related(("test-your-water/", "How to test your water"), ("softener-vs-salt-free/", "Need softening too? Salt vs salt-free"), ("springwell-review/", "SpringWell review"))}
{sources(("NSF: standards for water treatment systems", U['nsf_std']), ("NSF certified product listings (searched Nov 19, 2026)", U['nsf_list']), ("WQA product certification", U['wqa']), ("Minnesota Department of Health: water treatment scams", U['mdh_scams']), ("EPA: lead in drinking water", U['epa_lead']))}
'''
    faqs = [("Is a whole house water filter worth it on city water?", "Usually only for taste, odor, or sediment. If your utility meets EPA limits, a whole-house filter is a comfort upgrade, not a health requirement. Check your Consumer Confidence Report first."),
            ("What does NSF/ANSI 42 mean?", "It certifies reduction of aesthetic contaminants such as chlorine, taste, and odor. NSF/ANSI 53 covers contaminants with health effects, like lead."),
            ("Will a whole-house carbon filter remove chloramine?", "Not all are sold for it. If your utility uses chloramine, choose a model the maker sells specifically for chloramine and check its certification.")]
    art("whole-house-water-filter/", "Whole House Water Filter for City Water: Do You Need One? (Shortlist)",
        "When a whole-house filter makes sense on city water, how to read NSF 42/53 claims, and four systems with dated prices and certification status.",
        "Whole-house water filters for city water", body, [("whole-house-water-filter/", "City water filters")], faqs, minutes=8, money=True)

    # =========================================================== WELL WATER
    body = f'''
{answer("For well water, safety first, equipment second. Test for bacteria and nitrate (the CDC's yearly list), then for hardness, iron, manganese, and hydrogen sulfide. The best water softener for well water is a salt-based softener sized for your hardness plus iron. If iron or sulfur is high, an iron and sulfur filter goes in front of it. If bacteria shows up, you need disinfection (often UV), and certification class matters.")}
{DISCLOSURE}
<h2>Step 1: get a lab test, not a guess</h2>
<p>Private wells aren't covered by EPA public water rules. The CDC says to test at least once a year for total coliform bacteria, nitrates, total dissolved solids, and pH with a state-certified lab, and to ask your health department about local contaminants ({cite('CDC', U['cdc_wells'])}). For equipment choices, also test <strong>hardness, iron, manganese, and hydrogen sulfide</strong>. See <a href="{href('test-your-water/')}">how to test</a>.</p>
<p class="note">Good sign from one seller: SpringWell's policy says it holds well-system orders until it reviews a recent water test showing the system fits your water ({cite('SpringWell shipping and returns', U['sw_returns'])}). Any seller that will ship well equipment without seeing a test is guessing.</p>

<h2>Step 2: match the problem to the equipment</h2>
<div class="table-wrap"><table>
<tr><th>Test shows</th><th>What fixes it</th><th>Watch out for</th></tr>
<tr><td>Hardness</td><td>Salt-based softener (NSF/ANSI 44)</td><td>Salt-free units don't remove hardness, iron, or manganese ({cite('Nebraska Extension', U['unl_saltfree'])})</td></tr>
<tr><td>Iron, manganese, rotten-egg smell</td><td>Iron and sulfur filter (air or chemical oxidation) ahead of the softener</td><td>Iron and sulfur can foul softener resin and salt-free media; check each unit's limits</td></tr>
<tr><td>Coliform bacteria</td><td>Fix the source, shock the well, then consider UV disinfection</td><td>NSF/ANSI 55 <strong>Class A</strong> is for contaminated water. <strong>Class B</strong> is only for already-disinfected water ({cite('NSF', U['nsf_std'])})</td></tr>
<tr><td>Nitrate, arsenic, lead</td><td>Usually a certified point-of-use system (often reverse osmosis, NSF/ANSI 58)</td><td>Whole-house sediment and carbon won't fix these</td></tr>
<tr><td>Low pH (acidic)</td><td>Neutralizer</td><td>The CDC notes off-range pH can damage pipes and leach metals</td></tr>
</table></div>

<h2>Step 3: options by problem</h2>
<p>These are comparison options, not tested rankings. Prices are list prices on each maker's site {p(1)}.</p>
<h3>Softeners for well water</h3>
<ul>
<li>{link("US Water Systems Flexx-HD metered softener", U['usw_flexx'], "uswatersystems")}: $899 to $1,288.59 by size.</li>
<li>{link("US Water Systems Matrixx metered softener", U['usw_matrixx'], "uswatersystems")}: $1,094 to $1,694.</li>
<li>{link("SpringWell well filter + salt softener combo", U['sw_wsss'], "springwell")}: WSSS1 listed at $3,234 (regular $3,675); WSSS4 $3,696.</li>
</ul>
<p>Size any of them with the <a href="{href('softener-size-calculator/')}">calculator</a>, and include your iron number.</p>
<h3>Iron and sulfur filters</h3>
<ul>
<li>{link("iSpring WGB32BM (iron and manganese cartridge system)", U['isp_wgb32bm'], "ispring")}: $535.99. Cartridges, so ongoing filter costs, and best for lower levels.</li>
<li>{link("US Water Systems Flexx Oxi-Gen (air injection)", U['usw_oxigen'], "uswatersystems")}: $1,999.45 to $2,565.45.</li>
<li>{link("US Water Systems Flexx InFusion (iron and sulfur)", U['usw_infusion'], "uswatersystems")}: $2,195 to $2,452.45.</li>
<li>{link("SpringWell WS well water filter", U['sw_ws'], "springwell")}: WS1 listed at $2,100 (regular $2,625); WS4 $2,520.</li>
</ul>
<h3>UV disinfection</h3>
<ul>
<li>{link("SpringWell UV system", U['sw_uv'], "springwell")}: listed at $1,036 (regular $1,295). NSF's listing showed no SpringWell products on {CHECKED}. <strong>Check certification.</strong></li>
<li>Aquasana sells a well bundle with UV and says the UV filter is "NSF tested and certified." On NSF's listing, the two Aquasana UV units we found (AQ-UV-MF and AQ-UV-SF) are certified to NSF/ANSI 55 <strong>Class B</strong>. NSF says Class B is for reducing non-disease bacteria in water that's already disinfected. Ask which model ships, and whether it's Class A, before relying on it for a well with bacteria.</li>
</ul>

<h2>Read the warranty fine print for well water</h2>
<p>SpringWell's lifetime warranty on its salt-free FutureSoft line lists well-water conditions it doesn't cover: hydrogen sulfide, oils, copper above 1.30 mg/L, and iron or manganese ({cite('SpringWell warranty', U['sw_warranty'])}). Those are common in wells. That's one more reason to test first and pick salt-based softening with iron pretreatment when your numbers call for it.</p>
{related(("test-your-water/", "How to test well water"), ("softener-size-calculator/", "Softener sizing calculator"), ("springwell-review/", "SpringWell review"))}
{sources(("CDC: Guidelines for testing well water", U['cdc_wells']), ("EPA: Protect your home's water", U['epa_wells']), ("NSF: standards for water treatment systems", U['nsf_std']), ("NSF listings (searched Nov 19, 2026)", U['nsf_list']), ("Nebraska Extension G2275", U['unl_saltfree']), ("SpringWell warranty", U['sw_warranty']), ("SpringWell shipping and returns", U['sw_returns']))}
'''
    faqs = [("What is the best water softener for well water?", "A salt-based ion exchange softener sized for your hardness plus iron, with a dedicated iron and sulfur filter in front if your lab test shows high iron, manganese, or hydrogen sulfide. Salt-free conditioners don't remove hardness or iron."),
            ("Do I need UV for my well?", "Only if testing shows bacteria or your health department recommends it. For contaminated water, look for NSF/ANSI 55 Class A. Class B is for water that's already disinfected."),
            ("What should I test my well for before buying a system?", "The CDC's yearly list (total coliform, nitrates, total dissolved solids, pH) plus hardness, iron, manganese, and hydrogen sulfide for sizing.")]
    art("well-water/", "Best Water Softener and Filter for Well Water (Test First Guide)",
        "Test your well first, then match the problem: softener, iron and sulfur filter, or UV. Options with dated prices and NSF certification checks.",
        "Well water: test first, then pick by problem", body, [("well-water/", "Well water")], faqs, minutes=9, money=True)

    # =========================================================== DOOR TO DOOR
    body = f'''
{answer("You can say no, and you can usually undo a yes. Under the FTC's Cooling-Off Rule, a covered sale made at your home for $25 or more can be canceled until midnight of the third business day after the sale, and the seller has to give you the cancellation form. Get the pitch in writing, get your own test, and get two other quotes.")}
<h2>The pitch, and what state officials say about it</h2>
<p>Minnesota's Department of Health lists the common moves ({cite('MDH', U['mdh_scams'])}):</p>
<ul>
<li><strong>Implying they work with your city or the health department.</strong> MDH says to ask for a named contact at that agency and call them yourself.</li>
<li><strong>Reciting contamination stories</strong> from elsewhere, whether or not they affect your water.</li>
<li><strong>In-home "tests"</strong> that may only show naturally occurring minerals, plus claims that water should contain "zero" of anything.</li>
<li><strong>Misrepresenting drinking water standards</strong> to imply your water is unsafe.</li>
<li><strong>A "one-time" discount</strong> on a unit that's actually sold at a heavily inflated price.</li>
<li><strong>"Maintenance-free"</strong> claims. MDH says all treatment units need maintenance.</li>
</ul>
<p>Florida's Attorney General adds the color-change "free test" (almost any water fails it), prize promotions that require buying a unit, and false claims of government approval. An EPA registration number only means the product was registered, not that the EPA tested or approved it ({cite('Florida AG', U['fl_ag'])}).</p>

<h2>Red flags checklist</h2>
<div class="card"><ul>
<li>They won't leave a written price, model number, and contract to review.</li>
<li>The price drops a lot when you hesitate. A Reddit user in the Orlando area described a pitch that fell from about $11,000 to $3,500 from a company with no website, phone, or card. That's one account, but it's the classic pattern.</li>
<li>They push financing before you've seen the total price.</li>
<li>They can't name a certification (NSF/ANSI 42, 53, 44, 55, or 58) for the exact model, or the certification isn't on NSF's or WQA's listing.</li>
<li>They claim the government requires the system.</li>
<li>"Today only."</li>
</ul></div>

<h2>Your three-day right to cancel</h2>
<p>The FTC's Cooling-Off Rule covers door-to-door sales of $25 or more at your home, or $130 or more at temporary locations like hotel rooms or fairgrounds ({cite('16 CFR 429.0', U['cfr_4290'])}). The seller must ({cite('16 CFR 429.1', U['cfr_4291'])}):</p>
<ul>
<li>give you a dated receipt or contract telling you that you may cancel <strong>before midnight of the third business day</strong> after the sale;</li>
<li>give you two copies of a "Notice of Cancellation" form, and tell you about the right out loud;</li>
<li>refund your payments within 10 business days after getting your cancellation.</li>
</ul>
<p>To cancel, sign and date the notice (or write your own letter) and mail or deliver it before the deadline. Keep a copy and proof of mailing. Some states add more protection, so check with your state attorney general.</p>

<h2>What to do instead</h2>
<ol>
<li>Thank them and take a brochure. Don't let anyone "test" your water in your kitchen.</li>
<li>Get real numbers: your city's report or a certified lab (<a href="{href('test-your-water/')}">how</a>).</li>
<li>Decide what problem you're solving: <a href="{href('softener-vs-salt-free/')}">hardness</a>, <a href="{href('whole-house-water-filter/')}">taste</a>, or <a href="{href('well-water/')}">well contaminants</a>.</li>
<li>Get at least two written quotes. MDH suggests calling other water treatment companies for estimates.</li>
<li>Already signed? Use the three-day cancel. Report deceptive sales to your state attorney general.</li>
</ol>
{related(("test-your-water/", "How to test your water"), ("softener-vs-salt-free/", "Salt vs salt-free"), ("softener-size-calculator/", "Size a softener yourself"))}
{sources(("Minnesota Department of Health: Beware of water treatment scams", U['mdh_scams']), ("Florida Attorney General: How to protect yourself, water treatment devices", U['fl_ag']), ("eCFR 16 CFR 429.0 (definitions)", U['cfr_4290']), ("eCFR 16 CFR 429.1 (the Cooling-Off Rule)", U['cfr_4291']), ("r/orlando: Door-to-door water filtration scam?", "https://www.reddit.com/r/orlando/comments/1htj7oh/doortodoor_water_filtration_scam/"))}
'''
    faqs = [("Can I cancel a water softener I bought from a door-to-door salesman?", "Usually yes. The FTC Cooling-Off Rule lets you cancel a covered home sale of $25 or more until midnight of the third business day, and the seller must give you a cancellation form and refund within 10 business days."),
            ("Are free in-home water tests legit?", "Treat them as a sales tool. Florida's Attorney General says color-change tests used by some sellers would make almost any water, even spring water, look contaminated. Use your utility report or a state-certified lab."),
            ("Does the government require home water treatment?", "No. Florida's Attorney General calls claims that agencies require or recommend household purifiers false, and an EPA registration number doesn't mean EPA approval.")]
    art("door-to-door-water-sales/", "Door-to-Door Water Softener Sales: Red Flags and Your 3-Day Right to Cancel",
        "The in-home water test trick, high-pressure pricing, and how the FTC Cooling-Off Rule lets you cancel within three business days. State AG and health department sources.",
        "Door-to-door water sales: red flags and how to back out", body, [("door-to-door-water-sales/", "Sales red flags")], faqs, minutes=7)

    # =========================================================== CALCULATOR
    body = f'''
{answer("Grains needed between regenerations = hardness (gpg) × people × gallons per person per day × days between regenerations. Add about 4 gpg for every 1 ppm of iron. Then pick a softener whose rated capacity is comfortably above that number.")}
{DISCLOSURE}
<form class="calc" id="calc-form" autocomplete="off">
<label for="hard">Water hardness <span class="hint">from your water report or lab test</span></label>
<div class="row"><input id="hard" type="number" inputmode="decimal" min="0" step="0.1" value="12" aria-describedby="unit"><select id="unit" aria-label="Hardness unit"><option value="gpg">grains per gallon (gpg)</option><option value="mgl">mg/L (ppm) as CaCO₃</option></select></div>
<label for="iron">Iron, ppm (mg/L) <span class="hint">optional, mostly for wells; leave 0 if unknown</span></label>
<input id="iron" type="number" inputmode="decimal" min="0" step="0.1" value="0">
<label for="people">People in the home</label>
<input id="people" type="number" inputmode="numeric" min="1" step="1" value="3">
<label for="gpd">Gallons per person per day <span class="hint">75 is a common sizing assumption</span></label>
<input id="gpd" type="number" inputmode="numeric" min="10" step="5" value="75">
<label for="days">Days between regenerations <span class="hint">7 is typical</span></label>
<input id="days" type="number" inputmode="numeric" min="1" max="14" step="1" value="7">
<p><button class="btn" type="submit">Calculate</button></p>
<div class="result" id="out" aria-live="polite"><noscript>This calculator needs JavaScript. You can do the math by hand with the formula above.</noscript></div>
</form>

<h2>How the math works</h2>
<ol>
<li><strong>Convert units.</strong> If your report lists mg/L (or ppm) as calcium carbonate, divide by 17.1 to get grains per gallon.</li>
<li><strong>Add iron.</strong> Iron also uses up softener capacity. A common dealer rule of thumb adds about 4 gpg per 1 ppm of iron; some use 3 to 5. It's an estimate. Check your softener's spec sheet for its iron limit, too.</li>
<li><strong>Daily grains</strong> = adjusted hardness × people × gallons per person per day.</li>
<li><strong>Grains between regenerations</strong> = daily grains × days.</li>
<li><strong>Pick a size.</strong> Softeners are sold by nominal grain capacity (24,000, 32,000, 48,000, and so on), usually rated at the maximum salt setting. The calculator picks the smallest common size where your need is at most 75% of that rating, so the unit can run at a lower, more salt-efficient setting. About 32,000 grains per cubic foot of resin is a common industry convention. Treat both as rules of thumb, and compare with the maker's own sizing chart.</li>
</ol>
<h2>Where the 75 gallons comes from</h2>
<p>The EPA says the average American family uses more than 300 gallons of water a day at home, and roughly 70% of that is indoors ({cite('EPA WaterSense', U['epa_use'])}). That's about 210 gallons indoors, or about 70 gallons each for a family of three. Softeners usually treat indoor water, so 60 to 80 gallons per person is a reasonable range. If you have a big soaking tub or lots of laundry, go higher. Outdoor irrigation usually shouldn't run through the softener.</p>
<h2>Example</h2>
<p>A family of 4 with 15 gpg hardness and 1 ppm iron: (15 + 4) × 4 × 75 = 5,700 grains a day. Over 7 days that's 39,900 grains, so the rule-of-thumb pick is a 64,000-grain unit (39,900 is 62% of 64,000). A 48,000-grain unit would be at 83% of its rating, so it would need its maximum salt setting or more frequent regenerations.</p>
<h2>What the calculator doesn't cover</h2>
<ul>
<li><strong>Flow rate.</strong> Bigger homes with several bathrooms running at once need a valve and tank that can keep up. Check the unit's service flow rating.</li>
<li><strong>Salt-free conditioners.</strong> They don't remove grains, so this math doesn't apply. See <a href="{href('softener-vs-salt-free/')}">salt vs salt-free</a>.</li>
<li><strong>Health contaminants.</strong> A softener isn't a filter for bacteria, nitrate, or lead. See <a href="{href('well-water/')}">well water</a>.</li>
</ul>
{related(("test-your-water/", "Get your hardness number"), ("well-water/", "Well water options"), ("softener-vs-salt-free/", "Salt vs salt-free"))}
{sources(("EPA WaterSense: How we use water", U['epa_use']), ("Nebraska Extension G2275 (hardness classes)", U['unl_saltfree']), ("USGS: Hardness of water", U['usgs_hard']))}
'''
    faqs = [("How do I calculate what size water softener I need?", "Multiply hardness in grains per gallon (plus about 4 gpg per ppm of iron) by the number of people, by gallons per person per day (about 75), and by the days between regenerations (often 7). Choose a softener rated comfortably above that total."),
            ("What size water softener for a family of 4?", "It depends on hardness. At 10 gpg with no iron, a family of 4 using 75 gallons each needs about 21,000 grains per week, so a 32,000-grain unit fits by the 75% rule of thumb. At 20 gpg it's about 42,000 grains, so a 64,000-grain unit.")]
    art("softener-size-calculator/", "Water Softener Size Calculator (Free): Grains per Gallon × People",
        "Free water softener sizing calculator: enter hardness, iron, and household size to get the grains you need between regenerations and a rule-of-thumb softener size.",
        "Water softener sizing calculator", body, [("softener-size-calculator/", "Sizing calculator")], faqs, minutes=5, money=True,
        extra_head=f"<script defer src=\"{href('calc.js')}\"></script>")

    # =========================================================== SPRINGWELL REVIEW
    body = f'''
{answer("SpringWell sells direct, publishes its prices, and its well systems wait for a water test, which is good. But its headline \"6-month money-back guarantee\" doesn't cover installed systems unless SpringWell decides they're defective. Uninstalled returns carry a 10% restocking fee, up to 25% in some cases, and you pay return shipping. It's not BBB accredited and showed an F rating with 21 complaints in three years when we checked. NSF's listing showed no SpringWell products. Buy only after you've tested your water and are confident the system fits it.")}
{DISCLOSURE}
<p class="small">We haven't installed or lab-tested SpringWell equipment. This review is based on SpringWell's own published prices and policies, NSF's certification listing, the BBB profile, and public customer reports, all checked {CHECKED}.</p>

<h2>Prices (list prices on springwellwater.com)</h2>
<p>A "Thanksgiving Sale, 20% off select systems" banner was running when we checked {p(1)}.</p>
<div class="table-wrap"><table>
<tr><th>System</th><th>Listed price</th><th>Regular price</th></tr>
<tr><td>{link("Whole house filter CF1 / CF4 / CF+", U['sw_cf'], "springwell")}</td><td>$1,092 / $1,218 / $2,016</td><td>$1,365 / $1,523 / $2,520</td></tr>
<tr><td>{link("Salt-based softener SS1 / SS4 / SS+", U['sw_ss'], "springwell")}</td><td>$1,512 / $1,680 / $2,520</td><td>$1,890 / $2,100 / $3,150</td></tr>
<tr><td>{link("Salt-free FutureSoft FS1 / FS4 / FS+", U['sw_fs'], "springwell")}</td><td>$1,680 / $1,848 / $2,184</td><td>$2,100 / $2,310 / $2,730</td></tr>
<tr><td>{link("Filter + salt softener CSS1 / CSS4 / CSS+", U['sw_css'], "springwell")}</td><td>$2,310 / $2,587 / $4,435</td><td>$2,625 / $2,940 / $5,040</td></tr>
<tr><td>{link("Well water filter WS1 / WS4", U['sw_ws'], "springwell")}</td><td>$2,100 / $2,520</td><td>$2,625 / $3,150</td></tr>
<tr><td>{link("Well filter + salt softener WSSS1 / WSSS4", U['sw_wsss'], "springwell")}</td><td>$3,234 / $3,696</td><td>$3,675 / $4,200</td></tr>
<tr><td>{link("UV system", U['sw_uv'], "springwell")}</td><td>$1,036</td><td>$1,295</td></tr>
</table></div>
<p>Installation isn't included. One 2026 buyer reported about $800 for a plumber.</p>

<h2>The return policy, in plain English</h2>
<p>Product pages advertise a "6-month money-back guarantee." The actual policy says ({cite('SpringWell shipping and returns', U['sw_returns'])}):</p>
<ul>
<li>Returns are accepted within six months, but only if the product is <strong>"original, unused condition (uninstalled and in undamaged packaging)."</strong></li>
<li><strong>A 10% restocking fee</strong> applies to all approved non-defective returns, and up to <strong>25%</strong> for returns needing extra handling, inspection, or repackaging, or for refused deliveries.</li>
<li>Original shipping isn't refunded, and <strong>return shipping is on you</strong>.</li>
<li>The "6-month Performance Promise" covers troubleshooting, parts, or "other remedies." <strong>"Installed systems are not eligible for return unless determined defective by SpringWell Water,"</strong> and the policy says this promise focuses on "service resolution rather than full refunds for installed systems."</li>
</ul>
<div class="warn">Translation: if you install it and it simply doesn't do what you hoped (say, a salt-free conditioner that doesn't make your water feel soft), the policy doesn't promise your money back. That's exactly why you should test first and understand <a href="{href('softener-vs-salt-free/')}">what salt-free systems actually do</a>.</div>

<h2>Public complaints</h2>
<ul>
<li><strong>BBB:</strong> "Springwell Water Filtration Systems" (Daytona Beach, FL) is not BBB accredited. When we checked, the profile showed an <strong>F</strong> rating, <strong>21 complaints in the last 3 years</strong>, and <strong>8 in the last 12 months</strong>. By type: 13 service or repair, 4 product, 3 delivery, and 1 customer service. By status: 8 answered, 7 resolved, 5 unanswered, and 1 unresolved ({cite('BBB', U['bbb_sw'])}). One June 2026 complaint describes a nearly $3,500 order that hadn't shipped a month later, despite repeated ship dates.</li>
<li><strong>Reddit (2026):</strong> a buyer says the sales team recommended a salt-free combo (about $2,100, plus about $800 to install) for hard water and his wife's eczema. Five months later nothing had changed, support was slow, and returning it meant a 25% restocking fee and shipping a heavy box himself. He estimated he was out $1,400 to $1,500 ({cite('r/WaterTreatment', U['reddit_sw'])}). This is one customer's account and we couldn't verify it, but it lines up with the written policy above.</li>
</ul>
<p>BBB ratings and complaint counts change, and a complaint count alone doesn't measure a company's size or how many orders went fine. Check the current profile yourself.</p>

<h2>Warranty</h2>
<p>SpringWell offers a lifetime warranty against defects on covered parts like tanks, valves, housings, fittings, and FutureSoft media, plus 10 years on large tanks and 7 years on electronic heads. It excludes improper installation, freezing, and misapplication ({cite('SpringWell warranty', U['sw_warranty'])}). For salt-free FutureSoft on private wells, the warranty requires no hydrogen sulfide, no oils, copper under 1.30 mg/L, and no iron or manganese. Its carbon has a "guarantee of performance" on chlorine and chloramine for 6 years or 1 million gallons. A defect warranty doesn't help if the system was the wrong choice for your water.</p>

<h2>Certification</h2>
<p>SpringWell's product pages we opened didn't show a specific NSF or WQA certification for these systems, and NSF's certified-product listing returned "No Matching Products Found" for SpringWell on {CHECKED}. That doesn't mean the products don't work. It means there's no third-party certification we could confirm. <strong>Check certification</strong>, and ask SpringWell for listing numbers.</p>

<h2>What SpringWell does well</h2>
<ul>
<li>Clear, published pricing. No in-home sales visit needed.</li>
<li>Well-system orders are held until SpringWell reviews a recent water test.</li>
<li>Paid orders can be held up to 30 days, and prices from a sale are honored during the hold.</li>
<li>Long defect warranties on tanks and valves.</li>
</ul>

<h2>Who should consider it, and who shouldn't</h2>
<p><strong>Consider it</strong> if you've tested your water, know your hardness and iron numbers, want a salt-based softener or carbon filter sized to them, and are comfortable that a mismatch won't be refundable once installed.</p>
<p><strong>Skip it, or wait,</strong> if you're buying a salt-free system expecting "soft" water, haven't tested, or need a guaranteed refund after installation. Compare the alternatives on our <a href="{href('whole-house-water-filter/')}">city water</a> and <a href="{href('well-water/')}">well water</a> pages.</p>
{sources(("SpringWell: Shipping, orders and returns", U['sw_returns']), ("SpringWell: Warranty", U['sw_warranty']), ("BBB: Springwell Water Filtration Systems complaints", U['bbb_sw']), ("r/WaterTreatment: PSA about SpringWell (2026)", U['reddit_sw']), ("NSF certified product listings", U['nsf_list']), ("Nebraska Extension G2275", U['unl_saltfree']))}
'''
    faqs = [("Does SpringWell have a money-back guarantee?", "It advertises a 6-month money-back guarantee, but its written policy only accepts unused, uninstalled returns, with a 10% restocking fee (up to 25% in some cases) and return shipping paid by the customer. Installed systems aren't returnable unless SpringWell finds them defective."),
            ("Is SpringWell NSF certified?", "NSF's certified-product listing returned no SpringWell products when we searched on Nov 19, 2026. Ask the company for specific listing numbers before relying on certification claims."),
            ("What is SpringWell's BBB rating?", "When we checked on Nov 19, 2026, the BBB profile showed an F rating, not accredited, with 21 complaints in the last three years. Ratings change, so check the current profile.")]
    art("springwell-review/", "SpringWell Review: Prices, Return Policy Fine Print, and Complaints",
        "A skeptical SpringWell review: dated prices, what the 6-month money-back guarantee really covers, restocking fees, BBB complaints, warranty exclusions, and certification.",
        "SpringWell review: read the return policy first", body, [("springwell-review/", "SpringWell review")], faqs, minutes=9, money=True)

    # =========================================================== ABOUT / DISCLOSURE / PRIVACY
    add("about/", title=f"About {SITE_NAME}", desc="Who runs this site, how we research, and what we will never claim.",
        h1="About Test First Water", crumbs=[("about/", "About")], body=f'''
<p>{SITE_NAME} is a small independent guide to home water treatment. The idea is simple: <strong>test first, then treat</strong>. Too many people buy expensive systems after a kitchen-table sales demo, or buy a "salt-free softener" expecting soft water. We'd rather you spend less and get the right thing.</p>
<h2>How we research</h2>
<ul>
<li>We rely on public authorities first: the EPA, CDC, USGS, state health departments and attorneys general, university extension, and NSF and WQA certification listings.</li>
<li>Prices come from the maker's own product page, with the date we checked.</li>
<li>We only call a product "certified" if we found it on a certifier's listing. Otherwise we say "check certification."</li>
<li>We don't claim hands-on testing or lab results we didn't do, and we don't publish made-up reviews, star ratings, or quotes.</li>
</ul>
<h2>What we are not</h2>
<p>We aren't a dealer, plumber, lab, or doctor. Nothing here is medical, legal, or plumbing advice. For health concerns about your water, contact your local health department or the EPA Safe Drinking Water Hotline at (800) 426-4791 (listed on the CDC's well testing page).</p>
<h2>Contact</h2>
<p>Corrections are welcome: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>''')

    add("affiliate-disclosure/", title="Affiliate Disclosure", desc="How Test First Water may earn money, and how that is kept separate from recommendations.",
        h1="Affiliate disclosure", crumbs=[("affiliate-disclosure/", "Affiliate disclosure")], body=f'''
<p>Some links on this site go to water treatment brands such as SpringWell, Aquasana, iSpring, and US Water Systems. <strong>Right now none of them are affiliate links.</strong> They're plain links to the maker's product page.</p>
<p>We may apply to those brands' affiliate programs later. If we're approved, some links will become affiliate links. If you buy through one, we may earn a commission at no extra cost to you. We'll keep this page updated, and money pages show a short disclosure near the top, in line with the FTC's guidance that material connections should be disclosed clearly.</p>
<h2>What commissions will never change</h2>
<ul>
<li>We'll still tell you when you don't need a system at all.</li>
<li>We'll still publish return-policy fine print, complaints, and missing certifications, including for brands that pay us.</li>
<li>We don't accept payment for placement or for positive coverage.</li>
</ul>
<p>Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>''')

    add("privacy/", title="Privacy Policy", desc="Test First Water uses no analytics, ads, or tracking cookies.",
        h1="Privacy policy", crumbs=[("privacy/", "Privacy")], body=f'''
<p><strong>Short version: we don't track you.</strong></p>
<ul>
<li>No analytics, no ad networks, no tracking pixels, and no cookies set by this site.</li>
<li>The sizing calculator runs entirely in your browser. Your numbers are never sent anywhere.</li>
<li>This site is hosted on GitHub Pages. Like any web host, GitHub may log basic technical data such as IP addresses for security; see GitHub's privacy statement.</li>
<li>When you click a link to another site, that site's privacy policy applies. If we join affiliate programs later, those links may let the merchant or network set cookies on their site to credit the referral. We'll update this page if that happens.</li>
<li>If you email us, we use your email only to reply.</li>
</ul>
<p>Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>. Last updated {dstr}.</p>''')
