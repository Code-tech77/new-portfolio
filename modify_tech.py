import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove BlackArch list item
    # We find the <li> block containing BlackArch
    blackarch_regex = r'\s*<li class="tech-stack-box"[^>]*>\s*<img alt="BlackArch"[^>]*>\s*<span class="tooltip">BlackArch</span>\s*</li>'
    content = re.sub(blackarch_regex, '', content, flags=re.DOTALL)

    # 2. Update Azure image source
    # We find the Azure img tag and replace its src
    content = re.sub(
        r'<img alt="Azure" class="tech-stack-logo([^"]*)" src="[^"]+" />',
        r'<img alt="Azure" class="tech-stack-logo" src="./png/azure.png" />',
        content
    )

    # 3. Update AWS image source
    content = re.sub(
        r'<img alt="AWS" class="tech-stack-logo([^"]*)" src="[^"]+" />',
        r'<img alt="AWS" class="tech-stack-logo" src="./png/aws.png" />',
        content
    )

    # 4. Update VS Code image source
    content = re.sub(
        r'<img alt="VS Code" class="tech-stack-logo([^"]*)" src="[^"]+" />',
        r'<img alt="VS Code" class="tech-stack-logo" src="./png/vscode.png" />',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

for f in ['index.html', 'index-ar.html', 'index-es.html']:
    process_file(f)
