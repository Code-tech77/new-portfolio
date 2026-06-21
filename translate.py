import re

def process_file(filename, translations, is_rtl=False, lang_code='en', dropdown_lang='EN', dropdown_flag='🇬🇧'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update html tag
    if is_rtl:
        content = content.replace('<html lang="en">', '<html lang="ar" dir="rtl">')
    else:
        content = content.replace('<html lang="en">', f'<html lang="{lang_code}">')

    # Update Dropdown Desktop
    content = content.replace(
        '<span class="flag">🇬🇧</span> <span class="lang-text">EN</span>',
        f'<span class="flag">{dropdown_flag}</span> <span class="lang-text">{dropdown_lang}</span>'
    )
    
    # Update active class on dropdown
    content = content.replace('class="lang-option active"', 'class="lang-option"')
    if lang_code == 'ar':
        content = content.replace('href="index-ar.html" class="lang-option"', 'href="index-ar.html" class="lang-option active"')
    elif lang_code == 'es':
        content = content.replace('href="index-es.html" class="lang-option"', 'href="index-es.html" class="lang-option active"')

    # Translations
    for en_str, trans_str in translations.items():
        content = content.replace(en_str, trans_str)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Arabic Translations
ar_translations = {
    "&#60;Home&#62;": "&#60;الرئيسية&#62;",
    "&#60;AboutMe&#62;": "&#60;نبذة عني&#62;",
    "&#60;Ventures&#62;": "&#60;مشاريعي&#62;",
    "&#60;Skills&#62;": "&#60;مهاراتي&#62;",
    "&#60;Projects&#62;": "&#60;مشاريع برمجية&#62;",
    "&#60;Volunteer&#62;": "&#60;عمل تطوعي&#62;",
    "&#60;/Home&#62;": "&#60;/الرئيسية&#62;",
    "&#60;/AboutMe&#62;": "&#60;/نبذة عني&#62;",
    "&#60;/Founder&#62;": "&#60;/مؤسس&#62;",
    "&#60;/Skills&#62;": "&#60;/مهاراتي&#62;",
    "&#60;/Projects&#62;": "&#60;/مشاريع&#62;",
    "&#60;/Volunteer&#62;": "&#60;/تطوع&#62;",
    "Hello I'm Mohammed Zuoriki": "مرحباً، أنا محمد زوريقي",
    "Aspiring Cloud Security Engineer": "مهندس أمن سحابي طموح",
    "Cloud Security": "الأمن السحابي",
    "Let's Talk!": "لنتحدث!",
    "Resume": "السيرة الذاتية",
    "Tech Stack": "التقنيات",
    "Software Projects": "مشاريع برمجية",
    "Networking & Sec Projects": "مشاريع الشبكات والأمن",
    "Volunteer Work": "العمل التطوعي",
    "Top Certifications": "أهم الشهادات",
    "BACK TO TOP": "العودة للأعلى"
}

# Spanish Translations
es_translations = {
    "&#60;Home&#62;": "&#60;Inicio&#62;",
    "&#60;AboutMe&#62;": "&#60;SobreMí&#62;",
    "&#60;Ventures&#62;": "&#60;Proyectos&#62;",
    "&#60;Skills&#62;": "&#60;Habilidades&#62;",
    "&#60;Projects&#62;": "&#60;Proyectos&#62;",
    "&#60;Volunteer&#62;": "&#60;Voluntariado&#62;",
    "&#60;/Home&#62;": "&#60;/Inicio&#62;",
    "&#60;/AboutMe&#62;": "&#60;/SobreMí&#62;",
    "&#60;/Founder&#62;": "&#60;/Fundador&#62;",
    "&#60;/Skills&#62;": "&#60;/Habilidades&#62;",
    "&#60;/Projects&#62;": "&#60;/Proyectos&#62;",
    "&#60;/Volunteer&#62;": "&#60;/Voluntariado&#62;",
    "Hello I'm Mohammed Zuoriki": "Hola, soy Mohammed Zuoriki",
    "Aspiring Cloud Security Engineer": "Aspirante a Ingeniero de Seguridad en la Nube",
    "Cloud Security": "seguridad en la nube",
    "Let's Talk!": "¡Hablemos!",
    "Resume": "CV",
    "Tech Stack": "Tecnologías",
    "Software Projects": "Proyectos de Software",
    "Networking & Sec Projects": "Proyectos de Redes y Seguridad",
    "Volunteer Work": "Trabajo Voluntario",
    "Top Certifications": "Principales Certificaciones",
    "BACK TO TOP": "VOLVER ARRIBA"
}

process_file('index-ar.html', ar_translations, is_rtl=True, lang_code='ar', dropdown_lang='AR', dropdown_flag='🇸🇦')
process_file('index-es.html', es_translations, is_rtl=False, lang_code='es', dropdown_lang='ES', dropdown_flag='🇪🇸')
print("Translation complete!")
