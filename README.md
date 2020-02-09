# Disable C6 State for AMD CPUs on Linux

## Description

Issues with the C6 state being enabled on Linux causes an unresponsive system.

Disabling the C6 state fixes this issue with AMD CPUs on Linux.

## Usage

### `msr.conf`

```
sudo cp msr.conf /etc/modules-load.d/
```

### `zenstates.py`

```
sudo cp zenstates.py /opt/
```

### `zenstates.service`

```
sudo cp zenstates.service /etc/systemd/system/
```

### Enabling service

```
sudo modprobe msr
sudo systemctl enable zenstates.service
sudo systemctl start zenstates.service
```

> You can reboot instead of `modprobe msr`, but you will need to enable and start the service before the reboot.