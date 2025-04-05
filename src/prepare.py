import os
import csv
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import sys


def fix_xml_format(input_path: str, fixed_path: str):
    """Wrap raw XML rows in a single root tag to make it valid XML"""
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Wrap all content with a root
    wrapped = f"<root>\n{content}\n</root>"

    with open(fixed_path, "w", encoding="utf-8") as f:
        f.write(wrapped)

    print(f"✅ Fixed XML saved to {fixed_path}")


def parse_rows(xml_path: str, csv_path: str):
    """Parse fixed XML to CSV"""
    tree = ET.parse(xml_path)
    root = tree.getroot()

    rows = []
    for row in root.findall("row"):
        row_data = row.attrib

        # Clean up HTML tags from Body field (if exists)
        if "Body" in row_data:
            soup = BeautifulSoup(row_data["Body"], "html.parser")
            row_data["Body"] = soup.get_text()

        rows.append(row_data)

    # Write to CSV
    fieldnames = sorted(set().union(*(row.keys() for row in rows)))
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Parsed CSV saved to {csv_path}")


if __name__ == "__main__":
    # Get path from argument: <input_xml> <output_csv>
    input_path = sys.argv[1]
    output_csv = sys.argv[2]

    # Prepare path for fixed XML (stored in same place as input)
    fixed_path = os.path.join(os.path.dirname(input_path), "fixed_data.xml")

    fix_xml_format(input_path, fixed_path)
    parse_rows(fixed_path, output_csv)

