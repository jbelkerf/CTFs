#!/usr/bin/env python3
import subprocess
import string
import itertools
from pwn import *

def test_password(password):
    """
    Test a password against the binary
    """
    try:
        # Start the process
        p = process('./simple')  # Replace with actual binary name
        
        # Send the password
        p.sendline(password.encode())
        
        # Get response
        response = p.recvline(timeout=1)
        p.close()
        
        # Check if we got a positive response
        if b'yes' in response.lower() or b'correct' in response.lower() or b'raptor' in response.lower():
            return True, response
        return False, response
    except Exception as e:
        return False, str(e).encode()

def brute_force_sequential():
    """
    Try sequential approach with common patterns
    """
    # Since we know it starts with ELITESEC{ and ends with }, that's 10 chars used
    # We need 6 characters in the middle: ELITESEC{XXXXXX}
    
    prefix = "ELITESEC{"
    suffix = "}"
    middle_length = 6
    
    printables = string.printable.strip()  # All printable characters
    
    print(f"Trying all {len(printables)} printable characters for {middle_length} positions...")
    print(f"Total combinations: {len(printables) ** middle_length}")
    
    # Try some common patterns first
    common_middles = [
        "RAPTOR", "raptor", "Raptor", "R4PT0R", "r4pt0r",
        "FAST!!", "fast!!", "Fast!!", "F4ST!!", "f4st!!",
        "QUICK!", "quick!", "Quick!", "QU1CK!", "qu1ck!",
        "SPEED!", "speed!", "Speed!", "SP33D!", "sp33d!",
        "WINNER", "winner", "Winner", "W1NN3R", "w1nn3r"
    ]
    
    for middle in common_middles:
        if len(middle) == middle_length:
            password = prefix + middle + suffix
            print(f"Trying: {password}")
            success, response = test_password(password)
            if success:
                print(f"SUCCESS! Password found: {password}")
                print(f"Response: {response}")
                return password
    
    # If common patterns don't work, try systematic approach
    print("Common patterns failed, trying systematic approach...")
    
    # Try all combinations (this might take a while)
    count = 0
    for combo in itertools.product(printables, repeat=middle_length):
        middle = ''.join(combo)
        password = prefix + middle + suffix
        
        count += 1
        if count % 1000 == 0:
            print(f"Tried {count} combinations...")
        
        success, response = test_password(password)
        if success:
            print(f"SUCCESS! Password found: {password}")
            print(f"Response: {response}")
            return password
    
    return None

def interactive_mode():
    """
    Interactive mode to manually test passwords
    """
    print("Interactive mode - enter passwords to test")
    print("Format: ELITESEC{XXXXXX} where XXXXXX is 6 characters")
    print("Type 'quit' to exit")
    
    while True:
        password = input("\nEnter password to test: ").strip()
        if password.lower() == 'quit':
            break
        
        if len(password) != 16:
            print(f"Password length is {len(password)}, should be 16")
            continue
        
        if not password.startswith("ELITESEC{"):
            print("Password should start with 'ELITESEC{'")
            continue
        
        if not password.endswith("}"):
            print("Password should end with '}'")
            continue
        
        success, response = test_password(password)
        if success:
            print(f"SUCCESS! Password accepted!")
            print(f"Response: {response}")
            break
        else:
            print(f"Failed. Response: {response}")

def main():
    print("Raptor Password Cracker")
    print("=" * 50)
    print("Looking for 16-byte password in format: ELITESEC{XXXXXX}")
    print("I like Raptors, because they are fast. How fast are you at solving this tho?")
    print()
    
    # Check if binary exists
    try:
        with open('./simple', 'rb'):
            pass
    except:
        print("Error: Binary 'simple' not found in current directory")
        print("Please make sure the binary is named 'simple' and in the same directory")
        return
    
    print("Choose mode:")
    print("1. Automatic brute force")
    print("2. Interactive manual testing")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        print("\nStarting automatic brute force...")
        result = brute_force_sequential()
        if result:
            print(f"\n🎉 Flag found: {result}")
        else:
            print("\n❌ Password not found with brute force")
    elif choice == "2":
        interactive_mode()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()