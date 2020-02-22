# discord_python_exec
 Discord bot to execute Python-code

Uses discord to feed code to Pythons "exec()" function.<br/>
It's really important to limit the users having access to the "exec()" function as it executes ANY (Python) code given to it (literally rce).
I'm sure you are capable finding out your own discord ID - giyf.


This came to be as a friend and I were discussing fibonacci numbers and typing

!python<br/>
a,b,c = 1,1,0<br/>
print(f"{a} {b}",end="")<br/>
while c < 30:<br/>
  c += 1<br/>
  d = a+b<br/>
  a = b<br/>
  b = d<br/>
  print(f" {b}",end="")<br/>

 into my phone would have been faster than calculating 30 numbers by hand.<br/>
 (That being said.. googling the first x numbers would probably have been faster too; but i like to create and when an idea hits, it just gotta come out.)
