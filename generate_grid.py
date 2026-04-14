import re

projects = [
    {"name": "BOGD BANK", "url": "https://www.bogdbank.com/", "desc": "Brand evolution and strategic placement in the financial sector.", "img": "assets/logos/bogd_bank_sign.png"},
    {"name": "APCAC", "url": "http://apcac.org", "desc": "Website, marketing kit, brandbook"},
    {"name": "Amcham", "url": "http://amcham.mn", "desc": "Logo, website, marketing kit - brochure and brandbook"},
    {"name": "MahoneyLiotta", "url": "http://mlmongolia.com", "desc": "Logo, brandbook, marketing kit, brochure, website"},
    {"name": "Woodmont International", "url": "http://woodmontinternational.com", "desc": "Graphic design, website"},
    {"name": "Monos Group", "url": "http://www.monos.mn/", "desc": "Digital presence and group platform"},
    {"name": "Petrovis Group", "url": "http://petrovis.mn/", "desc": "Corporate identity and web ecosystem"},
    {"name": "MCS Holding", "url": "http://mcs.mn/", "desc": "Corporate identity and digital transformation for a leading enterprise."},
    {"name": "Inter Group", "url": "http://wordpress-166003-479729.cloudwaysapps.com/", "desc": "Web ecosystem (Under construction)"},
    {"name": "Altai Holding", "url": "http://wordpress-166003-629112.cloudwaysapps.com/en/", "desc": "Corporate platform (under development)"},
    {"name": "MCSI", "url": "https://www.mcsi.mn/mn", "desc": "Corporate portal"},
    {"name": "MCS Properties (Vita project)", "url": "http://vita.wild.agency/", "desc": "Real estate digital showcase (Under construction)"},
    {"name": "Ard Holdings", "url": "http://ardholdings.com", "desc": "Logo, brandbook, brochure, marketing kit and website for group and all subsidiaries (Credit, Daatgal, Assets)"},
    {"name": "Ard Securities", "url": "http://ardsecurities.com", "desc": "Financial services digital platform"},
    {"name": "Lend", "url": "http://lend.bold.partners", "desc": "Fintech product design"},
    {"name": "EMD", "url": "http://www.emd.gov.mn/", "desc": "Official government digital infrastructure"},
    {"name": "MCS Properties", "url": "http://mcsproperty.mn", "desc": "Real estate investment and platform portfolio"},
    {"name": "Mongolian Cosmetics Cluster", "url": "http://mongoliancosmetics.com/mn/", "desc": "Digital branding platform"},
    {"name": "Vista", "url": "http://vista.mn", "desc": "Brand identity and web interactive logic"},
    {"name": "Altai Cashmere", "url": "http://altaicashmere.mn", "desc": "E-commerce and brand website"},
    {"name": "Zaisan Square", "url": "http://zaisansquare.mn", "desc": "Premium commercial center website"},
    {"name": "Gobi Corporation", "url": "http://gobi.mn", "desc": "Corporate brand nexus"},
    {"name": "Gobi Shop", "url": "https://www.gobicashmere.com/", "desc": "Global premium e-commerce platform"},
    {"name": "MGG Properties", "url": "http://www.mggproperties.com/", "desc": "Bespoke web solutions redefining the property market."},
    {"name": "Gegeenten Entertainment Center", "url": "http://gec.mn", "desc": "A sophisticated digital footprint for premium real-estate/lifestyle."},
    {"name": "Corporate Convention Center", "url": "http://corpconvention.mn", "desc": "Event platform and digital interface"},
    {"name": "IET", "url": "http://iet.wild.agency/", "desc": "Logo, brandbook, digital marketing"},
    {"name": "Yoga Federation", "url": "http://yogafederation.mn", "desc": "Digital presence"},
    {"name": "Teppen", "url": "http://www.teppen.mn", "desc": "Digital presence"},
    {"name": "Mikoto", "url": "http://www.mikoto.mn/en/", "desc": "Brand identity and digital web portfolio"},
    {"name": "News Screening", "url": "http://news.screening.gov.mn", "desc": "Official digital platform"},
    {"name": "Master", "url": "http://www.master.mn/mn", "desc": "Brand portfolio"},
    {"name": "Dicom", "url": "http://beta.dicom.mn/", "desc": "Brand portfolio"}
]

html_snippets = []
for p in projects:
    if "img" in p:
        img_html = f'''                    <div class="card-img-wrapper">
                        <img src="{p['img']}" alt="{p['name']}" class="card-img">
                    </div>'''
    else:
        img_html = ''
        
    card = f'''                <div class="project-card glassmorphism">
{img_html}
                    <div class="card-content">
                        <span class="tag">BOLD / WILD</span>
                        <h3>{p['name']}</h3>
                        <p>{p['desc']}</p>
                        <a href="{p['url']}" target="_blank" class="card-link">View Project &rarr;</a>
                    </div>
                </div>'''
    html_snippets.append(card)

full_inner_html = "\n".join(html_snippets)

with open('index.html', 'r') as f:
    content = f.read()

pattern = r'<div class="projects-grid">.*?</div>\s*</section>'
replacement = f'<div class="projects-grid">\n{full_inner_html}\n            </div>\n        </section>'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(new_content)

print("Done generating 33 project grid cards.")
