'''TraceBack is used to print details of the error like the line number of the code'''


import traceback
try:
    print("Done")
    print("Done")
    print("Done")
    print("Done")
    print(5 / 0)
    print("Done")
    print("Done")
    print("Done")
except Exception as e:
    print(type(e).__name__)
    print(e)
    traceback.print_exc()
    print("-----")