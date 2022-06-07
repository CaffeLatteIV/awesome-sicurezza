import random
import getopt, sys

def p_test(n, randMax):
  a = random.randint(1, randMax) % n
  if ((a**(n-1)) % n) == 1:
    print("Primo")
  else: 
    print("Non Primo")

try:
# Get full command-line arguments
  full_cmd_arguments = sys.argv

  # rimuove il primo argument (call del file)
  argument_list = full_cmd_arguments[1:]

  short_options = "n:r:"
  arguments, values = getopt.getopt(argument_list, short_options)
  n = None
  r = 10000 #default

  for current_argument, current_value in arguments:
    if current_argument == "-n":
      n = int(current_value)
    elif current_argument == "-r":
      r = int(current_value)
  if not n:
    print("parametro -n mancante")
    sys.exit(2)
  p_test(n, r)
    
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(2)

