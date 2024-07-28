weight = int(input(" Weight: "))
weight_type = input("(K)g or (L)bs: ")

if weight_type.upper() =='K':
  f_weight = int(weight) * 2.20462
  print(f'Your weight is {round(f_weight)} pounds')
else :
    f_weight = int(weight) * 0.453592
    print(f"Your weight is {round(f_weight)} kilos")



