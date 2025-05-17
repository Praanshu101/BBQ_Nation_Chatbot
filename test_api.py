import requests

BASE_URL = "http://127.0.0.1:8000"

def test_endpoint(endpoint, params=None, method="GET", data=None):
    try:
        if method == "GET":
            response = requests.get(f"{BASE_URL}{endpoint}", params=params)
        elif method == "POST":
            response = requests.post(f"{BASE_URL}{endpoint}", json=data)
        else:
            raise ValueError("Unsupported HTTP method")
        print(f"\nTesting {endpoint} endpoint...")
        print("Response:", response.json())
    except Exception as e:
        print(f"Error testing {endpoint}: {e}")

if __name__ == "__main__":
    test_endpoint("/health")
    test_endpoint("/info", params={"query": "Koramangala"})
    test_endpoint("/classify", params={"query": "What are the veg starters available at Barbeque Nation?"})
    test_endpoint("/feedback", method="POST", data={"feedback": "Great service at the JP Nagar branch!"})
    test_endpoint("/raw", params={"query": "JP Nagar"})
    test_endpoint("/raw/nearest", params={"city": "Bengaluru"})