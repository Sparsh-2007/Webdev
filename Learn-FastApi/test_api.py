# Simple endpoint test script for FastAPI
import urllib.request
import json

BASE_URL = "http://127.0.0.1:8000"

def test_endpoints():
    print("Testing GET /posts ...")
    try:
        with urllib.request.urlopen(f"{BASE_URL}/posts") as response:
            data = json.loads(response.read().decode())
            print(f"Status: {response.status}, Received {len(data)} posts")
    except Exception as e:
        print(f"Server might not be running: {e}")

    print("Testing GET /posts/1 ...")
    try:
        with urllib.request.urlopen(f"{BASE_URL}/posts/1") as response:
            post = json.loads(response.read().decode())
            print(f"Found post: {post['title']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Run `uv run uvicorn main:app --reload` first before testing.")
    test_endpoints()
