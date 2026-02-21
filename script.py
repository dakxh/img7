#multithreaded
import requests
import random
import concurrent.futures
import time

image_urls = [
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/AA23+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Actor+Pics/Anushka+Shetty+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Bahubali.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Baahubali+2-+The+Conclusion+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Corpse+Bride+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Malyalam/Movie+pics/Chatha+Pacha+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Hindi/Movie+pics/Dhurandhar+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Tamil/Actor+Pics/Dhanush+K+Raja+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Dhandoraa+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/ENE+Repeat+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Malyalam/Movie+pics/Eko+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Fauzi+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Final+Destination+Bloodlines+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Geethanjali+Malli+Vachindi+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Guntur+Kaaram.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Gam+Gam+Ganesha+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Gangs+of+Godavari.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Harom+Hara+poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/How+To+Train+Your+Dragon+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Hanu-Man.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/If+Beale+Street+Could+Talk+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Iron+Lung+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Tamil/Movie+pics/Jailer+2+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Tamil/Movie+pics/Jana+Nayagan+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Jurassic+World+Rebirth+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Khaleja+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Kannada/Movie+pics/Kantara+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Malyalam/Movie+pics/Lokah-+Chapter+1+-+Chandra+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Tamil/Movie+pics/LIK+-+Love+Insurance+Kompany+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/La+La+Land+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Ladybird+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Lilo+%26+Stitch+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Maa+Inti+Bangaaram+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Tamil/Movie+pics/Master+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Actor+Pics/Jr+NTR+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Om+Bheem+Bush+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Pokiri+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Pushpa+2+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Actor+Pics/Prabhas+Poster.png",
    "https://knitt.s3.us-east-2.amazonaws.com/Hindi/Actor+Pics/Rakesh+Bedi+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Actor+Pics/Rashmika.jfif",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/The+Batman+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/The+Paradise+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Kannada/Movie+pics/Toxic-+A+Fairy+Tale+for+Grown-Ups+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Ustaad+Bhagat+Singh+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Varanasi.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Yatra+2.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Zootopia+2+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Zebra-poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/AA22x26+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Akhanda+2+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Athadu+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Avatar+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Hindi/Movie+pics/Baaghi+4.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Bhartha+Mahasayulaku+Wignyapthi+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Hindi/Movie+pics/Chhaava.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Clayface.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Crime101+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Devara+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Hindi/Movie+pics/De+De+Pyaar+De+2+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Hindi/Movie+pics/Dhurandhar2+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Malyalam/Movie+pics/Drishyam+3+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Drive+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Tamil/Movie+pics/Dude+Poster.jfif",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Funky.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Hindi/Movie+pics/Housefull+5.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Hindi/Movie+pics/Jaat.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Kalki+2898+AD+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/KA+poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/KPop+Demon+Hunters+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Lucky+Baskhar+poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Marty+Supreme+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Mana+Shankara+Vara+Prasad+Garu+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Mechanic+Rocky+poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Mickey+17+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Actor+Pics/Morgan+Freeman+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Music+Shop+Murthy+poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Nari+Nari+Naduma+Murari+Poster.png",
    "https://knitt.s3.us-east-2.amazonaws.com/Tamil/Actor+Pics/Nayanathara+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/NTRNEEL+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Passenger.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Peddi+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Pottel+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Malyalam/Actor+Pics/Prithviraj+Sukumaran+Poster.png",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Primate+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Pushpa+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Ranabaali+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Tamil/Movie+pics/Retta+Thala+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Resident+Evil.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Actor+Pics/Ryan+Gosling.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Salaar+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Hindi/Actor+Pics/Sara+Arjun+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Hindi/Movie+pics/Saiyaara.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Tamil/Movie+pics/Seyon+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Shelter+Posterf.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Sinners+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Snow+White+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Solo+Mio+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Show+Poster/Spider-Noir+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Srikakulam+Sherlock+Holmes+poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/They+Call+Him+OG+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/To+All+The+Boys+I've+Loved+Before+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Hindi/Movie+pics/War+2.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/The+Dinosaurs+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/35-Chinna+Katha+Kaadu+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Minecraft+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Tamil/Movie+pics/Mahaan+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/The+Rajasaab+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/The+RajaSaab.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/The+Angry+Birds+Movie+3.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/28+Years+Later-+The+Bone+Temple+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/Thunderbolts*+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/The+Great+Gatsby+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/The+Housemaid+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/The+Fantastic+Four-+First+Steps+Poster.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Manamey+Poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/The+Family+Star.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/English+/Movie+Poster/The+Threesome.jpeg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Movie+pics/Matka+poster.jpg",
    "https://knitt.s3.us-east-2.amazonaws.com/Telugu/Technician+Pics/Thaman+Poster.png"
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
    total_requests = 100000
    max_workers = 599

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