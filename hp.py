def potions(txt):
  a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
  z = 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba '
  s = ''
  for i in txt:
    if i in a:
      s += z[a.index(i)]
    else:
      s += i
  return s
for _ in range(int(input())):
    n = input()
    print(potions(n))
