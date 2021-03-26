import html

text = "&amp;, &reg;, &lt;, &gt;, &cent;, &pound;, &yen;, &euro;, &sect;, &copy;"

print(html.unescape(text))

text ="Hello;s's"
text = html.escape(text)
print(text)
print(html.unescape(text))