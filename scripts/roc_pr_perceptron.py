import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, auc, roc_curve

def roc_pr_percetron(targ_train, y_scores, model) -> None:
    """
    Grafica la curva PR y ROC de un perceptrón
    """

    precisions, recalls, thresholds = precision_recall_curve(targ_train, y_scores)
    fpr, tpr, thresholds = roc_curve(targ_train, y_scores)

    auc_score_PR = auc(recalls, precisions)
    auc_score_ROC = auc(fpr,tpr)

    fig = plt.figure(figsize=(18, 6))
    ax = fig.add_subplot(122)
    ax.plot(recalls,precisions, label = "AUC PR: {:.3f}".format(auc_score_PR))
    ax.plot([0, 1], [1, 0], color='0.5', ls=':')
    ax.set_xlabel('Recall')
    ax.set_ylabel('Precision')
    ax.set_title('Curva PR')
    ax.legend(loc='lower right', fontsize=14)

    ax2 = fig.add_subplot(121)
    ax2.plot(fpr, tpr,label = "AUC ROC: {:.3f}".format(auc_score_ROC))
    ax2.plot([0, 1], [0, 1], color='0.5', ls=':')
    ax2.set_xlabel('Tasa de falsos positivos (FPR)')
    ax2.set_ylabel('Tasa de verdaderos positivos (TPR) / Recall')
    ax2.set_title('Curva ROC')
    ax2.legend(loc='lower right', fontsize=14)

    AUC_data=[]
    AUC_data.append((fpr, tpr, recalls, precisions, model))
    
    return AUC_data