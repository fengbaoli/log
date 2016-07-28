import os
def gencounts(configfile):
    file = open(configfile)
    for t in file.readlines():
        contents = t.strip().split(':')
        filepath=contents[0]
        filename=contents[1]
        counts ="new"+filename
        tmpconffile= open("tmpconf.txt","a")
        newcontents=filepath+":"+filename+":"+counts+"\n"
        tmpconffile.write(newcontents)
        tmpconffile.close()
    file.close()
    os.remove(configfile)
    os.renames('tmpconf.txt',configfile)
gencounts("conf.txt")
