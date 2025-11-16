import hashlib
import time
import threading

def worker(start, end, salt, result):
    for password in range(start, end):
        attempt = salt + str(password)
        hash_result = hashlib.md5(attempt.encode()).hexdigest()
        
        if hash_result.startswith("0e") and hash_result[2:].isdigit():
            result['found'] = password
            return

def fast_find_magic_password():
    salt = "f789bbc328a3d1a3"
    result = {'found': None}
    threads = []
    num_threads = 4
    
    print(f"🚀 Starting {num_threads} threads to find magic password...")
    start_time = time.time()
    
    # Split work among threads
    chunk_size = 10000000  # 10 million per thread
    
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size
        thread = threading.Thread(target=worker, args=(start, end, salt, result))
        threads.append(thread)
        thread.start()
    
    # Wait for any thread to find it
    while result['found'] is None:
        time.sleep(1)
        # You could add a progress counter here
    
    # Stop all threads
    for thread in threads:
        thread.join()
    
    elapsed = time.time() - start_time
    print(f"\n🎉 FOUND: {result['found']}")
    print(f"⏱️  Time: {elapsed:.2f} seconds")
    return result['found']

fast_find_magic_password()