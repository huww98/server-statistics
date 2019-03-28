import concurrent.futures
import subprocess
import sys

class Servers:
    user = "huweiwen"

    def loadHostsFrom(self, path: str):
        with open(path) as ipFile:
            self.hosts = ipFile.read().splitlines()

    def _executeSsh(self, host: str, script: str):
        return subprocess.run(["ssh", "-o", "BatchMode=yes", self.user + "@" + host, script],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    def ssh(self, script: str):
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            future_to_host = {executor.submit(self._executeSsh, host, script): host for host in self.hosts}
            for future in concurrent.futures.as_completed(future_to_host.keys()):
                host = future_to_host[future]
                result: subprocess.CompletedProcess = future.result()
                if result.returncode == 0:
                    yield (host, result)
                    continue
                elif result.returncode == 255:
                    if "Resource temporarily unavailable" in result.stderr:
                        print(host + "\tErrorConnect", file=sys.stderr)
                        continue            
                    elif "Permission denied" in result.stderr:
                        print(host + "\tErrorDenied", file=sys.stderr)
                        continue
                print(host + "\t" + result.stderr, file=sys.stderr)
