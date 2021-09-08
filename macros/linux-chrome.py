# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Chrome', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.COMMAND, '[']),
        (0x004000, 'Fwd >', [Keycode.COMMAND, ']']),
        (0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x202000, '< Tab', [Keycode.COMMAND, '[']),
        (0x202000, 'Tab >', [Keycode.COMMAND, ']']),
        (0x400000, 'Down', [Keycode.SPACEBAR]),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', [Keycode.COMMAND, 'r']),
        (0x000040, 'New Tab', [Keycode.COMMAND, 't']),
        (0x000040, 'Incog', [Keycode.COMMAND, Keycode.SHIFT, 'n']),
        # 4th row ----------
        (0x101010, 'GCP', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                           'https://console.cloud.google.com/\n']),   # GCP Console in a new tab
        (0x000040, 'Windows', [Keycode.F12]),    # dev mode
        (0x101010, 'AWS', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                             'https://console.aws.amazon.com/\n']), # AWS Console in a new tab
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
