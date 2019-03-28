from servers import Servers

script = r"""
defs="/etc/login.defs"
min=$(grep "^UID_MIN" $defs)
max=$(grep "^UID_MAX" $defs)
awk -F':' -v "min=${min##UID_MIN}" -v "max=${max##UID_MAX}" '{ if ( $3 >= min && $3 <= max) print $1 }' /etc/passwd
"""

ignoredUsers = ["ubuntu", "test_01", "temp"]

s = Servers()
s.loadHostsFrom("ip.txt")
for host, result in s.ssh(script):
    users = result.stdout.splitlines()
    for u in users:
        if u not in ignoredUsers:
            print(host + "\t" + u)
