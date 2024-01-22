#! /usr/bin/env python3

import os
import requests

# Set the path to the feedback directory
feedback_directory = '/data/feedback'

# Function to list all .txt files in the specified directory
def list_feedback_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.txt')]

# Function to read content from a feedback file and create a dictionary
def read_feedback_file(file_path):
    feedback_dict = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        feedback_dict['title'] = lines[0].strip()
        feedback_dict['name'] = lines[1].strip()
        feedback_dict['date'] = lines[2].strip()
        feedback_dict['feedback'] = lines[3].strip()
    return feedback_dict

# Function to post feedback dictionary to the company's website
def post_feedback(feedback_dict, external_ip):
    url = f'http://{external_ip}/feedback'
    response = requests.post(url, json=feedback_dict)
    return response

# Main script
if __name__ == "__main__":
    # List all .txt files in the feedback directory
    feedback_files = list_feedback_files(feedback_directory)

    # Traverse over each feedback file
    for file_name in feedback_files:
        file_path = os.path.join(feedback_directory, file_name)

        # Read content from the feedback file and create a dictionary
        feedback_dict = read_feedback_file(file_path)

        # Replace <corpweb-external-IP> with the actual external IP address
        corpweb_external_ip = 'your_corpweb_external_ip'

        # Post the feedback dictionary to the company's website
        response = post_feedback(feedback_dict, corpweb_external_ip)

        # Check the response status_code and text
        print(f"File: {file_name}, Status Code: {response.status_code}, Response Text: {response.text}")
