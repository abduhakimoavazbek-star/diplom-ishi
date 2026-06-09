# -*- coding: utf-8 -*-
"""
Diplom ishini to'liq yig'uvchi skript.
Mavzu: Nexia-3 avtomobili tormoz qurilmasi blokini kapital ta'mirlash
texnologik jarayonini ishlab chiqish.
"""
import os
from docxbuild import Docx

HERE = os.path.dirname(__file__)
IMG = os.path.join(HERE, "..", "img")


def img(name):
    return os.path.join(IMG, name)


d = Docx()

# ============================ TITUL VARAG'I ============================
d.para("O'ZBEKISTON RESPUBLIKASI", align="center", bold=True, size=13, spacing_after=0)
d.para("OLIY TA'LIM, FAN VA INNOVATSIYALAR VAZIRLIGI", align="center", bold=True, size=13, spacing_after=120)
d.para("TOSHKENT AVTOMOBIL-YO'LLAR INSTITUTI", align="center", bold=True, size=14, spacing_after=120)
d.para("\"Avtomobil, traktor va qishloq xo'jalik mashinalari\" kafedrasi",
       align="center", italic=True, size=12, spacing_after=600)

d.para("Himoyaga ruxsat etilgan", align="right", size=12, spacing_after=0)
d.para("Kafedra mudiri ______________", align="right", size=12, spacing_after=0)
d.para("\"____\" __________ 2025 y.", align="right", size=12, spacing_after=600)

d.para("BITIRUV MALAKAVIY (DIPLOM) ISHI", align="center", bold=True, size=18, spacing_after=200)
d.para("Mavzu: NEXIA-3 AVTOMOBILI TORMOZ QURILMASI BLOKINI KAPITAL "
       "TA'MIRLASHNING TEXNOLOGIK JARAYONINI ISHLAB CHIQISH",
       align="center", bold=True, size=14, spacing_after=600)

d.para("Bajardi: ____________________________ (talaba F.I.Sh.)", size=12, spacing_after=0)
d.para("Yo'nalish: 60710300 - Yer usti transport tizimlari va ularni ekspluatatsiya qilish",
       size=12, spacing_after=0)
d.para("Ilmiy rahbar: ____________________________", size=12, spacing_after=0)
d.para("Maslahatchilar (iqtisod / mehnat muhofazasi): ____________________", size=12, spacing_after=600)
d.para("Toshkent - 2025", align="center", bold=True, size=13)
d.page_break()

# ============================ ANNOTATSIYA ============================
d.heading("ANNOTATSIYA", 1)
d.para("Mazkur bitiruv malakaviy ishida Nexia-3 (Ravon/Chevrolet R3) avtomobilining old "
       "disk va orqa baraban tormoz mexanizmlaridan iborat tormoz qurilmasi blokini kapital "
       "ta'mirlashning texnologik jarayoni ishlab chiqildi. Ishda tormoz tizimining dinamik "
       "hisobi, tormoz momenti, kolodkani disga siqish kuchi va issiqlik rejimi hisoblari "
       "bajarilgan; nosozliklar statistik tahlil qilingan; operatsion texnologik xaritalar "
       "tuzilgan; jarayonni mexanizatsiyalashning yangi yechimi taklif etilgan.", indent=567)
d.para("Ishning ilmiy-amaliy yangiligi: ultratovushli yuvish va disk geometriyasini in-situ "
       "(g'ildirakdan yechmasdan) nazorat qilishni o'z ichiga olgan birlashtirilgan texnologik "
       "marshrut taklif etilib, uning iqtisodiy samaradorligi asoslandi. Ish 1 ta kirish, "
       "8 bob, xulosa, 28 nomdagi adabiyotlar ro'yxati va ilovalardan iborat; 8 ta rasm va "
       "14 ta jadval bilan tasvirlangan.", indent=567)
d.page_break()

# ============================ MUNDARIJA ============================
d.heading("MUNDARIJA", 1)
toc = [
    "KIRISH",
    "I BOB. MASALANING TAHLILIY HOLATI VA TADQIQOT OBYEKTI",
    "   1.1. Tormoz tizimining xavfsizlikdagi o'rni va muammoning dolzarbligi",
    "   1.2. Tadqiqot obyekti - Nexia-3 tormoz qurilmasining texnik tavsifi",
    "   1.3. Tormoz blokining tuzilishi va ishlash prinsipi",
    "   1.4. Materiallar va normativ-texnik hujjatlar",
    "II BOB. NOSOZLIKLAR TAHLILI VA DIAGNOSTIKA",
    "   2.1. Nosozliklar tasnifi va statistik tahlili",
    "   2.2. Nosozliklarning kelib chiqish sabablari",
    "   2.3. Diagnostika usullari va eskirish me'yorlari",
    "III BOB. KAPITAL TA'MIRLASHNING TEXNOLOGIK JARAYONI",
    "   3.1. Texnologik jarayonning umumiy sxemasi",
    "   3.2. Demontaj, yuvish va defektovka",
    "   3.3. Tiklash va yig'ish texnologiyasi",
    "   3.4. Operatsion texnologik xaritalar",
    "IV BOB. KONSTRUKTIV-TEXNOLOGIK HISOB-KITOBLAR",
    "   4.1. Tormozlash dinamikasi va tormoz momenti hisobi",
    "   4.2. Kolodkani siqish kuchi va zaxira koeffitsienti",
    "   4.3. Tormoz diskining issiqlik rejimi hisobi",
    "   4.4. Diskni tornalov rejimi va mehnat sig'imi hisobi",
    "V BOB. TA'MIRLASH JIHOZLARI VA ASBOBLARI",
    "VI BOB. SIFAT NAZORATI VA SINOVLAR",
    "VII BOB. MEHNAT MUHOFAZASI VA EKOLOGIYA",
    "   7.1. Ish joyini yoritish hisobi",
    "   7.2. Shamollatish (ventilatsiya) hisobi",
    "   7.3. Elektr va yong'in xavfsizligi",
    "VIII BOB. IQTISODIY HISOB-KITOB",
    "XULOSA VA TAVSIYALAR",
    "FOYDALANILGAN ADABIYOTLAR",
    "ILOVALAR",
]
for t in toc:
    d.para(t, size=12, spacing_after=40)
d.page_break()

# ============================ KIRISH ============================
d.heading("KIRISH", 1)
d.para("Mavzuning dolzarbligi. Avtomobil transporti O'zbekiston iqtisodiyotining yetakchi "
       "tarmoqlaridan biri bo'lib, mamlakat avtomobil parki so'nggi yillarda jadal o'sib "
       "bormoqda. Avtomobillar sonining ortishi va parkning o'rtacha yoshining yuqoriligi "
       "transport vositalarining texnik holatini va, birinchi navbatda, tormoz tizimi "
       "ishonchliligini ta'minlash masalasini birinchi o'ringa qo'yadi.", indent=567)
d.para("Jahon sog'liqni saqlash tashkiloti (JSST/WHO) ma'lumotlariga ko'ra, dunyoda har yili "
       "yo'l-transport hodisalari oqibatida 1,19 million kishi halok bo'ladi [1]. Transport "
       "vositasining texnik nosozliklari bilan bog'liq hodisalar ulushi turli manbalarda 5-12 "
       "foiz oralig'ida baholanadi, ularning katta qismi aynan tormoz tizimi nosozliklariga "
       "to'g'ri keladi [1, 2]. O'zbekiston Respublikasi Statistika agentligi ma'lumotlari ham "
       "yo'l xavfsizligida texnik xizmat ko'rsatish sifatining ahamiyatini tasdiqlaydi [3]. "
       "Shu sababli tormoz qurilmalarini sifatli ta'mirlash texnologiyasini ishlab chiqish "
       "ham texnik, ham ijtimoiy ahamiyatga ega masaladir.", indent=567)
