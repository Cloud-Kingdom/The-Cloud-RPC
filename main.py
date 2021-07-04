from pypresence import Presence
import time
import json
import colorama

with open("./config.json", "r") as configjsonFile:
    configData = json.load(configjsonFile)
    STATE = configData["state"]
    DETAILS = configData["details"]
    LIK = configData["largeimagekey"]
    LIT = configData["largeimagetext"]
    SIK = configData["smallimagekey"]
    SIT = configData["smallimagetext"]
    CID = configData["clientid"]
    URL1 = configData["url1"]
    URL2 = configData["url2"]
    B1 = configData["b1"]
    B2 = configData["b2"]

    class bcolors:
        HEADER = "\033[0m"
        OKBLUE = "\033[94m"
        OKCYAN = "\033[96m"
        OKGREEN = "\033[92m"
        WARNING = "\033[93m"
        FAIL = "\033[91m"
        ENDC = "\033[0m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"

    time_AMPM = time.localtime()  # get struct_time
    start_time = time.strftime(
        f"[{bcolors.OKGREEN}%H:%M:%S %p{bcolors.HEADER}]", time_AMPM
    )


RPC = Presence(client_id=CID)
RPC.connect()


RPC.update(
    state=STATE,
    details=DETAILS,
    large_image=LIK,
    large_text=LIT,
    small_image=SIK,
    small_text=SIT,
    buttons=[{"label": B1, "url": URL1}, {"label": B2, "url": URL2}],
)
colorama.init()
print("\033[2J")
print(
    "Thanks for running the Cloud RPC Python Script\nMade by Jellisy#3301\n\nScript has started at",
    start_time,
    "\n",
)
while 1:
    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime(
        f"[{bcolors.OKGREEN}%H:%M:%S %p{bcolors.HEADER}]", named_tuple
    )
    print(time_string, "The Cloud RPC is running")
    time.sleep(15)  # Can only update presence every 15 seconds
