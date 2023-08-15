from graph_battery_rounds import make_graph

def main():
    input_combinations=[
                ["CIFAR10-R/EMNIST-R/Final-Non-IID1-0.2-0.8-Alpha3/NIID1-",
                "CIFAR10-R/EMNIST-R/FEDLE-Alpha0.1/Final-Non-IID1-0.2-0.8-Alpha0.1/NIID1-fedle-AvR_Battery_Round-0.8.csv",
                 "EMNIST-NIID1_DP-80_HT-20_Battery"],
                ["CIFAR10-R/EMNIST-R/Final-Non-IID2-0.2-0.8-Alpha3/NIID2-",
                "CIFAR10-R/EMNIST-R/FEDLE-Alpha0.1/Final-Non-IID2-0.2-0.8-Alpha0.1/NIID2-fedle-AvR_Battery_Round-0.8.csv",
                "EMNIST-NIID2_DP-20_HT-80_Battery"],
                 
                ["CIFAR10-R/MNIST-R/Final-Non-IID1-0.2-0.8-Alpha3/NIID1-", 
                "CIFAR10-R/MNIST-R/FEDLE-Alpha0.1/MNIST-FEDLE-Alpha0.1/Final-Non-IID1-0.2-0.8-Alpha0.1/NIID1-fedle-AvR_Battery_Round-0.8.csv", 
                "MNIST-NIID1_DP-80_HT-20_Battery"],
                ["CIFAR10-R/MNIST-R/Final-Non-IID2-0.2-0.8-Alpha3/NIID2-",
                 "CIFAR10-R/MNIST-R/FEDLE-Alpha0.1/MNIST-FEDLE-Alpha0.1/Final-Non-IID2-0.2-0.8-Alpha0.1/NIID2-fedle-AvR_Battery_Round-0.8.csv",
                "MNIST-NIID2_DP-20_HT-80_Battery"],
                

                ['CIFAR10-R/FASHION-MNIST-R/Final-Non-IID1-0.2-0.8-Alpha3/NIID1-',
                 'CIFAR10-R/FASHION-MNIST-R/FEDLE-Alpha0.1/Final-Non-IID1-0.2-0.8-Alpha0.1/NIID1-FEDLE-AvR_Battery_Round-0.8.csv',
                 'FASHION-MNIST-NIID1_DP-80_HT-20_Battery'],
                ['CIFAR10-R/FASHION-MNIST-R/Final-Non-IID2-0.2-0.8-Alpha3/NIID2-',
                 'CIFAR10-R/FASHION-MNIST-R/FEDLE-Alpha0.1/Final-Non-IID2-0.2-0.8-Alpha0.1/NIID2-FEDLE-AvR_Battery_Round-0.8.csv',
                 'FASHION-MNIST-NIID2_DP-20_HT-80_Battery'],


                ['CIFAR10-R/CIFAR10-R/Final-Non-IID1-0.2-0.8-Alpha3/NIID1-',
                "CIFAR10-R/CIFAR10-R/FEDLE-Alpha0.1/Final-Non-IID1-0.2-0.8-Alpha0.1/NIID1-FEDLE-AvR_Battery_Round-0.8.csv",
                'CIFAR-10-NIID1_DP-80_HT-20_Battery'],
                 ['CIFAR10-R/CIFAR10-R/Final-Non-IID2-0.2-0.8-Alpha3/NIID2-',
                "CIFAR10-R/CIFAR10-R/FEDLE-Alpha0.1/Final-Non-IID2-0.2-0.8-Alpha0.1/NIID2-FEDLE-AvR_Battery_Round-0.8.csv",
                'CIFAR-10-NIID2_DP-20_HT-80_Battery'],

                ['CIFAR10-R/CIFAR-100-R/Final-Non-IID1-0.2-0.8-Alpha3/NIID1-',
                 'CIFAR10-R/CIFAR-100-R/FEDLE-Alpha0.1/Final-Non-IID1-0.2-0.8-Alpha0.1/NIID1-fedle-AvR_Battery_Round-0.8.csv',
                 'CIFAR-100-NIID1_DP-80_HT-20_Battery'],
                ['CIFAR10-R/CIFAR-100-R/Final-Non-IID2-0.2-0.8-Alpha3/NIID2-',
                 'CIFAR10-R/CIFAR-100-R/FEDLE-Alpha0.1/Final-Non-IID2-0.2-0.8-Alpha0.1/NIID2-fedle-AvR_Battery_Round-0.8.csv',
                 'CIFAR-100-NIID2_DP-20_HT-80_Battery'],
                ]
                
    for input_combination in input_combinations:
        make_graph(input_combination[0], input_combination[1], input_combination[2])

if __name__ == "__main__":
    main()