import re
from bs4 import BeautifulSoup

def fix_navbar(filepath, proj_text, soft_proj_text, homelabs_text, cred_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Desktop Nav
    ul = soup.find('ul', class_='navbar-tabs-ul')
    if ul:
        # Projects
        proj_link = ul.find('a', href='#projects')
        if proj_link and proj_link.parent and 'nav-dropdown-container' not in proj_link.parent.get('class', []):
            li = proj_link.parent
            li['class'] = li.get('class', []) + ['nav-dropdown-container']
            proj_link['style'] = "cursor: default;"
            proj_link.string = f"&#60;{proj_text}&#62; ▾"
            
            # Create dropdown
            dropdown = soup.new_tag('ul', **{'class': 'nav-dropdown'})
            
            li1 = soup.new_tag('li')
            a1 = soup.new_tag('a', href='#projects')
            a1.string = soft_proj_text
            li1.append(a1)
            
            li2 = soup.new_tag('li')
            a2 = soup.new_tag('a', href='#homelabs')
            a2.string = homelabs_text
            li2.append(a2)
            
            dropdown.append(li1)
            dropdown.append(li2)
            li.append(dropdown)
            
        # Volunteer -> Credentials
        vol_link = ul.find('a', href='#Volunteer')
        if vol_link and vol_link.parent:
            vol_link['href'] = '#credentials'
            vol_link['aria-label'] = 'Credentials menu button'
            vol_link.string = f"&#60;{cred_text}&#62;"

    # Mobile Nav
    mobile_ul = soup.find('ul', id='mobile-ul')
    if mobile_ul:
        # Projects
        m_proj_link = mobile_ul.find('a', href='#projects')
        if m_proj_link and m_proj_link.parent and 'mobile-nav-dropdown-container' not in m_proj_link.parent.get('class', []):
            li = m_proj_link.parent
            li['class'] = li.get('class', []) + ['mobile-nav-dropdown-container']
            li['onclick'] = "this.classList.toggle('open')"
            m_proj_link['style'] = "cursor: pointer;"
            m_proj_link['href'] = '#'
            m_proj_link.string = f"&#60;{proj_text}&#62; ▾"
            
            # Create dropdown
            dropdown = soup.new_tag('ul', **{'class': 'mobile-nav-dropdown'})
            
            li1 = soup.new_tag('li')
            a1 = soup.new_tag('a', href='#projects', onclick='hidemenubyli()')
            a1.string = soft_proj_text
            li1.append(a1)
            
            li2 = soup.new_tag('li')
            a2 = soup.new_tag('a', href='#homelabs', onclick='hidemenubyli()')
            a2.string = homelabs_text
            li2.append(a2)
            
            dropdown.append(li1)
            dropdown.append(li2)
            li.append(dropdown)
            
        # Volunteer -> Credentials
        m_vol_link = mobile_ul.find('a', href='#Volunteer')
        if m_vol_link and m_vol_link.parent:
            m_vol_link['href'] = '#credentials'
            m_vol_link['aria-label'] = 'Credentials menu button'
            m_vol_link.string = f"&#60;{cred_text}&#62;"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup).replace('&amp;#60;', '&#60;').replace('&amp;#62;', '&#62;'))

fix_navbar('index-ar.html', 'المشاريع', 'مشاريع برمجية', 'مختبرات منزلية', 'الاعتمادات')
fix_navbar('index-es.html', 'Proyectos', 'Proyectos de Software', 'Laboratorios', 'Credenciales')
print("Navbar update complete")
