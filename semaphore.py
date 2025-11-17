
import threading
import time
import random

# Create a Semaphore that allows only 3 threads to access
# the resource at any given time.
access_semaphore = threading.Semaphore(3)

def access_shared_resource(thread_id):
    """
    A function representing a thread trying to access a limited resource.
    """
    
    # `with access_semaphore:` will block the thread until
    # a permit (one of the 3) is available.
    with access_semaphore:
        # Once the permit is acquired, the thread runs this code
        print(f"Thread {thread_id} is accessing the shared resource.\n")
        
        # Simulate work by sleeping for a random time
        sleep_time = random.uniform(1, 4)
        time.sleep(sleep_time)
        
        print(f"Thread {thread_id} has released its permit after {sleep_time:.2f} seconds.\n")
    
    # The permit is automatically released when the `with` block ends.

if __name__ == "__main__":
    threads = []
    
    # Create and start 7 threads
    for i in range(7):
        thread = threading.Thread(target=access_shared_resource, args=(i + 1,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete their execution
    for thread in threads:
        thread.join()

    print("\nAll threads have completed.\n")