# -*- coding: utf-8 -*-
"""RF_test_AUC

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dArlnAjw-vA2Il42Z2nZooE8v-K8qFOj
"""

def RF_test_AUC(X_train, y_train, X_test, y_test, n_estimators = 100):
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.metrics import roc_auc_score
  rf = RandomForestClassifier(n_estimators = n_estimators)
  rf.fit(X_train, y_train.values.ravel())
  y_pred = rf.predict_proba(X_test)    
  return roc_auc_score(y_test, y_pred[:, 1])