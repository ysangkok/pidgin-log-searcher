#!/usr/bin/env python3
#from plaintext2html import plaintext2html
import datetime
import re
from io import StringIO
import sys
from urllib.parse import quote_plus
from binascii import crc32

redir=True

if redir:
	old_stdout = sys.stdout
	sys.stdout = mystdout = StringIO()

try:
	l = sys.stdin.buffer.read().split(b"\n")
	print("""
	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
            "http://www.w3.org/TR/html4/loose.dtd">
	<head>
	<title>Chat log listing</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<style type="text/css">
	body {
		padding:0;
		margin:1cm;
		margin-right:16cm;
		background-color: #eee;
	}
	#leftpane {
	}
	#rightpane {
		position:fixed;
		width: 15cm;
		height:100%;
		right:0;
		top:0;
	}
	.jumplink {
		cursor:pointer;
	}
	#ifrm {
		width: 100%;
		height: 100%;
	}
	</style>
	<script type="text/javascript">
	function jump(url) {
		document.getElementById("ifrm").setAttribute('src', url);
	}
	</script>
	</head>
	<body>
	<div id="rightpane">
	<iframe src='about:blank' id='ifrm'>
	</iframe>
	</div>
	<div id="leftpane">
	""")
	def repl(m):
	        return "\"" + m.group(1) + "\">"
	p = re.compile("'(font-family:[^>]*)'>")
	ts = None
	month = None
	day = None

	htmlstrip = re.compile(r'<.*?>')

	for j in l:
		i=j.decode()
		i=i.strip()
		if len(i)==0: continue
		parts = i.split(":")
		inp = ":".join(parts[2:])
		if htmlstrip.sub("", inp).find("=") == -1: continue

		x = parts[0].split(".")
		newts = x[:2]
		newmonth = x[0].split("-")[:2]
		newday = x[0].split("-")[2]
		if newts != ts:
			print("<hr>")
			ts = newts
		if newmonth != month:
			d = datetime.date(int(newmonth[0]), int(newmonth[1]), 1).strftime("%B %Y")
			print("<h2>{0}</h2>".format(d))
			month = newmonth
		if newday != day:
			print("<h4>{0}</h4>".format(newday))
			day = newday

		print("<span class='jumplink' onclick='javascript:jump(\"getfile.php?f={0}#n{1}\");'>".format(quote_plus(parts[0]),parts[1]))
		inp = inp.replace("<br/>","<br>")
		print(p.sub(repl,inp))
		print("</span>")
		

	print("""
	</div>
	</body>
	</html>
	""")
finally:
	if redir:
		f = open("index.htm","wb")
		f.write(mystdout.getvalue().encode())
