from multiprocessing import cpu_count

VERSION = "1.1.1"
DEFAULT_PROCESSES = cpu_count()
CONFIG_FILE_NAMES = ["vermin.ini", "vermin.conf", ".vermin", "setup.cfg"]
CONFIG_SECTION = "vermin"
PROJECT_BOUNDARIES = [".git", ".svn", ".hg", ".bzr", "_darcs", ".fslckout"]
