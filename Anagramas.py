#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importando das bibliotecas para uso
import itertools
import pandas as pd


# In[2]:


#DEFININDO DAS FUNÇÕES

#Função para remover caracteres passados
def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string

#Criando função para definir se é anagrama ou não
def definirAnagrama(row):
    if row[0] in anagramas:
        return True
    else:
        return False


# In[7]:


#Solicitando a palavra para gerar os anagramas
palavra = input("Qual é a sua str[ing? ")

#Converter qualquer string para maiusculo
palavra = palavra.upper()

#Retirando os caracteres
palavra = chr_remove(palavra, "$(# ") # remove $,# e ( da string string com caracteres.

#Criando todos os anagramas possíveis da palavra digitada
anagramas = ["".join(perm) for perm in itertools.permutations(palavra)]


# In[4]:


#Lendo o arquivo de palavras e carregando em um dataframe para pesquisa
dfPalavras = pd.read_csv('palavras.txt', header = None)


# In[5]:


#Aplicando a função para alimentar a coluna de anagramas com True ou False
dfPalavras['anagrama'] = dfPalavras.apply(definirAnagrama, axis=1)


# In[6]:


#Retornando apenas os Anagramas
dfPalavras[dfPalavras.anagrama == True]

