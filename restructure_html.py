import bs4
from bs4 import BeautifulSoup

def process_file(filepath):
    print(f"Processing {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Fix IDs
    sections = soup.find_all('section', {'class': 'projects-section-container'})
    if len(sections) >= 3:
        # Software Projects
        if sections[1].get('id') == 'projects':
            pass
        # Networking & Sec Projects -> Homelabs
        if sections[2].get('id') == 'projects':
            sections[2]['id'] = 'homelabs'
            h2 = sections[2].find('h2')
            if h2:
                # Update text to homelabs if english
                if 'Networking' in h2.text:
                    h2.string = '&#60;/ Homelabs&#62;'
    
    # Certifications -> Credentials
    cert_section = soup.find(id='certifications')
    if cert_section:
        cert_section['id'] = 'credentials'
        h2 = cert_section.find('h2')
        if h2 and 'Certifications' in h2.text:
            h2.string = '&#60;/Credentials&#62;'
            
    # 2. Merge Cert Sliders and Duplicate cards
    sliders = soup.find_all('div', {'class': 'cert-slider'})
    if len(sliders) >= 2:
        first_slider = sliders[0]
        first_track = first_slider.find('div', {'class': 'cert-track'})
        
        all_cards = []
        for slider in sliders:
            track = slider.find('div', {'class': 'cert-track'})
            if track:
                all_cards.extend(track.find_all('div', {'class': 'cert-card'}))
        
        # Clear first track and append all cards TWICE for infinite loop
        if first_track:
            first_track.clear()
            for card in all_cards:
                # Deep copy card
                first_track.append(card.__copy__())
            for card in all_cards:
                # Append a second time
                first_track.append(card.__copy__())
                
        # Remove subsequent sliders
        for slider in sliders[1:]:
            slider.decompose()
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup).replace('&amp;#60;', '&#60;').replace('&amp;#62;', '&#62;'))

for path in ['index.html', 'index-ar.html', 'index-es.html']:
    process_file(path)
print("Restructure complete")
