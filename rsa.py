import math
import getopt, sys

from typing import Tuple
def xgcd(a: int, b: int) -> Tuple[int, int, int]:
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def egcd(a: int, b: int) -> Tuple[int, int, int]:
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    if a == 0:
        return (b, 0, 1)
    else:
        b_div_a, b_mod_a = divmod(b, a)
        g, x, y = egcd(b_mod_a, a)
        return (g, y - b_div_a * x, x)

def modinv(a: int, b: int) -> int:
    """return x such that (x * a) % b == 1"""
    g, x, _ = egcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b


def rsa(p,q):
  #finding N
  n = p*q
  print("N = ", n)

  #finding phi(N)
  phi_n = (p - 1) * (q - 1)
  print("phi(N) = (p-1)*(q-1) = ", phi_n)

  #finding e (in modo che sia relativamente primo a phi(N))
  found = False
  e = 3
  while not found and e<phi_n:
      if math.gcd(e, phi_n) == 1:
          found = True
          break
      e += 2 #tanto non può essere pari (credo?)
  print("Chosen e = ", e)

  #finding d
  d = modinv(e, phi_n)
  print("D = ", d)

  print("PublicKey = (e, n) = ", e, n)
  print("PrivateKey = (d, n) = ", d, n)

  
try:
# Get full command-line arguments
  full_cmd_arguments = sys.argv

  # rimuove il primo argument (call del file)
  argument_list = full_cmd_arguments[1:]

  short_options = "p:q:"
  arguments, values = getopt.getopt(argument_list, short_options)
  p = None
  q = None
  for current_argument, current_value in arguments:
    if current_argument == "-p":
      p = int(current_value)
    elif current_argument == "-q":
      q = int(current_value)
  if not p or not q:
    print("parametro -p o -q mancante")
    sys.exit(2)
  rsa(p,q)
    
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(2)

