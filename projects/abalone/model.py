import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from explainerdashboard import *

df = pd.read_csv('abalone_clear.csv',index_col=0)
df.reset_index(drop=True,inplace=True)
X = df.drop(['Sex','Rings'],axis=1)
y = df['Rings']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=245)

rf = RandomForestRegressor(n_estimators=300, max_depth=10, max_features=0.5)
rf.fit(X_train,y_train)

explainer = RegressionExplainer(rf,X_test,y_test)
db = ExplainerDashboard(explainer)
db.to_yaml("dashboard.yaml", explainerfile="explainer.joblib", dump_explainer=True)