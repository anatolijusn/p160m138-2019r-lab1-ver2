import sys

def greet(name: str, shout_count: int = 1):

    if shout_count is greet.__defaults__[0]:
       str=f"Hello, {name}{shout_count * '!'}"
       return str    
    else:
      return f"Hello, {name}{shout_count * '!'}"
def testgreet():
    name=sys.argv[1]
    if len(sys.argv)>2:
       shout_count=int(sys.argv[2])
       print(greet(name,shout_count))
    else:
      print(greet(name))
testgreet()
