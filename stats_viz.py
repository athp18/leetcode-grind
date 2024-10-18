import os
import base64
import xml.etree.ElementTree as ET

def count_problems():
    categories = ['easy', 'medium', 'hard']
    counts = {cat: len(os.listdir(cat)) for cat in categories if os.path.isdir(cat)}
    total = sum(counts.values())
    percentages = {cat: (count / total) * 100 for cat, count in counts.items()}
    return counts, percentages, total

def create_svg(counts, percentages):
    svg = ET.Element('svg', width='400', height='200', xmlns='http://www.w3.org/2000/svg')
    
    colors = {'easy': '#00ff00', 'medium': '#ffff00', 'hard': '#ff0000'}
    
    for i, (category, count) in enumerate(counts.items()):
        y = i * 60 + 20
        
        # Bar
        ET.SubElement(svg, 'rect', x='100', y=str(y), width=str(percentages[category] * 2), height='40', fill=colors[category])
        
        # Category label
        text = ET.SubElement(svg, 'text', x='0', y=str(y + 25), fill='white')
        text.text = category.capitalize()
        
        # Count and percentage
        count_text = ET.SubElement(svg, 'text', x='310', y=str(y + 25), fill='white', textAnchor='end')
        count_text.text = f'{count} ({percentages[category]:.1f}%)'

    return ET.tostring(svg, encoding='unicode')

def update_readme(svg_content, counts, percentages, total):
    svg_base64 = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
    
    with open('README.md', 'r') as file:
        readme_content = file.read()
    
    img_tag = f'<img src="data:image/svg+xml;base64,{svg_base64}" alt="LeetCode Statistics">'
    
    stats_section = f"""
## Statistics

- Easy: {counts['easy']} problems solved ({percentages['easy']:.1f}%)
- Medium: {counts['medium']} problems solved ({percentages['medium']:.1f}%)
- Hard: {counts['hard']} problems solved ({percentages['hard']:.1f}%)
- Total: {total} problems solved
"""
    
    # Replace existing content or add new content
    if '## Progress' in readme_content:
        start = readme_content.index('## Progress')
        end = readme_content.index('##', start + 1) if '##' in readme_content[start + 1:] else len(readme_content)
        new_content = f"## Progress\n\n{img_tag}\n{stats_section}"
        readme_content = readme_content[:start] + new_content + readme_content[end:]
    else:
        readme_content += f"\n## Progress\n\n{img_tag}\n{stats_section}"
    
    with open('README.md', 'w') as file:
        file.write(readme_content)

def main():
    counts, percentages, total = count_problems()
    svg_content = create_svg(counts, percentages)
    update_readme(svg_content, counts, percentages, total)
    #print("README.md has been updated with the latest LeetCode statistics.")

if __name__ == '__main__':
    main()
