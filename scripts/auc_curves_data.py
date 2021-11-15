import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import precision_recall_curve, roc_curve


def auc_curves_data (model,feat,targ) -> tuple:
    """
    Con `auc_curves_data` obtengo datos necesarios para realizar AOC de ROC y PR.
    """
    predicted_p = cross_val_predict(model,feat,targ,cv=10,method="predict_proba")
    fpr, tpr, thres = roc_curve(targ, predicted_p[:,1])
    precisions, recalls, thres = precision_recall_curve(targ, predicted_p[:,1])

    return (fpr, tpr, recalls, precisions)