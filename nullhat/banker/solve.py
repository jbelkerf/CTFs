from z3 import *

def solve_pin_corrected():
    s = Solver()
    
    # Create 38 byte variables for the PIN
    pin = [BitVec(f'pin_{i}', 32) for i in range(0x26)]  # Using 32-bit to avoid overflow
    
    # All characters must be printable ASCII (0x20-0x7E)
    for i in range(0x26):
        s.add(pin[i] >= 0x20)
        s.add(pin[i] <= 0x7E)
    
    # Add constraints - being very careful with operator precedence and types
    
    # Equation 1: *arg1 * 3 - arg1[1] * 2 == 0x37
    s.add(pin[0] * 3 - pin[1] * 2 == 0x37)
    
    # Equation 2: arg1[1] + arg1[2] - arg1[3] == 0x41
    s.add(pin[1] + pin[2] - pin[3] == 0x41)
    
    # Equation 3: -((arg1[4] * 5)) + arg1[2] * arg1[3] == 0x169b
    s.add(-(pin[4] * 5) + pin[2] * pin[3] == 0x169b)
    
    # Equation 4: arg1[5] * 2 + arg1[6] * 3 - arg1[7] == 0x132
    s.add(pin[5] * 2 + pin[6] * 3 - pin[7] == 0x132)
    
    # Equation 5: arg1[9] * 2 + arg1[7] - arg1[8] == 0x50
    s.add(pin[9] * 2 + pin[7] - pin[8] == 0x50)
    
    # Equation 6: arg1[8] * arg1[9] - arg1[0xa] == 0x207c
    s.add(pin[8] * pin[9] - pin[10] == 0x207c)
    
    # Equation 7: arg1[0xb] * 2 + arg1[0xa] - arg1[0xc] == 0xbd
    s.add(pin[11] * 2 + pin[10] - pin[12] == 0xbd)
    
    # Equation 8: arg1[0xd] + arg1[0xb] * 5 - arg1[0xc] * 3 == 0x17f
    s.add(pin[13] + pin[11] * 5 - pin[12] * 3 == 0x17f)
    
    # Equation 9: arg1[0xd] + arg1[0xe] - arg1[0xf] * 2 == 0x36
    s.add(pin[13] + pin[14] - pin[15] * 2 == 0x36)
    
    # Equation 10: arg1[0xe] * arg1[0xf] - arg1[0x10] * 3 == 0x107a
    s.add(pin[14] * pin[15] - pin[16] * 3 == 0x107a)
    
    # Equation 11: (arg1[0x11] << 2) + arg1[0x10] - arg1[0x12] == 0x1a3
    s.add((pin[17] << 2) + pin[16] - pin[18] == 0x1a3)
    
    # Equation 12: arg1[0x13] * 3 + arg1[0x11] * 2 - arg1[0x12] == 0x106
    s.add(pin[19] * 3 + pin[17] * 2 - pin[18] == 0x106)
    
    # Equation 13: arg1[0x15] + arg1[0x13] - arg1[0x14] * 2 == 0
    s.add(pin[21] + pin[19] - pin[20] * 2 == 0)
    
    # Equation 14: arg1[0x14] * 3 + arg1[0x15] - arg1[0x16] * 2 == 6
    s.add(pin[20] * 3 + pin[21] - pin[22] * 2 == 6)
    
    # Equation 15: arg1[0x16] + arg1[0x17] * 5 - arg1[0x18] == 0x1ec
    s.add(pin[22] + pin[23] * 5 - pin[24] == 0x1ec)
    
    # Equation 16: arg1[0x17] * arg1[0x18] - (arg1[0x19] << 2) == 0xf5c
    s.add(pin[23] * pin[24] - (pin[25] << 2) == 0xf5c)
    
    # Equation 17: arg1[0x1b] * 3 + arg1[0x19] * 2 - arg1[0x1a] == 0x155
    s.add(pin[27] * 3 + pin[25] * 2 - pin[26] == 0x155)
    
    # Equation 18: arg1[0x1a] + arg1[0x1b] - arg1[0x1c] * 2 == 0x67
    s.add(pin[26] + pin[27] - pin[28] * 2 == 0x67)
    
    # Equation 19: arg1[0x1e] + (arg1[0x1c] << 2) - arg1[0x1d] * 3 == 0x6c
    s.add(pin[30] + (pin[28] << 2) - pin[29] * 3 == 0x6c)
    
    # Equation 20: -((arg1[0x1f] * 5)) + arg1[0x1d] * arg1[0x1e] == 0x865
    s.add(-(pin[31] * 5) + pin[29] * pin[30] == 0x865)
    
    # Equation 21: arg1[0x1f] * 2 + arg1[0x1e] - arg1[0x20] == 0x5e
    s.add(pin[31] * 2 + pin[30] - pin[32] == 0x5e)
    
    # Equation 22: (arg1[0x21] << 2) + arg1[0x1f] - arg1[0x20] == 0x11f
    s.add((pin[33] << 2) + pin[31] - pin[32] == 0x11f)
    
    # Equation 23: arg1[0x22] * 2 + arg1[0x20] * 3 - arg1[0x21] == 0x12f
    s.add(pin[34] * 2 + pin[32] * 3 - pin[33] == 0x12f)
    
    # Equation 24: arg1[0x21] * arg1[0x22] - (arg1[0x23] << 2) == 0xde0
    s.add(pin[33] * pin[34] - (pin[35] << 2) == 0xde0)
    
    # Equation 25: arg1[0x23] * 2 + arg1[0x22] - arg1[0x24] == 0x58
    s.add(pin[35] * 2 + pin[34] - pin[36] == 0x58)
    
    # Equation 26: arg1[0x25] * 3 + arg1[0x23] - arg1[0x24] == 0x16f
    s.add(pin[37] * 3 + pin[35] - pin[36] == 0x16f)
    
    # Equation 27: arg1[0x25] + arg1[0x24] * 2 == 0xed
    s.add(pin[37] + pin[36] * 2 == 0xed)
    
    # Cross constraints
    s.add(pin[30] + pin[0] + pin[10] + pin[20] == 0xd7)
    s.add(pin[35] + pin[5] + pin[15] + pin[25] == 0x108)
    s.add(pin[31] + pin[1] + pin[11] + pin[21] == 0x122)
    
    # Checksums
    even_sum = Sum([pin[i] for i in range(0, 0x26, 2)])
    odd_sum = Sum([pin[i] for i in range(1, 0x26, 2)])
    s.add(even_sum == 0x56f)
    s.add(odd_sum == 0x582)
    
    # Try to solve
    if s.check() == sat:
        model = s.model()
        result = []
        for i in range(0x26):
            result.append(model[pin[i]].as_long())
        pin_str = ''.join(chr(b) for b in result)
        return pin_str
    else:
        print("No solution found")
        return None

# Run the corrected solver
print("Solving with corrected constraints...")
pin = solve_pin_corrected()
if pin:
    print(f"\n[SUCCESS] PIN: {pin}")
    print(f"\nVerifying...")
    verify_pin_detailed(pin)
else:
    print("Failed to find solution")
