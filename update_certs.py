import re
import os

files = {
    'en': '/Users/mohammedzuoriki/Desktop/PROJECTS/new-portfolio/index.html',
    'es': '/Users/mohammedzuoriki/Desktop/PROJECTS/new-portfolio/index-es.html',
    'ar': '/Users/mohammedzuoriki/Desktop/PROJECTS/new-portfolio/index-ar.html'
}

data = {
    'en': [
        {
            'title': 'AZ-104: Azure Administrator',
            'img': 'src/AZ-104.png',
            'sub': 'Microsoft | Date: 2024',
            'desc': 'Validates expertise in managing cloud services that span storage, security, networking, and compute capabilities across Microsoft Azure environments.'
        },
        {
            'title': 'Terraform Associate',
            'img': 'src/004.png',
            'sub': 'HashiCorp | Date: 2024',
            'desc': 'Demonstrates proficiency in basic concepts and skills associated with HashiCorp Terraform, including infrastructure as code, execution plans, and state management.'
        },
        {
            'title': 'Fortinet Certified Associate',
            'img': 'src/FCA.png',
            'sub': 'Fortinet | Date: 2024',
            'desc': 'Validates fundamental knowledge of cybersecurity concepts and Fortinet\'s basic network security solutions and principles.'
        },
        {
            'title': 'IBM MQ Certification',
            'img': 'src/MQ.png',
            'sub': 'IBM | Date: 2024',
            'desc': 'Proves knowledge of IBM MQ administration, messaging concepts, architecture, and the ability to configure and manage queue managers.'
        },
        {
            'title': 'Snowflake GenAI Professional',
            'img': 'src/snowflake.png',
            'sub': 'Snowflake | Date: 2024',
            'desc': 'Demonstrates the ability to leverage Snowflake\'s data capabilities for training, evaluating, and deploying Generative AI models.'
        }
    ],
    'es': [
        {
            'title': 'AZ-104: Azure Administrator',
            'img': 'src/AZ-104.png',
            'sub': 'Microsoft | Fecha: 2024',
            'desc': 'Valida la experiencia en la administración de servicios en la nube que abarcan almacenamiento, seguridad, redes y capacidades de computación en entornos de Microsoft Azure.'
        },
        {
            'title': 'Terraform Associate',
            'img': 'src/004.png',
            'sub': 'HashiCorp | Fecha: 2024',
            'desc': 'Demuestra competencia en conceptos básicos y habilidades asociadas con HashiCorp Terraform, incluida la infraestructura como código.'
        },
        {
            'title': 'Fortinet Certified Associate',
            'img': 'src/FCA.png',
            'sub': 'Fortinet | Fecha: 2024',
            'desc': 'Valida el conocimiento fundamental de los conceptos de ciberseguridad y las soluciones básicas de seguridad de red de Fortinet.'
        },
        {
            'title': 'IBM MQ Certification',
            'img': 'src/MQ.png',
            'sub': 'IBM | Fecha: 2024',
            'desc': 'Demuestra conocimientos sobre la administración de IBM MQ, conceptos de mensajería, arquitectura y capacidad para gestionar colas.'
        },
        {
            'title': 'Snowflake GenAI Professional',
            'img': 'src/snowflake.png',
            'sub': 'Snowflake | Fecha: 2024',
            'desc': 'Demuestra la capacidad de aprovechar los datos de Snowflake para entrenar, evaluar e implementar modelos de IA generativa.'
        }
    ],
    'ar': [
        {
            'title': 'AZ-104: Azure Administrator',
            'img': 'src/AZ-104.png',
            'sub': 'Microsoft | التاريخ: 2024',
            'desc': 'يثبت الخبرة في إدارة الخدمات السحابية التي تشمل التخزين والأمن والشبكات وقدرات الحوسبة عبر بيئات مايكروسوفت أزور.'
        },
        {
            'title': 'Terraform Associate',
            'img': 'src/004.png',
            'sub': 'HashiCorp | التاريخ: 2024',
            'desc': 'يثبت الكفاءة في المفاهيم والمهارات الأساسية المرتبطة بـ HashiCorp Terraform، بما في ذلك البنية التحتية ككود.'
        },
        {
            'title': 'Fortinet Certified Associate',
            'img': 'src/FCA.png',
            'sub': 'Fortinet | التاريخ: 2024',
            'desc': 'يثبت المعرفة الأساسية بمفاهيم الأمن السيبراني وحلول أمن الشبكات الأساسية من Fortinet.'
        },
        {
            'title': 'IBM MQ Certification',
            'img': 'src/MQ.png',
            'sub': 'IBM | التاريخ: 2024',
            'desc': 'يثبت المعرفة بإدارة IBM MQ، ومفاهيم المراسلة، والبنية، والقدرة على تكوين وإدارة مديري قوائم الانتظار.'
        },
        {
            'title': 'Snowflake GenAI Professional',
            'img': 'src/snowflake.png',
            'sub': 'Snowflake | التاريخ: 2024',
            'desc': 'يثبت القدرة على الاستفادة من إمكانات بيانات Snowflake لتدريب وتقييم ونشر نماذج الذكاء الاصطناعي التوليدي.'
        }
    ]
}

def generate_html(cert, lang):
    btn_text = 'Validate Certificate'
    if lang == 'es': btn_text = 'Validar Certificado'
    if lang == 'ar': btn_text = 'التحقق من الشهادة'
    
    return f'''          <div class="cert-card" data-aos="fade-up">
            <div class="cert-title">{cert["title"]}</div>
            <img alt="{cert["title"]}" class="cert-image" src="{cert["img"]}"
              style="height:130px; width:auto; display:block; margin-left:auto; margin-right:auto;" />
            <div class="cert-sub">{cert["sub"]}</div>
            <p class="cert-desc">{cert["desc"]}</p>
            <button class="cert-validate-btn">
              <a href="#" style="color: inherit; text-decoration: none;"><span>{btn_text}</span></a>
              <svg height="10px" viewbox="0 0 13 10" width="15px">
                <path d="M1,5 L11,5"></path>
                <polyline points="8 1 12 5 8 9"></polyline>
              </svg>
            </button>
          </div>'''

for lang, file_path in files.items():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    start_str = '<div class="cert-track cert-track-left">'
    start_idx = content.find(start_str)
    
    if start_idx == -1:
        print(f"Could not find cert-track in {file_path}")
        continue
        
    start_idx += len(start_str)
    end_str = '        </div>\n      </div>'
    end_idx = content.find(end_str, start_idx)
    
    track_content = content[start_idx:end_idx]
    
    # Split by <div class="cert-card"
    # Find all start indices
    card_starts = [m.start() for m in re.finditer(r'<div class="cert-card"', track_content)]
    
    if len(card_starts) < 9:
        print(f"Found less than 9 cards in {file_path}. Cannot replace the last 5.")
        continue
        
    # We want to keep cards 0, 1, 2, 3
    kept_content = track_content[:card_starts[4]]
    
    # Generate the 5 new cards
    new_cards_html = '\n'.join([generate_html(c, lang) for c in data[lang]])
    new_cards_html = '\n' + new_cards_html + '\n'
    
    # Write everything back
    new_track = kept_content + new_cards_html
    new_content = content[:start_idx] + new_track + content[end_idx:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Replaced cards 5-9 in {file_path}")

