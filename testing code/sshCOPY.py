import paramiko







ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
        ssh.connect('IP ADDRESS', username='HOSTNAME', password='PASSWORD')
except paramiko.SSHException:
        print "Connection Failed"
        quit()

ssh.exec_command('python db_argv.py %s %s' %(VARIABLES TO CHANGE))  //Pass variables like STR valus, ""
ssh.close()
