def cube(x):
    return x*x*x

lemon = cube(0.06)
cherry = cube(0.09)
clover = cube(0.14)
bell = cube(0.18)
diamond = cube(0.38)
chest = cube(0.12)
seven = cube(0.03)


lemon_pay = 43
cherry_pay = 35
clover_pay = 30
bell_pay = 21
diamond_pay = 11 
chest_pay = 32
seven_pay = 58

print(lemon*lemon_pay + cherry*cherry_pay + clover*clover_pay + bell*bell_pay + diamond*diamond_pay + chest*chest_pay + seven*seven_pay)