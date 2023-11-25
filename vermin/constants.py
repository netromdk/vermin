from multiprocessing import cpu_count

VERSION = "1.6.0"
DEFAULT_PROCESSES = cpu_count()
CONFIG_FILE_NAMES = ["vermin.ini", "vermin.conf", ".vermin", "setup.cfg"]
CONFIG_SECTION = "vermin"

PROJECT_BOUNDARIES = [
  ".bzr",       # Bazaar
  ".fslckout",  # Fossil
  ".git",       # Git
  ".hg",        # Mercurial
  ".p4root",    # Perforce Helix Core
  ".pijul",     # Pijul
  ".svn",       # Subversion
  "_darcs",     # Darcs
]
