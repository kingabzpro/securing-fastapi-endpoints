from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
import joblib

X, y = load_wine(return_X_y=True, as_frame=False)
model = RandomForestClassifier(n_estimators=200, random_state=42).fit(X, y)
joblib.dump(model, "wine_clf.joblib")
