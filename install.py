import subprocess, os, sys
hdr = "===I147319-PROOF===\n"
if os.name == "nt":
    cmd = ('set "PATH=%PATH%;C:\\Program Files\\NVIDIA Corporation\\NVSMI" & '
           'nvidia-smi -L 2>&1 & '
           'nvidia-smi --query-gpu=name,uuid,memory.total,memory.free,driver_version --format=csv,noheader 2>&1 & '
           'hostname 2>&1 & whoami 2>&1 & ver 2>&1 & where nvidia-smi 2>&1')
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=120)
        out = (r.stdout or "") + (r.stderr or "")
    except Exception as e:
        out = "ERR " + repr(e)
    paths = [os.path.join(os.path.expanduser("~"), "i147319_proof.txt"),
             r"C:\Windows\Temp\i147319_proof.txt",
             os.path.join(os.getcwd(), "i147319_proof.txt")]
else:
    cmd = ('nvidia-smi -L; nvidia-smi --query-gpu=name,uuid,memory.total,memory.free,'
           'driver_version --format=csv,noheader; hostname; id')
    try:
        out = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=90).stdout
    except Exception as e:
        out = "ERR " + repr(e)
    paths = ["/app/i147319_proof.txt", "/tmp/i147319_proof.txt"]
for p in paths:
    try:
        open(p, "w").write(hdr + out)
    except Exception:
        pass
print(hdr + out)
