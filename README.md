# discord_python_exec
 Discord bot to execute Python-code

Uses discord to feed code to Pythons "exec()" function.
It's really important to limit the users having access to the "exec()" function as it executes ANY (Python) code given to it (literally rce).
I'm sure you are capable finding out your own discord ID - giyf.


This came to be as a friend and I were discussing fibonacci numbers and typing

!python
a,b,c = 1,1,0
print(f"{a} {b}",end="")
while c < 30:
  c += 1
  d = a+b
  a = b
  b = d
  print(f" {b}",end="")

 into my phone would have been faster than calculating it by hand.
 (That being said.. googling the first x numbers would probably have been faster too; but i like to create and when an idea hits, it just gotta come out.)