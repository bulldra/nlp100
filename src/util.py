import subprocess


def unix_cmd(cmd):
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    return str(res.stdout)
