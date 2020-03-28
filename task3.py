while True:
    m=int(input("enter your maths score\n"))
    p=int(input("enter your physics score\n"))
    c=int(input("enter your chemistry score\n"))

    if m >= 35 and p>=35 and c>=35:
      a=(m+p+c)/3
      if a<=59: print("C")
      elif a>59 and a<=69: print("B")
      else: print("A")
    else: print("you haven't passed")