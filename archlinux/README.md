# Archlinux

# Table of Content

- [Download](#download)
- [Installation](#installation)
  - [Wifi Internet Connection](#wifi-internet-connection)
  - [Partition the disk](#partition-the-disk)
  - [Format the partitions](#format-partitions)
  - [Select the mirrors](#select-the-mirrors)
  - [Network Configuration](#network-configuration)
  - [Network Manager](#network-manager)
  - [GRUB Installation](#grub-installation)
  - [Create the user](#create-the-user)
  - [User root](#user-root)
  - [To turn off](#to-turn-off)
- [Configuration](#configuration)
- [Useful concepts](#useful-concepts)
  - [Pacman](#pacman)
- [Applications](#applications)
  - [Vscode](#vscode)
  - [VLC](#vlc)
- [QTile](#qtile)

# Download

[Download ISO file](https://archlinux.org/download/)

# Installation

[Installation Guide](https://wiki.archlinux.org/title/Installation_guide)

If you have BIOS instead of UEFI skip certain points from the wiki

> Before starting the installation, remove all partitions from the old OS disk and leave the disk unpartitioned

## Wifi Internet Connection

Words in quotes must be changed

```bash
$ iwctl
$ device list
$ station 'name' scan
$ station 'name' get-networks
$ station 'name' connect 'name_your_network'
$ exit
```

Check the connection:
`ping google.com`

## Partition the disk

Shows disks and partitions
`lsblk`

`fdisk -l`

Create 3 primary partitions with `cfdisk`

- `/` 20 GB
- `swap` 8 GB
- `/home` rest of storage

NEW

> In the terminal just put the G instead of GB

Once the partitions have been created the 3 partitions are located in the swap partition, then Type / Linux Swap.
Also press Bootable on the partition `/`

WRITE

YES

QUIT

`lsblk`

## Format partitions

Format as ext4 with exception of swap

## Select the mirrors

https://wiki.archlinux.org/title/Mirrors

The mirros are in the file `/etc/pacman.d/mirrorlist`

We will use reflector to select the fastest servers. You must run the command every so often so that you have the most recent mirrors. Before deleting existing mirrors

https://wiki.archlinux.org/title/Reflector

```bash
$ sudo pacman -S reflector
$ reflector --help
$ sudo reflector --sort rate -l 5 --save /etc/pacman.d/mirrorlist
```

## Network configuration:

```bash
127.0.0.1	localhost
::1		    localhost
127.0.1.1	elnombredemiequipo.localhost	elnombredemiequipo
```

## Network Manager

https://wiki.archlinux.org/title/NetworkManager

```bash
$ sudo pacman -S networkmanager
$ systemctl enable NetworkManager
```

## GRUB Installation

https://wiki.archlinux.org/title/GRUB

`sudo pacman -S grub`

### GRUB Installation on the HDD

In the partition root

`grub-install /dev/sda1`

### Create grub configuration file which is in boot

`grub-mkconfig -o /boot/grub/grub.cfg`

## Create the user

```bash
$ useradd -m 'name_username
$ passwd 'password_of_username''
```

## User root

For the user to have sudo permissions we must add it to the `wheel` group, which in Ubuntu is sudo

```bash
$ sudo pacman -S sudo
$ usermod -aG wheel,audio,video,storage 'name_username'
$ su 'user_name'
$ groups
$ exit
```

Uncomment the line `zwheel ALL=(ALL) ALL` if you want it to ask you for the password every time you type sudo:

```bash
$ nano /etc/sudoers
$ exit
```

## To turn off

`shutdown now`

Disconnect USB

# Configuration

# Useful concepts

## Pacman

https://wiki.archlinux.org/title/Pacman

Install a package

```bash
$ sudo pacman -S nombreDelPaquete
```

Uninstall a package and its dependencies (as long as they are not used by any other package)

```bash
$ sudo pacman -Rs nombreDelPaquete
```

Pacman saves important configuration files when removing certain applications and names them with the extension: .pacsave . To prevent the creation of these backup files, use the -n option:

```bash
$ sudo pacman -Rsn nombreDelPaquete
```

# Applications

https://wiki.archlinux.org/title/list_of_applications

## Vscode

https://wiki.archlinux.org/title/Visual_Studio_Code

Vscode installation. Exclusive launch of the Microsoft brand. `visual-studio-code-bin` stores the settings in `~/.config/Code/User/settings.json`

```bash
$ yay -S visual-studio-code-bin
```

- ### Font [JetBrains Mono](https://www.jetbrains.com/es-es/lp/mono/)

Unzip the font to `/usr/share/fonts` to install fonts system-wide) and run `fc-cache -f -v`. Restart your IDE. Go to settings of the editor and put in fonts 'JetBrains Mono'. Copy only `/tff /webfont` `/variable` directories

Go to the vscode configuration file and:

```c#
"editor.fontLigatures": true,
"editor.fontFamily": "'JetBrains Mono'"
```

My vscode settings file [here](./vscode/settings.json). Some configurations I copied from the blog of this crack [here](https://medium.com/@liaogg/minimal-vscode-setup-for-maximized-productivity-part-1-19db1c54697).

- ### Theme Gruvbox Material | Dracula

- ### Icons Material Icons

## VLC

```bash
$ sudo pacman -S vlc
```

## Transmission-gtk

Cliente BitTorrent

https://archlinux.org/packages/?name=transmission-gtk

```bash
$ sudo pacman -S transmission-gtk
```

## Gnome Disk Utility

https://archlinux.org/packages/extra/x86_64/gnome-disk-utility/

```bash
sudo pacman -S gnome-disk-utility
```

## Discord

https://wiki.archlinux.org/title/Discord

## Redshift

Luz nocturna

```bash
sudo pacman -S redshift
```

## Arduino

## RecordMyDesktop

Grabador de pantalla

https://aur.archlinux.org/packages/gtk-recordmydesktop

# QTile

The Qtile configuration file `~/.config/qtile/config.py`

My qtile setting file [here](./qtile/)
