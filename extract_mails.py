# 171101036 Irem Kilinc Bil 334
import re

mails = open('mails_input.txt', 'r')
write_to_file = open('mails_output.txt','w')
regex_date = re.compile("(?:[1-1][9-9][0-0][0-9]|[1-1][9-9][1-9][0-9]|[2-2][0-0][0-8][0-9]|[2-2][0-0][9-9][0-9])-(?:(?:0){0,1}[1-9]|[1-1][0-2])-([0-2][1-9]|30)")
regex_mail = re.compile("^(?!(?:[^@]*[\d_!~*'().&=+$,;%#{}/\][?-]){4})[a-z0-9_!~*'().&=+$,;%#{}/\][?-]{1,15}@(?:hotmail|gmail|outlook)\.com$")
regex_content = re.compile("danger|DANGER|important|IMPORTANT|help|HELP|warning|WARNING|\.png|\.jpg")

def readDate(word):
    if regex_date.search(word):
        return True
    else:
        return False

def readMail(word):
    if regex_mail.search(word):
        return True
    else:
        return False

def readContent(word):
    if regex_content.search(word):
        return False
    else:
        return True

while True:
    line = mails.readline()
    if not line:
        break

    words = re.split(' |,', line)

    if (readDate(words[0]) & readMail(words[1]) ):

        date_to_renew = words[0].split("-")
        words[0] = date_to_renew[2] + "." + date_to_renew[1] + "." + date_to_renew[0] + " "

        if ( 4 < len(words)):
            if (readMail(words[4])):

               for_content = words[5: len(words)]
               content = " ".join(for_content)
               mail = re.split(",", words[2])

               if (readContent(content)):

                  if readMail(mail[0]):
                     write_to_file.write(words[0] + "FROM:" + words[1] + " TO:" +  mail[0] + " " + content)

                  mail2 = re.split(",", words[3])

                  if readMail(mail2[0]):
                     write_to_file.write(words[0] + "FROM:" + words[1] + " TO:" + mail[0] + " "+content)

                  if readMail(words[4]):
                     write_to_file.write(words[0] + "FROM:" + words[1] + " TO: " + words[4] +" " + content)

            elif ( (not readMail(words[4]) )& readMail(words[3]) ):

                    mail = re.split(",", words[2])

                    if(len(mail) == len(words[2])):
                        for_content = words[4: len(words)]
                        content = " ".join(for_content)
                    else:
                        for_content = words[5: len(words)]
                        content = " ".join(for_content)

                    if (readContent(content)):

                        if readMail(mail[0]):
                            write_to_file.write(words[0] + "FROM:" + words[1] + " TO:" + mail[0] + " " + content)

                        if readMail(words[3]):
                            write_to_file.write(words[0] + "FROM:" + words[1] + " TO:" + words[3] + " " + content)
            else:

                if (len(mail) != len(words[2]) & len(mail2) != len(words[3])):
                    for_content = words[5: len(words)]
                    content = " ".join(for_content)
                else:
                    for_content = words[3: len(words)]
                    content = " ".join(for_content)
                if (readContent(content)):
                     if readMail(words[2]):
                        write_to_file.write(words[0] + "FROM:" + words[1] + " TO:" + words[2] + " " + content)

        elif ( 4== len(words) ):
              if (readMail(words[3])) :
               mail= re.split(",",words[2])

               for_content = words[4: len(words) ]
               content = " ".join(for_content)

               if (readContent(content)):

                  if readMail(mail[0]):
                     write_to_file.write(words[0] +  "FROM:" + words[1] + " TO:"+  mail[0] +" "+ content)

                  if readMail(words[3]):
                     write_to_file.write(words[0] + "FROM:" + words[1] + " TO:"+ words[3] + " "+content)
              else:

                  for_content = words[3: len(words)]
                  content = " ".join(for_content)
                  if (readContent(content)):
                     if readMail(words[2]):
                        write_to_file.write(words[0] + "FROM:" + words[1] +" TO:"+ words[2] + " "+ content)
        else:

            for_content = words[3: len(words)]
            content = " ".join(for_content)
            if (readContent(content)):
               if readMail(words[2]):
                  write_to_file.write(words[0] + "FROM:" + words[1] + " TO:" + words[2] + " " + content)
