import sqlite3
from collections import defaultdict

# Connect to the SQLite database
conn = sqlite3.connect('/data/freenas-v1.db')
cursor = conn.cursor()

# Fetch VM configurations
cursor.execute("SELECT * FROM vm_vm")
vm_configs = cursor.fetchall()

# Fetch VM devices
cursor.execute("SELECT * FROM vm_device")
vm_devices = cursor.fetchall()

# Organize devices by VM ID
vm_device_map = defaultdict(list)
for device in vm_devices:
    vm_id = device[3]  # vm_id is the 4th column in the vm_device table
    vm_device_map[vm_id].append(device)

# Print the organized data
for vm in vm_configs:
    vm_id = vm[0]  # id is the 1st column in the vm_vm table
    print(f"VM ID: {vm_id}")
    print(f"Name: {vm[1]}")
    print(f"Description: {vm[2]}")
    print(f"vCPUs: {vm[3]}")
    print(f"Memory: {vm[4]}")
    print(f"Autostart: {vm[5]}")
    print(f"Bootloader: {vm[6]}")
    print(f"Cores: {vm[7]}")
    print(f"Threads: {vm[8]}")
    print(f"Shutdown Timeout: {vm[9]}")
    print(f"CPU Mode: {vm[10]}")
    print(f"CPU Model: {vm[11]}")
    print(f"Hide from MSR: {vm[12]}")
    print(f"Ensure Display Device: {vm[13]}")
    print(f"Arch Type: {vm[14]}")
    print(f"Machine Type: {vm[15]}")
    print(f"UUID: {vm[16]}")
    print(f"CPUSet: {vm[17]}")
    print(f"NodeSet: {vm[18]}")
    print(f"Pin vCPUs: {vm[19]}")
    print(f"Min Memory: {vm[20]}")
    print(f"HyperV Enlightenments: {vm[21]}")
    print(f"Suspend on Snapshot: {vm[22]}")
    print(f"Command Line Args: {vm[23]}")
    print(f"Bootloader OVMF: {vm[24]}")
    print(f"Trusted Platform Module: {vm[25]}")
    print(f"Enable CPU Topology Extension: {vm[26]}")
    print("\nDevices:")
    for device in vm_device_map[vm_id]:
        print(f"  Device ID: {device[0]}")
        print(f"  Type: {device[1]}")
        print(f"  Attributes: {device[2]}")
        print(f"  Order: {device[4]}")
        print()
    print("-" * 80)

# Close the connection
conn.close()
