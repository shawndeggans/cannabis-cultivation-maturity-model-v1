import os
import re

def add_front_matter(md_file):
    with open(md_file, 'r+', encoding='utf-8') as file:
        content = file.read()
        title_search = re.search(r'^#{1,6}\s*(.+)', content, re.MULTILINE)
        title = title_search.group(1) if title_search else "No Title"

        # Remove any leading empty lines before the title
        content = re.sub(r'^\s*\n(#{1,6}\s*.+)', r'\1', content, flags=re.MULTILINE)

        # Construct the front matter
        front_matter = f'---\nlayout: default\ntitle: "{title}"\n---\n\n'
        
        # Convert .md links to Jekyll link tags
        content = re.sub(r'\]\((.*).md\)', r']({{ site.baseurl }}{% link \1.md %})', content)

        file.seek(0)
        file.write(front_matter + content)
        file.truncate()

def main():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                add_front_matter(os.path.join(root, file))

if __name__ == "__main__":
    main()
