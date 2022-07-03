# Archlinux

# Tabla de Contenido

- [Descarga](#descarga)
- [Instalación](#instalación)
  - [Conexión a internet wifi](#conexión-a-internet-wifi)
  - [Particionar el disco](#particionar-el-disco)
  - [Formatear las particiones](#formatear-particiones)
  - [Configurar las mirrors](#configurar-las-mirrors)
  - [Configuración de red](#configuración-de-red)
  - [Network Manager](#network-manager)
  - [Instalación del GRUB](#instalación-del-grub)
  - [Crear el usuario](#crear-el-usuario)
  - [Usuario root](#usuario-root)
  - [Apagar](#apagar)
- [Configuración](#configuración)
  - [Conceptos útiles](#conceptos-útiles)
    - [Pacman](#pacman)
  - [Conectar a wifi con netwokmanager](#conectar-a-wifi-con-networkmanager)
  - [Xorg](#xorg)
  - [Fuentes del SO](#fuentes-del-so)
  - [OS PROBER](#os-prober)
  - [Instalar un entorno de escritorio DE](#instalar-un-entorno-de-escritorio-de)
  - [Actualizar el sistema](#actualizar-el-sistema)
- [Aplicaciones](#aplicaciones)
  - [Vscode](#vscode)
  - [VLC](#vlc)
  - [Transmision GTK](#transmission-gtk)
  - [Gnome Disk Utility](#gnome-disk-utility)
  - [Discord](#discord)
  - [Redshift](#redshift)
  - [Arduino](#arduino)
  - [RecordMyDesktop](#recordmydesktop)
  - [Alacritty](#alacritty)
  - [Google Chrome](#google-chrome)
  - [Micro](#micro)
- [Crea tu propio DE](#crea-tu-propio-de)
- [QTile](#qtile)

# Descarga

[Descargar el fichero ISO](https://archlinux.org/download/)

# Instalación

[Guia de Instalación](<https://wiki.archlinux.org/title/Installation_guide_(Espa%C3%B1ol)>)

Si tiene BIOS en lugar de UEFI, omita ciertos puntos de la wiki.

> Antes de comenzar la instalación, elimine todas las particiones del disco antiguo del sistema operativo y deje el disco sin particionar.

## Conexión a internet wifi

Las palabras entre comillas deben cambiarse

```bash
$ iwctl
$ device list
$ station 'nombre' scan
$ station 'nombre' get-networks
$ station 'nombre' connect 'nombre_de_tu_red'
$ exit
```

Verifique la conexión:
`ping google.com`

## Particionar el disco

Mostrar discos y particiones
`lsblk`

`fdisk -l`

Crear 3 particiones primarias con `cfdisk`

- `/` 20 GB
- `swap` 8 GB
- `/home` resto del espacio

NEW

> En la terminal solo pon la G en lugar de GB.

Una vez que se han creado las tres particiones, ubiquese en la partición de swap, luego `Type / Linux Swap`.
También presione Bootable en la partición `/`

WRITE

YES

QUIT

`lsblk`

## Formatear particiones

Formatear como ext4 con excepción de swap

## Configurar las mirrors

https://wiki.archlinux.org/title/Mirrors_(Espa%C3%B1ol)

Las mirrors están en el archivo. `/etc/pacman.d/mirrorlist`

Usaremos reflector para seleccionar los servidores más rápidos. Debe ejecutar el comando cada cierto tiempo para que tenga las mirrors más recientes. Antes eliminar las mirrors existentes.
https://wiki.archlinux.org/title/Reflector_(Espa%C3%B1ol)

```bash
$ sudo pacman -S reflector
$ reflector --help
$ sudo reflector --sort rate -l 5 --save /etc/pacman.d/mirrorlist
```

## Configuración de red:

```bash
127.0.0.1	localhost
::1		    localhost
127.0.1.1	elnombredemiequipo.localhost	elnombredemiequipo
```

## Network Manager

Este programa nos permitirá tener internet al encender la pc

https://wiki.archlinux.org/title/NetworkManager

```bash
$ sudo pacman -S networkmanager
$ systemctl enable NetworkManager
```

## Instalación del GRUB

https://wiki.archlinux.org/title/GRUB_(Espa%C3%B1ol)

`sudo pacman -S grub`

### Instalación del GRUB en el HDD

En la partición root

`grub-install /dev/sda1`

### Crear el archivo de configuración de grub que está en el root

`grub-mkconfig -o /boot/grub/grub.cfg`

## Crear el usuario

```bash
$ useradd -m 'nombre_de_usuario'
$ passwd 'contraseña_del_usuario'
```

## Usuario root

Para que el usuario tenga permisos sudo debemos agregarlo al grupo `wheel`, que en Ubuntu es sudo

```bash
$ sudo pacman -S sudo
$ usermod -aG wheel,audio,video,storage 'nombre_del_usuario'
$ su 'nombre_de_usuario'
$ groups
$ exit
```

Quite el comentario de la línea `zwheel ALL=(ALL) ALL` si desea que le solicite la contraseña cada vez que escriba sudo:

```bash
$ nano /etc/sudoers
$ exit
```

## Apagar

`shutdown now`

Desconecte el USB

# Configuración

# Instalación de software

En arch se instala sotware con el gestor de paquetes `pacman` pero si el paquete que queremos descargar no se encuentra allí usamos [aur](<https://wiki.archlinux.org/title/Arch_User_Repository_(Espa%C3%B1ol)>).

Para usar debemos insalar `yay`:

```bash
$ sudo pacman -S git
$ cd /
$ cd opt/
$ sudo git clone 	https://aur.archlinux.org/yay-git.git
$ ls
$ sudo chown -R 'usuario':'grupo' ./yay-git
$ ls -l
$ cd yay-git/
$ sudo pacman -S base-devel
$ makepkg -si
```

> Usuario: carlos. Grupo: carlos

## Pacman

https://wiki.archlinux.org/title/Pacman_(Espa%C3%B1ol)

Instalar un paquete

```bash
$ sudo pacman -S 'nombreDelPaquete'
```

Desinstalar un paquete y sus dependencias (siempre y cuando no sean utilizadas por ningún otro paquete)

```bash
$ sudo pacman -Rs 'nombreDelPaquete'
```

Pacman guarda archivos de configuración importantes al eliminar ciertas aplicaciones y los nombra con la extensión: .pacsave. Para evitar la creación de estos archivos de copia de seguridad, utilice la opción -n:

```bash
$ sudo pacman -Rsn 'nombreDelPaquete'
```

## Conectar a wifi con networkmanager

[networkmanager](https://wiki.archlinux.org/title/NetworkManager#Usage)

```bash
$ sudo su
$ nmcli device wifi list
$ nmcli device wifi connect 'nombre_del_wifi' password 'nombre_de_clave'
$ nmcli device
```

## Xorg

De xorg deriva el diseño del teclado (**setxkbmap es**) y el compositor de imágenes (**Picom**)

https://wiki.archlinux.org/title/xorg

```bash
sudo pacman -S xorg
```

## Fuentes del SO

https://www.nerdfonts.com/

Nerdfonts son colecciones de fuentes que vienen con [iconos](https://www.nerdfonts.com/cheat-sheet). Lo usaremos para fuentes e íconos de la barra de tareas, terminal, vscode y otros. Mi fuente instalada es [UbuntuMono Nerd Font](https://www.nerdfonts.com/font-downloads)

```bash
$ sudo pacman -S binutils
$ yay -S nerd-fonts-ubuntu-mono
```

En caso de error:

```bash
$ sudo pacman -S ttf-dejavu ttf-liberation noto-fonts
```

## OS PROBER

Detectar otros SO desde el grub, como window

[Detectar otros sistemas operativos](<https://wiki.archlinux.org/title/GRUB_(Espa%C3%B1ol)#Detectar_otros_sistemas_operativos>)

```bash
$ sudo pacman -S os-prober
$ grub-mkconfig -o /boot/grub/grub.cfg
```

## Instalar un entorno de escritorio DE

Ver el DE actual:

```bash
$ echo $XDG_CURRENT_DESKTOP
```

- **XCFE**

  Usa Thunar como gestor de archivos

- **KDE Plasma**

  Activar el KDE login

  ```bash
  systemctl enable sddm
  ```

- **Mate**

- **GNOME**

- **Unity**

- **Cinamon**

## Actualizar el sistema

https://wiki.archlinux.org/title/System_maintenance_(Espa%C3%B1ol)

```bash
sudo pacman -S -Syu
```

Actualizar el firmware

```bash
yay -S wd719x-firmware aic94xx-firmware
```

# Aplicaciones

https://wiki.archlinux.org/title/List_of_applications_(Espa%C3%B1ol)

## Vscode

https://wiki.archlinux.org/title/Visual_Studio_Code

Instalación de vscode. Lanzamiento exclusivo de la marca Microsoft. `visual-studio-code-bin` almacena la configuración en `~/.config/Code/User/settings.json`

```bash
$ yay -S visual-studio-code-bin
```

- ### Fuente [JetBrains Mono](https://www.jetbrains.com/es-es/lp/mono/)

Descomprima la fuente en `/usr/share/fonts` para instalar fuentes en todo el sistema) y ejecute `fc-cache -f -v`. Reinicie su IDE. Vaya a la configuración del editor y coloque las fuentes 'JetBrains Mono'. Copie solo los directorios `/tff /webfont` `/variable`

Vaya al archivo de configuración de vscode y:

```c#
"editor.fontLigatures": true,
"editor.fontFamily": "'JetBrains Mono', UbuntuMono Nerd Font"
```

> Agregue `UbuntuMono Nerd Font` si ya lo tienes instalado [aqui](#fonts-for-the-so)

Mi archivo de configuración de vscode [aqui](./vscode/settings.json).Algunas configuraciones son copiadas del blog de este crack [aqui](https://medium.com/@liaogg/minimal-vscode-setup-for-maximized-productivity-part-1-19db1c54697).

- ### Tema Gruvbox Material | Dracula

- ### Iconos Material Icons

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

## Alacritty

https://alacritty.org/

```bash
sudo pacman -S alacritty
```

El archivo de configuración de alacritty `~/.config/alacritty/alacritty.yml`

Mi archivo de configuración [aquí](./alacritty/). Es necesario instalar las fuentes [**UbuntuMono Nerd Font**](#fonts-for-the-so) ya que el archivo las pide.

## Google Chrome

https://aur.archlinux.org/packages/google-chrome

```bash
$ yay -S google-chrome
$ google-chrome-stable
```

## Micro

Editor de terminal

```bash
$ yay -S micro
$ micro
```

- Ctrl + E para escribir comandos
- Ctrl + G para sacar el help
- Ctrl + Q para salir

# Crea tu propio DE

# QTile

http://www.qtile.org/

El archivo de configuración de Qtile `~/.config/qtile/config.py`

Mi archivo de configuración de Qtile [aquí](./qtile/)

Mi configuración solicita que se instalen ciertos programas:

- [Fonts](#fonts-for-the-so) (usadas en os widgets de Qtile)

### El .xsession
