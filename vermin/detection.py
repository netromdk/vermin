from stat import S_ISDIR, S_ISREG
from os import listdir, stat
from os.path import abspath, join, splitext
from multiprocessing import Pool, cpu_count

from .parser import Parser
from .source_visitor import SourceVisitor
from .config import Config

NOT_PY_CODE_EXTS = {
  "3dm",
  "3ds",
  "3g2",
  "3gp",
  "7z",
  "8svx",
  "DS_Store",
  "a",
  "aac",
  "ac",
  "adp",
  "aff",
  "ai",
  "aif",
  "aifc",
  "aiff",
  "aix",
  "alz",
  "am",
  "ape",
  "apk",
  "applescript",
  "ar",
  "arj",
  "as",
  "asf",
  "asm",
  "au",
  "avi",
  "bak",
  "baml",
  "bh",
  "bin",
  "bk",
  "bmp",
  "btif",
  "bz2",
  "bzip2",
  "c",
  "cab",
  "caf",
  "cat",
  "cc",
  "cdxml",
  "cfg",
  "cgm",
  "cl",
  "class",
  "cmx",
  "cnf",
  "coffee",
  "conf",
  "coverity",
  "cpio",
  "cpp",
  "cr2",
  "crt",
  "cs",
  "css",
  "css_t",
  "csv",
  "cur",
  "cxx",
  "d",
  "dart",
  "dat",
  "dcm",
  "deb",
  "dectest",
  "dex",
  "dic",
  "dict",
  "djvu",
  "dll",
  "dmg",
  "dng",
  "doc",
  "docm",
  "docx",
  "dot",
  "dotm",
  "dra",
  "dsk",
  "dsp",
  "dts",
  "dtshd",
  "dvb",
  "dwg",
  "dxf",
  "ebnf",
  "ecelp4800",
  "ecelp7470",
  "ecelp9600",
  "egg",
  "el",
  "elc",
  "eol",
  "eot",
  "epub",
  "epub",
  "erl",
  "es",
  "exe",
  "exr",
  "ext",
  "f",
  "f4v",
  "f90",
  "fasl",
  "fbs",
  "fh",
  "fla",
  "flac",
  "fli",
  "flv",
  "for",
  "fpx",
  "fs",
  "fsi",
  "fsscript",
  "fst",
  "fsx",
  "fvt",
  "g3",
  "gh",
  "gif",
  "go",
  "graffle",
  "gz",
  "gzip",
  "h",
  "h261",
  "h263",
  "h264",
  "hdr",
  "hdx",
  "hh",
  "hpp",
  "hrl",
  "hs",
  "html",
  "hxx",
  "i",
  "icns",
  "ico",
  "idl",
  "idx",
  "ief",
  "img",
  "ini",
  "ipa",
  "iso",
  "jar",
  "java",
  "jl",
  "jpeg",
  "jpg",
  "jpgv",
  "jpm",
  "js",
  "json",
  "jxr",
  "key",
  "key",
  "kt",
  "kts",
  "ktx",
  "l",
  "latex",
  "lha",
  "lhs",
  "lib",
  "lisp",
  "litcoffee",
  "lsp",
  "lua",
  "lvp",
  "lz",
  "lzh",
  "lzma",
  "lzo",
  "m",
  "m3u",
  "m4",
  "m4a",
  "m4v",
  "mak",
  "man",
  "mar",
  "md",
  "mdi",
  "mht",
  "mid",
  "midi",
  "mj2",
  "mka",
  "mkv",
  "ml",
  "mli",
  "mm",
  "mmr",
  "mng",
  "mobi",
  "mov",
  "movie",
  "mp3",
  "mp4",
  "mp4a",
  "mpeg",
  "mpg",
  "mpga",
  "mxu",
  "nasm",
  "nb",
  "nef",
  "nib",
  "npx",
  "nsi",
  "nsis",
  "numbers",
  "nupkg",
  "nuspec",
  "o",
  "oga",
  "ogg",
  "ogv",
  "otf",
  "pack",
  "pages",
  "pbm",
  "pcx",
  "pdb",
  "pdf",
  "pea",
  "pem",
  "pgm",
  "phar",
  "php",
  "php-s",
  "php3",
  "php4",
  "php5",
  "php7",
  "phps",
  "pht",
  "phtml",
  "pic",
  "pl",
  "plist",
  "pm",
  "png",
  "pnm",
  "pod",
  "pot",
  "potm",
  "potx",
  "ppa",
  "ppam",
  "ppm",
  "pps",
  "ppsm",
  "ppsx",
  "ppt",
  "pptm",
  "pptx",
  "pro",
  "proj",
  "ps",
  "ps1",
  "ps1xml",
  "psc1",
  "psd",
  "psd1",
  "psm1",
  "pssc",
  "pya",
  "pyc",
  "pyo",
  "pyv",
  "qt",
  "r",
  "rar",
  "ras",
  "raw",
  "rb",
  "rc",
  "rda",
  "rdata",
  "rds",
  "resources",
  "rgb",
  "rip",
  "rlc",
  "rlib",
  "rmf",
  "rmvb",
  "rs",
  "rst",
  "rtf",
  "rz",
  "s",
  "s3m",
  "s7z",
  "sccd",
  "scm",
  "scm",
  "scpt",
  "scpt",
  "scptd",
  "scss",
  "sgi",
  "shar",
  "sil",
  "sip",
  "sketch",
  "slk",
  "sln",
  "sml",
  "smv",
  "sndt",
  "snk",
  "so",
  "sql",
  "srl",
  "ss",
  "stl",
  "stp",
  "sub",
  "suo",
  "supp",
  "svg",
  "swf",
  "swift",
  "t",
  "tar",
  "tbc",
  "tbz",
  "tbz2",
  "tcl",
  "tex",
  "tga",
  "tgz",
  "thm",
  "thmx",
  "tif",
  "tiff",
  "tlz",
  "ttc",
  "ttf",
  "txt",
  "txz",
  "udf",
  "ui",
  "utf8",
  "uvh",
  "uvi",
  "uvm",
  "uvp",
  "uvs",
  "uvu",
  "valgrind",
  "vb",
  "vcxproj",
  "viv",
  "vob",
  "voc",
  "war",
  "wasm",
  "wat",
  "wav",
  "wax",
  "wbmp",
  "wdp",
  "weba",
  "webm",
  "webp",
  "whl",
  "wim",
  "wixproj",
  "wl",
  "wm",
  "wma",
  "wmv",
  "wmx",
  "woff",
  "woff2",
  "wpr",
  "wrm",
  "wvx",
  "wxl",
  "wxs",
  "xbm",
  "xhtml",
  "xif",
  "xla",
  "xlam",
  "xls",
  "xlsb",
  "xlsm",
  "xlsx",
  "xlt",
  "xltm",
  "xltx",
  "xm",
  "xmind",
  "xml",
  "xpi",
  "xpm",
  "xs",
  "xsl",
  "xwd",
  "xz",
  "yaml",
  "yml",
  "z",
  "zip",
  "zipx",
}

