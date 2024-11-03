import os
import base64
import xml.etree.ElementTree as ET

def count_problems():
    base_dir = 'leetcode_grind'
    categories = ['easy', 'medium', 'hard']
    counts = {}
    for cat in categories:
        path = os.path.join(base_dir, cat)
        if os.path.isdir(path):
            # Count only files (exclude directories)
            counts[cat] = len([file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))])
        else:
            counts[cat] = 0
    total = sum(counts.values())
    percentages = {cat: (count / total) * 100 if total > 0 else 0 for cat, count in counts.items()}
    return counts, percentages, total

def create_svg(counts, percentages):
    svg_width = 500
    bar_height = 40
    spacing = 20
    margin = 50
    svg_height = (bar_height + spacing) * len(counts) + margin

    svg = ET.Element('svg', width=str(svg_width), height=str(svg_height), xmlns='http://www.w3.org/2000/svg')

    colors = {'easy': '#4CAF50', 'medium': '#FFC107', 'hard': '#F44336'}

    for i, (category, count) in enumerate(counts.items()):
        y = margin + i * (bar_height + spacing)
        bar_length = percentages[category] * 3  # Scale factor for visibility

        # Bar
        ET.SubElement(svg, 'rect', x='150', y=str(y), width=str(bar_length), height=str(bar_height), fill=colors[category])

        # Category label
        label = ET.SubElement(svg, 'text', x='140', y=str(y + bar_height / 2 + 5), fill='black', font_size='14', text_anchor='end')
        label.text = category.capitalize()

        # Percentage label
        pct_label = ET.SubElement(svg, 'text', x=str(150 + bar_length + 10), y=str(y + bar_height / 2 + 5), fill='black', font_size='14', text_anchor='start')
        pct_label.text = f"{percentages[category]:.1f}%"

        # Count label inside the bar
        count_label = ET.SubElement(svg, 'text', x='155', y=str(y + bar_height / 2 + 5), fill='white', font_size='14', text_anchor='start')
        count_label.text = f"{count}"

    return ET.tostring(svg, encoding='unicode')

def update_readme(svg_content, counts, percentages, total):
    svg_base64 = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
    img_tag = f'<img src="data:image/svg+xml;base64,{svg_base64}" alt="LeetCode Statistics">'

    stats_section = f"""
<!-- LEETCODE_STATS_START -->
## Statistics

- **Easy:** {counts['easy']} problems solved ({percentages['easy']:.1f}%)
- **Medium:** {counts['medium']} problems solved ({percentages['medium']:.1f}%)
- **Hard:** {counts['hard']} problems solved ({percentages['hard']:.1f}%)
- **Total:** {total} problems solved
<!-- LEETCODE_STATS_END -->
"""

    progress_section = f"""
<!-- LEETCODE_SVG_START -->
## Progress

{img_tag}
{stats_section}
<!-- LEETCODE_SVG_END -->
"""

    readme_path = 'README.md'
    with open(readme_path, 'r', encoding='utf-8') as file:
        readme_content = file.read()

    # Replace existing Progress section between markers
    if '<!-- LEETCODE_SVG_START -->' in readme_content:
        start_marker = '<!-- LEETCODE_SVG_START -->'
        end_marker = '<!-- LEETCODE_SVG_END -->'
        start_index = readme_content.index(start_marker)
        end_index = readme_content.index(end_marker) + len(end_marker)
        readme_content = readme_content[:start_index] + progress_section + readme_content[end_index:]
    else:
        # If markers not found, append the Progress section at the end
        readme_content += progress_section

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(readme_content)

def main():
    counts, percentages, total = count_problems()
    svg_content = create_svg(counts, percentages)
    update_readme(svg_content, counts, percentages, total)
    print("README.md has been updated with the latest LeetCode statistics.")

if __name__ == '__main__':
    #main()
