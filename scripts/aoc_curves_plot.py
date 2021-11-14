import matplotlib.pyplot as plt
from sklearn.metrics import auc


def aoc_curves_plot(AOC_data) -> None:
    """
    Con `aoc_curves_plot`, a partir de datos obtenidos con `aoc_curves_data`,
    hago los plots
    """
    fig,(ax1,ax2) = plt.subplots(nrows=1,ncols=2,figsize=(20,8))

    for data in AOC_data:
        (fpr, tpr, recalls, precisions, model) = data

        roc_auc = auc(fpr, tpr)
        pr_auc = auc(recalls, precisions)

        ax1.plot(fpr,tpr,label = "{}:{:.3f}".format(str(model)[:3],roc_auc))
        ax1.plot([0,1],[0,1],'--k', alpha=0.5)
        ax1.set_xlabel('False Positive Rate')
        ax1.set_ylabel('True Positive Rate')
        ax1.set_title('Curva ROC')
        ax1.legend()
        
        ax2.plot(recalls,precisions,label = "PR AOC:{:.3f}".format(pr_auc))
        ax2.plot([1,0],[0.5,1],'--k', alpha=0.5)
        ax2.set_xlabel('Recall')
        ax2.set_ylabel('Precisión')
        ax2.set_title('Curva PR')
        ax2.legend()

    plt.show()