import sys

qwerty = "qwertyuiopasdfghjkl;zxcvbnm,./"
engram = "byou';ldwvciea,.htsngxjk-/rmfp"   

q2e = dict(zip(qwerty,engram))

line = sys.argv[1].strip()
print("".join([q2e.get(c, c) for c in line]))