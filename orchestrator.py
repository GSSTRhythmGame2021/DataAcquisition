import sh
import sys

cmdexe = sh.Command("powershell.exe")


cmdexe("python automation_template.py", _fg=True)
