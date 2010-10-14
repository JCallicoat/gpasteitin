#!/usr/bin/env python

import os, glob
from distutils.core import setup
# from gpasteitin import gpasteitin

dfiles     = (["resources/gpasteitin.ui"])
scripts    = [os.path.join("scripts", "gpasteitin")]
data_files = [("/usr/share/gpasteitin", dfiles),
              ("/usr/share/pixmaps", ["resources/gpasteitin.png"]),
              ("/usr/share/applications", ["resources/gpasteitin.desktop"])]

setup(name             = "GPasteItIn",
#       version          = gpasteitin.__VERSION__,
      version          = "0.7.4",
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
