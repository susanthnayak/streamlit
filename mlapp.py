import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
#from sklearn.tree import DecissionTree
#from sklearn.naive_bayes import KNeibhours
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

st.title('Data Science Aap')

def main():
	activities=['EDA','Data Visualisation','Model_Building','About Us']
	option=st.sidebar.selectbox('select option ',activities)

	if option=='EDA':
		st.subheader('Exploratory Data Analysis')
		data=st.file_uploader('Please upload your file',type='csv')
		st.success('You have successfully uploaded your file')

		if data is not None:
			df=pd.read_csv(data)
			st.dataframe(df.head())
			if st.checkbox('Display shape'):
				st.write(df.shape)
			if st.checkbox('Display the columns'):
				st.write(df.columns)
			if st.checkbox('select multiple columns'):
				selected_coluumns=st.multiselect('select your preferred columns',df.columns)
				df1=df[selected_coluumns]
				st.dataframe(df1)
			if st.checkbox('Display the summary'):
				st.write(df.describe())
			if st.checkbox('Look for the null values'):
				st.write(df.isnull().sum())
			if st.checkbox('Display the data types'):
				st.write(df.dtypes)
			if st.checkbox('Display correlation between the variables'):
				st.write(df.corr())
if __name__ == '__main__':
	main()