# tnvm-buddy
A small python script to assist in migrating pre-25.04 VMs


This script helps reduce the amount of clicks needed to collect the information needed pre-migration. Rather than going into the UI and clicking in each VM for each device, it simply dumps the contents of the database in a human readable format.

##https://www.truenas.com/docs/scale/gettingstarted/scalereleasenotes/
##For most up to date information click on the link above, but copied here for users of this script:

```
Preparing to Migrate VMs from 24.10
Screenshot or record existing VM configuration(s).

Go to Virtualization and click on a VM to expand that row. Click  Edit to open the Edit VM screen and note the existing configuration. Save your configuration settings in an external location to reference later. These settings do not migrate and must be recreated after upgrading to 25.04.

Record the existing zvol storage location and virtual device configuration.

Go to Virtualization and click on a VM to expand that row. Click device_hub Devices. Click more_vert in the Disk row and select Edit. Note the configured path in Zvol as well as the storage Mode and the Disk Sector Size. Continue to note all other VM devices and associated configuration settings. Record this information in an external location along with the configuration settings gathered above.

Locate or download the required iso image files.

Access the VM via Display or Serial Shell and confirm the installed OS and version. Refer to documentation for the installed OS if needed to locate the installed version.

If the installed image (iso) file is stored on the TrueNAS system or in an external location, note this path and record it along with the other configuration settings. If needed, download a fresh image file matching the installed OS and Version
```


---

## Usage

### Clone the Repository

Must be done as `root` in a location with write access such as `/root/` or `/mnt/tank/scripts`

```git clone https://github.com/nickf1227/tnvm-buddy.git && cd tnvm-buddy && python3 tnvmbuddy.py```


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