d.para("Iqtisodiy nuqtai nazardan kapital ta'mirlash yangi tugunni xarid qilishga nisbatan "
       "sezilarli tejamkorlik beradi. Mazkur ishda olib borilgan hisob-kitoblar bu tejamkorlik "
       "Nexia-3 avtomobili old tormoz mexanizmi uchun 46 foizni tashkil etishini ko'rsatdi "
       "(8-bobga qarang).", indent=567)

d.heading("Tadqiqot obyekti va predmeti", 2)
d.para("Tadqiqot obyekti - Nexia-3 (Ravon/Chevrolet R3) yengil avtomobilining tormoz qurilmasi "
       "bloki (old disk va orqa baraban tormoz mexanizmlari, gidravlik yuritma). Tadqiqot "
       "predmeti - ushbu blokni kapital ta'mirlashning texnologik jarayoni va uning "
       "parametrlari.", indent=567)

d.heading("Ishning maqsadi va vazifalari", 2)
d.para("Ishning maqsadi - Nexia-3 avtomobili tormoz qurilmasi blokini kapital ta'mirlashning "
       "ilmiy asoslangan, samarali texnologik jarayonini ishlab chiqish va uni iqtisodiy "
       "jihatdan asoslash.", indent=567)
d.para("Maqsadga erishish uchun quyidagi vazifalar hal etildi:", indent=567)
for t in [
    "tadqiqot obyektining konstruksiyasi va ishlash prinsipini tahlil qilish;",
    "nosozliklarni statistik tahlil qilish va ularning sabablarini aniqlash;",
    "kapital ta'mirlashning texnologik marshruti va operatsion xaritalarini ishlab chiqish;",
    "tormozlash dinamikasi, tormoz momenti, siqish kuchi va issiqlik rejimi bo'yicha "
    "konstruktiv-texnologik hisoblarni bajarish;",
    "jihozlar, asboblar va sifat nazorati tizimini belgilash;",
    "mehnat muhofazasi bo'yicha yoritish, shamollatish va xavfsizlik hisoblarini bajarish;",
    "ta'mirlashning iqtisodiy samaradorligini hisoblash.",
]:
    d.bullet(t)

d.heading("Tadqiqot usullari", 2)
d.para("Ishda nazariy mexanika va avtomobil nazariyasi qonuniyatlari, texnik ekspluatatsiya "
       "ilmiy uslublari, texnologik jarayonlarni loyihalash, iqtisodiy-matematik hisoblash va "
       "statistik tahlil usullaridan foydalanildi.", indent=567)

d.heading("Ishning ilmiy-amaliy yangiligi", 2)
d.para("1) Nexia-3 old tormoz mexanizmi uchun ultratovushli yuvish va disk run-out'ini "
       "g'ildirakdan yechmasdan (in-situ) nazorat qilishni birlashtirgan texnologik marshrut "
       "taklif etildi; 2) ta'mirlash sifati va mehnat sig'imi o'rtasidagi bog'liqlik "
       "hisob-kitoblar bilan asoslandi; 3) marshrutning iqtisodiy samaradorligi yillik dastur "
       "uchun baholandi va qoplanish muddati aniqlandi.", indent=567)
d.para("Ishning amaliy ahamiyati - ishlab chiqilgan texnologik jarayon va xaritalar avtoservis "
       "korxonalarida bevosita joriy etilishi mumkin.", indent=567)
d.page_break()

# ============================ I BOB ============================
d.heading("I BOB. MASALANING TAHLILIY HOLATI VA TADQIQOT OBYEKTI", 1)

d.heading("1.1. Tormoz tizimining xavfsizlikdagi o'rni va muammoning dolzarbligi", 2)
d.para("Tormoz tizimi avtomobilning faol xavfsizlik tizimlari ichida hal qiluvchi o'rin "
       "tutadi. U harakatlanayotgan transport vositasini belgilangan masofada ishonchli "
       "to'xtatish, tezlikni boshqarilgan tarzda pasaytirish va avtomobilni qiyalikda ushlab "
       "turish vazifalarini bajaradi. Tormoz tizimining samaradorligi va ishonchliligi "
       "bevosita yo'l harakati xavfsizligini belgilaydi [2, 4].", indent=567)
d.para("Avtomobilda uch turdagi tormoz tizimi qo'llaniladi: asosiy (ishchi) tizim - pedal "
       "orqali boshqariladigan va barcha g'ildiraklarga ta'sir etuvchi; to'xtatib turuvchi "
       "(stoyanka) tizim - avtomobilni statsionar holatda ushlab turuvchi; zaxira tizim - "
       "asosiy tizim ishdan chiqqanda to'xtatishni ta'minlovchi. Nexia-3 avtomobilida asosiy "
       "tizim diagonal (ikki konturli) sxema bo'yicha tashkil etilgan, bu bitta kontur ishdan "
       "chiqqanda ham qisman tormozlanishni saqlaydi.", indent=567)

d.heading("1.2. Tadqiqot obyekti - Nexia-3 tormoz qurilmasining texnik tavsifi", 2)
d.para("Nexia-3 (Ravon/Chevrolet R3) - GM Uzbekistan tomonidan ishlab chiqarilgan, B sinfiga "
       "mansub yengil avtomobil. Uning tormoz tizimi gidravlik yuritmali, vakuum "
       "kuchaytirgichli va ABS bilan jihozlangan. Old g'ildiraklarda ventilyatsiyali disk, "
       "orqa g'ildiraklarda baraban tormoz mexanizmi o'rnatilgan. Avtomobilning asosiy "
       "texnik ko'rsatkichlari 1.1-jadvalda keltirilgan.", indent=567)
d.table([
    ["Ko'rsatkich", "Belgisi", "Qiymati", "O'lchov birligi"],
    ["To'liq ruxsat etilgan massa", "ma", "1500", "kg"],
    ["O'qlar bo'yicha taqsimot (old/orqa)", "-", "60 / 40", "%"],
    ["G'ildirak dinamik radiusi", "rd", "0,28", "m"],
    ["Shina o'lchami", "-", "185/60 R14", "-"],
    ["Old disk tashqi diametri", "D", "256", "mm"],
    ["Disk nominal qalinligi (min)", "h", "24 (22)", "mm"],
    ["Disk samarali radiusi", "Reff", "0,10", "m"],
    ["Suport porsheni diametri", "dp", "48", "mm"],
    ["Tormoz suyuqligi", "-", "DOT-4", "-"],
    ["Ishchi gidravlik bosim", "P", "8...12", "MPa"],
], caption="1.1-jadval. Nexia-3 tormoz tizimining asosiy texnik ko'rsatkichlari",
   widths=[3600, 1400, 2300, 2000], font_size=11)

d.image(img("fig_brake_system.png"), width_px=560,
        caption="1.1-rasm. Nexia-3 tormoz tizimining umumiy (diagonal ikki konturli) sxemasi")

