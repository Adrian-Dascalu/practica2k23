import pyttsx3
engine = pyttsx3.init()
hello = "hello world"
engine.say(hello)
engine.save_to_file(hello, 'hello.mp3')
engine.runAndWait()

from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
print(solve(x**2 - 1, x))