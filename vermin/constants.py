from multiprocessing import cpu_count

VERSION = "1.0.3"
DEFAULT_PROCESSES = cpu_count()
CONFIG_FILE_NAMES = ["vermin.ini", "vermin.conf"]
PROJECT_BOUNDARIES = [".git", ".svn", ".hg", ".bzr", "_darcs", ".fslckout"]
