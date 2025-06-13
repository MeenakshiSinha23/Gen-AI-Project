import json

def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        print(posts)

if __name__ == "__main__":
    process_posts("C:/Users/Meenakshi Sinha/OneDrive/Desktop/Gen AI Project/data/raw_posts.json")
