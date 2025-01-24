# Naturalization Residence Map Generator

This repository contains the Python script, data files, and SVG map used to generate the "[File:Naturalization Residence Requirements by Country (Years of Residence).svg](https://commons.wikimedia.org/wiki/File:Naturalization_Residence_Requirements_by_Country_(Years_of_Residence).svg)" image on Wikimedia Commons.

## Description
This project uses a Python script to color an SVG world map based on the naturalization residence requirements for different countries. The map visually represents the years of residency needed for foreigners to apply for naturalization, using a color gradient from blue (low years) to red (high years), and black for countries where naturalization is not allowed.

## Data Sources

The data for naturalization residence requirements is sourced from:

*   [Wikipedia: Naturalization - Summary by country](https://en.wikipedia.org/w/index.php?title=Naturalization&oldid=1246939510#Summary_by_country) (as of 21/09/2024)

The blank world map used:

*   [Wikimedia Commons: BlankMap-World.svg](https://commons.wikimedia.org/wiki/File:BlankMap-World.svg) (Public Domain)

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/jnton/naturalization-residence-map-generator/
    cd naturalization-map-generator
    ```
2.  **Ensure you have Python installed.**
3.  **Place the CSV data files (`country_years.csv`, `country_iso_codes.csv`) in the `data/` folder and the SVG map (`BlankMap-World.svg`) in the `svg/` folder.**
4.  **Run the Python script from the project root directory:**
    ```bash
    python code/Naturalization.py
    ```
5.  **The generated colored SVG map will be saved as `world_map_colored.svg` in the project root directory.**
