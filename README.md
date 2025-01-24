# Naturalization Residence Map Generator

This repository contains the Python script, data files, and SVG map used to generate the original "[File:Naturalization Residence Requirements by Country (Years of Residence).svg](https://commons.wikimedia.org/wiki/File:Naturalization_Residence_Requirements_by_Country_(Years_of_Residence).svg)" image on Wikimedia Commons.

## Description
This project uses a Python script to color an SVG world map based on the naturalization residence requirements for different countries. The map visually represents the years of residency needed for foreigners to apply for naturalization, using a color gradient from blue (low years) to red (high years), and black for countries where naturalization is not allowed.

## Data Sources

The data for naturalization residence requirements is sourced from:

*   [Wikipedia: Naturalization - Summary by country](https://en.wikipedia.org/w/index.php?title=Naturalization&oldid=1246939510#Summary_by_country) (as of 21/09/2024). The content from Wikipedia is available under the [Creative Commons Attribution-ShareAlike 4.0 License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License).  Attribution is given to Wikipedia contributors.

The blank world map used:

*   [Wikimedia Commons: BlankMap-World.svg](https://commons.wikimedia.org/wiki/File:BlankMap-World.svg) (as of 14/08/2021). This file is in the **Public Domain** and is free to use without restrictions.

## How to Use

1.  **Download or clone the repository:**
    *   **Download (if you don't use Git):**  Download the ZIP file of the repository from GitHub and extract it to your computer.
    *   **Clone (using Git):**
        ```bash
        git clone https://github.com/jnton/naturalization-residence-map-generator.git
        cd naturalization-residence-map-generator
        ```

2.  **Ensure you have Python 3 installed.**

3.  **Make sure all files (`Naturalization.py`, `BlankMap-World.svg`, `country_iso_codes.csv`, `country_years.csv`) are in the same directory.** (As they are in the repository by default)

4.  **Run the Python script from the same directory using Python 3:**
    ```bash
    python3 Naturalization.py
    ```

5.  **The generated colored SVG map will be saved as `Naturalization Residence Requirements by Country (Years of Residence).svg` in the same directory.**
