import os
import sys

def format_alias_dir(path, alias, level=1):
    print "LEVEL                    =", level
    path  = str(path).split("\\")
    path_join = "\\".join(path[level:])
    alias = str(alias).split("\\")
    print "PATH                     =", path_join
    print "ALIAS                    =", alias
    if "\\" in alias[-1]:
        alias_join = "\\".join(alias)
        print "ALIAS JOIN               =", alias_join
    else:
        alias_join = alias_join = "\\".join(alias) + '\\'
        print "ALIAS JOIN               =", alias_join
    result = os.path.join(alias_join, path_join)
    if os.path.isdir(result):
        return result
    else:
        return False
    print "RESULT                   =", result
    
path = r'i:\160G Msc\MUSIC\INSTRUMENTAL\BAND\HELLOWEEN - DISCOGRAPHY\2015 - My God-Given Right (Deluxe Edition)'
alias = 'M:'
format_alias_dir(path, alias, int(sys.argv[1]))