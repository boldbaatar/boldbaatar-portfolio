import re

with open('quote.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Edit 1: Update Subtitle
html = html.replace('<span class="subtitle">AgencyPro</span>', '<span class="subtitle">AgencyPro / BOD Consulting & Partners</span>')

# Edit 2: Update Hero description to include motto
hero_desc = '<p class="desc">Вэбсайт хөгжүүлэлт, брэндинг, маркетинг болон технологийн цогц шийдлүүдийн дэлгэрэнгүй танилцуулга ба цар хүрээ.</p>'
new_hero_desc = hero_desc + '\n                <p style="color: var(--accent-1); font-size: 1.1rem; font-style: italic; max-width: 800px; margin: 1rem auto 0;">"Empowering our Partners to achieve consistent success by building synergy between Consulting, Branding, Digital Media and Technology"</p>'
html = html.replace(hero_desc, new_hero_desc)

# Edit 3: Update Branding Package price to higher bracket
old_price = '<div class="price-text" style="color: #fff;">33,500,000 ₮</div>'
new_price = '<div class="price-text" style="color: #fff;">33,500,000 - 45,000,000 ₮</div>'
html = html.replace(old_price, new_price)

# Edit 4: Inject the new Appendix Divs into the Detailed Appendix Section
appendix_insertion_marker = '<!-- Detailed Appendix Section -->\n        <section class="fade-in" style="margin-bottom: 4rem;">\n            <div class="glassmorphism" style="padding: 4rem; border-radius: 16px;">\n                <h3 style="font-family: var(--font-head); font-size: 2.2rem; margin-bottom: 2rem;">Дэлгэрэнгүй Мэдээлэл & <span class="gradient-text">Задаргаа</span></h3>\n                \n                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 3rem;">\n'

new_appendix_blocks = """
                    <div>
                        <h4 style="color: #ff90ff; margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">Visual Package (Брэндбүүк & Лого)</h4>
                        <ul class="quote-list" style="font-size: 0.9rem;">
                            <li><strong>01. Logo:</strong> Symbols, text, color, fonts, description, usage, dimensions, variations...</li>
                            <li><strong>02. Business documents:</strong> Memos, letterhead, envelope, business card, ID card, contract, folders...</li>
                            <li><strong>03. Documents for clients:</strong> Invitation, brochure, DVD cover, photo standards, signatures...</li>
                            <li><strong>04. Printing and materials:</strong> Billboard, flags, car 3d/print, exterior/interior signs...</li>
                            <li><strong>05. Marketing materials:</strong> Magazine layouts, merchandises (cup, cap, pen, flash drive, t-shirt)...</li>
                            <li><strong>06. Custom items:</strong> Determined by business domain and client requirements.</li>
                        </ul>
                    </div>

                    <div>
                        <h4 style="color: var(--accent-1); margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">Вэб Хөгжүүлэлтийн Үе Шатууд (Milestones)</h4>
                        <ul class="quote-list" style="font-size: 0.9rem;">
                            <li><strong>Week 1 (Start & Design):</strong> Contract, Management agreement, Research, Home & Subpage design, Photographic service.</li>
                            <li><strong>Week 2 (Development):</strong> UI, UX coding, Backend, Function modules.</li>
                            <li><strong>Week 3-4 (Testing):</strong> Bug fix, Security, Speed, Stability, Polishing.</li>
                            <li><strong>Week 5 (Review & Deployment):</strong> Polishing, Hosting and Management setup.</li>
                            <li><strong>Months 12-36+ (Maintenance):</strong> Yearly updates, improvement. Yearly hosting payment 200,000 ₮.</li>
                        </ul>
                    </div>
                    
                    <div>
                        <h4 style="color: #bdc2ff; margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">Цогц Кампанит Ажлууд (1-2 сар+)</h4>
                        <ul class="quote-list" style="font-size: 0.9rem;">
                            <li><strong>1. Content Marketing Package: 19,000,000 ₮</strong> Facebook Ads, Content Schedule/Publishing, Reporting, Engagement strategy.</li>
                            <li><strong>2. Full Marketing Campaign: 28,000,000 ₮</strong> App design, Social ad posters (27-28), advanced boost in engagement and likes calculation.</li>
                            <li><strong style="color: #ff90ff;">Notes:</strong> Facebook advertisement cost is separate (~$500+ advised). Traditional media/printing not covered. Quotes include 10% project management fee and 30% profit margin (+10% VAT).</li>
                        </ul>
                    </div>
                    
                    <div>
                        <h4 style="color: var(--accent-1); margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">Нэмэлт Консалтинг Системүүд</h4>
                        <ul class="quote-list" style="font-size: 0.9rem;">
                            <li><strong>Удирдлагын Системийн Хэрэгжилт:</strong> 1. Project preparation, 2. Planning & Doc, 3. Implementation, 4. Review, 5. Certification.</li>
                            <li><strong>Quality & Environment:</strong> Health, Safety and Food safety management systems.</li>
                            <li><strong>Security:</strong> Information security, Centralized control, and Laboratory quality systems.</li>
                            <li><strong>ISO Standard Trainings:</strong> Business administration, HR, Health and Safety, PECB trainings.</li>
                        </ul>
                    </div>
"""

html = html.replace(appendix_insertion_marker, appendix_insertion_marker + new_appendix_blocks)

with open('quote.html', 'w', encoding='utf-8') as f:
    f.write(html)