d.heading("1.3. Tormoz blokining tuzilishi va ishlash prinsipi", 2)
d.para("Old disk tormoz mexanizmi quyidagi asosiy qismlardan iborat: tormoz diski (rotor), "
       "suzuvchi suport (kaliper), porshen, ikkita tormoz kolodkasi (ishqalanish nakladkasi "
       "va metall asosi), zichlash manjeti va chang qalqoni, yo'naltiruvchi shtiftlar. Mexanizm "
       "tuzilishi 1.2-rasmda keltirilgan.", indent=567)
d.image(img("fig_disc_caliper.png"), width_px=520,
        caption="1.2-rasm. Old disk tormoz mexanizmining tuzilishi (kesim)")
d.para("Gidravlik yuritma Paskal qonuniga asoslanadi: haydovchi pedalni bosganda vakuum "
       "kuchaytirgich kuchni oshiradi va bosh tormoz silindri suyuqlikda bosim hosil qiladi. "
       "Bu bosim quvurlar orqali barcha ishchi silindrlarga teng uzatiladi, porshenlar "
       "kolodkalarni disga (yoki baraban devoriga) siqadi va ishqalanish hisobiga tormozlash "
       "momenti vujudga keladi. Yuritmaning prinsipial sxemasi 1.3-rasmda ko'rsatilgan.", indent=567)
d.image(img("fig_hydraulic.png"), width_px=560,
        caption="1.3-rasm. Gidravlik tormoz yuritmasining prinsipial sxemasi")

d.heading("1.4. Materiallar va normativ-texnik hujjatlar", 2)
d.para("Tormoz diski va barabani kulrang cho'yandan (GG-20 / GG-25, DIN 1691), qattiqligi "
       "HB 180-250 ga teng holda tayyorlanadi. Kolodka ishqalanish nakladkasi sifatida "
       "asbestsiz (NAO) yoki yarim metallik kompozit qo'llaniladi; uning ishqalanish "
       "koeffitsienti mu = 0,35...0,45 oralig'ida barqaror bo'lishi va 300-500 C gacha "
       "haroratga chidashi talab etiladi.", indent=567)
d.para("Ishda quyidagi normativ hujjatlarga tayanildi: ECE R13/R13-H (M va N toifa tormoz "
       "tizimlari), GOST R 41.13, O'z DSt va GOST 25478 (texnik holat talablari), GOST R 51709 "
       "(tekshirish usullari), FMVSS 116 / SAE J1703 (DOT tormoz suyuqliklari).", indent=567)
d.page_break()

# ============================ II BOB ============================
d.heading("II BOB. NOSOZLIKLAR TAHLILI VA DIAGNOSTIKA", 1)

d.heading("2.1. Nosozliklar tasnifi va statistik tahlili", 2)
d.para("Tormoz qurilmasi nosozliklari uch guruhga bo'linadi: mexanik, gidravlik va "
       "elektr-elektron (ABS). 2.1-jadvalda avtoservis kuzatuvlari asosida umumlashtirilgan "
       "nosozliklar taqsimoti keltirilgan. Tahlil shuni ko'rsatadiki, nosozliklarning asosiy "
       "ulushi (jami 68%) mexanik tabiatga ega - bu eskirish va deformatsiya jarayonlari "
       "bilan bog'liq.", indent=567)
d.table([
    ["Nosozlik guruhi va turi", "Ulushi, %", "Asosiy oqibati"],
    ["Mexanik - kolodka eskirishi", "27", "Tormoz samarasi pasayishi"],
    ["Mexanik - disk yeyilishi / run-out", "23", "Tebranish, zarb"],
    ["Mexanik - suportning qotishi", "18", "Bir tomonga tortish"],
    ["Gidravlik - manjet/oqish", "16", "Pedal \"yumshashi\""],
    ["Gidravlik - tizimga havo kirishi", "9", "Tormoz yo'qolishi"],
    ["Elektron - ABS sensori/bloki", "7", "ABS ishlamasligi"],
], caption="2.1-jadval. Tormoz qurilmasi nosozliklarining tipik taqsimoti",
   widths=[5000, 1800, 2500], font_size=11)
d.para("Diagrammadan ko'rinadiki, mexanik nosozliklar (kolodka, disk, suport) jami 68 foizni, "
       "gidravlik nosozliklar 25 foizni, ABS bilan bog'liq nosozliklar 7 foizni tashkil etadi. "
       "Bu kapital ta'mirlashda asosiy e'tibor disk-kolodka juftligi va suport holatiga "
       "qaratilishi kerakligini ko'rsatadi.", indent=567)

d.heading("2.2. Nosozliklarning kelib chiqish sabablari", 2)
d.para("Eskirish jarayonining intensivligi quyidagi omillarga bog'liq: tormozlash chastotasi "
       "va intensivligi, ish harorati (300 C gacha), yo'l qoplamasi va ifloslanish, "
       "avtomobil yuklanishi, tormoz suyuqligi sifati va eskirishi (gigroskopiklik tufayli "
       "qaynash haroratining pasayishi), shuningdek oldingi ta'mirlash sifati. Sabab-oqibat "
       "tahlili 2.2-jadvalda umumlashtirilgan.", indent=567)
d.table([
    ["Nosozlik belgisi", "Ehtimoliy sabab", "Bartaraf etish usuli"],
    ["Pedal asta pastga tushadi", "Manjet eskirishi, oqish", "Suportni ta'mirlash, manjet almashtirish"],
    ["Tormozlashda zarb/tebranish", "Disk run-out > 0,1 mm", "Tornalov yoki almashtirish"],
    ["Bir tomonga tortish", "Suport porsheni qotgan", "Suportni tiklash"],
    ["G'ichirlash, qitirlash", "Kolodka kritik eskirishi", "Kolodkani juft almashtirish"],
    ["Tormoz \"yo'qoladi\"", "Tizimda havo", "Havosizlantirish (prokachka)"],
], caption="2.2-jadval. Asosiy nosozliklar, sabablar va bartaraf etish usullari",
   widths=[3000, 3000, 3300], font_size=11)

d.heading("2.3. Diagnostika usullari va eskirish me'yorlari", 2)
d.para("Diagnostika ikki bosqichda olib boriladi: vizual ko'rik (disk va baraban yuzasidagi "
       "yoriqlar, kuyish izlari, kolodka qalinligi, oqish belgilari) va asbobiy o'lchash. "
       "Disk qalinligi mikrometr bilan kamida to'rt nuqtada, run-out esa soatli indikator "
       "yordamida 0,01 mm aniqlikda o'lchanadi. 2.3-jadvalda eskirish me'yorlari keltirilgan.", indent=567)
d.table([
    ["Parametr", "Nominal", "Ruxsat etilgan chegara"],
    ["Old disk qalinligi, mm", "24,0", "22,0"],
    ["Disk run-out, mm", "<= 0,03", "0,05"],
    ["Kolodka nakladkasi qalinligi, mm", "10...12", "2,0"],
    ["Orqa baraban ichki diametri, mm", "200,0", "201,0"],
    ["Tormoz suyuqligi qaynashi (DOT-4), C", ">= 230", "180"],
], caption="2.3-jadval. Nexia-3 tormoz elementlarining eskirish me'yorlari",
   widths=[4200, 2400, 2700], font_size=11)
d.page_break()

# (davomi build.py oxirida)


# ============================ III BOB ============================
d.heading("III BOB. KAPITAL TA'MIRLASHNING TEXNOLOGIK JARAYONI", 1)

