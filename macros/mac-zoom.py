# MACROPAD Hotkeys: ZOOM

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'ZOOM', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400000, 'Camera', [Keycode.COMMAND, Keycode.SHIFT, 'V']),
        (0x000000, '', [Keycode.SHIFT, Keycode.COMMAND, 'n']),
        (0x004000, 'Switch Cam', [Keycode.COMMAND, Keycode.SHIFT, 'N']),
        # 2nd row ----------
        (0x004000, 'Scrn Share', [Keycode.COMMAND, Keycode.SHIFT, 'S']),
        (0x000000, '', [Keycode.OPTION, Keycode.COMMAND, 'f']),
        (0x000000, '', [Keycode.CONTROL, Keycode.COMMAND, ' ']),
        # 3rd row ----------
        (0x004000, 'Hand', [Keycode.OPTION, 'y']),
        (0x000000, '', [Keycode.SHIFT, Keycode.COMMAND, 'o']),
        (0x004000, 'Chat', [Keycode.SHIFT, Keycode.COMMAND, 'h']),
        # 4th row ----------
        (0x202000, 'PTT', [Keycode.SPACEBAR]),
        (0x000000, '', [Keycode.OPTION, Keycode.SHIFT, Keycode.COMMAND, 'D' ]),
        (0x202000, 'Mute', [Keycode.COMMAND, Keycode.SHIFT, 'A']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
