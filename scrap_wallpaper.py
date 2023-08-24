# given a webpage, scrap all the wallpaper links and download them
import os
import requests
from bs4 import BeautifulSoup

# URL of the HTML page
url = "https://www.ghibli.jp/works/mononoke/"

# Create a folder to save images
output_folder = "mononoke"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Send a GET request to the URL
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all image links within the "gallery" class
    image_links = soup.select(".gallery img")
    
    # Download and save each image
    for idx, img_link in enumerate(image_links, start=1):
        img_url = img_link["src"]
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            img_filename = f"image_{idx:03d}.jpg"
            img_path = os.path.join(output_folder, img_filename)
            
            with open(img_path, "wb") as img_file:
                img_file.write(img_response.content)
                
            print(f"Downloaded {img_filename}")
        else:
            print(f"Failed to download {img_url}")
else:
    print("Failed to retrieve the HTML content.")

print("Download complete!")
