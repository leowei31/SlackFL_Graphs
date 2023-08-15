import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import csv
from matplotlib.legend_handler import HandlerLine2D

def make_graph(directory, slackfl_directory, graph_name):
    rounds = []
    train_loss = []
    slackfl_min = []
    slackfl_max = []
    with open(slackfl_directory, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rounds.append(int(row.get('round')))
            train_loss.append(float(row.get('average_test_accuracy')))
            temp = [float(row.get('test_accuracy_a')), float(row.get('test_accuracy_b')), float(row.get('test_accuracy_c')),float(row.get('test_accuracy_d')),float(row.get('test_accuracy_e'))]
            slackfl_min.append(min(temp))
            slackfl_max.append(max(temp))
        r0=np.array(rounds)
        t0=np.array(train_loss)

    rounds = []
    train_loss = []
    bonly_min = []
    bonly_max = []
    with open(directory +'BONLY-AvR_test_accuracy.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rounds.append(int(row.get('round')))
            train_loss.append(float(row.get('average_test_accuracy')))
            temp = [float(row.get('test_accuracy_a')), float(row.get('test_accuracy_b')), float(row.get('test_accuracy_c')),float(row.get('test_accuracy_d')),float(row.get('test_accuracy_e'))]
            bonly_min.append(min(temp))
            bonly_max.append(max(temp))
        r1=np.array(rounds)
        t1=np.array(train_loss)

    rounds = []
    train_loss = []
    cubc_max = []
    cubc_min = []
    with open(directory +'CUCB-AvR_test_accuracy.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rounds.append(int(row.get('round')))
            train_loss.append(float(row.get('average_test_accuracy')))
            temp = [float(row.get('test_accuracy_a')), float(row.get('test_accuracy_b')), float(row.get('test_accuracy_c')),float(row.get('test_accuracy_d')),float(row.get('test_accuracy_e'))]
            cubc_min.append(min(temp))
            cubc_max.append(max(temp))
        r2=np.array(rounds)
        t2=np.array(train_loss)     
    
    rounds = []
    train_loss = []
    poc_min = []
    poc_max = []

    with open(directory +'POC-AvR_test_accuracy.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rounds.append(int(row.get('round')))
            train_loss.append(float(row.get('average_test_accuracy')))
            temp = [float(row.get('test_accuracy_a')), float(row.get('test_accuracy_b')), float(row.get('test_accuracy_c')),float(row.get('test_accuracy_d')),float(row.get('test_accuracy_e'))]
            poc_min.append(min(temp))
            poc_max.append(max(temp))
        r4=np.array(rounds)
        t4=np.array(train_loss)   

    rounds = []
    train_loss = []
    withb_min = []
    withb_max = []
    with open(directory +'WITHB-AvR_test_accuracy.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rounds.append(int(row.get('round')))
            train_loss.append(float(row.get('average_test_accuracy')))
            temp = [float(row.get('test_accuracy_a')), float(row.get('test_accuracy_b')), float(row.get('test_accuracy_c')),float(row.get('test_accuracy_d')),float(row.get('test_accuracy_e'))]
            withb_min.append(min(temp))
            withb_max.append(max(temp))
        r5=np.array(rounds)
        t5=np.array(train_loss)   

    plt.rcParams["figure.figsize"] = (10,7)
        
    fig, ax = plt.subplots()
    # line1, = ax.plot(t1, marker='o', label='FedLE', linewidth=2)
    # line2, = ax.plot(t2, label='FedBO', linestyle='--')
    # line3, = ax.plot(t3, label='FedAvg-B', linewidth=0.9)
    line0, = ax.plot(t0, label='SlackFL (' + r'$\alpha$' +'=0.1)', linewidth=2, color = 'green' )
    line5, = ax.plot(t5, label='FedAvg-T', linewidth=2, color= 'purple')
    line1, = ax.plot(t1, label='FedAvg-Tonly', linewidth=2, color = 'blue')
    line2, = ax.plot(t2, label='Fed-cucb', linewidth=2, color= 'orange')
    # line3, = ax.plot(t3, label='SlackFL', linewidth=2)
    line4, = ax.plot(t4, label='pow-d', linewidth=2, color = 'red')

    ax.fill_between(range(len(t0)), t0, slackfl_min, color='green', alpha=0.1)
    ax.fill_between(range(len(t0)), t0, slackfl_max, color='green', alpha=0.1)
    ax.fill_between(range(len(t1)), t1, bonly_min, color='blue', alpha=0.1)
    ax.fill_between(range(len(t1)), t1, bonly_max, color='blue', alpha=0.1)
    ax.fill_between(range(len(t1)), t2, cubc_min, color='orange', alpha=0.1)
    ax.fill_between(range(len(t1)), t2, cubc_max, color='orange', alpha=0.1)
    # ax.fill_between(range(len(t1)), t3, FEDLE_min, color='green', alpha=0.1)
    # ax.fill_between(range(len(t1)), t3, FEDLE_max, color='green', alpha=0.1)
    ax.fill_between(range(len(t1)), t4, poc_min, color='red', alpha=0.1)
    ax.fill_between(range(len(t1)), t4, poc_max, color='red', alpha=0.1)
    ax.fill_between(range(len(t1)), t5, withb_min, color='purple', alpha=0.1)
    ax.fill_between(range(len(t1)), t5, withb_max, color='purple', alpha=0.1)

    ax.set_ylim(0, ax.get_ylim()[1])
    # plt.title("Server Accuracy", x=0.5, y=1.02)
    # plt.title("FedLE-CIFAR", x=0.5, y=1.02, fontsize=13)
    # plt.title(graph_name, x=0.5, y=1.02, fontsize=13)

    plt.xlabel('Training Rounds', fontsize=28)
    plt.ylabel('Test Accuracy', fontsize=28)
    plt.margins(x=0.01)
    ax.margins(x=0.01)
    # ax.legend(handler_map={line1: HandlerLine2D(numpoints=1)},prop={'size':11})
    legend = ax.legend(handler_map={line1: HandlerLine2D(numpoints=1)},prop={'size':20})
    legend.get_frame().set_alpha(0.5)

    plt.savefig( graph_name + '.pdf', format='pdf',dpi=1200,bbox_inches='tight')
