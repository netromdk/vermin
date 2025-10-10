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

def sgr(msg, *codes):
  """Wrap message in ANSI Select Graphic Rendition codes for console styling."""
  codes = ";".join(str(c) for c in codes)
  return "\033[{}m{}\033[0m".format(codes, msg)
