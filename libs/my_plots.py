
import imp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import model_selection
from sklearn import metrics



def plot_learning_curve(model, X, y, cv, scoring='f1', ax=None, title=""):
    train_size, train_scores, valid_scores = model_selection.learning_curve(
        estimator=model,
        X=X,
        y=y,
        cv=cv,
        scoring=scoring
    )
    train_scores_mean = np.mean(train_scores, axis=1)
    valid_scores_mean = np.mean(valid_scores, axis=1)
    
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 5))
    
    ax.plot(train_size, train_scores_mean, label='train')
    ax.plot(train_size, valid_scores_mean, label='valid')
    ax.set_title('Learning curve '+title)
    ax.set_xlabel('train size')
    ax.set_ylabel(scoring + ' score')
    ax.xaxis.set_ticks(train_size)
    ax.set_ylim(0, 1)
    ax.legend()
    
    
#Функция для визуализации модели
def plot_probabilities_2d(X, y, model):
    #Генерируем координатную сетку из всех возможных значений для признаков
    #Glucose изменяется от x1_min = 44 до x2_max = 199, 
    #BMI — от x2_min = 18.2 до x2_max = 67.1
    #Результат работы функции — два массива xx1 и xx2, которые образуют координатную сетку
    xx1, xx2 = np.meshgrid(
        np.arange(X.iloc[:, 0].min()-1, X.iloc[:, 0].max()+1, 0.1),
        np.arange(X.iloc[:, 1].min()-1, X.iloc[:, 1].max()+1, 0.1)
    )
    #Вытягиваем каждый из массивов в вектор-столбец — reshape(-1, 1)
    #Объединяем два столбца в таблицу с помощью hstack
    X_net = np.hstack([xx1.reshape(-1, 1), xx2.reshape(-1, 1)])
    #Предсказываем вероятность для всех точек на координатной сетке
    #Нам нужна только вероятность класса 1
    probs = model.predict_proba(X_net)[:, 1]
    #Переводим столбец из вероятностей в размер координатной сетки
    probs = probs.reshape(xx1.shape)
    #Создаём фигуру и координатную плоскость
    fig, ax = plt.subplots(figsize = (10, 5))
    #Рисуем тепловую карту вероятностей
    contour = ax.contourf(xx1, xx2, probs, 100, cmap='bwr')
    #Рисуем разделяющую плоскость — линию, где вероятность равна 0.5
    bound = ax.contour(xx1, xx2, probs, [0.5], linewidths=2, colors='black');
    #Добавляем цветовую панель 
    colorbar = fig.colorbar(contour)
    #Накладываем поверх тепловой карты диаграмму рассеяния
    sns.scatterplot(x=X.iloc[:, 0], y=X.iloc[:, 1], hue=y, palette='seismic', ax=ax)
    #Даём графику название
    ax.set_title('Scatter Plot with Decision Boundary');
    #Смещаем легенду в верхний левый угол вне графика
    ax.legend(bbox_to_anchor=(-0.05, 1))
    
def plot_pr_find_value(model, X, y, cv, method='predict_proba', col=1):
    y_cv_proba_pred = model_selection.cross_val_predict(model, X, y, cv=cv, method='predict_proba') 
    y_cv_proba_pred = y_cv_proba_pred[:,col]
    precission, recall, threholds = metrics.precision_recall_curve(y, y_cv_proba_pred)
    
    f1_score = 2*precission*recall/(precission+recall)
    idx = np.argmax(f1_score)

    print(f'Best threholds = {round(threholds[idx], 2)}, f1_score = {round(f1_score[idx], 2)}')

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(precission, recall, label='Desigion tree PR')
    ax.scatter(precission[idx], recall[idx], label='best f1 score', marker='o', color='black')
    ax.set_title('Precision-recall curve')
    ax.set_xlabel('Recall')
    ax.set_ylabel('precision')
    ax.legend()
    
    return threholds[idx], f1_score[idx]