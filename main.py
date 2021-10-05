
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


def is_superprime(n) :
 ok = 1
 copien = n
 while (copien > 0 ) :
  if( is_prime(copien) == 0) :
   ok = 0
   break
  copien = copien // 10

 return ok


def main():
    print(get_largest_prime_below(3))
    print(get_age_in_days(1 , 10 , 2001))
    print(is_superprime(237))

if __name__ == "__main__":
    main()
