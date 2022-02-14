import random

def main():
  dice_rolls = 2
  dice_sum = 0 
  for i in range(0, dice_rolls):
    roll = random.randint(0,6)
    dice_sum +=roll
    if roll == 1:
      print(f'You have rolleda {roll} ! Critical fail!!')
    elif roll == 6:
      print(f'You rolled a {roll}!! Critical Success!!')
    else:
      print(f'You have rolled a {roll}')
  print(f'You have a rolled a total of {dice_sum}')
if __name__== "__main__":
  main()