import os
import xml.etree.ElementTree as ET

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
        
        # Bar
        ET.SubElement(svg, 'rect', x='100', y=str(y), width=str(percentages[category] * 2), height='40', fill=colors[category])
        
        # Category label
        text = ET.SubElement(svg, 'text', x='0', y=str(y + 25), fill='white')
        text.text = category.capitalize()
        
        # Count and percentage
        count_text = ET.SubElement(svg, 'text', x='310', y=str(y + 25), fill='white', textAnchor='end')
        count_text.text = f'{count} ({percentages[category]:.1f}%)'

    return ET.tostring(svg, encoding='unicode')

def main():
    counts, percentages = count_problems()
    svg_content = create_svg(counts, percentages)
    
    with open('leetcode_stats.svg', 'w') as f:
        f.write(svg_content)

if __name__ == '__main__':
    main()
