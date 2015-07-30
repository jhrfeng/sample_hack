#-- encoding:utf-8 --
import win32api

def exe1():
	win32api.ShellExecute(0, 'open', 'QQ furl', '', '', 1)

def exe2():
	win32api.ShellExecute(0, 'open', 'mp3file url', '', '', 1)

exeShell = {"1":exe1, "2":exe2}

print "--------------******----------\n"
print "1: QQ        2: xxx.mp3"
print "--------------******----------\n"

option = -1

while str(option) != 'exit':
    option = raw_input("«Î ‰»Î—°‘ÒœÓ£∫")
    exeShell.get(option)()
	
else:
	print "ending......"
