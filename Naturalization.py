import csv
import os
import xml.etree.ElementTree as ET

# Define the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Paths to the CSV files and SVG file
country_years_path = os.path.join(script_dir, 'country_years.csv')
country_iso_path = os.path.join(script_dir, 'country_iso_codes.csv')
svg_filename = 'BlankMap-World.svg'  # Change if your SVG has a different name
svg_path = os.path.join(script_dir, svg_filename)

# Verify that the CSV files exist
if not os.path.isfile(country_years_path):
    raise FileNotFoundError(f"'{country_years_path}' does not exist. Please ensure 'country_years.csv' is in the script directory.")

if not os.path.isfile(country_iso_path):
    raise FileNotFoundError(f"'{country_iso_path}' does not exist. Please ensure 'country_iso_codes.csv' is in the script directory.")

# Load the country_years.csv data
country_data = {}
with open(country_years_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        country = row['Country'].strip()
        years = row['Residence Requirement'].strip()
        if years.upper() == 'N/A':
            country_data[country] = 'N/A'
            continue
        try:
            # Handle possible fractional years like '2.5 years'
            years_num = float(years.split()[0])
            country_data[country] = years_num
        except ValueError:
            print(f"Warning: Invalid number of years for {country}: '{years}'. Skipping this country.")
            continue

# Load the country_iso_codes.csv data
country_iso = {}
with open(country_iso_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        country = row['Country'].strip()
        iso_code = row['ISO_Code'].strip().lower()
        country_iso[country] = iso_code

# Define the list of countries to be colored black
black_countries_iso = ['cn', 'kp', 'mm', 'pw', 'va']  # China, North Korea, Myanmar, Palau, Vatican City

# Define color mapping for each specific year as per the final legend
year_color_map = {
    # Under 5 Years
    2: '#0033CC',      # 2 years: Deep Blue
    2.5: '#0059FF',    # 2.5 years: Bright Blue
    3: '#3399FF',      # 3 years: Standard Blue
    4: '#66B2FF',      # 4 years: Light Blue
    5: '#99CCFF',      # 5 years: Pale Blue


    # 7-10 Years
    7: '#FFF87A',      # 7 years: Light Yellow
    8: '#FFEB66',      # 8 years: Golden Yellow
    9: '#FFD000',      # 9 years: Bright Yellow

    # 10-19 Years
    10: '#FFAA00',     # 10 years: Bright Orange
    12: '#F08000',     # 12 years: Orange
    14: '#F06000',     # 14 years: Dark Orange
    15: '#FF4400',     # 15 years: Orange Red

    # 20+ Years
    20: '#CC0000',     # 20 years: Dark Red
    25: '#990000',     # 25 years: Very Dark Red
    30: '#660000',     # 30 years: Deep Red
    35: '#330000',     # 35 years: Darkest Red
}

# Function to get color based on year
def get_color(year):
    if year == 'N/A':
        return '#000000'  # Black for no naturalization allowed
    # Handle exact match for specific years
    color = year_color_map.get(year)
    if color:
        return color
    else:
        # If year is not in the map, determine the closest category
        if year < 5:
            # Assign to the closest lower or upper shade
            if year < 2.5:
                return '#0033CC'
            elif 2.5 < year < 3:
                return '#0059FF'
            elif 3 < year < 4:
                return '#3399FF'
            else:
                return '#66B2FF'
        elif 5 <= year <= 9:
            if year < 7:
                return '#99CCFF'
            elif year < 8:
                return '#FFF87A'
            elif year < 9:
                return '#FFEB66'
            else:
                return '#FFD000'
        elif 10 <= year <= 19:
            if year < 12:
                return '#FFAA00'
            elif year < 14:
                return '#F08000'
            elif year < 15:
                return '#F06000'
            else:
                return '#FF4400'
        elif year >= 20:
            if year < 25:
                return '#CC0000'
            elif year < 30:
                return '#990000'
            elif year < 35:
                return '#660000'
            else:
                return '#330000'
        else:
            return '#c0c0c0ff'  # Default color for undefined cases

# Generate CSS styles for each country
css_styles = ""
for country, years in country_data.items():
    iso_code = country_iso.get(country)
    if not iso_code:
        print(f"Warning: ISO code not found for {country}. Skipping color assignment.")
        continue
    if iso_code in black_countries_iso:
        color = '#000000'  # Black for special cases
    else:
        color = get_color(years)
    css_styles += f'.{iso_code} {{ fill: {color}; }}\n'

# Load the SVG file
if not os.path.isfile(svg_path):
    raise FileNotFoundError(f"SVG file '{svg_path}' does not exist. Please ensure your SVG map is named correctly and located in the script directory.")

tree = ET.parse(svg_path)
root = tree.getroot()

# Namespace handling (SVG uses namespaces)
namespaces = {'svg': 'http://www.w3.org/2000/svg'}

# Find or create the <style> tag
style_tag = root.find('svg:style', namespaces)
if style_tag is None:
    style_tag = ET.SubElement(root, '{http://www.w3.org/2000/svg}style', attrib={'type': 'text/css'})
    style_tag.text = "\n"

# Append the generated CSS styles
style_tag.text += "\n/* Naturalization Residence Requirements */\n" + css_styles

# Save the updated SVG
output_svg_path = os.path.join(script_dir, 'world_map_colored.svg')
tree.write(output_svg_path)

print(f"Successfully generated '{output_svg_path}'.")
