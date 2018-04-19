#! /usr/bin/env python
# coding=utf-8
import paramiko,time,logging,os

#Master Mysql
master_mysql={
    'hostname':'192.168.0.27',
    'username':'root',
    'password':'123456'

}
#Slave Mysql
slave_mysql={
    'hostname': '192.168.0.30',
    'username': 'root',
    'password': '123456'

}
#以当前日期为日志名
log_file='%s_es.log'%(time.strftime ("%Y%m%d", time.localtime ()))
logging.basicConfig (level=logging.INFO,
                             format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                             datefmt='%a, %d %b %Y %H:%M:%S',
                             filename=log_file,
                             filemode='a')

def check_sync(mysqlIP):
	'''
	检查虚拟Ip绑定在主/从Mysql
	'''
    ssh_client=paramiko.SSHClient()
    try:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            hostname='192.168.0.205',
            username='root',
            password='123456'

        )
        stdin,stdout,stderr = ssh_client.exec_command("ip a")
        studout=stdout.readlines()
        st=[]
        for s in studout:
                st.append(str(s))
        result=''.join(st)
        if mysqlIP in result:
            return True
        else:
            return False
        ssh_client.close()
    except Exception as e:
        logging.error(e)
        ssh_client.close()
		
def stop_master_Mysql():
    '''
	stop Master Mysql
	'''
	try:
        os.popen('/etc/init.d/mysqld stop')
    except Exception as e:
        logging.error(e)

def start_master_Mysql():
	'''
	start Master Mysql
	'''
    try:
        os.popen('/etc/init.d/mysqld start')
    except Exception as e:
        logging.error(e)

if __name__=='__main__':
    num=1
    try:
         while True:
                stop_master_Mysql()
                time.sleep(0.5)
                if check_sync(mysqlIP=slave_mysql['hostname']):
                        logging.info (msg='NUM:%s Switch to Slave Suceess' % num)
                        start_master_Mysql()
                        time.sleep(0.5)
                        if check_sync(mysqlIP=master_mysql['hostname']):
                                logging.info(msg='NUM:%s Switch to Master Suceess'%num)
                        else:
                                logging.info (msg='NUM:%s Switch to Master Fail'%num)
                        num+=1
                else:
                        logging.info (msg='NUM:%s Switch to Master Fail' % num)
    except Exception as e:
        logging.error(e)
        print num
