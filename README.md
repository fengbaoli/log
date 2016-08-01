Real time log synchronization 
======
#Introduction
######Real time log synchronization is a real-time log or file synchronization procedures, mainly contains two aspects: server client and client. Client mainly to collect the log or the contents of the document, server data is received and will receive data storage and documentation
#Support
######1 support configuration synchronization interval<br/>
######2 support synchronization from Linux to any directory to the windowns directory<br/>
######3 support print debug log<br/>
######4 support incremental log synchronization<br/>
#Install
######1 download log, the address is:https://github.com/fengbaoli/log.git 
######2 starts at server.py windowns (the default port is 8000).
######3 in the Linux side using git download <br/>
git clone  https://github.com/fengbaoli/log.git 
######4 to modify the collog.conf file below conf
[client]
Logpath = /var/log/httpd ====> to log path acquisition
ConfigFile = log.conf ====> default parameters
IP = ====>server 10.224.192.132 end IP
Port = 8000 ====>server listener port
Interval_time = 10 ====> sampling interval
[server]
BUFSIZE = 1024 =====>server end default parameters
Port = 8000 =====>server listener port
Receive_path=logs =====> collection log path

