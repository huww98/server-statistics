from servers import Servers

s = Servers()
s.loadHostsFrom("ip.txt")
for host, result in s.ssh("lsb_release -d | cut -f2"):
    print(host + "\t" + result.stdout.rstrip())
