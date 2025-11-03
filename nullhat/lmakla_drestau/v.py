# GDB Python script to extract the decrypted password
# Save as extract_password.py and run in GDB with: source extract_password.py

import gdb

class ExtractPassword(gdb.Command):
    """Extract the decrypted password from sub_401360"""
    
    def __init__(self):
        super(ExtractPassword, self).__init__("extract_password", gdb.COMMAND_USER)
    
    def invoke(self, arg, from_tty):
        # Set breakpoint after the decryption loop
        # The decrypted string should be at [rbp-0x88] (v0 variable)
        
        print("Setting breakpoint after decryption loop in sub_401360...")
        
        # Breakpoint right before strcmp (address may vary)
        bp = gdb.Breakpoint("*sub_401360+210")  # Adjust offset if needed
        
        print("Run the program and enter any input...")
        gdb.execute("run")
        
        # Read the decrypted password from stack
        try:
            rbp = int(gdb.parse_and_eval("$rbp"))
            password_addr = rbp - 0x88
            
            # Read 20 bytes
            inferior = gdb.selected_inferior()
            password_bytes = inferior.read_memory(password_addr, 20)
            
            password = password_bytes.tobytes().decode('ascii', errors='replace')
            
            print(f"\n{'='*60}")
            print(f"DECRYPTED PASSWORD FOUND!")
            print(f"{'='*60}")
            print(f"Address: 0x{password_addr:x}")
            print(f"Password: '{password}'")
            print(f"Hex: {password_bytes.tobytes().hex()}")
            print(f"{'='*60}")
            
        except Exception as e:
            print(f"Error extracting password: {e}")
            print("Try manually: x/20c $rbp-0x88")

# Register the command
ExtractPassword()

print("GDB command 'extract_password' registered!")
print("Usage: Just type 'extract_password' in GDB")
