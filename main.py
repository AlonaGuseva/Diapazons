#Izveidot funkciju, kas parbauda, vai skaitlis atrodas lietotaja noteikta diapazona vai ne
def noteiktDiapazonu(d1,d2,sk):
  rezultats = "Skaitlis nav diapazona"
  if d1>=sk<=d2:
    rezultats = "Skaitlis ir diapazona"
  return rezultats

d1 = int(input("Ievadi diapazona sākumu: "))
d2 = int(input("Ievadi diapazona beigas: "))
sk = int(input("Ievadi skaitlis: "))
rez = noteiktDiapazonu(d1,d2,sk)
print(rez)
