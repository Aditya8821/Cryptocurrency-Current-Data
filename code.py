import requests
print("\n1.Bitcoin \n2.Ethereum \n3.Dogecoin \n4.Litecoin \n5.Cardano \n6.Stellar  \n7.Polkadot\n ")
url='https://cryptantapi.root.sx/getPrice/'
a=input("Enter Currency Name: ")
print("\n-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
url+=a
response = requests.get(url)
status_code = response.status_code
if status_code == 200:
    print( "Currency: ", a)
    print( "Price in USD: ",response.json()['priceUsd'],'$')
    print( "Percentage change in 24 hrs: ",response.json()['percentChange24hUsd'],'%')
    print( "Last Updated: ",response.json()['lastUpdated'][:10])
else:
    print("Invalid Currency!!!")
print("Done")
