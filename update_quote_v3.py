import re

with open('quote.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Terms Payment info
target_terms = '<span>Урьдчилгаа: 60%</span>\n                    <span>Явцын төлбөр: 20%</span>\n                    <span>Үлдэгдэл: 20%</span>'
new_terms = '<span>Урьдчилгаа төлбөр: 70%</span>\n                    <span>Үлдэгдэл төлбөр: 30%</span>'
html = html.replace(target_terms, new_terms)

# 2. Append Team list to Appendix
hook_team = '<li><strong style="color: #ff90ff;">Notes:</strong> Facebook advertisement cost is separate'
new_team = '<li><strong>Marketing Team:</strong> Маркетингийн мэргэжилтэн, Дизайнер, Фото зурагчин, Сэтгүүлч, Сошиал мэргэжилтэн зэрэг тусгай баг ажиллана.</li>\n                            ' + hook_team
html = html.replace(hook_team, new_team)

# 3. Add the Massive Training Curriculum Section right before the Detailed Appendix
target_insertion = '        <!-- Detailed Appendix Section -->'
new_curriculum = """
        <!-- Training & Curriculum Expansion -->
        <section class="fade-in" style="margin-top: 8rem;">
            <h2 class="section-title">Сургалт Консалтинг <span class="gradient-text">& Хөтөлбөрүүд</span></h2>
            <p style="text-align:center; color: rgba(255,255,255,0.6); margin-top:-2rem; margin-bottom: 3rem;">Нарийвчилсан сэдэв, агуулга болон төсөв үнэлгээ (2025)</p>
            
            <div class="glassmorphism" style="padding: 4rem; border-radius: 16px; margin-bottom: 4rem;">
                <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-start; margin-bottom: 3rem;">
                    <div>
                        <h3 style="font-size: 2.2rem; font-family: var(--font-head); font-weight: 800; color: #fff; margin-bottom: 1.5rem;">Сургалтын Төсөв & Үнэлгээ</h3>
                        <ul class="quote-list" style="max-width: 600px; font-size: 1.05rem;">
                            <li><strong>Дан танхимын лекц (1-2 цаг, 50 хүртэл хүн):</strong> <span style="color: var(--accent-1); font-weight: 700;">2,900,000 ₮ / 1 цаг</span></li>
                            <li><strong>Зөвлөх, практик хосолсон (1 цаг, 2 баг):</strong> <span style="color: var(--accent-1); font-weight: 700;">2,700,000 ₮ / 1 цаг</span></li>
                            <li><strong>1+ өдрийн цогц сургалт (8 цаг+):</strong> <span style="color: var(--accent-1); font-weight: 700;">2,350,000 ₮ / 1 цаг</span></li>
                            <li style="margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.1);"><strong>Нийт Сургалтын Багц Жишээ (10-14 цаг):</strong> <span style="font-size: 1.8rem; color: #ff90ff; font-weight: 900; margin-left:1rem;">29,600,000 ₮</span></li>
                        </ul>
                    </div>
                    <div style="background: rgba(0,0,0,0.4); padding: 2.5rem; border-radius: 12px; max-width: 450px;">
                        <h4 style="color: var(--accent-1); font-size: 1.2rem; margin-bottom: 1rem;">Сургалтын Нөхцөл:</h4>
                        <ul class="quote-list" style="font-size: 0.95rem;">
                            <li>Сургалт хамгийн багадаа 1-3 хоног байна.</li>
                            <li>Сургалтын анги танхим, өдрийн хоол, кофе, ус, интернет, проекторыг захиалагч бүрэн хариуцна.</li>
                            <li>Америкийн Маркетингийн Холбооны (AMA) үнэгүй ба төлбөртэй темплэйтүүд ашиглагдана.</li>
                            <li>Оролцогчид лаптоптой байх.</li>
                        </ul>
                    </div>
                </div>

                <h3 style="font-size: 2rem; font-family: var(--font-head); font-weight: 800; color: #fff; margin-bottom: 2rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 1rem;">Брэнд Гэж Юу Вэ? Брэнд Бүтээх Хөтөлбөр</h3>
                <div class="quote-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));">
                    <div style="background: rgba(255,255,255,0.03); padding: 2rem; border-radius: 12px; border-top: 3px solid var(--accent-1);">
                        <h4 style="color: #fff; font-size: 1.2rem; margin-bottom: 0.8rem;">1. Илтгэл, Ярилцлага (2 цаг)</h4>
                        <p style="font-size: 0.9rem; color: rgba(255,255,255,0.7); line-height: 1.6;">Үндсэн ойлголтууд болон Монголын, дэлхийн Кэйсүүд.</p>
                    </div>
                    <div style="background: rgba(255,255,255,0.03); padding: 2rem; border-radius: 12px; border-top: 3px solid #ff90ff;">
                        <h4 style="color: #fff; font-size: 1.2rem; margin-bottom: 0.8rem;">2. Бүтээх Аргачлалууд (1 цаг)</h4>
                        <p style="font-size: 0.9rem; color: rgba(255,255,255,0.7); line-height: 1.6;">Суурь нөхцөл, хандлага. Дэвшилтэт ба уламжлалт маркетингийг хослуулан бага зардлаар өндөр үр дүнд хүрэх стратеги.</p>
                    </div>
                    <div style="background: rgba(255,255,255,0.03); padding: 2rem; border-radius: 12px; border-top: 3px solid #bdc2ff;">
                        <h4 style="color: #fff; font-size: 1.2rem; margin-bottom: 0.8rem;">3. Брэнд Консепт (3-4 цаг)</h4>
                        <p style="font-size: 0.9rem; color: rgba(255,255,255,0.7); line-height: 1.6;">Брэндийн давуу талыг гаргах. Мессэж, утга санаа (WHY, HOW, WHAT). Дизайн сэтгэлгээгээр консепт гаргах процессууд.</p>
                    </div>
                    <div style="background: rgba(255,255,255,0.03); padding: 2rem; border-radius: 12px; border-top: 3px solid var(--accent-1);">
                        <h4 style="color: #fff; font-size: 1.2rem; margin-bottom: 0.8rem;">4. Брэнд Дизайн (1 цаг/баг)</h4>
                        <p style="font-size: 0.9rem; color: rgba(255,255,255,0.7); line-height: 1.6;">Хялбар, зардал багатай загвар бүтээх техник, аргачлал. Шаардлага болон дизайны процесс.</p>
                    </div>
                    <div style="background: rgba(255,255,255,0.03); padding: 2rem; border-radius: 12px; border-top: 3px solid #ff90ff;">
                        <h4 style="color: #fff; font-size: 1.2rem; margin-bottom: 0.8rem;">5. Цахим Брэнд хоногшуулалт</h4>
                        <p style="font-size: 0.9rem; color: rgba(255,255,255,0.7); line-height: 1.6;">Зорилтот бүлэгтээ хямд хүрэх. Брэнд-хэрэглэгчийн үнэ цэнийн холбоог бэхжүүлж, үнэнч хэрэглэгчийг хувиргах.</p>
                    </div>
                </div>

                <h3 style="font-size: 2rem; font-family: var(--font-head); font-weight: 800; color: #fff; margin-top: 4rem; margin-bottom: 2rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 1rem;">Нэмэлт Сургалтын Агуулгууд</h3>
                <div class="quote-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                    <div>
                        <h4 style="color: var(--accent-1); font-size: 1.1rem; margin-bottom: 0.8rem;">Интернет & Сошиал Маркетинг</h4>
                        <ul class="quote-list" style="font-size: 0.9rem;">
                            <li>Дэвшилтэт хэрэгслүүдийг бодитоор ашиглах. Цахим дүр төрхөө хоногшуулах стратеги.</li>
                            <li>Үнэнч хэрэглэгчдэд тулгуурласан зардал багатай борлуулалт буюу Inbound Marketing.</li>
                            <li>Олон нийтийн сүлжээний (Facebook, Instagram гэх мэт) алгоритм, тактикууд, хандлагыг удирдах.</li>
                        </ul>
                    </div>
                    <div>
                        <h4 style="color: #bdc2ff; font-size: 1.1rem; margin-bottom: 0.8rem;">Агуулга & Хэрэглэгчийн Технологи</h4>
                        <ul class="quote-list" style="font-size: 0.9rem;">
                            <li>Чанартай агуулгыг төлөвлөх, бүтээх, түгээх вайрал (Viral) ба SEO хайлтын борлуулалт.</li>
                            <li>Шинэ үеийн зан төлөвт нийцэх Dynamic болон User-generated контент, гар утасны (Mobile web) танилцуулга.</li>
                            <li>Имейл маркетинг болон интерактив хэрэглэгчийн урт хугацааны систем барих.</li>
                        </ul>
                    </div>
                    <div>
                        <h4 style="color: #ff90ff; font-size: 1.1rem; margin-bottom: 0.8rem;">Мэдлэгийн Удирдлагад IT Ашиглах</h4>
                        <ul class="quote-list" style="font-size: 0.9rem;">
                            <li>Ажлын дотоод төлөвлөлт, хамтын ажиллагааны Cloud клауд хэрэгслүүд ашиглах, мэдлэгийг нөөцлөх.</li>
                            <li>Байгууллагын файлыг системчлэх, архив болон мэдлэгийн сан зохион байгуулах.</li>
                            <li>Мэдээллийн алдагдлыг зогсоох, зардлыг үнэмлэхүй бууруулах Realtime мэдээллийн технологиуд.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

"""
html = html.replace(target_insertion, new_curriculum + target_insertion)

with open('quote.html', 'w', encoding='utf-8') as f:
    f.write(html)

