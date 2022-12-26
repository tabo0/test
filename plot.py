from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import  torch
import  random
#import pandas as pd
def prune():
    # 练习的数据：
    data1 = np.load('D:\code\py\\test\\headPrune.npy')-0.05
    data2 = np.load('D:\code\py\\test\\ffnPrune.npy')-0.05
    #data = pd.DataFrame(data)
    fig, axes = plt.subplots(1, 2)
    # 绘制热度图：
    x=[ round(3/14*(i+1),1)for i in range(14)]
    y=[i+1 for i in range(12)]
    plt1=sns.heatmap(data1.T,ax=axes[0],xticklabels=x,yticklabels=y, cmap="YlGnBu")
    plt1.set_title('Per-layer MHA Pruning Rate')
    plt1.set_xlabel('Epoch')
    plt1.set_ylabel('Layer')
    plt2=sns.heatmap(data2.T,ax=axes[1],xticklabels=x,yticklabels=y, cmap="YlGnBu")
    plt2.set_title('Per-layer FFN Pruning Rate')
    plt2.set_xlabel('Epoch')
    plt2.set_ylabel('Layer')
    plt.show()
def avg():
    # 练习的数据：
    data1 = np.load('D:\code\py\\test\\ProbMean.npy')

    # 绘制热度图：
    x=[ round(3/14*(i+1),1)for i in range(14)]
    y=[i+1 for i in range(12)]
    plt1=sns.heatmap(data1.T,xticklabels=x,yticklabels=y,cmap = 'RdBu')
    plt1.set_title('Mean value of attention probs')
    plt1.set_xlabel('Epoch')
    plt1.set_ylabel('Layer')
    plt.show()

def ablation():
    # 构造x轴刻度标签、数据
    labels = ['NDCG@10', 'Hit@10']
    first = [36.22, 36.00,36.08,35.98]
    second = [52.47, 52.03, 53.16, 52.23]
    # 三组数据
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 3))
    l=['Alg','$alg_{w/o \\, \\alpha}$','$alg_{w/o \\, \\beta}$','$alg_{w/o \\, w}$']
    width = 0.05
    x =  [ width *i for i in range(4)]  # x轴刻度标签位置
    x1 = [width  * (i+6) for i in range(4)]
    # 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
    for i in range(4):
        ax1.bar(x[i], first[i], width, label=l[i],alpha=0.8)
    ax1.set_ylim(34, 37)
    ax1.set_xticks([0.075,0.375])
    ax1.set_xticklabels(labels)

    plt1 = ax1.twinx()
    for i in range(4):
        plt1.bar(x1[i], second[i], width, label=l[i],alpha=0.8)
    plt1.set_ylim(51, 54)

    #---------------------------------------------
    first = [54.72, 53.97,54.00,49.78]
    second = [75.71, 75.46, 75.26, 71.47]

    width = 0.05
    x =  [ width *i for i in range(4)]  # x轴刻度标签位置
    x1 = [width  * (i+6) for i in range(4)]
    # 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
    for i in range(4):
        ax2.bar(x[i], first[i], width, label=l[i],alpha=0.8)
    ax2.set_ylim(49, 55)

    ax2.set_xticks([0.075,0.375])
    ax2.set_xticklabels(labels)
    plt2 = ax2.twinx()
    for i in range(4):
        plt2.bar(x1[i], second[i], width, label=l[i],alpha=0.8)
    plt2.set_ylim(71, 76)
    #------------------------------------------------
    first = [57.91, 57.57,57.67,57.10]
    second = [76.88, 77.04, 77.06, 76.68]


    width = 0.05
    x =  [ width *i for i in range(4)]  # x轴刻度标签位置
    x1 = [width  * (i+6) for i in range(4)]
    # 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
    for i in range(4):
        ax3.bar(x[i], first[i], width, label=l[i],alpha=0.8)
    ax3.set_ylim(57, 58)
    ax3.set_xticks([0.075,0.375])
    ax3.set_xticklabels(labels)

    plt3 = ax3.twinx()
    for i in range(4):
        plt3.bar(x1[i], second[i], width, label=l[i],alpha=0.8)
    plt3.set_ylim(76, 78)
    # ax1.bar(x - 0.5 * width, second, width, label='$alg_{w/o \\, \\alpha}$')
    # plt1 = ax1.twinx()
    # plt1.bar(x + 0.5 * width, third, width, label='$alg_{w/o \\, \\beta}$')
    # plt1.bar(x + 1.5 * width, fourth, width, label='$alg_{w/o \\, w}$')




    # plt.legend(loc=0, prop={'size': 16})

    ax2.legend(loc='center', bbox_to_anchor=(0.5, 1.05),ncol=4, prop={'size': 20})

    plt.show()
