import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'),
              ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'),
              ('relev--ant', '-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]


def MED(S, T):
  if (S == ""):
    return (len(T))
  elif (T == ""):
    return (len(S))
  else:
    if (S[0] == T[0]):
      return (MED(S[1:], T[1:]))
    else:
      return (1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T):

  ## when we create an empty 2D array, the next thing is to fill in all elements -- BOTTOM UP

  arr = [[0 for n in range(len(T) + 1)] for m in range(len(S) + 1)]

  # Iterating through each element of the 2D array
  for m in range(len(S) + 1):
    for n in range(len(T) + 1):
      if (S == ""):  # Base
        arr[m][n] = n

      elif (T == ""):  # Base
        arr[m][n] = m

      elif S[m - 1] == T[n - 1]:  # -1 bc index with
        # strings starts at 0 but array starts w n/m =1
        # checks if characters are equal
        # if so, no edits and use diagonal edit dist
        arr[m][n] = arr[m - 1][n - 1]

      else:
        arr[m][n] = 1 + min(arr[m][n - 1], arr[m - 1][n])

  return (arr[len(S)][len(T)], arr)
  #return (arr[len(S)][len(T)])


# def fast_align_MED(S, T):
#   opt, arr = fast_MED(S, T)
#   string_s = ""
#   string_t = ""

#   m = len(S) - 1
#   n = len(T) - 1

#   while (m and n >= 0):
#     if (S[m] == T[n]):
#       letter_s = (S[m], string_s)
#       string_s = "".join(letter_s)

#       letter_t = (T[n], string_t)
#       string_t = "".join(letter_t)

#       n -= 1
#       m -= 1
#     elif arr[m - 1][n] >= arr[m][n - 1]:
#       letter_s = (S[m], string_s)
#       string_s = "".join(letter_s)

#       letter_t = ("-", string_t)
#       string_t = "".join(letter_t)

#       n -= 1
#     else:
#       letter_s = ("-", string_s)
#       string_s = "".join(letter_s)

#       letter_t = (T[n], string_t)
#       string_t = "".join(letter_t)

#       m -= 1

#   return (string_s, string_t)


def fast_align_MED(S, T):
  opt, arr = fast_MED(S, T)
  string_s = ""
  string_t = ""

  m = len(S) - 1
  n = len(T) - 1

  while m >= 0 and n >= 0:
    if S[m] == T[n]:
      string_s = S[m] + string_s
      string_t = T[n] + string_t
      m -= 1
      n -= 1
    elif m > 0 and arr[m - 1][n] <= arr[m][n - 1]:
      string_s = S[m] + string_s
      string_t = "-" + string_t
      m -= 1
    else:
      string_s = "-" + string_s
      string_t = T[n] + string_t
      n -= 1

  while m >= 0:
    string_s = S[m] + string_s
    string_t = "-" + string_t
    m -= 1

  while n >= 0:
    string_s = "-" + string_s
    string_t = T[n] + string_t
    n -= 1

  return string_s, string_t


print(fast_align_MED('book', 'back'))
#print(fast_MED('book', 'back'))

#print(MED('book', 'baok'))

print(fast_align_MED('kookaburra', 'kookybird'))
#print(MED('kookaburra', 'kookybird'))

#print(fast_MED('elephant', 'relevant')[1])
#print(MED('elephant', 'relevant'))

#print(fast_MED('battle', 'bitter')[0])
#print(MED('battle', 'bitter'))
