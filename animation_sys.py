import time
import os

delay = 0.06
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def anim(anim_name : str):
    file = open(f"{anim_name}.txt", "r", encoding="utf-8")
    content = file.read()
    frames = content.split("---FRAME---")

    for frame in frames:
        print(frame.strip())
        time.sleep(delay)
        clear_console()

pvStr = str(3) +  "       "
item1 = False
item2 = False
item1M = False
item2M = False
logTxt = '\033[31mcaca boudn  iudnqwijhdbqwih b qwuib idwq qbw ihubqw'+'\033[0m'
logTxtBetter = logTxt + ''.join([' ' for i in range(132-len(logTxt))])
pvP = 3
pvPtxt = '<3 '*pvP
pvPtxtBetter = pvPtxt  + ''.join([' ' for i in range(9-len(pvPtxt))])
pvD = 3
pvDtxt = '<3 '*pvD
pvDtxtBetter = pvDtxt  + ''.join([' ' for i in range(9-len(pvDtxt))])
var = "\033[90m\033[9m"

txt = f"""

                                            \033[31m                           sxsccll"\033[0m
                                            \033[31m                      llllllllcclllllllr\033[0m
                                            \033[31m                   clllllllllllllllllllllll\033[0m
        ┏━━━━━━━━━━━━━━━━┓                  \033[31m                 >clrrllllllllllllllllllrrlc>\033[0m                            ┏━━━━━━━━━━━━━━━━┓
        ┃  \033[94m   PLAYER\033[0m     ┃                  \033[31m                ;vr%)<<)%llllllllllll%><>icrv;\033[0m                           ┃ \033[31m   MAFIOSO\033[0m     ┃
        ┃                ┃                  \033[31m               _^)=:,,:_:/illlllllc>='',;,,">^_\033[0m                          ┃                ┃
        ┃  PV : \033[94m{pvPtxtBetter}\033[0m┃                  \033[31m              ''<)>v<|/^_-'+vlllc>^_-:="))i<%  :\033[0m                         ┃  PV : \033[31m{pvDtxtBetter}\033[0m┃
        ┃                ┃                  \033[31m             `_,xxlc\033[90m┃ ┃\033[31mlc<'-_+%ll>;--^il\033[90m┃ ┃\033[31mlxv'__\033[0m                        ┃                ┃
        ┃  {var if item1 else ''}bag of powder\033[0m ┃                  \033[31m             __:%) \033[90m┃   ┃\033[31m</+=vrl)||/|i""\033[90m┃   ┃\033[31mii'__\033[0m                        ┃  {var if item1M else ''}bag of powder\033[0m ┃
        ┃                ┃                  \033[31m             ___^>x%\033[90m┃ ┃\033[31mxlrc+^+=^vrlli=="\033[90m┃ ┃\033[31m%<:___\033[0m                        ┃                ┃
        ┃  {var if item2 else ''}monocle\033[0m       ┃                  \033[31m              ___'^)>vlrrllc;-'__<lllrrci>|;____\033[0m                         ┃  {var if item1M else ''}monocle\033[0m       ┃
        ┃                ┃                  \033[31m               _____'^><)/^;^>xv";^+|<)):'_____\033[0m                          ┃                ┃
        ┃                ┃                  \033[31m                ^________-'/">l% );--________\033[0m                            ┃                ┃
        ┗━━━━━━━━━━━━━━━━┛                  \033[31m                  ________':::=,:::_________\033[0m                             ┗━━━━━━━━━━━━━━━━┛
                                            \033[31m                   _______________________-\033[0m
                                            \033[31m                     ____________________\033[0m
                                            \033[31m                    ______________________\033[0m
                                            \033[31m                   ________________________\033[0m
                                            \033[31m                  __________________________\033[0m
                                            \033[31m                 ____________________________\033[0m
                                            \033[31m                ______________________________\033[0m
                                            \033[31m               _______________________________-\033[0m
                                            \033[31m               ________________________________\033[0m
                                            \033[31m              __________________________________\033[0m
                                            \033[31m              `_------------------------------_`\033[0m
                            bkbbbbbbbbbbbbbbbbbbbbbbbbbbYG[?IIIIIIIIIIdqwdq************dqwdwIPYYbbbZbbYbbbbbbbbZbbYbbYbbYb
                          YYYAOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkkkkkkkkkkkkk&&&&&&&&&&kkkkkkkkkkkkkkkkYYZ
                        bYYOYbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbPJ1Ib*I!tzwGYbbbbbbbbbbbbbbbOYY
                       YYOYbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbYYYYkOOkkkOOOOO&6,.       okbbbbbbbbbbbbbbbbbYkYY
                     bYYkbbbbbbbbbbbbbbbbbbbbbbbYkkkkkkkkkkkkkkkkkkkkkkkkkAGgggh5ueaa[?[7oat]?;`      .1kbbbbbbbbbbbbbbbbbbOYYQ
                   GYYObbbbbbbbbbbbbbbbbbYOOOOkAh555555FFFFFFFFFFppppp6F2w7c````    \\              `-'<2YbbbbbbbbbbbbbbbbbbbYkYb
                 GYYOYbbbbbbbbbbbbbbbbbbYq#####C-                                               -':,+)16ZbbbbbbbbbbbbbbbbbbbbbbOYYg
                bYOYbbbbbbbbbbbbbbbbbbbbO%                                                 =/^+r17TySXYYbbbbbbbbbbbbbbbbbbbbbbbbYOYb
              bYYkbbbbbbbbbbbbbbbbbbbbbbGzdbbbbbb______dwqsssssrrrrrrrrxii%    _\\\\\%sc*7gggEZkkkkkYbbbbbbbbbbbbbbbbbbbbbbbbbbbbkYYd
            ZbYObbbbbbbbbbbbbbbbbbbbbbbbbYkkkkkkkkkkkkkkkkYYYYYYYYYYYYYYbbYYPPPPGZGGGGGkkkkYbYYbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbYOYY
          bYYOYbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbYYYYbbYYYYYbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbkYbY 
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃                                                                                                                                 ┃
        ┃    {logTxtBetter                                                                                                                         }  ┃
        ┃                                                                                                                                 ┃"""

print(txt)