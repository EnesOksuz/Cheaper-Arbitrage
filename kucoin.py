import requests
def get_all_coins():
    coins2=[]
    kucoin_cur = "https://api.kucoin.com/api/v1/currencies"
    res_kucoin_cur= requests.get(kucoin_cur).json()
    for x in range(len(res_kucoin_cur["data"])):
        coins2.append(res_kucoin_cur["data"][x]["currency"])
    coins=list(dict.fromkeys(coins2))
    return coins

def find_cheap_chains(coin_name):
    solana_coins=[]
    avax_coins=[]
    matic_coins=[]
    bsc_coins=[]
    for x in range(len(coin_name)):
        kucoin_currency_detail = requests.get(f"https://api.kucoin.com/api/v2/currencies/{coin_name[x]}").json()
        for y in range(len(kucoin_currency_detail["data"]["chains"])):
            
            if(kucoin_currency_detail["data"]["chains"][y]["chainName"]=="SPL(Solana)"):
                solana_coins.append(coin_name[x])
                print("done1")
            elif(kucoin_currency_detail["data"]["chains"][y]["chainName"]=="AVAX"):
                avax_coins.append(coin_name[x])
                print("done2")
            elif(kucoin_currency_detail["data"]["chains"][y]["chainName"]=="MATIC"):
                matic_coins.append(coin_name[x])
                print("done3")
            elif(kucoin_currency_detail["data"]["chains"][y]["chainName"]=="BEP20"):
                bsc_coins.append(coin_name[x])
                print("done4")
            


    print(solana_coins)
    print(avax_coins)
    print(matic_coins)
    print(bsc_coins)
    print("done")
find_cheap_chains(get_all_coins())