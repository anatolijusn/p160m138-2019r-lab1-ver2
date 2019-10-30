import sys



def greet(greeted_name: str):
 return f"Hello, {greeted_name}!"
def testgreet():
    name=sys.argv[1]
    print(greet(name))

testgreet()
