
class F:
   def read(self, filename):
      # with = cierre automático
       with open(filename, "r",encoding= "utf-8") as f:
          for linea in f:
             print(linea.strip())

   def write(self,filename):
      with open(filename,"w",encoding="utf-8") as f:
         f.write("Encabezado\n")
         f.writelines(["linea 1\n","linea 2\n", "linea 3\n", "linea 4\n"])                

f = F()
f.read("note.txt")
f.write("note.txt")
