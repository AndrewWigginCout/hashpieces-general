import hashlib
import os
import json

def hash_dir(root):
    rv=[]
    for path,dirs,files in os.walk(root):
        for file in files:
            if os.path.splitext(file)[1]==".py": continue
            fullpath=os.path.join(path,file)
            leaf=fullpath[len(root):]
            if leaf[0]=="/" or leaf[0]=="\\":
                leaf=leaf[1:]
            rv.append((leaf,hash_pieces(fullpath)))
    return rv
def hash_pieces(file):
    handle = open(file,'rb')
    v=[]
    chsize=2**19
    while (s := handle.read(chsize)):
        m = hashlib.sha1()
        m.update(s)
        v.append( m.hexdigest() )
    handle.close()
    return v
def write_pretty(j,fn):
    with open(fn, "w") as write_file:
        json.dump(j, write_file, indent=2)

cwd=os.getcwd()
bigv=hash_dir(cwd)
write_pretty(bigv,os.path.join(cwd,"sha1hashes.txt"))
