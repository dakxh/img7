#multithreaded
import requests
import random
import concurrent.futures
import time

image_urls = [
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Dhandoraa+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Geethanjali+Malli+Vachindi+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Gam+Gam+Ganesha+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Harom+Hara+poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Tamil/Movie+pics/Jailer+2+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/The+Batman+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Crime101+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Hindi/Movie+pics/Dhurandhar2+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/KPop+Demon+Hunters+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Mana+Shankara+Vara+Prasad+Garu+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Passenger.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Pottel+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Malyalam/Actor+Pics/Prithviraj+Sukumaran+Poster.png",
    "https://knitt.s3.us-east-2.amazonaws.com/Tamil/Movie+pics/Seyon+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Srikakulam+Sherlock+Holmes+poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/28+Years+Later-+The+Bone+Temple+Poster.jpeg"
]
headers = {
    "Host" : "knitt.s3.us-east-2.amazonaws.com",
    "Accept-Encoding" : "gzip, deflate, br",
    "Priority":"u=0, i",
    "Cache-Control": "no-cache, no-store, must-revalidate",
    "pragma": "no-cache",
    "referer": "https://www.knitt.app/",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Connection": "close",
    "Expires": "0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}
def fetch_url(request_id):
    target_url = random.choice(image_urls)
    try:
        cache_bust_value = int(time.time() * 1000)
        params = {
        "_": cache_bust_value
        }
        response = requests.get(target_url, headers=headers,params=params)
        return f"[{request_id}] Status: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"[{request_id}] Error for {target_url}: {e}"
def run_multithreaded_check():
    total_requests = 20000
    max_workers = 299

    print(f"Starting execution: {total_requests} requests with up to {max_workers} concurrent threads...")
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(fetch_url, i) for i in range(1, total_requests + 1)]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

    duration = time.time() - start_time
    print("\n--- Execution Finished ---")
    print(f"Total time: {duration:.2f} seconds")
    print(f"Average throughput: {total_requests / duration:.2f} requests/second")

if __name__ == "__main__":
    run_multithreaded_check()

