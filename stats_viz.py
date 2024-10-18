import os
import xml.etree.ElementTree as ET
import base64

def count_problems():
    categories = ['easy', 'medium', 'hard']
    counts = {cat: len(os.listdir(cat)) for cat in categories if os.path.isdir(cat)}
    total = sum(counts.values())
    percentages = {cat: (count / total) * 100 for cat, count in counts.items()}
    return counts, percentages

def create_svg(counts, percentages):
    svg = ET.Element('svg', width='400', height='200', xmlns='http://www.w3.org/2000/svg')
    
    colors = {'easy': '#00ff00', 'medium': '#ffff00', 'hard': '#ff0000'}
    
    for i, (category, count) in enumerate(counts.items()):
        y = i * 60 + 20
        ET.SubElement(svg, 'rect', x='100', y=str(y), width=str(percentages[category] * 2), height='40', fill=colors[category])
        text = ET.SubElement(svg, 'text', x='0', y=str(y + 25), fill='white')
        text.text = category.capitalize()
        
        count_text = ET.SubElement(svg, 'text', x='310', y=str(y + 25), fill='white', textAnchor='end')
        count_text.text = f'{count} ({percentages[category]:.1f}%)'

    return ET.tostring(svg, encoding='unicode')

def update_readme(svg_content):
    with open('README.md', 'r') as file:
        readme_content = file.read()

    svg_base64 = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
    img_tag = f'<img src="data:image/svg+xml;base64,{svg_base64}" alt="LeetCode Statistics">'
    
    if '![LeetCode Statistics]' in readme_content:
        readme_content = readme_content.replace('![LeetCode Statistics]', img_tag)
    elif '<img src="data:image/svg+xml;base64,' in readme_content:
        start = readme_content.index('<img src="data:image/svg+xml;base64,')
        end = readme_content.index('>', start) + 1
        readme_content = readme_content[:start] + img_tag + readme_content[end:]
    else:
        readme_content = readme_content.replace('## Progress', f'## Progress\n\n{img_tag}')
    
    with open('README.md', 'w') as file:
        file.write(readme_content)

def main():
    counts, percentages = count_problems()
    svg_content = create_svg(counts, percentages)
    update_readme(svg_content)

if __name__ == '__main__':
    main()