def zhexian():

    game = ['1', '2', '3', '4']

    beauty1 = [35.47, 35.90, 36.22, 35.53]
    beauty2 = [51.40, 52.19, 52.47, 51.23]
    s=20
    fig, (ax1,ax2,ax3) =plt.subplots( 1, 3, figsize=(10,3))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5)
    plt1 = ax1.twinx()
    lns1=ax1.plot(game, beauty1, c='red', label="NDCG@10")
    lns2=plt1.plot(game, beauty2, c='green', linestyle='--', label="Hit@10")
    ax1.scatter(game, beauty1, marker='v', c='red')
    plt1.scatter(game, beauty2, marker='s', c='green')
    lns = lns1 + lns2
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc=0, prop={'size': s})
    cd1 = [54.28, 57.01, 57.91, 57.23]
    cd2 = [74.01, 76.20, 76.88, 76.58]
    plt2 = ax2.twinx()
    lns1=ax2.plot(game, cd1, c='red', label="NDCG@10")
    lns2=plt2.plot(game, cd2, c='green', linestyle='--', label="Hit@10")
    ax2.scatter(game, cd1, marker='v', c='red')
    plt2.scatter(game, cd2, marker='s', c='green')
    lns = lns1 + lns2
    labs = [l.get_label() for l in lns]
    ax2.legend(lns, labs, loc=0, prop={'size': s})


    game1 = [49.48, 53.89, 54.72, 52.45]
    game2 = [71.34, 74.79, 75.71, 73.61]
    plt3 = ax3.twinx()
    lns1=ax3.plot(game, game1, c='red', label="NDCG@10")
    lns2=plt3.plot(game, game2, c='green', linestyle='--', label="Hit@10")
    ax3.scatter(game, game1, marker='v', c='red')
    plt3.scatter(game, game2, marker='s', c='green')
    lns = lns1 + lns2
    labs = [l.get_label() for l in lns]
    ax3.legend(lns, labs, loc=0, prop={'size': s})
    plt.show()

    #         L = 1 & 35.47 & 51.40 & 54.28 & 74.01 & 49.48 & 71.34\ \
    #         L = 2 & 35.90 & 52.19 & 57.01 & 76.20 & 53.89 & 74.79\ \
    #         L = 3 & 36.22 & 52.47 & 57.91 & 76.88 & 54.00 & 75.26\ \
    #         L = 4 & 35.53 & 51.23 & 57.23 & 76.58 & 52.45 & 73.61

