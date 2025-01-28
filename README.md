# tnvm-buddy
A small python script to assist in migrating pre-25.04 VMs
Below is a `README.md` file for the Python script provided earlier. This document explains the purpose, usage, and requirements of the script.

---

## Usage

### 1. Clone the Repository (if applicable)

If this script is part of a repository, clone it to your local machine:


### View the Output

The script will output the VM configurations and their associated devices in a structured format. For example:

```
VM ID: 2
Name: morgan
Description: pfsense - 10.69.10.1
vCPUs: 1
Memory: 4096
Autostart: 1
Bootloader: UEFI
Cores: 8
Threads: 2
Shutdown Timeout: 90
CPU Mode: HOST-PASSTHROUGH
CPU Model: 
Hide from MSR: 0
Ensure Display Device: 1
Arch Type: 
Machine Type: 
UUID: 71d77054-f7ce-4dce-8a8a-6004d744ba74
CPUSet: 
NodeSet: 
Pin vCPUs: 0
Min Memory: 0
HyperV Enlightenments: 0
Suspend on Snapshot: 0
Command Line Args: 
Bootloader OVMF: OVMF_CODE.fd
Trusted Platform Module: 0
Enable CPU Topology Extension: 0

Devices:
  Device ID: 18
  Type: DISK
  Attributes: {"path": "/dev/zvol/ice/vms/morgan-64k", "type": "AHCI", "logical_sectorsize": null, "physical_sectorsize": null, "iotype": "THREADS"}
  Order: 1002

  Device ID: 19
  Type: NIC
  Attributes: {"type": "VIRTIO", "mac": "00:a0:98:5b:70:cc", "nic_attach": "eno1", "trust_guest_rx_filters": false}
  Order: 1003

...
--------------------------------------------------------------------------------
```

## Database Schema

The script assumes the following tables exist in the SQLite database:

### `vm_vm` Table
- Contains VM configurations such as name, description, vCPUs, memory, and more.

### `vm_device` Table
- Contains device mappings for each VM, including device type, attributes, and order.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

This `README.md` provides a clear overview of the script, its purpose, and how to use it. You can customize it further based on your specific needs or repository structure.