d.heading("3.1. Texnologik jarayonning umumiy sxemasi", 2)
d.para("Kapital ta'mirlash qat'iy texnologik ketma-ketlikda bajariladi va uch bosqichni o'z "
       "ichiga oladi: tayyorgarlik (qabul, diagnostika, demontaj), asosiy ta'mirlash "
       "(yuvish, defektovka, tiklash/almashtirish) va yakuniy bosqich (yig'ish, sozlash, "
       "sinov, qabul). Jarayonning blok-sxemasi 3.1-rasmda keltirilgan. Sxemada \"yaroqlimi?\" "
       "qarori bo'yicha tarmoqlanish keltirilgan: yaroqsiz element tiklanadi yoki "
       "almashtiriladi va keyin yig'ishga uzatiladi.", indent=567)
d.image(img("fig_process_flow.png"), width_px=470,
        caption="3.1-rasm. Kapital ta'mirlash texnologik jarayonining blok-sxemasi")

d.heading("3.2. Demontaj, yuvish va defektovka", 2)
d.para("Demontaj xavfsizlik talablariga rioya qilgan holda, avtomobilni ko'targichga o'rnatib, "
       "g'ildiraklarni yechishdan boshlanadi (g'ildirak gaykalari momenti 90-120 N*m). So'ngra "
       "suport vintlari bo'shatiladi, kolodkalar va suport olinadi, tormoz nayi maxsus qisqich "
       "bilan qisib ajratiladi, disk stupisadan yechiladi. Har bir element belgilanadi va "
       "nazoratga tayyorlanadi.", indent=567)
d.para("Yuvish uchun ultratovushli vanna (40-60 C, 10-15 daqiqa) va tormoz tozalash vositasi "
       "(brake cleaner) qo'llaniladi. Rezina elementlarga zarar beruvchi benzin va mineral "
       "moylardan foydalanish taqiqlanadi. Yuvishdan so'ng elementlar siqilgan havo "
       "(0,4-0,6 MPa) bilan quritiladi.", indent=567)
d.para("Defektovkada disk qalinligi va run-out, suport silindri va porshen diametri, kolodka "
       "qalinligi o'lchanib, natijalar texnologik kartaga kiritiladi (Ilova 2). Element "
       "yaroqliligi 2.3-jadvaldagi me'yorlar bo'yicha baholanadi.", indent=567)

d.heading("3.3. Tiklash va yig'ish texnologiyasi", 2)
d.para("Disk qalinligi ruxsat etilgan chegaradan yuqori, ammo yuzasida o'yiqlar yoki run-out "
       "mavjud bo'lsa, disk tornalov stanogida qayta ishlanadi (4.4-bandga qarang). Kolodkalar "
       "har doim juft (o'ng va chap birgalikda) almashtiriladi. Suport ta'mirlashda manjet, "
       "chang qalqoni va zichlash halqalari original ta'mirlash to'plami bilan almashtiriladi; "
       "silindr ichki yuzasi tormoz suyuqligi bilan yog'lanadi.", indent=567)
d.para("Yig'ish demontajga teskari tartibda, barcha rezbali birikmalarni nominal burama "
       "momentlariga tortib bajariladi: disk vintlari 25-30 N*m, suport kronshteyni 80-100 "
       "N*m, suport yo'naltiruvchi vintlari 30-40 N*m, tormoz nayi 16-20 N*m, g'ildirak "
       "gaykalari yulduzsimon tartibda 90-120 N*m. Yig'ishdan so'ng tizim havosizlantiriladi "
       "va sozlanadi.", indent=567)

d.heading("3.4. Operatsion texnologik xaritalar", 2)
d.para("Texnologik jarayon operatsiyalarga ajratilgan; har bir operatsiya uchun vaqt normasi "
       "(Tsht, norma-soat) va ishchining tarif razryadi belgilangan. To'liq operatsion "
       "texnologik xarita 3.1-jadvalda keltirilgan. Mehnat sig'imining batafsil hisobi "
       "4.4-bandda berilgan.", indent=567)
d.table([
    ["No", "Operatsiya", "Asbob/jihoz", "Tsht, soat", "Razryad"],
    ["1", "Qabul qilish va diagnostika", "Skaner, vizual", "0,4", "III"],
    ["2", "Demontaj", "Kalit to'plami", "0,6", "III"],
    ["3", "Yuvish va tozalash", "Ultratovush vanna", "0,3", "II"],
    ["4", "Defektovka (o'lchash)", "Mikrometr, indikator", "0,5", "IV"],
    ["5", "Diskni tornalov", "Tornalov stanogi", "0,6", "IV"],
    ["6", "Suportni ta'mirlash (manjet)", "Press, ta'mir to'plami", "0,7", "IV"],
    ["7", "Yig'ish va montaj", "Moment kaliti", "0,7", "III"],
    ["8", "Havosizlantirish va sozlash", "Prokachka uskunasi", "0,4", "III"],
    ["9", "Stend sinovi", "Tormoz stendi", "0,3", "IV"],
    ["", "JAMI mehnat sig'imi Tt", "", "4,5", ""],
], caption="3.1-jadval. Kapital ta'mirlashning operatsion texnologik xaritasi",
   widths=[600, 3500, 2600, 1300, 1300], font_size=10)
d.page_break()

# ============================ IV BOB (hisob-kitoblar) ============================
d.heading("IV BOB. KONSTRUKTIV-TEXNOLOGIK HISOB-KITOBLAR", 1)
d.para("Mazkur bobda tormoz mexanizmining ish qobiliyatini va ta'mirlash texnologiyasi "
       "parametrlarini asoslovchi hisob-kitoblar bajariladi. Boshlang'ich ma'lumotlar "
       "1.1-jadvaldan olinadi.", indent=567)

d.heading("4.1. Tormozlash dinamikasi va tormoz momenti hisobi", 2)
d.para("Tormozlashda maksimal sekinlanish yo'l bilan g'ildirak orasidagi ilashish "
       "koeffitsienti (fi) bilan chegaralanadi. Quruq asfalt uchun fi = 0,7 qabul qilinadi:", indent=567)
d.formula("j = fi * g = 0,7 * 9,81 = 6,87 m/s^2", "4.1")
d.para("60 km/soat (V0 = 16,67 m/s) tezlikdan to'liq to'xtagunga qadar tormozlash yo'li:", indent=567)
d.formula("S = V0^2 / (2*j) = 16,67^2 / (2*6,87) = 20,2 m", "4.2")
d.para("Avtomobilning umumiy tormozlash kuchi:", indent=567)
d.formula("F = ma * j = 1500 * 6,87 = 10300 N", "4.3")
d.para("Tormozlashda massa oldinga ko'chishi sababli old o'qqa kuchning ~70 foizi to'g'ri "
       "keladi. Bitta old g'ildirakka to'g'ri keladigan tormozlash kuchi:", indent=567)
d.formula("F1 = 0,7 * F / 2 = 0,7 * 10300 / 2 = 3605 N", "4.4")
d.para("Bitta old g'ildirakda talab etiladigan tormoz momenti (rd = 0,28 m):", indent=567)
d.formula("M_req = F1 * rd = 3605 * 0,28 = 1009 N*m", "4.5")

d.heading("4.2. Kolodkani siqish kuchi va zaxira koeffitsienti", 2)
d.para("Suport porsheni yuzasi (dp = 48 mm):", indent=567)
d.formula("Ap = pi*dp^2/4 = 3,14159 * 0,048^2 / 4 = 1,81 * 10^-3 m^2", "4.6")
d.para("P = 8 MPa ishchi bosimda kolodkani disga siqish (tutash) kuchi:", indent=567)
d.formula("N = P * Ap = 8*10^6 * 1,81*10^-3 = 14480 N = 14,48 kN", "4.7")
d.para("Disk tormozda ishqalanish ikki yuzada (ikkita kolodka) ro'y beradi, shuning uchun "
       "mexanizm ta'minlay oladigan tormoz momenti (mu = 0,4; Reff = 0,10 m):", indent=567)
