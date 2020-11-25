# 171101036 Irem Kilinc Bil 334
import re

url_file = open('urls.txt', 'r')
write_to_file = open('urls_output.txt', 'w')
regex = re.compile("https:\/\/(?:www)?(?:\.)?(?:[^\d\W]){1,12}\.(?:com|org|net)(?:\/)?(?:.)*")

while True :
   line = url_file.readline()
   if not line:
       break

   if regex.search(line):
       write_to_file.write("valid \n")
   else:
       write_to_file.write(" not valid \n")

