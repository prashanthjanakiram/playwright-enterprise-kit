"""Smart HTML table parser - converts tables to JSON for easy assertions."""

from bs4 import BeautifulSoup
import pandas as pd

class SmartGridParser:
    def __init__(self, page, selector):
        self.page = page
        self.selector = selector
        self.table_content = None
    
    def to_json(self):
        """Extract table as list of dictionaries."""
        # Get table HTML
        table_html = self.page.locator(self.selector).inner_html()
        soup = BeautifulSoup(table_html, 'html.parser')
        table = soup.find('table')
        
        if not table:
            return []
        
        # Extract headers
        headers = [th.get_text(strip=True) for th in table.find('thead').find_all('th')]
        
        # Extract rows
        rows = []
        for tr in table.find('tbody').find_all('tr'):
            cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
            if len(cells) == len(headers):
                row_dict = dict(zip(headers, cells))
                rows.append(row_dict)
        
        return rows
    
    def find_row_by_text(self, column, value):
        """Find specific row by column value."""
        data = self.to_json()
        return next((row for row in data if row.get(column) == value), None)