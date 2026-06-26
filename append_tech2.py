import re

html_to_add = """          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Kali Linux" class="tech-stack-logo needtobeinvert" src="https://cdn.simpleicons.org/kalilinux/white" />
            <span class="tooltip">Kali Linux</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Ubuntu" class="tech-stack-logo" src="https://cdn.simpleicons.org/ubuntu" />
            <span class="tooltip">Ubuntu</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Arch Linux" class="tech-stack-logo" src="https://cdn.simpleicons.org/archlinux" />
            <span class="tooltip">Arch Linux</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="BlackArch" class="tech-stack-logo needtobeinvert" src="https://cdn.simpleicons.org/archlinux/white" />
            <span class="tooltip">BlackArch</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Linux Mint" class="tech-stack-logo" src="https://cdn.simpleicons.org/linuxmint" />
            <span class="tooltip">Linux Mint</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Azure" class="tech-stack-logo" src="https://cdn.simpleicons.org/microsoftazure" />
            <span class="tooltip">Azure</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="AWS" class="tech-stack-logo needtobeinvert" src="https://cdn.simpleicons.org/amazonaws/white" />
            <span class="tooltip">AWS</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="NumPy" class="tech-stack-logo" src="https://cdn.simpleicons.org/numpy" />
            <span class="tooltip">NumPy</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Eclipse" class="tech-stack-logo" src="https://cdn.simpleicons.org/eclipseide" />
            <span class="tooltip">Eclipse</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="VS Code" class="tech-stack-logo" src="https://cdn.simpleicons.org/visualstudiocode" />
            <span class="tooltip">VS Code</span>
          </li>
"""

for f_name in ['index.html', 'index-ar.html', 'index-es.html']:
    with open(f_name, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the closing </ul> of tech-stack-wrapper
    match = re.search(r'</ul>\s*</div>\s*</div>\s*</section>', content)
    if match:
        insertion_point = match.start()
        new_content = content[:insertion_point] + html_to_add + content[insertion_point:]
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {f_name}")
    else:
        print(f"Could not find injection point in {f_name}")

