def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
 
 

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
 
 

def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
 
 

def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
 
 

def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
 
 

def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
 
 

def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
 
 

def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
 
 

prCyan("""
██╗ ██████╗ ███████╗
██║██╔════╝ ██╔════╝
██║██║  ███╗█████╗  
██║██║   ██║██╔══╝  
██║╚██████╔╝██║     
╚═╝ ╚═════╝ ╚═""")

prYellow("""
 TEAM: _____              _               
 |  ___|_ _  ___ ___| | ___  ___ ___ 
 | |_ / _` |/ __/ _ \ |/ _ \/ __/ __|
 |  _| (_| | (_|  __/ |  __/\__ \__ \
 |_|  \__,_|\___\___|_|\___||___/___/
                                     
""")

prGreen("AUTHOR: ABUTALHA")


# importing the necessary packages 

import time 

import sys 

import os 

  
# Function for implementing the loading animation 

def load_animation(): 

  

    # String to be displayed when the application is loading 

    load_str = "𝙄𝙉𝙎𝙏𝘼 𝙄𝙉𝙁𝙊𝙍𝙈𝘼𝙏𝙄𝙊𝙉 𝙏𝙊𝙊𝙇 𝙇𝙊𝘼𝘿 𝙁𝙊𝙍 𝘽𝙊𝙊𝙈"

    ls_len = len(load_str) 

  

  

    # String for creating the rotating line 

    animation = "|/-\\"

    anicount = 0

      

    # used to keep the track of 

    # the duration of animation 

    counttime = 0        

      

    # pointer for travelling the loading string 

    i = 0                     

  

    while (counttime != 100): 

          

        # used to change the animation speed 

        # smaller the value, faster will be the animation 

        time.sleep(0.075)  

                              

        # converting the string to list 

        # as string is immutable 

        load_str_list = list(load_str)  

          

        # x->obtaining the ASCII code 

        x = ord(load_str_list[i]) 

          

        # y->for storing altered ASCII code 

        y = 0                             

  

        # if the character is "." or " ", keep it unaltered 

        # switch uppercase to lowercase and vice-versa  

        if x != 32 and x != 46:              

            if x>90: 

                y = x-32

            else: 

                y = x + 32

            load_str_list[i]= chr(y) 

          

        # for storing the resultant string 

        res =''              

        for j in range(ls_len): 

            res = res + load_str_list[j] 

              

        # displaying the resultant string 

        sys.stdout.write("\r"+res + animation[anicount]) 

        sys.stdout.flush() 

  

        # Assigning loading string 

        # to the resultant string 

        load_str = res 

  

          

        anicount = (anicount + 1)% 4

        i =(i + 1)% ls_len 

        counttime = counttime + 1

      

    # for windows OS 

    if os.name =="nt": 

        os.system("cls") 

          

    # for linux / Mac OS 

    else: 

        os.system("clear") 

  
# Driver program 

if __name__ == '__main__':  

    load_animation() 

  

    # Your desired code continues from here  

    # s = input("Enter your name: ") 

    s ="Loading"





import instaloader, sys

def banner():
        print("""
██╗ ██████╗ ███████╗
██║██╔════╝ ██╔════╝
██║██║  ███╗█████╗  
██║██║   ██║██╔══╝  
██║╚██████╔╝██║     
╚═╝ ╚═════╝ ╚═╝     
TOOL FOR INSTAGRAM                    
\033[0m
\033[41m# Coder Abutalha/Faceless\033[1;0m | \033[\033[0m
""")

banner()

x = instaloader.Instaloader()

#Login dulu
try:
	uname = input("\033[1;36mUsername: \033[0;30m")
	passwd = input("\033[1;36mPassword: \033[0;30m")

	x.login(uname,passwd)
	print("\033[1;32mLogin successful...")

except:
	print("\033[1;31mLogin failed!")
	sys.exit()

#Suruh user masukin username target
username = input("\033[1;32mMasukkan username: \33[0m")
if username == "":
	print("\033[1;31mUser not found!")
	sys.exit()

y = instaloader.Profile.from_username(x.context, username)

print("\033[1;32mUsername : \033[0m",y.username)
print("\033[1;32mID : \033[0m",y.userid)
print("\033[1;32mNama : \033[0m",y.full_name)
print("\033[1;32mTerverifikasi : \033[0m",y.is_verified)
print("\033[1;32mDiprivasi : \033[0m",y.is_private)
print("\033[1;32mAkun bisnis : \033[0m",y.is_business_account)
print("\033[1;32mNama kategori bisnis : \033[0m",y.business_category_name)
print("\033[1;32mBiografi : \033[0m",y.biography)
print("\033[1;32mPengikut : \033[0m",y.followers)
print("\033[1;32mMengikuti : \033[0m",y.followees)
print("\033[1;32mURL foto profil : \033[0m",y.profile_pic_url)
print("\033[1;32mURL eksternal : \033[0m",y.external_url)
print("\033[1;32mPostingan : \033[0m",y.mediacount)
print("\033[1;32mIGTV : \033[0m",y.igtvcount)
print("\033[1;32mMemiliki cerita yang dapat dilihat : \033[0m",y.has_viewable_story)
print("\033[1;32mMemiliki cerita publik : \033[0m",y.has_public_story)
print("\033[1;32mMemiliki sorotan : \033[0m",y.has_highlight_reels)
print("\033[1;32mDiikuti user lain : \033[0m",y.followed_by_viewer)
print("\033[1;32mMengikuti user lain : \033[0m",y.follows_viewer)
print("\033[1;32mDiblokir user lain : \033[0m",y.blocked_by_viewer)
print("\033[1;32mPernah memblokir user lain : \033[0m",y.has_blocked_viewer)
print("\033[1;32mDiminta user lain : \033[0m",y.requested_by_viewer)
print("\033[1;32mMeminta user lain : \033[0m",y.has_requested_viewer)
for i in y.get_followers():
	print("\033[1;32mPengikut : \033[0m",i)
for i in y.get_followees():
	print("\033[1;32mMengikuti : \033[0m",i)
for i in y.get_similar_accounts():
	print("\033[1;32mAkun serupa : \033[0m",i)
