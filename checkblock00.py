from PyFunceble import test as PyFunceble
import urllib3
urllib3.disable_warnings()

readfile = open("src/splitblock00", "r")
file = open('dest/deadblock00', 'w+')
for line in readfile:
  line_list = line.strip()
  domain_stats = str(PyFunceble (line_list))
  print(f"{line_list} is {domain_stats}")
  if domain_stats != "ACTIVE":
    file.writelines(f"{line_list}\n")

readfile.close()
file.close()
