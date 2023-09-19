import os

def make_folder(name: str):
    os.mkdir(name)

def make_file(name: str, content=""):
    fd = os.open(name, os.O_RDWR|os.O_CREAT)
    os.write(fd, content.encode())

def create_rooted_file():
     for file in myfiles:
        make_file(file)

def make_tree():
     for i in range(len(myfolders)):
        make_folder(myfolders[i]['folder']["name"])
        try:
            for k in myfolders[i]['folder']["subfolder"]:
                make_folder(os.path.join(myfolders[i]['folder']["name"], k))
        except:
            try:
                for file in myfolders[i]['folder']["file"]:
                    make_file(os.path.join(myfolders[i]['folder']["name"], file))
            except:
                continue

myfolders = [
              {"folder":{"name":"data", "subfolder":["cleaned", "processed", "raw"]}},
              {"folder":{"name":"docs"}}, 
              {"folder":{"name":"LICENCE"}},
              {"folder":{"name":"Makeifle"}},
              {"folder":{"name":"models"}},
              {"folder":{"name":"notebooks","file":["main.ipynb"]}}, 
              {"folder":{"name":"reports"}},
              {"folder":{"name":"src","file":["utils.y","process.py","train.py"]}}
                    ]
myfiles = ['README_.md','requirement.txt']
if __name__=="__main__":
   make_tree()
   create_rooted_file()