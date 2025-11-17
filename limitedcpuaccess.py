import multiprocessing
import time

def limited_task():
    """A simple function that runs an infinite loop to simulate CPU load."""
    print("Task started. Simulating CPU load...")
    while True:
        # This infinite loop will keep the process busy
        pass

if __name__ == "__main__":
    # Create a new process that targets the `limited_task` function
    process = multiprocessing.Process(target=limited_task)
    
    # Start the process
    process.start()

    # Define the time limit in seconds
    time_limit = 5

    # Wait for the process to finish, but only for `time_limit` seconds
    process.join(time_limit)

    # After 5 seconds, check if the process is still running
    if process.is_alive():
        print(f"Task exceeded {time_limit} seconds. Terminating...")
        
        # If it's still running, terminate it
        process.terminate()
        process.join() # Wait for termination to complete
    else:
        print("Task completed in time.")