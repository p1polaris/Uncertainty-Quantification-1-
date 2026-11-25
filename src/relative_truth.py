import numpy as np

def compute_confusion_matrix(y_true, y_pred, labels):
    """Return confusion matrix. y_true/y_pred are 1-D label arrays."""
    import numpy as np
    cm = np.zeros((len(labels), len(labels)), dtype=int)
    idx = {lab: i for i, lab in enumerate(labels)}
    for t, p in zip(y_true, y_pred):
        cm[idx[t], idx[p]] += 1
    return cm

def class_fvc(class_raster, fvc_raster, class_value):
    """Area-weighted mean FVC within pixels of a given class."""
    import numpy as np
    mask = class_raster == class_value
    if mask.sum() == 0:
        return np.nan
    return float(np.nanmean(fvc_raster[mask]))

def build_relative_truth(class_raster, fvc_raster, labels):
    """Return {class: FVC} relative truth."""
    return {lab: class_fvc(class_raster, fvc_raster, lab) for lab in labels}