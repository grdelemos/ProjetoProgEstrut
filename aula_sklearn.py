import pandas as pd
import numpy as np
from sklearn import tree

train = pd.read_csv('Treino_arvore.csv') 
y_train = train['caro?']
x_train = train.drop(['caro?'], axis=1).values 
decision_tree = tree.DecisionTreeClassifier()
decision_tree.fit(x_train, y_train)

with open("aula.dot", 'w') as f:
     f = tree.export_graphviz(decision_tree,
                              out_file=f,
                              max_depth = 20,
                              impurity = True,
                              feature_names = list(train.drop(['caro?'], axis=1)),
                              class_names = ['barato', 'media', 'caro'],
                              rounded = True,
                              filled= True )
        
        
       