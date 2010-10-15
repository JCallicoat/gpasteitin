#!/usr/bin/env python

import os, glob, sys
from distutils.core import setup
<<<<<<< local
import version
=======
# from gpasteitin import gpasteitin
>>>>>>> other

dfiles     = (["resources/gpasteitin.ui"])
scripts    = [os.path.join("scripts", "gpasteitin")]
data_files = [("/usr/share/gpasteitin", dfiles),
              ("/usr/share/pixmaps", ["resources/gpasteitin.png"]),
              ("/usr/share/applications", ["resources/gpasteitin.desktop"])]

setup(name             = "GPasteItIn",
<<<<<<< local
      version          = version.__VERSION__,
=======
#       version          = gpasteitin.__VERSION__,
      version          = "0.7.4",
>>>>>>> other
      description      = "Simple snippet / paste tool for GTK+",
      long_description = "Simple snippet / paste tool for GTK+",
      author           = "Jordan Callicoat",
      author_email     = "jordan.callicoat@rackspace.com",
      url              = "",
      download_url     = "",
      license          = "BSD",
      platforms        = ["POSIX", "OS X", "Windows"],
      keywords         = [],
      packages         = ["gpasteitin"],
      scripts          = scripts,
      data_files       = data_files,
      )
