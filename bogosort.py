import random
import sys


def build_deck(size: int):
  return list(range(size))

# writing our own shuffle (fisher-yates)
def fy_shuffle(array: list[int]):

  for i in reversed(array):
    j = random.randint(0, len(array) - 1)

    temp = array[i]
    array[i] = array[j]
    array[j] = temp

  return array


def bogo_sort(input: list[int]):

  sorted = False
  attempts = 0

  while not sorted:

    done = True

    tmp = fy_shuffle(input)

    for i in tmp:
      if i != tmp[i]:
        done = False

    attempts += 1

    sorted = done

  return attempts

size = int(sys.argv[1])

input = fy_shuffle(build_deck(size))
total = bogo_sort(input)
print("Attempts: ", total)
