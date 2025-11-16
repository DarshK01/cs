import os

shutdown = input("Do you wish to shutdown your computer? (yes/no): ")

if shutdown.lower() == "no":
    print("Shutdown cancelled.")
else:
    print("[SIMULATION] System would shut down now.")
    # os.system("shutdown /s /t 1")  # Disabled for safety
