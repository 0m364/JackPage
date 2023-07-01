import requests
import os

def copy_webpage(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Check that the HTTP status code is 200 (OK)
        content = response.content # Get bytes instead of text
        return content
    except (requests.exceptions.HTTPError, 
            requests.exceptions.ConnectionError, 
            requests.exceptions.Timeout) as err:
        print(f"Error occurred while fetching the webpage: {err}")
        return None

def save_offline_copy(content, page_name):
    try:
        os.makedirs("mod", exist_ok=True)
        with open(f"mod/{page_name}.html", "wb") as file: # Open in binary mode
            file.write(content)
        print("Offline copy saved successfully!")
    except IOError as err:
        print(f"An error occurred while saving the offline copy: {err}")

# Prompt user for the website URL
website_url = input("Please enter the URL of the webpage you want to copy: ")

# Copy the webpage
webpage_content = copy_webpage(website_url)

if webpage_content:
    # Prompt user to enter a name for the offline copy
    page_name = input("Please enter a name for the offline copy: ")

    # Save the offline copy
    save_offline_copy(webpage_content, page_name)

