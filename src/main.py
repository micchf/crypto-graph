from data.crypto_data import CryptoData

def main():
    test = CryptoData('BTCUSDT', '1m', 100)
    test.export_graph_image('prova')

if __name__ == '__main__':
    main()