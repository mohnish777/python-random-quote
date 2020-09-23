import random
def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.read()
  #f=open('quotes.txt','w')
  #f.write('mohnish')
  #f.write('krishna')
  
  f.close()
  last=len(quotes)-1
  rnd=random.randint(0,last)

  print(quotes)

if __name__== "__main__":
  main()
