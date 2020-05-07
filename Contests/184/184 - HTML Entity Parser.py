def entityParser(text):
    return text.replace("&quot;", r'"').replace("&apos;", r"'").replace("&amp;", '&').replace("&gt;", '>').replace("&lt;", '<').replace( "&frasl;", r"/")

print(entityParser("x &gt; y &amp;&amp; x &lt; y is always false"))