import os
import nbformat as nbf
import subprocess


def run_git(cmd):
    for i in cmd:
        cmd_result = subprocess.run(i, capture_output=True, text=True, shell=True)

    if cmd_result.returncode == 0:
        print("Git command run succesfully")
        print("Sortie de la commande :")
        print(cmd_result.stdout)
    else:
        print("Git command run with error")        
        print(cmd_result.stderr)

def write_notebook(file_name:str, source_code:str):
    notebook = nbf.v4.new_notebook()

    code = nbf.v4.new_code_cell(source=source_code)
    notebook['cells'].append(code)
    nbf.write(notebook, file_name)


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

python_code="""import os

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
   create_rooted_file()"""



myfolders = [
              {"folder":{"name":"data", "subfolder":["cleaned", "processed", "raw"]}},
              {"folder":{"name":"docs"}}, 
              {"folder":{"name":"LICENCE"}},
              {"folder":{"name":"Makeifle"}},
              {"folder":{"name":"models"}},
              {"folder":{"name":"notebooks","file":["main.ipynb"]}}, 
              {"folder":{"name":"reports"}},
              {"folder":{"name":"src","file":["utils.py","process.py","train.py"]}}
                    ]
myfiles = ['README_.md','requirement.txt']

if __name__=="__main__":
    make_tree()
    create_rooted_file()
    make_file("src/utils.py", python_code)
    write_notebook("notebooks/main_notebook.ipynb", python_code)
    run_git(['git init'])
