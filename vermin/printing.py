def nprint(msg, config):
  if not config.quiet():
    print(msg)

def verbose_print(msg, level, config):
  if config.verbose() >= level and not config.quiet():
    print(msg)

def vprint(msg, config):
  verbose_print(msg, 1, config)

def vvprint(msg, config):
  verbose_print(msg, 2, config)