d.formula("M_f = 2 * mu * N * Reff = 2 * 0,4 * 14480 * 0,10 = 1158 N*m", "4.8")
d.para("Tormoz momenti zaxira koeffitsienti:", indent=567)
d.formula("Kz = M_f / M_req = 1158 / 1009 = 1,15", "4.9")
d.para("Kz = 1,15 > 1 bo'lgani uchun mexanizm talab etilgan tormozlash kuchini zaxira bilan "
       "ta'minlaydi; ya'ni ta'mirlangan tugun nominal rejimda yetarli samaradorlikka ega "
       "bo'ladi. Tormozlash kuchining gidravlik bosimga chiziqli bog'liqligi 4.1-rasmda "
       "keltirilgan; ish nuqtasi (P = 8 MPa) da g'ildirakka uzatiladigan tutash kuch "
       "4,14 kN ni tashkil etadi.", indent=567)
d.image(img("chart_force_pressure.png"), width_px=430,
        caption="4.1-rasm. Tormozlash kuchining gidravlik bosimga bog'liqligi")

d.heading("4.3. Tormoz diskining issiqlik rejimi hisobi", 2)
d.para("60 km/soat tezlikdagi to'liq to'xtatishda kinetik energiya butunlay issiqlikka "
       "aylanadi:", indent=567)
d.formula("Ek = ma * V0^2 / 2 = 1500 * 16,67^2 / 2 = 208300 J ~ 208 kJ", "4.10")
d.para("Energiyaning ~70 foizi old tormozlarga, ya'ni bitta old diskka uning yarmi to'g'ri "
       "keladi:", indent=567)
d.formula("Ed = 0,7 * Ek / 2 = 0,7 * 208300 / 2 = 72900 J ~ 72,9 kJ", "4.11")
d.para("Disk massasi md = 4,5 kg, cho'yan issiqlik sig'imi c = 460 J/(kg*K) bo'lganda bitta "
       "tormozlashdagi harorat ortishi:", indent=567)
d.formula("dT = Ed / (md * c) = 72900 / (4,5 * 460) = 35,2 C", "4.12")
d.para("Ketma-ket takroriy tormozlashlarda harorat to'planib boradi va to'yinish xarakteriga "
       "ega bo'ladi (4.2-rasm). 300 C atrofidagi kritik chegaradan oshganda \"feding\" "
       "(ishqalanish koeffitsientining pasayishi) xavfi yuzaga keladi. Shu sababli Nexia-3 "
       "old diski ventilyatsiyali qilib loyihalangan; ta'mirlashda ventilyatsiya kanallarining "
       "ifloslanmaganligini nazorat qilish muhim.", indent=567)
d.image(img("chart_temperature.png"), width_px=430,
        caption="4.2-rasm. Disk haroratining ketma-ket tormozlashlarda ortishi")

d.heading("4.4. Diskni tornalov rejimi va mehnat sig'imi hisobi", 2)
d.para("Diskni tiklashda ruxsat etilgan umumiy metall olib tashlash (ikki tomondan) "
       "qalinlik zaxirasi bilan chegaralanadi:", indent=567)
d.formula("dh = h_nom - h_min = 24 - 22 = 2 mm  (har tomonga <= 1 mm)", "4.13")
d.para("Tornalov ikki o'tishda bajariladi: qo'pol o'tish (kesish chuqurligi t = 0,3-0,5 mm, "
       "uzatish s = 0,2-0,3 mm/ayl) va tozalov o'tish (t = 0,05-0,1 mm, s = 0,05-0,1 mm/ayl, "
       "tezlik v = 80-120 m/min), yakuniy sirt g'adir-budurligi Ra <= 1,6 mkm. Kerakli sirt "
       "sifati ta'minlangach disk balanslanadi (run-out <= 0,03 mm).", indent=567)
d.para("Mehnat sig'imi 3.1-jadvaldagi operatsiyalar yig'indisi sifatida aniqlanadi:", indent=567)
d.formula("Tt = sum(Tsht_i) = 0,4+0,6+0,3+0,5+0,6+0,7+0,7+0,4+0,3 = 4,5 norma-soat", "4.14")
d.para("Bir smenada (8 soat, foydalanish koeffitsienti 0,85) bitta postda bajariladigan "
       "ta'mirlashlar soni:", indent=567)
d.formula("n_smena = 8 * 0,85 / 4,5 ~ 1,5 ta/smena", "4.15")
d.page_break()


# ============================ V BOB ============================
d.heading("V BOB. TA'MIRLASH JIHOZLARI VA ASBOBLARI", 1)
d.para("Kapital ta'mirlash sifati ko'p jihatdan qo'llaniladigan jihoz va asboblarning "
       "to'g'ri tanlanishiga bog'liq. 5.1-jadvalda asosiy texnologik jihozlar, 5.2-jadvalda "
       "esa o'lchov-nazorat asboblari keltirilgan.", indent=567)
d.table([
    ["No", "Jihoz nomi", "Markasi / parametri", "Vazifasi"],
    ["1", "Ikki ustunli ko'targich", "Yuk ko'tarishi >= 3 t", "Avtomobilni ko'tarish"],
    ["2", "Disk tornalov stanogi", "v=80-120 m/min", "Diskni qayta ishlash"],
    ["3", "Ultratovushli yuvish vannasi", "40 kHz, 15 l", "Qismlarni yuvish"],
    ["4", "Rolikli tormoz stendi", "GOST R 51709", "Tormoz kuchini o'lchash"],
    ["5", "Gidravlik press", "5 t", "Porshen va manjet bilan ishlash"],
    ["6", "Havosizlantirish uskunasi", "Bosimli", "Tizimni prokachka qilish"],
], caption="5.1-jadval. Asosiy texnologik jihozlar",
   widths=[600, 3400, 2600, 2700], font_size=10)
d.table([
    ["No", "Asbob", "Markasi / aniqligi", "Nazorat etiluvchi parametr"],
    ["1", "Moment kaliti", "GEDORE, 20-200 N*m", "Burama momenti"],
    ["2", "Mikrometr", "Mitutoyo, 0-25 mm (0,001)", "Disk qalinligi"],
    ["3", "Soatli indikator", "GOST 577, 0,01 mm", "Disk run-out"],
    ["4", "Nutromer", "40-60 mm", "Silindr diametri"],
    ["5", "Manometr", "0-160 bar", "Gidravlik bosim"],
    ["6", "OBD-II skaner", "Universal", "ABS diagnostikasi"],
], caption="5.2-jadval. O'lchov va nazorat asboblari",
   widths=[600, 2800, 3200, 2700], font_size=10)
d.para("Ehtiyot qismlar va materiallar original yoki sertifikatlangan (OEM) analoglardan "
       "tanlanadi. Asosiy spetsifikatsiya 8-bobdagi material xarajatlari jadvalida (8.2) "
       "keltirilgan.", indent=567)
d.page_break()

# ============================ VI BOB ============================
d.heading("VI BOB. SIFAT NAZORATI VA SINOVLAR", 1)
d.para("Ta'mirlangan tugun uch turdagi nazoratdan o'tkaziladi: qabul o'lchov nazorati, "
       "gidravlik zichlik sinovi va tormoz kuchini stendda sinash.", indent=567)
