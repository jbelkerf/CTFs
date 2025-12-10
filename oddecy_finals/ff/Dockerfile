FROM ubuntu:22.04

# Avoid prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Update and install system dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    # Build essentials
    build-essential \
    gcc \
    g++ \
    make \
    cmake \
    git \
    wget \
    curl \
    # Python and pip
    python3 \
    python3-pip \
    python3-dev \
    # Debugging tools
    gdb \
    gdb-multiarch \
    strace \
    ltrace \
    # Binary analysis tools
    binutils \
    file \
    checksec \
    patchelf \
    # Hex editors and utilities
    hexedit \
    xxd \
    vim \
    nano \
    # Libraries
    libc6-dbg \
    libc6-dev \
    libssl-dev \
    # Network tools
    netcat-traditional \
    socat \
    # Other utilities
    tmux \
    screen \
    tree \
    less \
    unzip \
    zip \
    p7zip-full \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages for reverse engineering
RUN pip3 install --no-cache-dir \
    pwntools \
    angr \
    capstone \
    keystone-engine \
    unicorn \
    ropper \
    z3-solver \
    pycryptodome \
    requests \
    colorama \
    IPython \
    ipdb

# Install GEF (GDB Enhanced Features)
RUN wget -q https://github.com/hugsy/gef/raw/main/gef.py -O /root/.gdbinit-gef.py && \
    echo "source /root/.gdbinit-gef.py" > /root/.gdbinit

# Install pwndbg as alternative (commented out, uncomment if preferred over GEF)
# RUN cd /root && \
#     git clone https://github.com/pwndbg/pwndbg && \
#     cd pwndbg && \
#     ./setup.sh

