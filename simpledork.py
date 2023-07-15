import sys
import random
import time
from fake_useragent import UserAgent
import subprocess

try:
    from googlesearch import search
except ImportError:
    print("SimpleDork requires python google lib to be installed!")
    print("Please run pip install google")
 
print("""

░██████╗██╗███╗░░░███╗██████╗░██╗░░░░░███████╗██████╗░░█████╗░██████╗░██╗░░██╗
██╔════╝██║████╗░████║██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
╚█████╗░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░██║░░██║██║░░██║██████╔╝█████═╝░
░╚═══██╗██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░██║░░██║██║░░██║██╔══██╗██╔═██╗░
██████╔╝██║██║░╚═╝░██║██║░░░░░███████╗███████╗██████╔╝╚█████╔╝██║░░██║██║░╚██╗
╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
""")

ua = UserAgent()

if len(sys.argv) >= 3:
	if __name__ == "__main__":
		query = sys.argv[1]
		pages = int(sys.argv[2])
		querysleep = int(sys.argv[3])
                
		print("\x1b[0;30;41mA longer sleeptime between each Google search is recommended to prevent Google CAPTCHA\x1b[0m\n")
		print("\x1b[0;30;41mTo prevent google captcha this is going to take a while. Go grab a coffee! ;)\x1b[0m\n")
	try:
		for j in search(query, tld="co.in", num=pages, stop=pages, pause=querysleep + random.randrange(10, 100), user_agent=ua.random):
			print(j)
	except Exception as e:
		print(f"An error occurred during the search: {e}")
else:
	print("Usage: python3 simpledork.py QUERY AMOUNTOFPAGESTOSEARCH SLEEPTIMEBETWEENSEARCH")
	print("Example: python3 simpledork.py inurl:" + '"' + "/admin/login.php" +'"' + " 10 10")
sys.exit(1)

	
