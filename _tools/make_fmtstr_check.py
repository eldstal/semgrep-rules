#!/usr/bin/env python3
#
# Generates semgrep rules to look for custom printf style functions,
# called with a non-constant format string
#
# Input is a JSON with known functions:
#
# {
#    functions : {  "1": [ "printf" ],
#                   "2": [ "dprintf" ]
#                },
#    exceptions : [ "\"...\"", "UNQUOTE(\"...\")" ]
# }
#
# Functions 1 have the format string as the first parameter
# Functions 2 have the format string as the second parameter, etc.
# Exceptions are values (semgrep syntax) which should not be matched
# such as known patterns or commonly used macros and such.
# If no exceptions are specified, only "..." is used, i.e. "Don't match if the
# format string is a string literal".
#
# The above will generate the following ruleset:
# 
#  pattern-either:
#  - patterns:
#    - pattern: printf(...)
#    - pattern-not: printf("...",...)
#    - pattern-not: printf(UNQUOTE("..."),...)
#  - patterns:
#    - pattern: dprintf(...)
#    - pattern-not: dprintf($A,"...",...)
#    - pattern-not: dprintf($B,UNQUOTE("..."),...)

import json
import sys


def main():
  if len(sys.argv) < 2:
    sys.stderr.write("make_fmtstr_check.py <functions.json>\n")
    return 1

  print("  pattern-either:")

  for t in sys.argv[1:]:
    template = json.load(open(t, "r"))

    if "functions" not in template:
      sys.stderr.write(f"There are no functions in the template JSON file {t}.")
      continue

    if "exceptions" not in template:
      sys.stderr.write(f"There are no exceptions in the template JSON file {t}. Defaulting to \"...\"\n")
      template["exceptions"] = [ "\"...\"" ]


    for k, func_names in template["functions"].items():
      arg_pos = int(k)
      if arg_pos is None or arg_pos < 1:
        sys.stderr.write(f"Unexpected key {k} in functions. Ignoring.\n")
        continue
      #print(f"Functions with format string as arg {arg_pos}: {str(func_names)}")
      placeholders = [ f"$ARG{n+1}" for n in range(arg_pos-1) ]
      initial_args = ",".join(placeholders)
      if len(placeholders) > 0:
        initial_args = initial_args + ","

      for func in func_names:
        print("  - patterns:")
        print(f"    - pattern: {func}(...)")
        for e in template["exceptions"]:
          print(f"    - pattern-not: {func}({initial_args}{e},...)")





if __name__ == "__main__":
  sys.exit(main())

