Mysql-keepalived高可用测试

1、Mysql主数据库监控
	监控脚本和keepalive放在同一个环境
	Master_Moninter.py实现了监控Mysql主数据的mysql进程
		当mysql进程被停掉了，会立刻kill掉keepalived的进程；为了让虚拟Ip绑定到从Mysql上，实现主从切换
	Slave_Moninter.py实现了监控Mysql主数据的mysql进程
		当mysql进程被停掉了，会立刻kill掉keepalived的进程；为了让虚拟Ip绑定到从Mysql上，实现主从切换

		当mysql服务被启动之后，检查keepalived的服务是否开启；如果没有开启就会立刻启动keepalived的服务，

2、Mysql从数据库监控
	Slave_Moninter.py实现监控主从同步的状态
		进入从mysql，Show Slave Status查询出Slave_IO_Running和Slave_SQL_Running，如果其中一个不是Yes，就会发出警告通知；
		在监控中如果出现异常，会在本地保存异常信息日志
3、相关依赖
	MySQLdb
	安装方法：
		1、安装pip
			yum -y install epel-release
			yum -y install python-pip
			yum clean all

		2、安装MySQL_Python
			yum install gcc
			yum install mysql-devel
			yum install python-devel
			pip install -Iv https://pypi.python.org/packages/source/M/MySQL-python/MySQL-python-1.2.5.zip#md5=654f75b302db6ed8dc5a898c625e030c

		3、验证是否安装成功
