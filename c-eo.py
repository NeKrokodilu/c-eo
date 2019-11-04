#!/usr/bin/env python3
import sys

location = sys.argv[1]
with open(location, "r") as dosiero:
    dosiero = dosiero.read().split("\n")
    for i in range(0, len(dosiero)-1):
        if dosiero[i].startswith("#difinu"):
            dosiero[i] = dosiero[i].replace("#difinu", "#define")
        elif dosiero[i].startswith("#inkluzivu"):
            dosiero[i] = dosiero[i].replace("#inkluzivu", "#include")
    with open("out.c", "w") as output:
        output.write("\n".join(dosiero))


