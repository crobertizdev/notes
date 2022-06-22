# Arhlinux

# Table of Content

- [Download](#download)
- [Installation](#installation)
  - [Wifi Internet Connection](#wifi-internet-connection)
  - [Partition the disk](#partition-the-disk)
  - [GRUB Installation](#grub-installation)
  - [Create the user](#create-the-user)
  - [Format the partitions](#format-partitions)
  - [Network Configuration](#network-configuration)
  - [Network Manager](#network-manager)
  - [GRUB Installation](#grub-installation)
  - [Create the user](#create-the-user)
  - [Create the user](#create-the-user)
  - [User root](#user-root)
  - [To turn off](#to-turn-off)

# Download

[Download ISO file](https://archlinux.org/download/)

# Installation

[Installation Guide](https://wiki.archlinux.org/title/Installation_guide)

If you have BIOS instead of UEFI skip certain points from the wiki

> Before starting the installation, remove all partitions from the old OS disk and leave the disk unpartitioned, only MBR formatted

## Wifi Internet Connection

Words in quotes must be changed

```bash
iwctl
device list
station 'name' scan
station 'name' get-networks
station 'name' connect 'name_your_network'
exit
```

Check the connection:
`ping google.com`

## Partition the disk

Shows disks and partitions

`lsblk`

`fdisk -l`

Create 3 primary partitions

- `/` 20 GB
- `swap` 8 GB
- `/home` rest of storage

`cfdisk`

NEW

> In the terminal just put the G instead of GB

Once the partitions have been created, the 3 partitions are located in the swap partition, then Type / Linux Swap.
Also press Bootable on the partition /

WRITE

YES

QUIT

`lsblk`

## Format partitions

Format as ext4 with exception of swap

## Network configuration:

```bash
127.0.0.1	localhost
::1		    localhost
127.0.1.1	elnombredemiequipo.localhost	elnombredemiequipo
```

## Network Manager

https://wiki.archlinux.org/title/NetworkManager

```bash
sudo pacman -S networkmanager
systemctl enable NetworkManager
```

## GRUB Installation

`sudo pacman -S grub`

### GRUB Installation on the HDD

In the partition root

`grub-install /dev/sda1`

### Create grub configuration file which is in boot

`grub-mkconfig -o /boot/grub/grub.cfg`

## Create the user

```bash
useradd -m 'name_username
passwd 'password_of_username''
```

## User root

For the user to have sudo permissions we must add it to the `wheel` group, which in Ubuntu is sudo

```bash
sudo pacman -S sudo
usermod -aG wheel,audio,video,storage 'name_username'
su 'user_name'
groups
exit
```

Uncomment the line `zwheel ALL=(ALL) ALL` if you want it to ask you for the password every time you type sudo:

```bash
nano /etc/sudoers
exit
```

## To turn off

`shutdown now`

Disconnect USB
