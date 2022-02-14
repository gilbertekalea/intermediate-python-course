import random

def main():
  dice_rolls = 2
  for i in range(0, dice_rolls):
    roll = random.randint(0,6)
    dice_sum +=roll
    print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')
if __name__== "__main__":
  main()