import ctypes
import string
import os
import time
LICNECE = """
Olmaz#0 Nitro Generator
"""

USE_WEBHOOK = True

print(LICNECE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


try:  
    from discord_webhook import DiscordWebhook  
except ImportError:  
    
    input(
        f"şu kodu çalıştır '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\neğer webhook kullanmıyorsan bu mesajı önemseme.\ndevam etmek için enter bas.")
    USE_WEBHOOK = False
try:  
    import requests  
except ImportError:  
    
    input(
        f"şu kodu çalıştır '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nÇıkmak için enter")
    exit()  
try:  
    import numpy  
except ImportError:  
    
    input(
        f"şu kodu çalıştır '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nçıkmak için enter")
    exit()  


url = "https://github.com"
try:
    response = requests.get(url)  
    print("internetin kontrol ediliyor.")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    
    input("İnternete bağlı değilsin yada ananın amından internet çekiyorsun\nenter bas çıkmak için")
    exit()  


class NitroGen:  
    def __init__(self):  
        self.fileName = "Nitro Codes.txt"  

    def main(self):  
        os.system('cls' if os.name == 'nt' else 'clear') 
        if os.name == "nt":  
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator and Checker - Olmaz#0")  
        else:  
            print(f'\33]0;Nitro Generator and Checker - Olmaz#0\a',
                  end='', flush=True)  

        print(""" Olmaz#0 Nitro Generator-Checker
                                                        """)  
        time.sleep(2)  
        
        self.slowType("Olmaz#0/Goku Nitro Generator And Checkers", .02)
        time.sleep(1)  
        
        self.slowType(
            "\nKaç tane Kod Denenecek ", .02, newLine=False)

        try:
            num = int(input(''))  
        except ValueError:
            input(" numara yazmadın ki amına kodumun oğlu\nPress enter to exit")
            exit()  

        if USE_WEBHOOK:
            
            self.slowType(
                "Webhook kullanmak istersen yapıştır istemiyorsan enterla geç: ", .02, newLine=False)
            url = input('')  
            
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook(  
                        url=url,
                        content=f"```bakıyom nitro kodlarına\neğer biri çalışıyorsa çalışanını atacam```"
                    ).execute()

       

        valid = []  
        invalid = 0  
        chars = []
        chars[:0] = string.ascii_letters + string.digits

       
        c = numpy.random.choice(chars, size=[num, 16])
        for s in c:  
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"  

                result = self.quickChecker(url, webhook)  

                if result:  
                    
                    valid.append(url)
                else:  
                    invalid += 1  
            except KeyboardInterrupt:
                
                print("\nInterrupted by user")
                break  

            except Exception as e:  
                print(f" Error | {url} ")  

            if os.name == "nt":  
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Olmaz#0 - {len(valid)} Valid | {invalid} Invalid - Olmaz#0")  
                print("")
            else:  
               
                print(
                    f'\33]0;Olmaz#0 - {len(valid)} Valid | {invalid} Invalid - Olmaz#0\a', end='', flush=True)

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid)}""")  

        
        input("\nProgram çalışması bitti. çıkmak için 5 kere entera bas.")
        [input(i) for i in range(4, 0, -1)]  

    
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:  
            
            print(i, end="", flush=True)
            time.sleep(speed)  
        if newLine:  
            print()  

    def quickChecker(self, nitro:str, notify=None):  
       
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)  

        if response.status_code == 200: 
            
            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file: 
               
                file.write(nitro)

            if notify is not None:  
                DiscordWebhook( 
                    url=url,
                    content=f"Nitro kodu bulundu amk @everyone \n{nitro}"
                ).execute()

            return True  

       
        else:
            
            print(f" Invalid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False  


if __name__ == '__main__':
    Gen = NitroGen()  
    Gen.main()  
#ty for logicguy1