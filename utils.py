from nglview import show_file
from pymol import cmd
tmpfile = "/tmp/current.cif"
def draw():
    cmd.save(tmpfile)
    return show_file(tmpfile)