import random

CACHE_CAPACITY = 3  
NUM_REQUESTS = 50   
MAX_ID = 5         


def generate_input_file(filename="data/input/input3.in"):

    requests = [random.randint(1, MAX_ID) for _ in range(NUM_REQUESTS)]
    
    with open(filename, 'w') as f:

        f.write(f"{CACHE_CAPACITY} {NUM_REQUESTS}\n")
        
        requests_str = " ".join(map(str, requests))
        f.write(f"{requests_str}\n")
        
    print(f"Generated '{filename}'.")
    print(f"Cache Size (k) : {CACHE_CAPACITY}")
    print(f"Requests (m)   : {NUM_REQUESTS}")

if __name__ == "__main__":
    generate_input_file()