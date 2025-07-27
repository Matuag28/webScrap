from bs4 import BeautifulSoup
import os
import pandas as pd


d = {'title': [], 'price': [], 'link': []}

for file in os.listdir("data"):
    try:

        with open(f'data/{file}') as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        t = soup.find("h2")
        title = t.get_text() if t else None

        # Find the link - look for anchor tag that contains the h2 or is nearby
        link = None
        if t:
            # First try to find anchor within h2
            l = t.find("a")
            if l and l.has_attr('href'):
                link = l['href']
            else:
                # If not found in h2, look for anchor in parent that contains h2
                parent = t.parent
                if parent:
                    l = parent.find("a")
                    if l and l.has_attr('href'):
                        link = l['href']
                    else:
                        # Look for any anchor tag with a proper product link
                        all_links = soup.find_all("a", href=True)
                        for anchor in all_links:
                            href = anchor.get('href')
                            if href and '/dp/' in href:  # Product links contain /dp/
                                link = href
                                break
        
        # Add https://amazon.in/ prefix to the link if it exists and doesn't already have it
        if link:
            if not link.startswith('http'):
                link = "https://amazon.com" + link

        p = soup.find("span", attrs={"class": 'a-price-whole'})
        price = p.get_text().strip() if p else None

        # Show the extracted data
        print(f"File: {file}")
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Price: {price}")
        print("-" * 50)
        
        # Add to dictionary if we have valid data
        if title and link and price:
            d['title'].append(title)
            d['price'].append(price)
            d['link'].append(link)

        
    except Exception as e:
        print(e)


# Create DataFrame and save to CSV
if d['title']:  # Only create DataFrame if we have data
    df = pd.DataFrame(data=d)
    df.to_csv("data.csv", index=False)
    print(f"\nSuccessfully saved {len(df)} records to data.csv")
else:
    print("No data was collected successfully")