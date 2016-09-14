#!/bin/bash
echo "Content-type: text/html"

echo ""
echo "Welcome"
echo ""

saveIFS=$IFS
IFS="=&"
parm=($QUERY_STRING)
IFS=$saveIFS

echo ${parm[1]}

echo "<html><head><link rel="stylesheet" type="text/css"href="style.css"><title>Time</title></head>"
echo "<body id="background-color">"
echo "<div id="wrap">"
echo "    <div id="left_col">"
echo " <h1>Time</h1>"
date
echo "    </div>"
echo "   <div id="right_col">"

echo "<object  data="http://www.web-source.net" width="100%" height="100%">"
echo "    <embed src="http://www.web-source.net" width="100%" height="100%"> </embed>"
 echo "   Error: Embedded data could not be displayed."
echo "</object>"

echo "    </div>"
echo "</div>"
echo "</body></html>"
exit 0
