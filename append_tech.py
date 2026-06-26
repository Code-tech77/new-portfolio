import re

html_to_add = """          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Notion" class="tech-stack-logo needtobeinvert" src="https://cdn.simpleicons.org/notion/white" />
            <span class="tooltip">Notion</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Next.js" class="tech-stack-logo needtobeinvert" src="https://cdn.simpleicons.org/nextdotjs/white" />
            <span class="tooltip">Next.js</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Vercel" class="tech-stack-logo needtobeinvert" src="https://cdn.simpleicons.org/vercel/white" />
            <span class="tooltip">Vercel</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Node.js" class="tech-stack-logo" src="https://cdn.simpleicons.org/nodedotjs" />
            <span class="tooltip">Node.js</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Shell Scripting" class="tech-stack-logo needtobeinvert" src="https://cdn.simpleicons.org/gnubash/white" />
            <span class="tooltip">Shell Scripting</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Tailscale" class="tech-stack-logo needtobeinvert" src="https://cdn.simpleicons.org/tailscale/white" />
            <span class="tooltip">Tailscale</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Pi-hole" class="tech-stack-logo" src="https://cdn.simpleicons.org/pihole" />
            <span class="tooltip">Pi-hole</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="SQL" class="tech-stack-logo" src="https://cdn.simpleicons.org/mysql" />
            <span class="tooltip">SQL</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Cowrie" class="tech-stack-logo needtobeinvert" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg" />
            <span class="tooltip">Cowrie</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Firebase" class="tech-stack-logo" src="https://cdn.simpleicons.org/firebase" />
            <span class="tooltip">Firebase</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Java" class="tech-stack-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg" />
            <span class="tooltip">Java</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Hostinger" class="tech-stack-logo" src="https://cdn.simpleicons.org/hostinger" />
            <span class="tooltip">Hostinger</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="Vite" class="tech-stack-logo" src="https://cdn.simpleicons.org/vite" />
            <span class="tooltip">Vite</span>
          </li>
          <li class="tech-stack-box" data-aos="fade-up">
            <img alt="TensorFlow" class="tech-stack-logo" src="https://cdn.simpleicons.org/tensorflow" />
            <span class="tooltip">TensorFlow</span>
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