def probably_python_file(path):
  _, ext = splitext(path.lower())
  ext = ext[1:]

  # Always scan definite Python files.
  if ext in {"py", "py3", "pyw", "pyj", "pyi"}:
    return True

  # Skip all non-code Python files.
  if ext in {"pyc", "pyd", "pxd", "pyx", "pyo"} or ext in NOT_PY_CODE_EXTS:
    return False

  # Try opening file for reading as a text device.
  try:
    with open(path, mode="rt") as fp:
      for _i in range(10):
        # A script with a magic line might contain "python".
        line = fp.readline().lower().strip()
        if line.startswith("#!") and "python" in line:
          return True
  except Exception:
    # Not python if not readable text file.
    return False

  return False

# Called concurrently in an iterative fashion. Each invocation will return accepted paths and a list
# of further arguments tuples, if any.
def detect_paths_incremental(args):
  (paths, depth, hidden, ignore_chars) = args
  accepted = []
  further_args = []
  for path in paths:
    if any(ic in path for ic in ignore_chars):
      continue  # pragma: no cover
    if not hidden and path != "." and path[0] == ".":
      continue
    path = abspath(path)

    # Only invoke os.stat() once per path. Instead of twice via a call to isdir() and isfile()
    # that calls os.stat() internally.
    try:
      st = stat(path)
    except OSError:
      continue

    if S_ISDIR(st.st_mode):
      files = [join(path, p) for p in listdir(path) if hidden or p[0] != "."]
      further_args.append((files, depth + 1, hidden, ignore_chars))
    elif S_ISREG(st.st_mode) and (depth == 0 or probably_python_file(path)):
      accepted.append(path)
  return (accepted, further_args)

# Some detected paths might not be python code since not all files use extensions like ".py" and
# ".pyw", for instance. But try directly specified files on CLI, on depth 0, in any case (non-pyhton
# files will be ignored when trying to parse them). Paths containing chars in `ignore_chars` will be
# ignored.
def detect_paths(paths, hidden=False, processes=cpu_count(), ignore_chars=None):
  pool = Pool(processes=processes) if processes > 1 else None
  accept_paths = []
  depth = 0
  ignore_chars = ignore_chars or []
  args = [(paths, depth, hidden, ignore_chars)]

  # Automatically don't use concurrency when only one process is specified to be used.
  def act(args):
    if processes == 1:
      return [detect_paths_incremental(arg) for arg in args]  # pragma: no cover
    return pool.imap(detect_paths_incremental, args)

  while args:
    new_args = []
    for (acc, further_args) in act(args):
      if acc:
        accept_paths += acc
      if further_args:
        new_args += further_args
    args = new_args

  if pool:
    pool.close()
  return accept_paths

def visit(source, config=None, path=None):
  """Analyze source code and yield source code visitor instance which can be queried for further
information. A default config will be used if it isn't specified. If path is specified, it will
occur in errors instead of the default '<unknown>'.
  """
  if config is None:
    config = Config()

  parser = Parser(source, path)
  (node, mins, novermin) = parser.detect(config)
  if node is None:
    return mins

  visitor = SourceVisitor(config=config, path=path)
  visitor.set_no_lines(novermin)
  visitor.tour(node)

  # Ensure that minimum versions are calculatd such that `output_text()` invocations make sense.
  visitor.minimum_versions()

  return visitor

def detect(source, config=None, path=None):
  """Analyze and detect minimum versions from source code. A default config will be used if it isn't
  specified. If path is specified, it will occur in errors instead of the default '<unknown>'.
  """
  visitor = visit(source, config, path)
  if isinstance(visitor, SourceVisitor):
    return visitor.minimum_versions()
  return visitor
