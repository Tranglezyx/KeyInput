from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 1. 加载示例数据（鸢尾花iris数据集）
iris = datasets.load_iris()
X = iris.data  # 特征（花瓣长度、宽度等等）
y = iris.target  # 标签（花的种类）

# 2. 分成训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 3. 选择一个模型（K最近邻分类器）
model = KNeighborsClassifier()

# 4. 训练模型
model.fit(X_train, y_train)

# 5. 测试模型
accuracy = model.score(X_test, y_test)

print(f"测试集准确率：{accuracy:.2f}")
