import random

def primary():


  f = open("quotes.txt", "a")
  f.write("\nadd new random " + str(random.randint(1, 100)))
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  

  last = len(quotes)-1

  
  for i in range(3):
    rnd = random.randint(0, last)
    print(quotes[rnd].strip())
    
if __name__== "__main__":
  primary()
