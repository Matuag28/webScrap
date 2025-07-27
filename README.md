🕸️ WebScrap: Automated HTML Data Extraction
WebScrap is a Python-based project that automates data extraction from large collections of offline HTML files — perfect for scraping product data like laptops from e-commerce platforms. This tool enables you to process hundreds of saved product pages and generate clean, structured data in a single CSV file.

✨ Features
🔁 Batch Processing — Scans all HTML files in the data/ directory.

🧠 Smart Parsing — Uses BeautifulSoup for flexible HTML traversal.

📦 Clean Output — All results are saved in data.csv with structured columns.

🧩 Easily Extensible — Modular code; add or modify fields effortlessly.

⚙️ Core Workflow
📥 Input
Save your HTML product pages into the data/ folder.
Example: hundreds of laptop listings.

🚀 Run the Script
bash
Copy
Edit
python collect.py
The script will:

Read every .html file

Parse key information (title, specs, price, etc.)

Save the extracted data into data.csv

🧠 Fields Extracted
The script collects:

🏷️ Product Title

💰 Price

🧮 Specifications (RAM, Storage, CPU, etc.)

🏬 Seller / Shop Name

🌟 Ratings and Reviews

🖼️ Image URLs (if available)

💡 Want to extract more? You can easily update collect.py to include any tag or attribute.

🛠️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Matuag28/webscrap.git
cd webscrap
2. Install Dependencies
bash
Copy
Edit
pip install beautifulsoup4
3. Add HTML Files
Place your .html files inside the data/ directory.

4. Run the Extractor
bash
Copy
Edit
python collect.py
🧪 Customization
Want to scrape a different kind of page (e.g., phones, furniture, books)?


📄 License
This project is provided for educational and demonstration purposes.
Feel free to use, modify, and share it with attribution.
