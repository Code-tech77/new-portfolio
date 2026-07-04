import re

files = {
    '/Users/mohammedzuoriki/Desktop/PROJECTS/new-portfolio/index.html': {
        'az': 'Date: July 2026',
        'tf': 'Date: August 2026',
        'fca': 'Date: Feb 2026',
        'ibm': 'Date: January 2026',
        'sf': 'Date: March 2026'
    },
    '/Users/mohammedzuoriki/Desktop/PROJECTS/new-portfolio/index-es.html': {
        'az': 'Fecha: julio 2026',
        'tf': 'Fecha: agosto 2026',
        'fca': 'Fecha: febrero 2026',
        'ibm': 'Fecha: enero 2026',
        'sf': 'Fecha: marzo 2026'
    },
    '/Users/mohammedzuoriki/Desktop/PROJECTS/new-portfolio/index-ar.html': {
        'az': 'التاريخ: يوليو 2026',
        'tf': 'التاريخ: أغسطس 2026',
        'fca': 'التاريخ: فبراير 2026',
        'ibm': 'التاريخ: يناير 2026',
        'sf': 'التاريخ: مارس 2026'
    }
}

for file_path, dates in files.items():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Validate Certificate Buttons
    # The button looks like: <button class="cert-validate-btn"> ... </button>
    content = re.sub(r'<button class="cert-validate-btn">.*?</button>', '', content, flags=re.DOTALL)

    # 2. Update Dates
    # Since the structure is fixed, we can just replace specific strings
    # But some might be generic like 'Date: 2024'. Let's replace them carefully based on the preceding company name.
    
    if 'index.html' in file_path:
        content = content.replace('Microsoft | Date: 2024', f'Microsoft | {dates["az"]}')
        content = content.replace('HashiCorp | Date: 2024', f'HashiCorp | {dates["tf"]}')
        content = content.replace('Fortinet | Date: 2024', f'Fortinet | {dates["fca"]}')
        content = content.replace('IBM | Date: 2024', f'IBM | {dates["ibm"]}')
        content = content.replace('Snowflake | Date: 2024', f'Snowflake | {dates["sf"]}')
    elif 'index-es.html' in file_path:
        content = content.replace('Microsoft | Fecha: 2024', f'Microsoft | {dates["az"]}')
        content = content.replace('HashiCorp | Fecha: 2024', f'HashiCorp | {dates["tf"]}')
        content = content.replace('Fortinet | Fecha: 2024', f'Fortinet | {dates["fca"]}')
        content = content.replace('IBM | Fecha: 2024', f'IBM | {dates["ibm"]}')
        content = content.replace('Snowflake | Fecha: 2024', f'Snowflake | {dates["sf"]}')
    elif 'index-ar.html' in file_path:
        content = content.replace('Microsoft | التاريخ: 2024', f'Microsoft | {dates["az"]}')
        content = content.replace('HashiCorp | التاريخ: 2024', f'HashiCorp | {dates["tf"]}')
        content = content.replace('Fortinet | التاريخ: 2024', f'Fortinet | {dates["fca"]}')
        content = content.replace('IBM | التاريخ: 2024', f'IBM | {dates["ibm"]}')
        content = content.replace('Snowflake | التاريخ: 2024', f'Snowflake | {dates["sf"]}')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path}")

