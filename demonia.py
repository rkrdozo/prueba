#!/usr/bin/env python
'''Daemon example'''

import os, sys, time

def main ():
    '''This is the main function run by the daemon.
    '''
    fout = open ('/tmp/daemon.log', 'a')
    fout.write ('daemon started with pid %d\n' % os.getpid())
    c = 0
    while 1:
		fout.write ('Count: %d\n' % c)
		fout.flush()
		c = c + 1
		time.sleep(5)
		

if __name__ == '__main__':
    pid = os.fork ()
    if pid == 0: # if pid is child...
        os.setsid() # Create new session and sets process group.
        pid = os.fork () # Will have INIT (pid 1) as parent process...
        if pid == 0: # if pid is child...
            main ()
