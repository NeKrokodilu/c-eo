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
        elif dosiero[i].startswith("#maldif"):
            dosiero[i] = dosiero[i].replace("#maldif", "#undef")
        elif dosiero[i].startswith("#sedif"):
            dosiero[i] = dosiero[i].replace("#sedif", "#ifdef")
        elif dosiero[i].startswith("#sendif"):
            dosiero[i] = dosiero[i].replace("#sendif", "#ifndef")
        elif dosiero[i].startswith("#se"):
            dosiero[i] = dosiero[i].replace("#se", "#if")
        elif dosiero[i].startswith("#alie"):
            dosiero[i] = dosiero[i].replace("#alie", "#else")
        elif dosiero[i].startswith("#alse"):
            dosiero[i] = dosiero[i].replace("#alse", "#elif")
        elif dosiero[i].startswith("#findif"):
            dosiero[i] = dosiero[i].replace("#findif", "#endif")
        elif dosiero[i].startswith("#eraro"):
            dosiero[i] = dosiero[i].replace("#eraro", "#error")
        elif dosiero[i].startswith("#pragmato"):
            dosiero[i] = dosiero[i].replace("#pragmato", "#pragma")
    with open("out.c", "w") as output:
        output.write("\n".join(dosiero))
