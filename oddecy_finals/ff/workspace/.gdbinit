# Custom GDB configuration

# Disable confirmation prompts
set confirm off

# Show assembly in Intel syntax
set disassembly-flavor intel

# Auto-load .gdbinit from current directory
set auto-load safe-path /

# Better display
set print pretty on
set print array on
set print array-indexes on

# History
set history save on
set history size 10000
set history filename ~/.gdb_history

# Anti-anti-debug helpers
define hook-stop
    # You can add commands to run on each stop
end

# Custom commands
define patch_nop
    set *(unsigned char*)$arg0 = 0x90
    set *(unsigned char*)($arg0+1) = 0x90
    set *(unsigned char*)($arg0+2) = 0x90
end

document patch_nop
Syntax: patch_nop ADDR
Patches 3 bytes at ADDR with NOPs
end

define skip_call
    set $pc = $pc + 5
end

document skip_call
Skips the current call instruction (5 bytes)
end
