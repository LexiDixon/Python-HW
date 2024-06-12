

def main() :

  hours = int(input("Enter a value between 0 and 23: "))
  mintues = int(input("Enter a value between 0 and 59: "))
  hours, mintues = validate(hours, mintues)

  print(f'You entered {hours} hours and {mintues} mintues')

  
def validate(hours, mintues) :
    
    if hours < 0 or hours > 23:
      hours = 0
      print("Invalid hours")
      hours = int(input("Enter a value between 0 and 23: "))
    if mintues < 0 or mintues > 59:
      mintues = 0
      print("Invalid mintues")
      mintues = int(input("Enter a value between 0 and 59: "))
    
    return hours, mintues

main()
