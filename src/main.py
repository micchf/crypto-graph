from data.crypto_data import CryptoData

def main():
    test = CryptoData('BTCUSDT', '1h', 1000)
    test.showGraph()

if __name__ == '__main__':
    main()