def pca(x,x1,x2,x3):

    x_dr = PCA(2).fit_transform(x)
    x1 = PCA(2).fit_transform(x1)
    x2 = PCA(2).fit_transform(x2)
    x3 = PCA(2).fit_transform(x3)
    fig,(ax1) = plt.subplots(1, 1, figsize=(6, 3))

    rng = np.random.RandomState(0)
    colors = rng.rand(x1.shape[0])
    sizes = 100 * rng.rand(x1.shape[0])
    colors1 = rng.rand(x1.shape[0])
    sizes1 = 100 * rng.rand(x1.shape[0])
    colors2 = rng.rand(x1.shape[0])
    sizes2 = 100 * rng.rand(x1.shape[0])
    colors3 = rng.rand(x1.shape[0])
    sizes3 = 100 * rng.rand(x1.shape[0])
    ax1.scatter(x1[:,0],x1[:,1], c=colors1, s=sizes1, alpha=0.5, cmap='viridis', label="$alg_{w/o \\, \\alpha}$")
    ax1.scatter(x2[:, 0], x2[:, 1], c=colors2, s=sizes2, alpha=0.5, cmap='viridis', marker='s', label="$alg_{w/o \\, \\beta}$")
    ax1.scatter(x3[:, 0], x3[:, 1], c=colors3, s=sizes3, alpha=0.5, cmap='viridis', marker='D', label="$alg_{w/o \\, w}$")
    ax1.scatter(x_dr[:,0],x_dr[:,1], c=colors, s=sizes, alpha=0.5, cmap='viridis', marker='v', label="alg")
    # ax1.legend(loc=0, prop={'size': 20})

    # left, bottom, width, height = 0.15, 0.7, 0.15, 0.15
    # ax2 = fig.add_axes([left, bottom, width, height])
    # ax2.scatter(x1[:,0],x1[:,1], c=colors1, s=sizes1, alpha=0.5, cmap='viridis', label="$alg_{w/o \\, \\alpha}$")
    # ax2.scatter(x2[:, 0], x2[:, 1], c=colors2, s=sizes2, alpha=0.5, cmap='viridis', marker='s', label="$alg_{w/o \\, \\beta}$")
    # ax2.scatter(x3[:, 0], x3[:, 1], c=colors3, s=sizes3, alpha=0.5, cmap='viridis', marker='D', label="$alg_{w/o \\, w}$")
    # ax2.scatter(x_dr[:,0],x_dr[:,1], c=colors, s=sizes, alpha=0.5, cmap='viridis', marker='v', label="alg")

    plt.show()
if __name__=='__main__':
    # avg()
    # ablation()
    # path = 'D:\software\ecnu\onedrive\桌面\DGSR/Games_ba_50_G_0_dim_50_UM_50_IM_50_K_2_layer_3_l2_0.0001_usel2_False_usexTime_True_usejTime_True_duibi_False_0.5_1e-06_topk_no_useOld_False_seed_3407_updateNode.pkl'
    # model = torch.load(path,map_location=torch.device('cpu'))
    # path1 = 'D:\software\ecnu\onedrive\桌面\DGSR/Games_ba_50_G_1_dim_50_UM_50_IM_50_K_2_layer_3_l2_0.0001_usel2_False_usexTime_False_usejTime_True_duibi_False_0.5_1e-06_topk_no_useOld_False_seed_3407_updateNode.pkl'
    # model1 = torch.load(path1,map_location=torch.device('cpu'))
    # path2 = 'D:\software\ecnu\onedrive\桌面\DGSR/Games_ba_50_G_1_dim_50_UM_50_IM_50_K_2_layer_3_l2_0.0001_usel2_False_usexTime_True_usejTime_False_duibi_False_0.5_1e-06_topk_no_useOld_False_seed_3407_updateNode.pkl'
    # model2 = torch.load(path2,map_location=torch.device('cpu'))
    #
    # path3='D:\software\ecnu\onedrive\桌面\DGSR/Games_ba_50_G_1_dim_50_UM_50_IM_50_K_2_layer_3_l2_0.0001_usel2_False_usexTime_True_usejTime_True_duibi_False_0.5_1e-06_topk_no_useOld_True_seed_3407.pkl'
    # model3 = torch.load(path3, map_location=torch.device('cpu'))
    zhexian()
    # pca(model['item_embedding.weight'],model1['item_embedding.weight'],model2['item_embedding.weight'],model3['item_embedding.weight'])
