#!/usr/bin/env python
# coding: utf-8

# # Problemática

# Realizar a leitura de uma base de dados de nascidos vivos provenientes da base do DataSUS e apresentar dados descritivos para melhor análise dos resultados

# # Importar biblioteca

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')


# # Leitura dos dados

# In[2]:


df=pd.read_csv('./sinasc_ro_2019.csv')
df.head(5)


# # Configurações no dataframe

# In[3]:


# Exibir todas as colunas
pd.set_option('max_columns', None)

#Transformar colunas para o snake case
df.columns = df.columns.str.lower()

df.head(5)


# # Configurações gráficas seaborn

# In[85]:


sns.set_style(style='darkgrid')


# # Boxplot com idade da mãe

# In[86]:


# Boxplot com pandas
plt.figure()
df['idademae'].plot.box()
plt.show()


# In[87]:


# Boxplot com seaborn
plt.figure()
sns.boxplot(y='idademae', data=df, color='yellow')
plt.show()


# # Boxplot do peso do bêbe

# In[88]:


# Boxplot com pandas
plt.figure()
df['peso'].plot.box()
plt.show()


# In[89]:


# Boxplot com seaborn
plt.figure()
sns.boxplot(y='peso', data=df, color='red')
plt.show()


# # Histograma com idade da mãe

# In[90]:


# Histograma com pandas
plt.figure()
df['idademae'].hist()
plt.show()


# In[91]:


# Histograma com seaborn
sns.displot(data=df,
           x='idademae',
           bins=20,
           alpha=.25,
           element='step',
           kde=True)


# # Histograma com peso do bêbe

# In[92]:


# Histograma com pandas
plt.figure()
df['peso'].hist()
plt.show()


# In[93]:


# Histograma com seaborn
sns.displot(data=df,
           x='peso',
           bins=20,
           alpha=.50,
           element='step',
           kde=True,
           color='red')

