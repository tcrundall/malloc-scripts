#!/usr/bin/env python

strUsers = 'rpulley  ,    jsmith, svai,   jsatriani     ,ymalmsteen   '
arrUsers = strUsers.split(',')

for user in arrUsers:
	trimUser = user.strip()
	trimUserR = user.strip()
	trimUserL = user.lstrip()

	firstInitial =trimUser[:1]
	lastInitial = trimUser[1:2]
	lastName = trimUser[1:]

	print 'User : \'' + user + '\''
	print 'LTrim: \'' + trimUserL + '\''
	print 'RTrim: \'' + trimUserR + '\''
	print ' Trim: \'' + trimUser + '\''

	print 'First Initial:', firstInitial.upper()
	print 'Last Initial: ', lastInitial.upper()
	print 'Last Name:', lastName

	print ''
