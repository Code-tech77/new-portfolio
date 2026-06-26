import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the cert-slider div and its inner cert-track
    slider_match = re.search(r'(<div aria-label="Certificates carousel" class="cert-slider">\s*)<div class="cert-track">(.*?)</div>\s*</div>', content, re.DOTALL)
    
    if not slider_match:
        print(f"Could not find cert-slider in {filepath}")
        return

    prefix = slider_match.group(1)
    track_content = slider_match.group(2)
    
    # We will split the track_content by '<div class="cert-card"'
    # But actually, the user said "each row have 6 credentials".
    # Currently there are 12 cert-cards in the track (which is 6 items duplicated, or 4 items duplicated 3 times).
    # Let's count them:
    cards = re.findall(r'<div class="cert-card".*?</button>\s*</div>', track_content, re.DOTALL)
    print(f"{filepath} has {len(cards)} cards")
    
    # Let's take the first 6 cards for row 1 (and duplicate them to make 12 for infinite scroll)
    # Wait, the prompt says "each row have 6 credentials ... 2 rows".
    # If we have 12 cards currently, maybe they meant 6 distinct ones?
    # I'll just put 12 cards in the first row (6 distinct + 6 duplicates) and 12 cards in the second row (same or different order).
    # Let's use the first 6 cards (which might be 4 distinct + 2 repeat) as the items for row 1.
    # And maybe shuffle or reverse for row 2 to make it look different.
    
    if len(cards) < 12:
        # Just duplicate the cards so we have 12
        while len(cards) < 12:
            cards.extend(cards)
    
    cards = cards[:12] # Ensure exactly 12
    
    # Row 1: 6 cards duplicated
    row1_cards = cards[:6] + cards[:6]
    # Row 2: 6 cards duplicated (let's reverse the 6 cards so it looks different)
    row2_base = cards[:6][::-1]
    row2_cards = row2_base + row2_base
    
    row1_html = '\n'.join(row1_cards)
    row2_html = '\n'.join(row2_cards)
    
    new_slider_html = f'{prefix}<div class="cert-track cert-track-left">\n{row1_html}\n</div>\n<div class="cert-track cert-track-right" style="margin-top: 30px;">\n{row2_html}\n</div>\n      </div>'
    
    new_content = content.replace(slider_match.group(0), new_slider_html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}")

for f in ['index.html', 'index-ar.html', 'index-es.html']:
    process_file(f)
