#! /usr/bin/env Python

import os
import subprocess
import sys
import time


def moninter_mysql():
        #print '*********************MySQL_Master_Moninter is starting*******************************'
        try:
                ret=os.popen('ps aux|grep mysql').readlines()
                r=''.join(ret)
                if r.find('/usr/local/mysql/bin/mysqld')==-1:
                        keep=os.popen('pgrep -l keep')
                        k= keep.readlines()[0].split()[0]
                        subprocess.call(['kill','-9','%s'%k])
                else:
                        keeps=os.popen('ps aux |grep mysql').readlines()
                        ks=''.join(keeps)
                        if ks.find('keepalived -f /etc/keepalived/keepalived.conf -d -D')==-1:
                                subprocess.call(['keepalived','-f','/etc/keepalived/keepalived.conf','-d','-D'])
                        pass
        except Exception as e:
                with open('moninter.log','w')as m:
                        t=time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime ())
                        m.write(t+':'+''+'e')
               # print '*********************************MySQL_Master_Moninter has Stopped*****************'

if __name__=='__main__':
        while True:
                moninter_mysql()
