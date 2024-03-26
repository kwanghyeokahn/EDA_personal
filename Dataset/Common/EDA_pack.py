
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


class DataVisualizer:
    def __init__(self, data):
        self.data = data
    
    # 상관관계 히트맵
    def plot_correlation_heatmap(self):
        numeric_data = self.data.select_dtypes(include=[np.number])
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title('Correlation Heatmap')
        plt.show()
    # 명목형 변수 분포
    def plot_categorical_distribution(self, column):
        plt.figure(figsize=(10, 6))
        sns.countplot(x=column, data=self.data)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.show()
    # 수치형 변수 히스토그램
    def plot_numerical_distribution(self, column):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()
    # 박스 플롯    
    def box_plot(self, categorical_x, numerical_y):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=categorical_x, y=numerical_y, data=self.data)
        plt.title(f'Boxplot {categorical_x} of {numerical_y}')
        plt.xlabel(categorical_x)
        plt.ylabel(numerical_y)
        plt.show()
    # 박스플롯 & 히스토그램 플롯    
    def box_his_plot(self, categorical_col, numerical_col):
        g = sns.FacetGrid(data=self.data, col=categorical_col, height=4, aspect=1)
        g.map_dataframe(sns.boxplot, x=numerical_col, color="red", flierprops=dict(markerfacecolor='red', marker='D'))
        g.map_dataframe(sns.histplot, x=numerical_col, kde=True, color="skyblue", alpha=0.7)
        g.set_axis_labels(f'{numerical_col}', "Frequency")
        g.set_titles(col_template="{col_name}")
        g.set(ylim=(0, 25), xlim=(0, 60))
        plt.show()
        
        
    ## plotly 패키지 활용
    # 박스플롯 & 히스토그램 플롯
    def plotly_box_his_plot(self,column):
        fig = px.histogram(self.data[column], nbins=10, marginal='box', labels={'value':str(column)})
        fig.update_layout(title_text='Box plot and Histogram')
        fig.show()