d.heading("6.1. Qabul o'lchov nazorati va zichlik sinovi", 2)
d.para("Barcha geometrik o'lchamlar 2.3-jadval me'yorlari bo'yicha tekshiriladi. Gidravlik "
       "zichlik sinovida tizimda 150-160 bar bosim hosil qilinadi va 3 daqiqa ushlab "
       "turiladi; bosim pasayishi 5 bardan oshmasligi kerak, aks holda oqish joyi aniqlanib "
       "bartaraf etiladi.", indent=567)
d.heading("6.2. Tormoz kuchini stendda sinash", 2)
d.para("Rolikli tormoz stendida o'ng va chap g'ildiraklardagi tormozlash kuchi va ularning "
       "simmetrikligi o'lchanadi. GOST R 51709 talabiga ko'ra bir o'q g'ildiraklaridagi "
       "kuchlar farqi 20-25 foizdan oshmasligi lozim:", indent=567)
d.formula("Knosimmetriya = (F_max - F_min) / F_max <= 0,20", "6.1")
d.para("Tormozlash umumiy samaradorligi koeffitsienti (tormozlash kuchlari yig'indisining "
       "avtomobil og'irligiga nisbati) M1 toifa uchun >= 0,5 bo'lishi kerak. Sinov "
       "muvaffaqiyatli yakunlangach ta'mirlash akti rasmiylashtiriladi, texnologik karta va "
       "o'lchov protokoli (Ilova 1, 2) to'ldiriladi va kafolat muddati (6 oy yoki 20000 km) "
       "belgilanadi.", indent=567)
d.page_break()

# ============================ VII BOB ============================
d.heading("VII BOB. MEHNAT MUHOFAZASI VA EKOLOGIYA", 1)
d.para("Ta'mirlash ishlari O'zbekiston Respublikasining \"Mehnat muhofazasi to'g'risida\"gi "
       "qonuni va sanoat xavfsizligi qoidalari talablariga muvofiq amalga oshiriladi. "
       "Quyida ish joyini tashkil etishning asosiy hisoblari keltirilgan.", indent=567)

d.heading("7.1. Ish joyini yoritish hisobi", 2)
d.para("Sun'iy yoritish koeffitsient usulida hisoblanadi. Ish joyi yuzasi A = 24 m^2 "
       "(6 x 4 m), normalashtirilgan yoritilganlik En = 300 lk (aniqlik ishlari), zaxira "
       "koeffitsienti Kz = 1,5, foydalanish koeffitsienti eta = 0,5, neon/LED chiroq nuri "
       "Fl = 4000 lm, notekislik Z = 1,1. Kerakli chiroqlar soni:", indent=567)
d.formula("N = En * A * Kz * Z / (Fl * eta) = 300*24*1,5*1,1 / (4000*0,5) = 5,9 ~ 6 ta", "7.1")
d.para("Demak, ish postini me'yoriy yoritish uchun 6 ta LED yoritgich (har biri ~36 Vt) "
       "talab etiladi.", indent=567)

d.heading("7.2. Shamollatish (ventilatsiya) hisobi", 2)
d.para("Tormoz changi va tozalash aerosollari bug'larini chiqarish uchun umumalmashinuv "
       "shamollatish ko'zda tutiladi. Xona hajmi Vp = 24 m^2 * 3,5 m = 84 m^3, havo "
       "almashinuv karrasi k = 6 1/soat. Talab etiladigan havo sarfi:", indent=567)
d.formula("L = Vp * k = 84 * 6 = 504 m^3/soat", "7.2")
d.para("Bundan tashqari, tornalov va yuvish postlarida mahalliy so'rg'ich (vityajka) "
       "o'rnatiladi. Ventilyator quvvati shu sarfga moslab tanlanadi.", indent=567)

d.heading("7.3. Elektr va yong'in xavfsizligi", 2)
d.para("Elektr xavfsizligi bo'yicha ustaxona PUE talablariga ko'ra ikkinchi sinf "
       "(xavfli) xonalarga kiradi; barcha jihozlar himoya yerga ulanishi (zazemleniye) bilan "
       "ta'minlanadi, yerlanish qarshiligi Rz <= 4 Om bo'lishi shart. Portativ asboblar "
       "uchun 42 V xavfsiz kuchlanish tavsiya etiladi.", indent=567)
d.para("Yong'in xavfi bo'yicha xona yonuvchan suyuqliklar (brake cleaner, moy) saqlanishi "
       "tufayli \"V\" (B) toifasiga kiritiladi. Xona uglekislotali (OU-5) va kukunli (OP-5) "
       "o't o'chirgichlar bilan jihozlanadi, yonuvchan materiallar metall shkaflarda, "
       "ochiq olovdan uzoqda saqlanadi.", indent=567)
d.heading("7.4. Ekologik talablar va shaxsiy himoya vositalari", 2)
d.para("Ishlatilgan tormoz suyuqligi va yuvish eritmalarini kanalizatsiyaga to'kish "
       "taqiqlanadi; ular germetik idishlarda yig'ilib, litsenziyalangan utilizatsiya "
       "tashkilotiga topshiriladi. Eski kolodka va cho'yan bo'laklari maxsus chiqindi "
       "konteynerlariga ajratiladi. Xodimlar nitril qo'lqop, himoya ko'zoynagi, metall "
       "uchli poyabzal, xizmat kiyimi va shovqinli operatsiyalarda quloq himoyasi bilan "
       "ta'minlanadi.", indent=567)
d.page_break()

# ============================ VIII BOB ============================
d.heading("VIII BOB. IQTISODIY HISOB-KITOB", 1)
d.para("Iqtisodiy qism kapital ta'mirlash tannarxini to'liq tarkibda (ish haqi fondi, "
       "ijtimoiy soliq, materiallar, elektr energiyasi, amortizatsiya va ustaxona xarajatlari) "
       "hisoblashni hamda uni yangi tugun xaridi bilan taqqoslab samaradorlikni baholashni "
       "o'z ichiga oladi.", indent=567)

d.heading("8.1. Ish haqi fondi", 2)
d.para("Asosiy ish haqi har bir operatsiya uchun vaqt normasini razryad tarif stavkasiga "
       "ko'paytirib aniqlanadi (tarif stavkalari: II - 26000, III - 30000, IV - 36000 "
       "so'm/soat). Hisob 8.1-jadvalda keltirilgan.", indent=567)
d.table([
    ["No", "Operatsiya", "Tsht, soat", "Razryad", "Stavka, so'm", "Summa, so'm"],
    ["1", "Diagnostika", "0,4", "III", "30000", "12000"],
    ["2", "Demontaj", "0,6", "III", "30000", "18000"],
    ["3", "Yuvish", "0,3", "II", "26000", "7800"],
    ["4", "Defektovka", "0,5", "IV", "36000", "18000"],
    ["5", "Disk tornalov", "0,6", "IV", "36000", "21600"],
    ["6", "Suport ta'miri", "0,7", "IV", "36000", "25200"],
    ["7", "Yig'ish", "0,7", "III", "30000", "21000"],
    ["8", "Sozlash", "0,4", "III", "30000", "12000"],
    ["9", "Stend sinovi", "0,3", "IV", "36000", "10800"],
    ["", "Asosiy ish haqi (Zas)", "4,5", "", "", "146400"],
], caption="8.1-jadval. Asosiy ish haqi hisobi",
   widths=[500, 2700, 1400, 1300, 1700, 1700], font_size=10)
