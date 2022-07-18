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
  - [Instalación de software](#instalación-de-software)
    - [AUR](#aur)
    - [Pacman](#pacman)
    - [Curl](#curl)
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
  - [Nano](#nano)
  - [Neovim](#neovim)
- [Crea tu propio DE](#crea-tu-propio-de)
  - [Instalar un login manager](#instalar-un-login-manager)
  - [Instalar un gestor de ventanas](#instalar-un-gestor-de-ventanas)
    - [Qtile](#qtile)
    - [Instalación de Qtile](#instalación-de-qtile)

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
`lsblk -f`

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

Seleccionar servidores para las descargas de programas.

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

[Usuarios y grupos](<https://wiki.archlinux.org/title/Users_and_groups_(Espa%C3%B1ol)>)

[Su](<https://wiki.archlinux.org/title/Su_(Espa%C3%B1ol)>)

[Sudo](<https://wiki.archlinux.org/title/Sudo_(Espa%C3%B1ol)>)

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

Habilitar la cuenta de superuser y asignarle una contraseña Esto para distros como Ubuntu ya que alli viene deshabilitada:

```bash
$ sudo passwd root
```

miclave: supercarlos

## Apagar

`shutdown now`

Desconecte el USB

# Configuración

## Hostname

Nombre del equipo

https://wiki.archlinux.org/title/Network_configuration#Set_the_hostname

## Distribución de teclado

```bash
setxkbmap es
```

Los cambios no son permanentes por los que se deben agragar al archivo `.xsession`

## Abrir otra terminal

Ctrl + Alt +F2

## Instalación de software

### AUR

En arch se instala sotware con el gestor de paquetes `pacman` pero si el paquete que queremos descargar no se encuentra allí usamos [aur](<https://wiki.archlinux.org/title/Arch_User_Repository_(Espa%C3%B1ol)>).

Para usar debemos instalar `yay`, un ayudante de aur:

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

[Más de yay](https://tecnoysoft.com/es/instalacion-y-uso-basico-de-yay/)

### Pacman

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

### Curl

```bash
$ sudo su
$ sudo pacman -S curl
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

De xorg deriva el diseño del teclado (**setxkbmap es**) , el compositor de imágenes (**Picom**) y el menu (**rofi**)

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

## Micro

Editor de terminal

```bash
$ yay -S micro
$ micro
```

## Nano

https://wiki.archlinux.org/title/Nano_(Espa%C3%B1ol)

Editor de terminal

```bash
sudo pacman -S nano
```

- Ctrl + E para escribir comandos
- Ctrl + G para sacar el help
- Ctrl + Q para salir

## Neovim

https://wiki.archlinux.org/title/Neovim_(Espa%C3%B1ol)

Editor de terminal

```bash
$ sudo pacman -S nvim
$ nvim
```

[Guia de nvim](https://platzi.com/blog/guia-definitiva-para-vim-y-neovim-instalacion-comandos-y-trucos/)

[Buscar y reemplazar](https://atareao.es/tutorial/vim/buscar-y-reemplazar-en-vim/#:~:text=Para%20realizar%20una%20b%C3%BAsqueda%20en,aparecer%C3%A1n%20todas%20las%20coincidencias%20resaltadas.)

## Rofi

https://wiki.archlinux.org/title/Rofi

```bash
$ sudo pacman -S rofi
```

Temas de rofi

```bash
$ sudo pacman -S sed
$ sudo pacman -S which
```

Seleccionar los temas

```bash
rofi-theme-selector
```

## Detectar android

https://wiki.archlinux.org/title/Media_Transfer_Protocol

```bash
$ sudo pacman -S mtpfs
$ sudo pacman -S gvfs-mtp
$ sudo pacman -S gvfs-gphoto2
```

## Audio

[Pulseaudio](https://wiki.archlinux.org/title/PulseAudio)

```bash
$ sudo pacman -S pulseaudio
```

Instalar un frontend

```bash
$ sudo pacman -S pavucontrol
```

Para que funcionen las teclas de volumen:

```bash
sudo pacman -S pactl
```

Para que funcionen las teclas de brillo:

```bash
sudo pacman -S brightnessctl
```

## Polkit

https://wiki.archlinux.org/title/Polkit

```bash
$ sudo pacman -S polkit
$ yay -S xfce-polkit
```

Interfaz grafica de policykit

```bash
$ yay -S polkit-explorer-git
$ polkitex
```

Iniciar `xfce-polkit` en el .xsession

### Dar permisos a gparted (hago esto porque en mi equipo solo hay un usuario)

```bash
$ nvim /usr/share/polkit-1/actions
```

Ir al archivo policy del gparted `org.gnome.gparted.policy`. Modificar el `<allow_any>, <allow_inactive>, <allow_active>` de `auth_admin` por `yes`

## Xsession

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

Mi archivo de configuración [aquí](./alacritty/). Es necesario instalar las fuentes [**UbuntuMono Nerd Font**](#fuentes-del-so) ya que el archivo las pide.

## Google Chrome

https://aur.archlinux.org/packages/google-chrome

```bash
$ yay -S google-chrome
$ google-chrome-stable
```

## Thunar

```bash
sudo pacman -S thunar
```

## Feh

[Arch Wiki](<https://wiki.archlinux.org/title/Feh_(Espa%C3%B1ol)>)

[Documentación oficial](https://man.finalrewind.org/1/feh/)

Visor de imagenes manejado por terminal. Se puede utilizar para establecer el fondo de pantalla.

```bash
$ sudo pacman -S
$ feh --bg-scale Downloads/wallpaper.png
```

Los cambios no son permanentes por los que se deben agragar al archivo `.xsession`

## Mirage

Visor de imagenes de interfaz gŕafica. Viene con previsualizador de miniaturas.

```bash
yay -S mirage
```

## Typora

Editor de markdown

```bash
$ sudo snap install typora
$ typora
```

## Firefox

```bash
sudo pacman -S firefox
```

## Brave

```bash
yay -S brave-bin
```

## Virtual Box

Maquina virtual. Instalar un SO dentro de nuestro SO

[Leer](<https://wiki.archlinux.org/title/VirtualBox_(Espa%C3%B1ol)#Pasos_para_preparar_Arch_Linux_como_sistema_anfitri%C3%B3n>)

```bash
sudo pacman -S virtualbox
```

Para usar virtualbox activar la virtualizacion desde la BIOS.

- Nuevo. En nombre poner el nombre del SO
- Crear un Disco virtual ahora tipo Virtual Box Disk Imagess
- Reservado dinamicamente
- Elegir el tamaño del disco duro virtual
- Antes de iniciar la maquina virtual ir a configuracion / Sistema / Procesador. SI tenes varios nucleos asignarselos para que funcione un poco mas fluido.
- Luego a Pantalla y asignarle toda la memoria de video
- Iniciar y seleccionar la imagen ISO
- Al iniciar el So cambiar la resolucion

Mas recursos:

https://www.youtube.com/watch?v=KEJros9bYkg

https://denovatoanovato.net/instalar-virtualbox-en-archlinux/

## Wine

Los programas de wine se instalan en el directorio `~/.wine`

https://wiki.archlinux.org/title/wine

Habilitar [multilib](https://wiki.archlinux.org/title/Official_repositories#multilib)

```bash
sudo pacman -S wine-gecko
sudo pacman -S wine-mono
sudo pacman -S wine
```

```bash
$ winecgf
$ regedir
$ wine control
```

Ejecutar un .exe

```bash
wine paquete.exe
```

Desintalar programas

```bash
wine uninstaller
```

Programas con wine:

- HWInfo

## Gparted

Editor de particiones

```bash
$ sudo pacman -S gparted
$ sudo gparted
```

## Visor de PDF

```bash
sudo pacman -S epdfview
```

[Redimensaionar particiones](https://thelinuxforce.wordpress.com/2012/03/24/redimensionar-particiones-home-y-raiz-entre-otras-con-gparted/). En la parte de de 'Espacio libre a continuacion (MB) es donde se va indicar el nuevo espacio que se va crear '

[Guía de usuario](https://wiki.winehq.org/Wine_User%27s_Guide#Using_Wine)

# Crea tu propio DE

- Todo personalizado
- Gestor de ventana tipo tiling permitiendo cambiar entre ventanas usando el teclado
- Gestor de archivos basado en terminal
- Sin programas inutiles
- Consume pocos recursos
- Mucho rendimiento
- Guarda tus configuraciones en github

## Instalar un Display manager (Gestor de pantalla)

Administrador de visualizacón o administrador de inicio de sesión

[systemd](https://wiki.archlinux.org/title/Systemd#Basic_systemctl_usage)

[Display manager arch](https://wiki.archlinux.org/title/Display_manager#Loading_the_display_manager)

[Ligthdm arh](https://wiki.archlinux.org/title/LightDM)

```bash
$ sudo pacman -S lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings
$ systemctl enable lightdm
```

Para personalizar el gestor de pantalla instalado abrir el archivo con el nombre del gestor de pantalla instalado. En el caso de `ligthdm-gtk-greeter` abrir `sudo lightdm-gtk-greeter-settings`

Si tienes otro gestor de pantalla primero desactivas ese y luego activas el nuevo:

```bash
$ systemctl disable sdm
```

Para que el cambio surja efecto ir al archivo: `/etc/lightdm/lightdm.conf` y colocar el lightdm instalado en esta linea. Descomentar esa linea

```bash
$ greeter-session = lightdm-gtk-greeter
```

[Personalizar lightdm](https://geekland.eu/personalizar-y-configurar-lightdm/)

[Iniciar sesion como root](https://atareao.es/como/crear-una-entrada-para-acceder-como-root-en-ubuntu-con-lightdm/)

## Instalar un gestor de ventanas

En `/usr/share/xsessions` podemos ver los gestores de ventanas instalados

## Qtile

http://www.qtile.org/

[Documentación](http://docs.qtile.org/en/stable/)

## Instalación de Qtile

```bash
sudo pacman -S qtile
```

El archivo de configuración de Qtile `~/.config/qtile/config.py`

## Configuración de Qtile

Instalar la terminal de Qtile

```bash
sudo pacman -S xterm
```

Mi directorio de configuración de Qtile [aquí](./qtile/)

Mi configuración solicita que se instalen ciertos programas:

- [Fonts](#fuentes-del-so) (usadas en os widgets de Qtile)

- [Rofi](#rofi)

### Mis atajos de teclado

| Tecla    | Función                |
| :------- | :--------------------- |
| Ctrl + B | Navegador              |
| Ctrl + E | Explorador de archivos |
| Ctrl + L | Alacritty              |
| Lemon    | 1$                     |

# Instalacion de android como dual boot en Arch

[Util](https://rootsudo.wordpress.com/2014/03/22/instalar-android-en-pc-y-arrancar-desde-grub2/comment-page-1/)

[Video Detallado](https://www.youtube.com/watch?v=q4gtgVICQ6g)
