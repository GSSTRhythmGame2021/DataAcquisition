import os
import sh
import sys

os.system('poetry run python3 dataacquisition/acquisition.py')
cmdexe = sh.Command("powershell.exe")


cmdexe("python automation_template.py", _fg=True)
