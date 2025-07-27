WebScrap: Automated HTML Data Extraction
Overview
This project automates the extraction of product information from a large collection of offline HTML files. It's designed to parse hundreds of saved product pages (such as laptops from an e-commerce site), extracting relevant details and compiling them into a single CSV dataset for easy analysis or further processing.

Features
Batch Processing: Works with entire directories of HTML files.

Flexible Parsing: Uses Python and BeautifulSoup for robust extraction, accommodating minor page structure variations.

Clean Output: Consolidates results into a single CSV (data.csv) with clearly labeled columns.

Extensible: Code is modular—easy to adapt for other types of listings or additional fields.

Core Workflow
Input Data:

Place your HTML files in the data/ directory. The sample repository includes hundreds of HTML product pages.

Run the Script:

The primary script (collect.py) loads all HTML files, parses each for features like title, price, specifications, etc., and appends results to a CSV.

Output:

You’ll get a dataset file (data.csv) where each row contains the relevant information for one product.

Field Extraction
The script extracts fields such as:

Product title

Price

Technical specs (RAM, storage, CPU, etc.)

Seller or shop name

Ratings and reviews

Image links (if present)

And any other attributes present in the HTML structure

You can easily edit the script to add or remove fields as needed.

How to Use
Install dependencies

bash
pip install beautifulsoup4
Put HTML files into the data/ folder.

Run the main script:

bash
python collect.py
Find your results in data.csv




Customization
To adapt to a new type of page (e.g., not laptops or with different HTML), edit the parsing sections in collect.py or use the helper scripts for experiments.

License
This project is for educational and demonstration purposes.

Feel free to adjust sections based on your specific extraction fields, description, or audience.
