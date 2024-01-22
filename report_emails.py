#!/usr/bin/env python3

import os
import datetime
from reports import generate_report

# Set the path to the descriptions directory
descriptions_directory = 'supplier-data/descriptions'

# Function to process text data from description files
def process_description_files(directory):
    report_paragraph = ""
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                # Read data from the file and format it
                name = file.readline().strip()
                weight = file.readline().strip()
                report_paragraph += f'name: {name}\nweight: {weight}\n\n'
    return report_paragraph

# Main method
if __name__ == "__main__":
    # Process text data from description files
    paragraph = process_description_files(descriptions_directory)

    # Set the report title
    title = f"Processed Update on {datetime.date.today()}"

    # Set the file path for the PDF report
    attachment = '/tmp/processed.pdf'

    # Generate the report using the reports module
    generate_report(attachment, title, paragraph)
