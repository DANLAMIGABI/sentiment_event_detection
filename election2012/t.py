# approach 1: pattern for "generic smiley"
import re
eyes, noses, mouths = r":;8BX=", r"-~'^", r")(/\|DP"
pattern1 = "[%s][%s]?[%s]" % tuple(map(re.escape, [eyes, noses, mouths]))

# approach 2: disjunction of a list of smileys
smileys = """:-) :) :o) :] :3 :c) :> =] 8) =) :} :^) 
             :D 8-D 8D x-D xD X-D XD =-D =D =-3 =3 B^D""".split()
pattern2 = "|".join(map(re.escape, smileys))

text = "bla bla bla :-/ more text8^P and another smiley =-D even more text"
print (re.findall(pattern1, text))
