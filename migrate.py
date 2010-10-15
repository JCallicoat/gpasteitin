#!/usr/bin/python

import os

try:
    from configobj import ConfigObj
except:
    sys.exit ("This program requires python-configobj.")

try:
    from xdg import BaseDirectory
except ImportError:
    sys.exit ("This program requires python-xdg.")

template = {
    "profile" : "Default",
    "Default" : {
        "Options" : {
            "snip_color"    : "#0000FF",
            "clip_color"    : "#FF0000",
            "single_column" : False,
            "clip_size"     : 8,
            "wrap_width"    : 4,
            "initial_clip"  : True,
            "x"             : 0,
            "y"             : 0
        },
        "Snippets" : {}
    }
}

config_path = BaseDirectory.save_config_path ("gpasteitin")
config_file = os.path.join (config_path, "config")
config      = ConfigObj (config_file, write_empty_values = True)

try:
    config[config["profile"]]
except KeyError:
    config.merge (template)

    try:
        config["Default"]["Options"].merge (config["Options"])
        del config["Options"]
    except KeyError:
        pass

    try:
        config["Default"]["Snippets"].merge (config["Snippets"])
        del config["Snippets"]
    except KeyError:
        pass

    config.write ()

