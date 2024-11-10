import os
import base64
import xml.etree.ElementTree as ET
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def validate_solution_file(filepath):
    """
    Validate if a file is a legitimate solution file.
    """
    valid_extensions = {'.py', '.java', '.cpp', '.js', '.go', '.ts'}
    
    # Check file extension
    _, ext = os.path.splitext(filepath)
    if ext not in valid_extensions:
        return False
    
    # Check file size (shouldn't be empty)
    if os.path.getsize(filepath) == 0:
        logging.warning(f"Empty file found: {filepath}")
        return False
    
    # Check if it's a hidden file
    if os.path.basename(filepath).startswith('.'):
        return False
    
    return True

def get_solution_files(directory):
    """
    Get all valid solution files in a directory.
    """
    solution_files = []
    if not os.path.exists(directory):
        logging.error(f"Directory does not exist: {directory}")
        return []
    
    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)
        if os.path.isfile(filepath) and validate_solution_file(filepath):
            solution_files.append(filepath)
    
    return solution_files

def count_problems():
    """
    Count problems in each difficulty category.
    """
    base_dir = 'leetcode_grind'
    categories = ['easy', 'medium', 'hard']
    counts = {}
    
    if not os.path.exists(base_dir):
        logging.error(f"Base directory '{base_dir}' does not exist!")
        return {}, {}, 0
    
    # Count valid solution files in each category
    for cat in categories:
        path = os.path.join(base_dir, cat)
        solution_files = get_solution_files(path)
        counts[cat] = len(solution_files)
        
        # Log the files found
        logging.info(f"Found {counts[cat]} valid solutions in {cat}:")
        for file in solution_files:
            logging.info(f"  - {os.path.basename(file)}")
    
    total = sum(counts.values())
    if total == 0:
        logging.warning("No valid solution files found!")
        return counts, {cat: 0 for cat in categories}, 0
    
    percentages = {cat: (count / total) * 100 for cat, count in counts.items()}
    return counts, percentages, total

def create_svg(counts, percentages):
    """
    Create SVG visualization of problem counts.
    """
    svg_width = 500
    bar_height = 40
    spacing = 20
    margin = 50
    svg_height = (bar_height + spacing) * len(counts) + margin
    
    svg = ET.Element('svg', {
        'width': str(svg_width),
        'height': str(svg_height),
        'xmlns': 'http://www.w3.org/2000/svg'
    })
    
    # Add title and description for accessibility
    title = ET.SubElement(svg, 'title')
    title.text = 'LeetCode Problem Solving Statistics'
    
    colors = {
        'easy': '#4CAF50',
        'medium': '#FFC107',
        'hard': '#F44336'
    }
    
    for i, (category, count) in enumerate(counts.items()):
        y = margin + i * (bar_height + spacing)
        bar_length = percentages[category] * 3  # Scale factor for visibility
        
        # Bar
        ET.SubElement(svg, 'rect', {
            'x': '150',
            'y': str(y),
            'width': str(bar_length),
            'height': str(bar_height),
            'fill': colors[category]
        })
        
        # Labels
        ET.SubElement(svg, 'text', {
            'x': '140',
            'y': str(y + bar_height / 2 + 5),
            'fill': 'black',
            'font-size': '14',
            'text-anchor': 'end'
        }).text = category.capitalize()
        
        ET.SubElement(svg, 'text', {
            'x': str(150 + bar_length + 10),
            'y': str(y + bar_height / 2 + 5),
            'fill': 'black',
            'font-size': '14',
            'text-anchor': 'start'
        }).text = f"{percentages[category]:.1f}%"
        
        ET.SubElement(svg, 'text', {
            'x': '155',
            'y': str(y + bar_height / 2 + 5),
            'fill': 'white',
            'font-size': '14',
            'text-anchor': 'start'
        }).text = str(count)
    
    return ET.tostring(svg, encoding='unicode')

def update_readme(svg_content, counts, percentages, total):
    """
    Update README.md with new statistics.
    """
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
    
    try:
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
        
        logging.info("README.md has been successfully updated")
        
    except Exception as e:
        logging.error(f"Error updating README.md: {str(e)}")
        raise

def main():
    try:
        logging.info("Starting LeetCode statistics update...")
        
        counts, percentages, total = count_problems()
        if total == 0:
            logging.error("No valid solutions found. Please check your directory structure.")
            return
        
        svg_content = create_svg(counts, percentages)
        update_readme(svg_content, counts, percentages, total)
        
        logging.info(f"""
Statistics update completed:
- Easy: {counts['easy']} solutions
- Medium: {counts['medium']} solutions
- Hard: {counts['hard']} solutions
- Total: {total} solutions
""")
        
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")
        raise

if __name__ == '__main__':
    main()
