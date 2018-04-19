#! /usr/bin/env python

import MySQLdb


class __Config ():
    Slave_IP = '192.168.0.30'  # slave_IP
    Slave_Port = 3306
    Slave_User = 'moninter'
    Slave_Passwd = 'moninter'


def Check_Slave():
        try:
                con = MySQLdb.connect(host=__Config.Slave_IP, db='mysql', user=__Config.Slave_User,
                                        passwd=__Config.Slave_Passwd, port=__Config.Slave_Port, )
                cur = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
                cur.execute('Show Slave Status')
                result = cur.fetchone()
                if result['Slave_IO_Running'] == 'Yes' and result['Slave_SQL_Running'] == 'Yes':
                        pass
                else:
                        pass  # send warnning message
        except Exception as e:
                with open('slave.log', 'w')as s:
                        s.write(e)


if __name__ == "__main__":
        while True:
                Check_Slave()
