import random


def build_deck(size):
  return list(range(0, size))

# writing our own shuffle (fisher-yates)
def fy_shuffle(array):

  for i in reversed(array):
    j = random.randint(0, len(array) - 1)

    temp = array[i]
    array[i] = array[j]
    array[j] = temp

  return array

#
def bogo_sort(input):

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




print("enter a size to be sorted:")
size = int(input())


input = fy_shuffle(build_deck(size))
total = bogo_sort(input)
print("Attempts: ", total)
