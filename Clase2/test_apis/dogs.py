import requests
import random

def get_random_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["status"] == "success":
            return data["message"]
        else:
            print("Failed to fetch dog image.")
            return None
    except requests.RequestException as e:
        print(f"Error fetching dog image: {e}")
        return None

def main():
    print("🔹 Dog CEO API Test 🔹\n")
    image_url = get_random_dog_image()
    if image_url:
        print(f"🐶 Random Dog Image: {image_url}\n")

if __name__ == "__main__":
    main()
