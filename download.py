import requests
from bs4 import BeautifulSoup

def extract_image_url(pinterest_url):
    try:
        response = requests.get(pinterest_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        image_tags = soup.find_all('img', class_=['h-image-fit', 'h-unsplash-img'])
        print(f"image tag {image_tags}")
        if not image_tags:
            image_tags = soup.find_all('img', attrs={'src': lambda src: src and src.startswith('https://i.pinimg.com/')})
        if image_tags:
            return image_tags[0]['src']

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from URL: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

def download_image(image_url, filename):
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(52000):
                f.write(chunk)
        print(f"Image downloaded and saved as: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    print("I can only download photos.")
    pinterest_url = input("Enter the Pinterest pin URL: ")
    image_url = extract_image_url(pinterest_url)
    print(f"Image url {image_url}")
    if image_url:
        filename = image_url.split('/')[-1]
        download_image(image_url , filename)
    else:
        print("Image URL not found. Consider respecting Pinterest's terms of service.")
    zeros = input("Do you wanna to download another photo(YES/NO): ")
    zeros=zeros.lower()
    if zeros=="yes":
        while True:
            pinterest_url = input("Enter the Pinterest pin URL: ")
            image_url = extract_image_url(pinterest_url)
            print(f"Image url {image_url}")
            if image_url:
                filename = image_url.split('/')[-1]
                download_image(image_url , filename)
                ones = input("Do you wanna to download another photo(YES/NO): ")
                ones=ones.lower()
                if ones=="no":
                    break
                elif ones!=("yes"or"no"):
                    print("Send Yes or No only.")           
            else:
                print("Image URL not found. Consider respecting Pinterest's terms of service.")
    elif zeros=="no":
        print("Ok bye")
    else:
        print("Send Yes or No only")
            
            