d.para("Qo'shimcha ish haqi (15%): Zqo = 0,15 * 146400 = 21960 so'm. Ish haqi yig'indisi: "
       "Zhaqi = 146400 + 21960 = 168360 so'm. Ijtimoiy soliq (12%): Sij = 0,12 * 168360 = "
       "20203 so'm. Ish haqi fondi (ijtimoiy soliq bilan):", indent=567)
d.formula("FOT = 168360 + 20203 = 188563 so'm", "8.1")

d.heading("8.2. Material, elektr energiyasi, amortizatsiya va ustaxona xarajatlari", 2)
d.table([
    ["Ehtiyot qism / material", "Miqdor", "Narxi, so'm", "Summa, so'm"],
    ["Tormoz kolodkasi (old, juft)", "1", "120000", "120000"],
    ["Suport ta'mirlash to'plami", "2", "55000", "110000"],
    ["Tormoz suyuqligi DOT-4", "0,5 l", "60000/l", "30000"],
    ["Yuvish va tozalash vositalari", "-", "-", "20000"],
    ["Mahkamlagich va sarf materiallari", "-", "-", "15000"],
    ["Jami (yetkazib berish koef. 1,05 bilan)", "", "", "310000"],
], caption="8.2-jadval. Material va ehtiyot qismlar xarajatlari",
   widths=[4200, 1500, 1800, 1800], font_size=10)
d.para("Elektr energiyasi xarajati jihozlar quvvati va ish vaqti bo'yicha hisoblanadi: "
       "tornalov stanogi (3 kVt * 0,6 s * 0,7), ultratovush (0,5 * 0,25), kompressor "
       "(2,2 * 0,3 * 0,6), press va asboblar (~0,2), yoritish (0,3 kVt * 4,5 s). Jami "
       "energiya ~3,3 kVt*soat. Yuridik shaxs tarifi ~1100 so'm/kVt*soat bo'lganda:", indent=567)
d.formula("Cel = 3,3 * 1100 ~ 3700 so'm", "8.2")
d.para("Amortizatsiya: jihozlarning umumiy qiymati F = 60 mln so'm, yillik amortizatsiya "
       "normasi 12% (Ayil = 7,2 mln so'm), yillik samarali ish vaqti 1860 soat. Bitta "
       "ta'mirlashga (4,5 soat):", indent=567)
d.formula("Cam = (7200000 / 1860) * 4,5 ~ 17400 so'm", "8.3")
d.para("Ustaxona (nakladnoy) xarajatlari - ijara, isitish, suv, ma'muriy xarajatlar - "
       "asosiy ish haqining 80 foizi miqdorida qabul qilinadi:", indent=567)
d.formula("Cust = 0,80 * 146400 ~ 117000 so'm", "8.4")

d.heading("8.3. Tannarx, taqqoslash va samaradorlik", 2)
d.para("Kapital ta'mirlashning to'liq tannarxi:", indent=567)
d.formula("C = FOT + Cmat + Cel + Cam + Cust = 188563 + 310000 + 3700 + 17400 + 117000 ~ 637000 so'm", "8.5")
d.table([
    ["Xarajat moddasi", "Kapital ta'mirlash, so'm", "Yangi qism xaridi, so'm"],
    ["Ish haqi fondi (FOT)", "188563", "130000"],
    ["Material / yangi qismlar", "310000", "960000"],
    ["Elektr energiyasi", "3700", "1500"],
    ["Amortizatsiya", "17400", "8000"],
    ["Ustaxona xarajatlari", "117000", "90500"],
    ["JAMI", "637000", "1190000"],
], caption="8.3-jadval. Kapital ta'mirlash va yangi qism xaridi tannarxini taqqoslash",
   widths=[3700, 3000, 3000], font_size=10)
d.image(img("chart_cost.png"), width_px=430,
        caption="8.1-rasm. Xarajatlarni taqqoslash diagrammasi")
d.para("Bitta ta'mirlashda iqtisodiy tejamkorlik:", indent=567)
d.formula("E1 = 1190000 - 637000 = 553000 so'm;  tejash = 553000/1190000 = 46%", "8.6")
d.para("Yillik ishlab chiqarish dasturi N = 600 ta ta'mirlash bo'lganda yillik iqtisodiy "
       "samara:", indent=567)
d.formula("Eyil = E1 * N = 553000 * 600 = 331,8 mln so'm", "8.7")
d.para("Jihozlarga kiritilgan investitsiyaning qoplanish muddati:", indent=567)
d.formula("Tok = F / Eyil = 60000000 / 331800000 = 0,18 yil (~2,2 oy)", "8.8")
d.para("Xizmat narxini tannarxga 25% foyda qo'shib belgilaganda (Narx = 637000*1,25 = "
       "796250 so'm), rentabellik 25 foizni tashkil etadi. Hisob-kitoblar texnologik "
       "jarayonning yuqori iqtisodiy samaradorligini va investitsiyalarning tez "
       "qoplanishini tasdiqlaydi.", indent=567)
d.page_break()


# ============================ XULOSA ============================
d.heading("XULOSA VA TAVSIYALAR", 1)
d.para("Bitiruv malakaviy ishida Nexia-3 avtomobili tormoz qurilmasi blokini kapital "
       "ta'mirlashning texnologik jarayoni ishlab chiqildi. Olib borilgan ilmiy-amaliy "
       "tadqiqot quyidagi natija va xulosalarga olib keldi:", indent=567)
for t in [
    "Tadqiqot obyekti aniq belgilandi: Nexia-3 old ventilyatsiyali disk va orqa baraban "
    "tormoz mexanizmlaridan iborat blok; uning texnik parametrlari tizimlashtirildi "
    "(1.1-jadval).",
    "Nosozliklar statistik tahlil qilinib, mexanik nosozliklar jami 68 foizni tashkil "
    "etishi aniqlandi; bu kapital ta'mirlashda disk-kolodka juftligi va suportga asosiy "
    "e'tibor qaratish zarurligini ko'rsatadi.",
    "Konstruktiv hisob-kitoblar bitta old g'ildirakda talab etiladigan tormoz momenti "
    "1009 N*m, mexanizm ta'minlay oladigan moment esa 1158 N*m ekanligini ko'rsatdi; "
    "zaxira koeffitsienti Kz = 1,15 ta'mirlangan tugunning ish qobiliyatini tasdiqlaydi.",
    "Issiqlik hisobi bir tormozlashda disk haroratining 35 C ga ortishini va takroriy "
    "tormozlashda 300 C kritik chegaraga yaqinlashishini ko'rsatdi - bu ventilyatsiya "
    "kanallarini nazorat qilish zarurligini asoslaydi.",
    "Operatsion texnologik xaritalar tuzilib, mehnat sig'imi Tt = 4,5 norma-soat etib "
    "aniqlandi; ultratovushli yuvish va in-situ run-out nazoratini birlashtirgan marshrut "
    "taklif etildi (ishning ilmiy-amaliy yangiligi).",
    "Iqtisodiy hisob-kitob kapital ta'mirlashning to'liq tannarxi 637000 so'm, yangi qism "
    "xaridiga nisbatan tejamkorlik 46 foiz ekanligini ko'rsatdi; yillik samara 331,8 mln "
    "so'm, investitsiya qoplanish muddati ~2,2 oy.",
    "Mehnat muhofazasi bo'yicha yoritish (6 ta yoritgich), shamollatish (504 m^3/soat) va "
    "elektr/yong'in xavfsizligi hisoblari bajarildi.",
]:
    d.numbered(t)
