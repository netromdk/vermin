from .config import Config

def nprint(msg):
  if not Config.get().quiet():
    print(msg)

def verbose_print(msg, level):
  c = Config.get()
  if c.verbose() >= level and not c.quiet():
    print(msg)

def vprint(msg):
  verbose_print(msg, 1)

def vvprint(msg):
  verbose_print(msg, 2)
