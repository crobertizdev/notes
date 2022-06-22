from libqtile.config import Key
from libqtile.command import lazy

# Keybindings

# Tecla Window
mod = "mod4"

keys = [
    # ------------ Window Configs ------------

    # Change window sizes (MonadTall)
    Key([mod, "control"], "l", lazy.layout.grow()),
    Key([mod, "control"], "h", lazy.layout.shrink()),

    # Moves focus to the next window
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Use previous layout on the actual group
    Key([mod, "shift"], "Tab", lazy.prev_layout()),

    # Toggle floating
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Kill window
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),

    # Shutdown Qtile
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Toggle between split and unsplit sides of stack
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # ------------ App Configs ------------
    
    # Terminal
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show run")),

    # Window Nav
    Key([mod, 'shift'], "m", lazy.spawn("rofi -show")),

    # Browser
    Key([mod], "b", lazy.spawn("google-chrome-stable")),

    # Explorer
    Key([mod], "e", lazy.spawn("thunar")),
    # Key([mod], "e", lazy.spawn("pcmanfm")),

    # Captura de pantalla
    Key([], "KP_Delete", lazy.spawn("xfce4-screenshooter -r")),

    # Redshift
    Key([mod], "r", lazy.spawn("redshift -O 2400")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Switch focus of monitors
    # Key([mod], "period", lazy.next_screen()),
    # Key([mod], "comma", lazy.prev_screen()),

    # ------------ Hardware Configs ------------

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    # Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    # Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]