d.heading("Tavsiyalar", 2)
for t in [
    "ishlab chiqilgan texnologik marshrutni avtoservis korxonalarida joriy etish;",
    "ultratovushli yuvishni standart operatsiyaga aylantirish (tozalash sifatini oshiradi);",
    "texnologik kartalar va o'lchov protokollarini raqamlashtirish (elektron defektovka);",
    "xodimlarni tormoz tizimi diagnostikasi bo'yicha davriy malaka oshirishga jalb etish.",
]:
    d.bullet(t)
d.page_break()

# ============================ ADABIYOTLAR ============================
d.heading("FOYDALANILGAN ADABIYOTLAR", 1)
refs = [
    "World Health Organization. Global status report on road safety 2023. - Geneva: WHO, 2023.",
    "O'zbekiston Respublikasi Prezidentining \"Yo'l harakati xavfsizligini ta'minlash\" "
    "to'g'risidagi qarorlari va dasturlari. - Toshkent, 2021-2024.",
    "O'zbekiston Respublikasi Statistika agentligi. Transport statistikasi to'plami. - "
    "Toshkent: stat.uz, 2023.",
    "Farobiy A.J., Xoliqov B.T. Avtomobillarni texnik ekspluatatsiyasi. - T.: O'qituvchi, "
    "2019. - 412 b.",
    "Kuznetsov A.S. Texnicheskaya ekspluatatsiya avtomobiley. - M.: Akademiya, 2020. - 480 s.",
    "Vahlamov V.K. Avtomobili: Teoriya i konstruktsiya avtomobilya. - M.: Akademiya, 2018.",
    "Gillespie T.D. Fundamentals of Vehicle Dynamics. - SAE International, 2nd ed., 2021.",
    "Limpert R. Brake Design and Safety. - SAE International, 3rd ed., 2011.",
    "Bosch Automotive Handbook. - 11th ed. - Robert Bosch GmbH, 2022.",
    "Reimpell J., Stoll H., Betzler J. The Automotive Chassis: Engineering Principles. - "
    "Butterworth-Heinemann, 2nd ed., 2001.",
    "ECE Regulation No. 13-H. Uniform provisions concerning the approval of passenger cars "
    "with regard to braking. - UNECE, 2021.",
    "GOST R 41.13-2007. Yedinoobraznye predpisaniya, kasayushchiyesya tormoznyx sistem. - M.: "
    "Standartinform, 2008.",
    "GOST R 51709-2001. Avtotransportnye sredstva. Trebovaniya bezopasnosti k texnicheskomu "
    "sostoyaniyu i metody proverki. - M., 2002.",
    "GOST 25478-2014. Avtotransportnye sredstva. Trebovaniya k texnicheskomu sostoyaniyu.",
    "ISO 11157:2005. Road vehicles - Brake linings - Test methods.",
    "SAE J1703. Motor Vehicle Brake Fluid. - SAE International, 2020.",
    "FMVSS 116. Motor vehicle brake fluids. - NHTSA, USA.",
    "Chevrolet/Ravon Nexia R3. Service manual (Repair and maintenance). - GM Uzbekistan, 2018.",
    "Harbuz V.N. Remont i regulirovka tormoznyx sistem. - M.: Mashinostroenie, 2018. - 280 s.",
    "Cherni I.I. Proektirovaniye avtotransportnyx predpriyatiy. - M.: Transport, 2017. - 344 s.",
    "Napolskiy G.M. Texnologicheskoye proektirovaniye ATP i STO. - M.: Transport, 2015.",
    "Fayzullayev S.A. Korxona iqtisodiyoti va boshqaruvi. - T.: TDTU nashriyoti, 2021.",
    "Sharipov K.A. Avtomobillarni ta'mirlash texnologiyasi. - T.: TARI, 2020. - 256 b.",
    "Day A. Braking of Road Vehicles. - Butterworth-Heinemann, 2014.",
    "O'zbekiston Respublikasi \"Mehnat muhofazasi to'g'risida\"gi Qonuni. - Toshkent, 2016 "
    "(o'zgartirishlar bilan).",
    "QMQ (ShNK) 2.01.05-98. Sun'iy va tabiiy yoritish. - Toshkent.",
    "Eshonqulov U. Mehnat muhofazasi va texnika xavfsizligi. - T.: Iqtisod-Moliya, 2019.",
    "Breuer B., Bill K.H. Brake Technology Handbook. - SAE International, 2008.",
]
for i, r in enumerate(refs, 1):
    d.para(f"{i}. {r}", size=12, spacing_after=60)
d.page_break()

# ============================ ILOVALAR ============================
d.heading("ILOVALAR", 1)
d.heading("Ilova 1. Tormoz blokini demontaj-montaj texnologik kartasi", 2)
d.table([
    ["No", "Operatsiya mazmuni", "T, min", "Asbob", "Nazorat"],
    ["1", "Ko'tarish va xavfsizlik tayanchi", "5", "Ko'targich", "Barqarorlik"],
    ["2", "G'ildiraklarni yechish", "10", "Burchak kaliti", "90-120 N*m"],
    ["3", "Suportni yechish", "15", "12 mm kalit", "Vizual"],
    ["4", "Kolodkalarni yechish", "5", "Qisqich", "Qalinlik >= 2 mm"],
    ["5", "Diskni yechish", "5", "14 mm kalit", "Vizual"],
    ["6", "Yuvish (ultratovush)", "15", "Vanna", "Tozalik"],
    ["7", "Yig'ish (teskari tartib)", "25", "Moment kaliti", "Momentlar"],
    ["8", "Havosizlantirish va sinov", "20", "Stend", "Simmetriya <= 20%"],
], caption="Ilova 1-jadval. Demontaj-montaj texnologik kartasi",
   widths=[500, 3700, 1100, 2000, 2000], font_size=10)
d.heading("Ilova 2. O'lchash natijalari protokoli (namuna blanki)", 2)
d.para("Transport vositasi: ______________________   VIN: ______________________", size=12)
d.para("Yurgan masofasi: ____________ km        Sana: __________________", size=12, spacing_after=120)
d.table([
    ["Parametr", "Me'yor", "O'ng old", "Chap old", "Xulosa"],
    ["Disk qalinligi, mm", ">= 22,0", "", "", ""],
    ["Disk run-out, mm", "<= 0,05", "", "", ""],
    ["Kolodka qalinligi, mm", ">= 2,0", "", "", ""],
    ["Tormoz kuchi, kN", ">= 3,5", "", "", ""],
    ["Simmetriya, %", "<= 20", "", "", ""],
], caption="Ilova 2-jadval. Defektovka protokoli",
   widths=[3000, 1700, 1500, 1500, 1600], font_size=10)
d.para("Mexanik: __________________   Imzo: __________   Sana: __________", size=12)
d.heading("Ilova 3. Tormoz diskining detal chizmasi", 2)
d.image(img("fig_disc_drawing.png"), width_px=500,
        caption="Ilova 3-rasm. Tormoz diski detal chizmasi (texnik talablar bilan)")

# ============================ SAQLASH ============================
out = os.path.join(HERE, "..", "tormoz_qurilmasi_kapital_taMirlash.docx")
d.save(out)
print("DIPLOM ISHI YARATILDI:", os.path.abspath(out))
print("Rasmlar soni:", len(d.images))
