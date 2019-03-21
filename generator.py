#--------------------------------------------------
#---COLORS-----------------------------------------
#--------------------------------------------------

file = open("colors.less", "w+")
colors = [
	('red', '#FF4956'),
	('orange', '#FFA768'),
	('yellow', '#FFD77C'),
	('green', '#58DD6A'),
	('blue', '#4C73FF'),
	('purple', '#BB4FFF'),
	('pink', '#F282FF'),
	('brown', '#B26945'),
	('black', '#000000'),
	('white', '#FFFFFF')
]

file.write("@darkamount:15%;\n")
file.write("@lightamount:10%;\n")
file.write("\n")


# Couleurs 
for color in colors :
	file.write('@'+color[0]+'_light:lighten('+color[1]+', @lightamount);\n')
file.write('\n')

for color in colors :
	file.write('@'+color[0]+':'+color[1]+';\n')
file.write('\n')

for color in colors :
	file.write('@'+color[0]+'_dark:darken('+color[1]+', @darkamount);\n')
file.write('\n')

# Classes fond
for color in colors :
	file.write('.'+color[0]+'-light { background-color:@'+color[0]+'_light; }\n')
file.write('\n')

for color in colors :
	file.write('.'+color[0]+' { background-color:@'+color[0]+'; }\n')
file.write('\n')

for color in colors :
	file.write('.'+color[0]+'-dark { background-color:@'+color[0]+'_dark; }\n')
file.write('\n')


# Classes texte
for color in colors :
	file.write('.'+color[0]+'-light-t { color:@'+color[0]+'_light; }\n')
file.write('\n')

for color in colors :
	file.write('.'+color[0]+'-t { color:@'+color[0]+'; }\n')
file.write('\n')

for color in colors :
	file.write('.'+color[0]+'-dark-t { color:@'+color[0]+'_dark; }\n')
file.write('\n')


# Classes fond:hover
for color in colors :
	file.write('.'+color[0]+'-light-h { &:hover { background-color:@'+color[0]+'_light; } }\n')
file.write('\n')

for color in colors :
	file.write('.'+color[0]+'-h { &:hover { background-color:@'+color[0]+'; } }\n')
file.write('\n')

for color in colors :
	file.write('.'+color[0]+'-dark-h { &:hover { background-color:@'+color[0]+'_dark; } }\n')
file.write('\n')


# Classes texte:hover
for color in colors :
	file.write('.'+color[0]+'-light-t-h { &:hover { color:@'+color[0]+'_light; } }\n')
file.write('\n')

for color in colors :
	file.write('.'+color[0]+'-t-h { &:hover { color:@'+color[0]+'; } }\n')
file.write('\n')

for color in colors :
	file.write('.'+color[0]+'-dark-t-h { &:hover { color:@'+color[0]+'_dark; } }\n')
file.write('\n')

# Classes fond:darker
for color in colors :
	file.write('.'+color[0]+'-light-d { background-color:@'+color[0]+'_light; &:hover { background-color:@'+color[0]+'; } }\n')
file.write('\n')

for color in colors :
	file.write('.'+color[0]+'-d { background-color:@'+color[0]+'; &:hover { background-color:@'+color[0]+'_dark; } }\n')
file.write('\n')


file.close()

#---------------------
#--COLUMNS------------
#---------------------

file = open('columns_more.less', 'w+')

posvars = [
	('-s', '@pos-1'),
	('-S', '@pos-2'),
	('-m', '@pos-3'),
	('-M', '@pos-4'),
	('-l', '@pos-5'),
	('-L', '@pos-6')
]

file.write(".row { display:flex; flex-wrap:wrap; }\n")

for x in [('t', 'start'), ('b', 'end'), ('c', 'center')] :
	for y in [('l', 'start'), ('r', 'end'), ('c', 'center')] :
		file.write(".row-"+x[0]+"-"+y[0]+" { .row(); justify-content:"+y[1]+"; align-items:"+x[1]+"; }\n")
	file.write("\n")
file.write("\n")

file.write(".column { display:flex; flex-wrap:wrap; flex-direction:column; }\n")

for x in [('t', 'start'), ('b', 'end'), ('c', 'center')] :
	for y in [('l', 'start'), ('r', 'end'), ('c', 'center')] :
		file.write(".column-"+x[0]+"-"+y[0]+" { .column(); align-items:"+y[1]+"; justify-content:"+x[1]+"; }\n")
	file.write("\n")
file.write("\n")


for s in posvars :
	file.write(".space"+s[0]+" { & > * { .m("+s[1]+"/2); } }\n")

for opt in [('h', 'l', 'r'), ('v', 't', 'b')] :
	for s in posvars :
		file.write(".space-"+opt[0]+s[0]+" { & > * { .m-"+opt[1]+"("+s[1]+"/2); .m-"+opt[2]+"("+s[1]+"/2); } }\n")

for p in [('w', 'width'), ('h', 'height')] :
	for a in [('', ''), ('M', 'max-'), ('m', 'min-')] :
		for i in range(50, 1001, 50) :
			file.write('.'+a[0]+p[0]+str(i)+' { '+a[1]+p[1]+':'+str(i)+'px; }\n')
		for i in range(5, 101, 5) :
			file.write('.'+a[0]+p[0]+str(i)+'p { '+a[1]+p[1]+':'+str(i)+'%; }\n')
		file.write('\n')
	file.write('\n')
file.write('\n');

file.close()

file = open('general_more.less', 'w+')

for p in [('p', 'padding'), ('m', 'margin')] :
	file.write('//\n// '+p[1]+'\n//\n')
	for s in ['', '-l', '-t', '-r', '-b'] :
		for w in posvars :
			file.write('.'+p[1]+s+w[0]+' { .'+p[0]+s+'('+w[1]+'); }\n')
		file.write('\n');
	file.write('\n');
file.write('\n');

fontvars = [
	('-s', '@font-1'),
	('-S', '@font-2'),
	('-m', '@font-3'),
	('-M', '@font-4'),
	('-l', '@font-5'),
	('-L', '@font-6')
]

file.write('//\n// fonts\n//\n')
for w in fontvars :
	file.write(".font"+w[0]+' { font-size:'+w[1]+'; }\n')
file.write('\n');

file.close()