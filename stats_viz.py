import os
import xml.etree.ElementTree as ET

def count_problems():
    categories = ['easy', 'medium', 'hard']
    counts = {}
    
    # Debug print
    print("Current working directory:", os.getcwd())
    for cat in categories:
        path = f"./{cat}"
        if not os.path.exists(path):
            print(f"Warning: Directory {path} does not exist!")
            counts[cat] = 0
        else:
            try:
                counts[cat] = len([file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))])
                print(f"Found {counts[cat]} files in {path}")
            except Exception as e:
                print(f"Error reading directory {path}: {str(e)}")
                counts[cat] = 0
            
    total = sum(counts.values())
    print(f"Total problems found: {total}")
    
    # Avoid division by zero
    percentages = {cat: (count / total) * 100 if total > 0 else 0 for cat, count in counts.items()}
    return counts, percentages, total

def create_svg(counts, percentages):
    svg_width = 500
    bar_height = 40
    spacing = 20
    margin = 50
    svg_height = (bar_height + spacing) * len(counts) + margin * 2
    
    # Create SVG element
    svg = ET.Element('svg', {
        'width': str(svg_width),
        'height': str(svg_height),
        'xmlns': 'http://www.w3.org/2000/svg',
        'viewBox': f'0 0 {svg_width} {svg_height}'
    })
    
    # Add title
    title = ET.SubElement(svg, 'text', {
        'x': str(svg_width // 2),
        'y': str(margin // 2),
        'text-anchor': 'middle',
        'font-size': '18',
        'font-weight': 'bold'
    })
    title.text = 'LeetCode Progress'
    
    colors = {'easy': '#4CAF50', 'medium': '#FFC107', 'hard': '#F44336'}
    
    for i, (category, count) in enumerate(counts.items()):
        y = margin + i * (bar_height + spacing)
        # Scale the bar length based on percentage (max width = 300px)
        bar_length = min(300, percentages[category] * 3)
        
        # Background bar (grey)
        ET.SubElement(svg, 'rect', {
            'x': '150',
            'y': str(y),
            'width': '300',
            'height': str(bar_height),
            'fill': '#f0f0f0'
        })
        
        # Progress bar
        ET.SubElement(svg, 'rect', {
            'x': '150',
            'y': str(y),
            'width': str(bar_length),
            'height': str(bar_height),
            'fill': colors[category]
        })
        
        # Category label
        label = ET.SubElement(svg, 'text', {
            'x': '140',
            'y': str(y + bar_height // 2 + 5),
            'fill': 'black',
            'font-size': '14',
            'text-anchor': 'end'
        })
        label.text = category.capitalize()
        
        # Percentage and count label
        count_label = ET.SubElement(svg, 'text', {
            'x': '460',
            'y': str(y + bar_height // 2 + 5),
            'fill': 'black',
            'font-size': '14',
            'text-anchor': 'end'
        })
        count_label.text = f"{count} ({percentages[category]:.1f}%)"
    
    try:
        return ET.tostring(svg, encoding='unicode')
    except Exception as e:
        print(f"Error generating SVG: {str(e)}")
        return None

def main():
    try:
        print("Starting LeetCode statistics update...")
        counts, percentages, total = count_problems()
        svg_content = create_svg(counts, percentages)
        if svg_content:
            with open('leetcode_stats.svg', 'w', encoding='utf-8') as f:
                f.write(svg_content)
            print("SVG image saved as leetcode_stats.svg")
        else:
            print("Failed to generate SVG content")
        print("Process completed successfully")
    except Exception as e:
        print(f"Error in main process: {str(e)}")

if __name__ == '__main__':
    main()