# Install Ghidra
RUN wget -q https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.2.1_build/ghidra_11.2.1_PUBLIC_20241105.zip -O /tmp/ghidra.zip && \
    apt-get update && apt-get install -y openjdk-17-jdk && \
    unzip -q /tmp/ghidra.zip -d /opt/ && \
    mv /opt/ghidra_* /opt/ghidra && \
    rm /tmp/ghidra.zip && \
    rm -rf /var/lib/apt/lists/*

ENV GHIDRA_HOME=/opt/ghidra

# Install radare2
RUN git clone --depth 1 https://github.com/radareorg/radare2 /tmp/radare2 && \
    cd /tmp/radare2 && \
    sys/install.sh && \
    rm -rf /tmp/radare2

# Install rizin (modern radare2 fork)
RUN pip3 install --no-cache-dir meson ninja && \
    git clone --depth 1 https://github.com/rizinorg/rizin /tmp/rizin && \
    cd /tmp/rizin && \
    meson setup build && \
    meson compile -C build && \
    meson install -C build && \
    rm -rf /tmp/rizin

# Install cutter (GUI for rizin/radare2) dependencies
RUN apt-get update && apt-get install -y \
    qtbase5-dev \
    qtchooser \
    qt5-qmake \
    qtbase5-dev-tools \
    && rm -rf /var/lib/apt/lists/*

# Install IDA Free (if you have license, mount it)
# Note: IDA Free requires manual download, this is a placeholder
# You can mount IDA from host or download manually

# Install one_gadget for finding RCE gadgets
RUN apt-get update && apt-get install -y ruby ruby-dev && \
    gem install one_gadget seccomp-tools && \
    rm -rf /var/lib/apt/lists/*

# Install ROPgadget
RUN pip3 install --no-cache-dir ROPgadget

# Install AFL++ for fuzzing (optional but useful)
RUN apt-get update && apt-get install -y \
    llvm \
    clang \
    && rm -rf /var/lib/apt/lists/* && \
    git clone --depth 1 https://github.com/AFLplusplus/AFLplusplus /opt/AFLplusplus && \
    cd /opt/AFLplusplus && \
    make all && \
    make install

# Create workspace directory
RUN mkdir -p /workspace
WORKDIR /workspace

# Create a helper script for common tasks
RUN echo '#!/bin/bash\n\
echo "================================================="\n\
echo "  Reverse Engineering Docker Environment"\n\
echo "================================================="\n\
echo ""\n\
echo "Available tools:"\n\
echo "  - GDB with GEF (gdb)"\n\
echo "  - radare2/rizin (r2, rizin)"\n\
echo "  - Ghidra (/opt/ghidra/ghidraRun)"\n\
echo "  - Python3 with pwntools, angr, z3"\n\
echo "  - ROPgadget, ropper, one_gadget"\n\
echo "  - strace, ltrace, checksec"\n\
echo ""\n\
echo "Your workspace: /workspace"\n\
echo ""\n\
echo "Quick commands:"\n\
echo "  checksec <binary>     - Check binary protections"\n\
echo "  r2 -AA <binary>       - Analyze binary with radare2"\n\
echo "  gdb <binary>          - Debug with GEF"\n\
echo "  python3 solve.py      - Run your solve script"\n\
echo ""\n\
echo "================================================="\n\
' > /usr/local/bin/welcome && chmod +x /usr/local/bin/welcome

# Set up .bashrc for convenience
RUN echo 'alias ll="ls -lah"' >> /root/.bashrc && \
    echo 'alias r2="radare2"' >> /root/.bashrc && \
    echo 'alias ghidra="/opt/ghidra/ghidraRun"' >> /root/.bashrc && \
    echo 'export PATH=$PATH:/opt/ghidra' >> /root/.bashrc && \
    echo 'welcome' >> /root/.bashrc

# Anti-anti-debugging patches helper script
RUN echo '#!/usr/bin/env python3\n\
import sys\n\
import os\n\
\n\
def patch_binary(filename):\n\
    """Helper to patch common anti-debug checks"""\n\
    with open(filename, "rb") as f:\n\
        data = bytearray(f.read())\n\
    \n\
    # Add your patching logic here\n\
    # Example: NOP out certain calls\n\
    \n\
    output = filename + ".patched"\n\
    with open(output, "wb") as f:\n\
        f.write(data)\n\
    \n\
    os.chmod(output, 0o755)\n\
    print(f"Patched binary saved to: {output}")\n\
\n\
if __name__ == "__main__":\n\
    if len(sys.argv) < 2:\n\
        print("Usage: patch_binary.py <binary>")\n\
        sys.exit(1)\n\
    patch_binary(sys.argv[1])\n\
' > /usr/local/bin/patch_binary.py && chmod +x /usr/local/bin/patch_binary.py

# Create a template solve script
RUN echo '#!/usr/bin/env python3\n\
from pwn import *\n\
import angr\n\
import claripy\n\
\n\
# Configuration\n\
binary_path = "./challenge"\n\
context.binary = binary_path\n\
context.log_level = "debug"\n\
\n\
def solve_with_angr():\n\
    """Use angr for symbolic execution"""\n\
    proj = angr.Project(binary_path, auto_load_libs=False)\n\
    \n\
    # Create symbolic input\n\
    flag = claripy.BVS("flag", 48 * 8)  # 48 bytes\n\
    \n\
    # Set up initial state\n\
    state = proj.factory.entry_state(\n\
        stdin=angr.SimFile("/dev/stdin", content=flag)\n\
    )\n\
    \n\
    # Add constraints (e.g., printable characters)\n\
    for i in range(48):\n\
        byte = flag.get_byte(i)\n\
        state.add_constraints(byte >= 0x20, byte <= 0x7e)\n\
    \n\
    # Find success/failure addresses\n\
    simgr = proj.factory.simulation_manager(state)\n\
    \n\
    # Run until we find success\n\
    # simgr.explore(find=0xADDRESS, avoid=0xADDRESS)\n\
    \n\
    print("[*] Solving with angr...")\n\
    # Add your solving logic\n\
\n\
def solve_with_z3():\n\
    """Use Z3 directly for constraint solving"""\n\
    from z3 import *\n\
    \n\
    # Create solver\n\
    s = Solver()\n\
    \n\
    # Add your constraints\n\
    print("[*] Solving with Z3...")\n\
\n\
def dynamic_solve():\n\
    """Use dynamic analysis with pwntools"""\n\
    p = process(binary_path)\n\
    \n\
    # Interact or script the solution\n\
    p.interactive()\n\
\n\
if __name__ == "__main__":\n\
    print("[*] Starting solver...")\n\
    # Choose your approach\n\
    # solve_with_angr()\n\
    # solve_with_z3()\n\
    dynamic_solve()\n\
' > /workspace/solve_template.py && chmod +x /workspace/solve_template.py

# Create GDB script for anti-anti-debug
RUN echo '# GDB script to bypass anti-debugging\n\
\n\
# Catch ptrace calls\n\
catch syscall ptrace\n\
commands\n\
  set $rax = 0\n\
  continue\n\
end\n\
\n\
# Skip common debugger detection\n\
# Add breakpoints on detection functions and modify return values\n\
\n\
# Example:\n\
# break *0x400000\n\
# commands\n\
#   set $rax = 0\n\
#   continue\n\
# end\n\
' > /workspace/anti_debug.gdb

CMD ["/bin/bash"]