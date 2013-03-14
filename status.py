from sys import stdout
from time import sleep
progress = ['|','/','-','\\']
for i in range(1,100):
    for j in progress:
        stdout.write("\r%s %d percentage" % (j,i))
        stdout.flush()
        sleep(1)
stdout.write("\n")
