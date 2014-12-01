#!/usr/bin/python
# -*- coding: utf-8 -*-

import string,urllib2,re
from ftplib import FTP  
import threading, random, sys, httplib, base64, Queue, getopt,os,socket
try:
    import msvcrt
    is_shouhu = 1
except:
    is_shouhu = 0
    print "Is linux or have no msvcrt"

bufsize=1024  
def Get(filename):  
    command='RETR '+filename  
    ftp.retrbinary(command,open(filename,'wb').write,bufsize)  
    print 'download successfully'  
def Put(filename):  
    command='STOR '+filename  
    filehandler=open(filename,'rb')  
    ftp.storbinary(command,filehandler,bufsize)  
    filehandler.close()  
    print 'upload successfully'  
def PWD():  
    print ftp.pwd()  
def Size(filename):  
    print ftp.size(filename)  
def Help():  
    print '''  
    ==============================  
         Simple Python FTP  
    ==============================  
    cd       enter document  
    delete   delete file  
    dir      get files list  
    get      download file  
    help     help  
    mkdir    create document  
    put      upload file  
    pwd      get current path  
    rename   rename file name  
    rmdir    delete document  
    size     get file size  
    '''  

def cmd():
    actions={'dir':ftp.dir,'pwd':PWD,'cd':ftp.cwd,'get':Get,  
         'put':Put,'help':Help,'rmdir':ftp.rmd,  
         'mkdir':ftp.mkd,'delete':ftp.delete,  
         'size':Size,'rename':ftp.rename}  
    while True:  
        print 'pyftp',  
        cmds=raw_input  
        cmd=string.split(cmds)  
        try:  
            if len(cmd)==1:  
                if string.lower(cmd[0])=='quit':  
                    break  
                else:  
                    actions[string.lower(cmd[0])]  
            elif len(cmd)==2:  
                actions[string.lower(cmd[0])](cmd[1])  
            elif len(cmd)==3:  
                actions[string.lower(cmd[0])](cmd[1],cmd[2])  
            else:  
                print 'type error'  
        except:  
            print 'command error' 

class ftp_saber(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)

        def run(self):
            while 1:
                if queue.empty() == True:
                    break
                self.ip = queue.get()
                print self.ip
                try:
                    self.ftp=FTP(self.ip)
                    self.ftp.login('anonymous','')
                    jilu.write(ip+"||anonymous\n")
                    continue
                except:
                    pass
                try:
                    self.ftp.quit()
                except:
                    pass


class ThreadGetKey(threading.Thread):
    def run(self):
        while 1:
            try:
                chr = msvcrt.getch()
                if chr == 'q':
                    print "stopped by your action ( q )" 
                    os._exit(1)
                else:
                    continue
            except:
                print "Is linux or have no msvcrt"
                os._exit(1)

if __name__ == '__main__':
    #get_ip_url = 'http://xxxx/xxxx.php?ip='
    # server=raw_input('enter FTP server info: ')  
    ftp_file = open('c:/ftp.txt','r')
    jilu = open('c:/jilu.txt','a+')

        # print ip
        # html = urllib2.urlopen(get_ip_url+ip)
        # domains = re.findall('host.:.([^}]*)"',html.read())
        # ftp=FTP(ip)
        # for domain in domains:
        #     username=password= re.search('\.([^\.]*)\..[^\.]*$',domain).group(1)
        #     print 123
        #     ftp.login(username,password)  
        #     print ftp.getwelcome()
        #     jilu = open('c:/jilu.txt','a+')
        #     jilu.write(ip+"||"+username+"||"+ftp.getwelcome())
        #     ftp.quit()
        #     break
        # ftp.quit()
    ############
    if is_shouhu:
        shouhu = ThreadGetKey()
        shouhu.setDaemon(True)
        shouhu.start()
    ##############threads start########
    threads = [] 
    queue = Queue.Queue()
    for server in ftp_file.readlines(): 
        server = server.strip()
        queue.put(server)

    ftp_file.close()

    for i in range(15):
        a = ftp_saber()
        a.start()
        threads.append(a)
    for j in threads:
        j.join()


    jilu.close()
