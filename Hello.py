import sys



def greet(name: str):
 return f"Hello, {name}!"
def testgreet():
    name=sys.argv[1]
    print(greet(name))

testgreet()
