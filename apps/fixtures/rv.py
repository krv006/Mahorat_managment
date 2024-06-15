import json

country = [
    "Afg'oniston", "Armaniston", "Ozarbayjon", "Bahrayn", "Bangladesh", "Butan", "Bruney", "Kambodja", "Xitoy",
    "Kipr", "Gruziya", "Hindiston", "Indoneziya", "Eron", "Iroq", "Isroil", "Yaponiya", "Iordaniya", "Qozog'iston",
    "Quvayt", "Qirg'iziston", "Laos", "Livan", "Malayziya", "Maldiv orollari", "Mongoliya", "Myanma", "Nepal",
    "Shimoliy Koreya", "Ummon", "Pokiston", "Falastin", "Filippin", "Qatar", "Rossiya", "Saudiya Arabistoni",
    "Singapur", "Janubiy Koreya", "Shri-Lanka", "Suriya", "Tayvan", "Tailand", "Tojikiston", "Turkmaniston",
    "Birlashgan Arab Amirliklari", "O'zbekiston", "Vyetnam", "Yaman", "Buyuk Britaniya", "Germaniya", "Fransiya",
    "Italiya", "Ispaniya", "Niderlandiya", "Belgiya", "Shveytsariya", "Avstriya", "Shvetsiya", "Norvegiya",
    "Daniya", "Finlandiya", "Irlandiya", "Gretsiya", "Portugaliya", "Polsha", "Chexiya", "Vengriya", "Avstraliya",
    "Rossiya (g'arbiy qismi)", "Ukraina", "Ruminiya", "Bolgariya", "Xorvatiya", "Serbiya", "Slovakiya", "Sloveniya"
]

json_list = []
for i, davlat in enumerate(country, start=1):
    json_list.append({
        "model": "app_name.book",
        "pk": i,
        "fields": {
            "title": davlat
        }
    })

json_data = json.dumps(json_list, ensure_ascii=False, indent=2)

with open('country.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

learning = [
    "Tanlang",
    "110 000 - Pedagogika",
    "210 000 - Art",
    "220 000 - Gumanitar fanlar",
    "310 000 - Jurnalistika va Ijtimoiy axborot",
    "320 000 - Biznes va boshqaruv",
    "330 000 - To'g'ri",
    "410 000 - Tabiiy fanlar",
    "510 000 - Muhandislik fanlari",
    "520 000 - Kompyuter texnologiyalari va informatika",
    "530 000 - Ishlab chiqarish va qayta ishlash sanoati",
    "540 000 - Arxitektura va qurilish",
    "555 000 - Aloqa va axboratlashtirish, telekommunikatsiya texnologiyalari",
    "610 000 - Qishloq, o'rmon va baliq xo'jaligi",
    "620 000 - Qishloq xo'jaligi texnikasi",
    "620 000 - Qishloq xo'jaligi irrigatsiyasi va melirotsiyasi",
    "630 000 - Veterinariya tibbiyoti",
    "710 000 - Sog'liqni saqlash",
    "710 000 - Ijtimoiy ta'minot",
    "810 000 - Texnik xizmat ko'rsatish",
    "820 000 - Transport",
    "830 000 - Atrof-muhitni muhofaza qilish",
    "840 000 - Hayot xavfsizligi"
]

json_list = []
for i, learning in enumerate(learning, start=1):
    json_list.append({
        "model": "apps.Employee",
        "pk": i,
        "fields": {
            "title": learning
        }
    })

json_data = json.dumps(json_list, ensure_ascii=False, indent=2)

with open('learn.json', 'w', encoding='utf-8') as f:
    f.write(json_data)
