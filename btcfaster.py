import os
path = "C:/"
os.chdir(path)

while True:
    balance = os.popen("bitcoin-cli -testnet -rpcuser=murat -rpcpassword=murat12 getbalance").read().replace('\n', '')
    murat="'""'" " '""'" " true"
    deneme=balance + " " + murat
    if balance != "0.00000000":
        print(balance)
        gonder = os.system("bitcoin-cli -testnet -rpcuser=murat -rpcpassword=murat12 sendtoaddress tb1qgcdn4yhcg5xdx5l36nnkrw0qklex4w5wx458eu" " " + deneme)
        print(gonder)
        print(balance)
