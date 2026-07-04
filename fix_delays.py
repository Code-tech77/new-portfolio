import re

files = [
    '/Users/mohammedzuoriki/Desktop/PROJECTS/new-portfolio/index.html',
    '/Users/mohammedzuoriki/Desktop/PROJECTS/new-portfolio/index-es.html',
    '/Users/mohammedzuoriki/Desktop/PROJECTS/new-portfolio/index-ar.html'
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = '<div class="cert-track cert-track-left">'
    start_idx = content.find(start_str)
    if start_idx == -1: continue
    start_idx += len(start_str)
    
    end_str = '        </div>\n      </div>'
    end_idx = content.find(end_str, start_idx)
    
    track_content = content[start_idx:end_idx]
    
    # We want to replace data-aos="fade-up" data-aos-delay="..." or just data-aos="fade-up"
    # with the correct delays based on their 0-indexed position
    
    cards = track_content.split('<div class="cert-card"')
    
    new_track = cards[0] # Usually just whitespace
    
    delays = [0, 150, 300]
    
    for i in range(1, len(cards)):
        card_content = cards[i]
        delay = delays[(i-1) % 3]
        
        # Remove any existing data-aos attributes
        card_content = re.sub(r'\s*data-aos="[^"]*"', '', card_content)
        card_content = re.sub(r'\s*data-aos-delay="[^"]*"', '', card_content)
        
        # Re-add them cleanly
        if delay == 0:
            new_track += f'<div class="cert-card" data-aos="fade-up"{card_content}'
        else:
            new_track += f'<div class="cert-card" data-aos="fade-up" data-aos-delay="{delay}"{card_content}'
            
    new_content = content[:start_idx] + new_track + content[end_idx:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Fixed delays in {file_path}")

