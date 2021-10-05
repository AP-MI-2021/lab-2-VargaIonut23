def is_prime(n):
 if n < 2:
  return 0
 elif n == 2:
  return 1
 elif n % 2 == 0:
  return 0
 else:
  for i in range(3, n, 2):
   if n % i == 0:
    return 0
 return 1


def get_largest_prime_below(n) :
 for i in range (n , 1 , -1) :
  if is_prime(i) == 1 :
   return i

def test_get_largest_prime_below():
 assert get_largest_prime_below(9) == 7
 assert get_largest_prime_below(3) == 3
 assert get_largest_prime_below(14) == 13
 assert get_largest_prime_below(17) == 17
 assert get_largest_prime_below(42) == 41

def get_age_in_days(zi, luna , an) :
 if an % 4 == 0 and an % 100 == 0 and an % 400 == 0 :
  ok = 1
 elif an % 4 == 0 and an % 100 != 0 :
  ok = 1
 else :
  ok = 0
 ziletotale = 0

 for i in range (an+1 , 2021 , 1):
  if i % 4 == 0 and i % 100 == 0 and i % 400 == 0:
   ziletotale = ziletotale + 366
  elif i % 4 == 0 and i % 100 != 0:
   ziletotale = ziletotale + 366
  else :
   ziletotale = ziletotale + 365
# am calculat numarul de zile al anilor aflati intre cei doi ani pe care ii cunoastem
 if luna == 1 or luna == 3 or luna == 5 or luna == 7 or luna == 8 or luna == 10 or luna == 12 :
  ziletotale = ziletotale + 31 - zi + 1
 elif luna == 4 or luna == 6 or luna == 9 or luna == 11:
  ziletotale = ziletotale + 30 - zi + 1
 elif luna == 2 and ok == 1 :
  ziletotale = ziletotale + 29 - zi + 1
 else :
  ziletotale = ziletotale + 28 - zi + 1
# am calculat numarul de zile ramase din luna nasterii acelei persoane
 for i in range (luna+1 , 13 , 1):
  if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
   ziletotale = ziletotale + 31
  elif i == 4 or i == 6 or i == 9 or i == 11:
   ziletotale = ziletotale + 30
  elif i == 2 and ok == 1 :
   ziletotale = ziletotale + 29
  else :
   ziletotale = ziletotale + 28
# am calculat numarul zilelor lunilor ramase din anul care ni s a dat
 for i in range (1 , 10 , 1):
  if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
   ziletotale = ziletotale + 31
  elif i == 4 or i == 6 or i == 9 or i == 11:
   ziletotale = ziletotale + 30
  elif i == 2 and ok == 1 :
   ziletotale = ziletotale + 29
  else :
   ziletotale = ziletotale + 28

 return ziletotale
# am calculat numarul zilelor din anul curent
# am luat ca data de referinta ziua de 1.10.2021

def test_get_age_in_days() :
 assert get_age_in_days (1 , 10 , 2001) == 7305
 assert get_age_in_days(2, 12, 2010) == 3956
 assert get_age_in_days(23, 3, 2003) == 6767
 assert get_age_in_days(25, 12, 1989) == 11603
 assert get_age_in_days(11, 9, 2005) == 5864


def is_superprime(n) :
 ok = 1
 copien = n
 while (copien > 0 ) :
  if( is_prime(copien) == 0) :
   ok = 0
   break
  copien = copien // 10

 return ok

def test_is_superprime() :
  assert is_superprime (233) == 1
  assert is_superprime (27) == 0
  assert is_superprime (71) == 1
  assert is_superprime (235) == 0
  assert is_superprime (31) == 1

shouldRun = True

while shouldRun:
    print("1.Determina cel mai mare numar prim mai mic decat cel dat")
    print("2.Determina numarul de zile de la o data pana in prezent")
    print("3.Determina daca un numar este superprim")
    print("4.Iesire")
    optiune = int(input("Selectati optiunea: "))
    if optiune == 1:
      test_get_largest_prime_below()
      n = int(input("Dati numarul: "))
      print(get_largest_prime_below(n))
    elif optiune == 2:
      test_get_age_in_days()
      ziua = int(input("Dati ziua: "))
      luna = int(input("Dati luna: "))
      anul = int(input("Dati anul: "))
      print(get_age_in_days (ziua , luna ,anul))
    elif optiune == 3:
      test_is_superprime()
      n=int(input("Dati numarul: "))
      print(is_superprime(n))
    elif optiune == 4:
      shouldRun = False
    else :
      print("Optiune gresita! Reincercati!")