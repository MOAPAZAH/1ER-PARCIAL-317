from multiprocessing import Process
def imprime(descripcion):
  hh = descripcion+""
  gg = "" 
  num = len(hh)+0
  for i in range(num):
    gg = hh[i]+gg
  if(hh==gg):
    print(hh+" = Es palindrome\n")
  else: 
      print(hh+" = No es palindrome\n")

if __name__=="__main__":
  nombres = ["juan","oto","moises", "victoria","ala","ana"]
  procesos=[] 
  for i in nombres:
    proc = Process(target=imprime, args=(i,))
    procesos.append(proc)
    proc.start()