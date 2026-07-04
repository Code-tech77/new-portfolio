import re

files = [
    '/Users/mohammedzuoriki/Desktop/PROJECTS/new-portfolio/index.html',
    '/Users/mohammedzuoriki/Desktop/PROJECTS/new-portfolio/index-es.html',
    '/Users/mohammedzuoriki/Desktop/PROJECTS/new-portfolio/index-ar.html'
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the cert-track block
    start_str = '<div class="cert-track cert-track-left">'
    start_idx = content.find(start_str)
    
    if start_idx == -1:
        continue
        
    start_idx += len(start_str)
    
    # We need to find the end of the cert-track block.
    # It ends with '</div>' before '</div>' of cert-slider
    end_str = '        </div>\n      </div>'
    end_idx = content.find(end_str, start_idx)
    
    track_content = content[start_idx:end_idx]
    
    # Find all cert-cards
    card_starts = [m.start() for m in re.finditer(r'<div class="cert-card"', track_content)]
    
    if len(card_starts) > 9:
        # Keep only up to the 9th card
        ninth_start = card_starts[8]
        tenth_start = card_starts[9]
        
        # The content to keep is from start to the beginning of the 10th card
        kept_content = track_content[:tenth_start]
        
        new_content = content[:start_idx] + kept_content + '\n' + content[end_idx:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned {file_path}")
    else:
        print(f"Already {len(card_starts)} cards in {file_path}")

