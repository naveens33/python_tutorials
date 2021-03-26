# Text Wrap
import textwrap

text = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
wrap = textwrap.TextWrapper(4)
string = wrap.fill(text)
print(string)