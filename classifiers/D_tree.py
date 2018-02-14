import graphviz
from sklearn.datasets import load_iris
from sklearn import tree
import pymysql
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
sentiment_selector=("SELECT id,Anger,Disgust,Fear,Joy,Sadness,Surprise FROM goal")
# os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")






# X = [[0, 0], [1, 1]]
# Y = [0, 1]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X, Y)
# print(clf.predict([[0., 1.]]))
