# -*- coding: UTF-8 -*-

# -----------------------------------------------
#    GRAPHS
#    partitionCyclesLink.py
#    Fernando Igor
#    github/fernandoigor/partitionCyclesLink
#------------------------------------------------

import sys
import random
import time
import math
global custo
global menorCaminho
menorCaminho=[]
global custoTotal
custoTotal = 0
custo = sys.maxint
#print sys.maxint
def splitMat(mat):
  vRandom = []                #ARMAZENA EM ORDEM ALEATORIA O ID DOS VERTICES
  vCiclos = []                #ARMAZENA A ROTA
  sizeSplit = 10
  if sizeSplit >= len(mat):
    sizeSplit = len(mat)
  while 1:
    vProximos = []              #VETOR COM OS VERTICES AINDA NAO USADOS
    vEscolha = []               #VETOR PARA ESCOLHER RANDOMICAMENTE O VERTICE
    count = 0
    for x in xrange(len(mat)):
      usado = 0
      for y in xrange(len(vRandom)):
        if x == vRandom[y]:
          usado = 1
          break
      if usado == 0:
        count+=1
        vEscolha.append(x)
    if count == 0:            #TERMINA O WHILE SE NAO HOUVER MAIS VERTICES
      break
    randInicio = random.randint(0,len(vEscolha)-1)  
    for x in xrange(len(vEscolha)):
      if x != randInicio:
        vProximos.append(vEscolha[x])
    for x in range(0,len(vProximos)):
      for y in range(0,len(vProximos)):
        p1 = vProximos[x]
        p2 = vProximos[y]
        if (mat[randInicio][p1] + mat[p1][randInicio]) < (mat[randInicio][p2] + mat[p2][randInicio]):
          temp = vProximos[x]
          vProximos[x] = vProximos[y]
          vProximos[y] = temp
    vRandom.append(vEscolha[randInicio])
    sizeSplitTemp = sizeSplit
    if len(vProximos) <= sizeSplitTemp:
      sizeSplitTemp = len(vProximos)+1
    for x in range(0,sizeSplitTemp-1):
      vRandom.append(vProximos[x])
  start = 0
  end = sizeSplit
  tamanho = len(mat)
  count = 0
  while end <= tamanho+1:
    if start == end:
      break
    sizeSplit = end-start
    bestWayMat(mat,vRandom,start,end,sizeSplit)
    vCiclos = link(menorCaminho,mat,vCiclos)
    count+=1
    start = end
    end = end+sizeSplit
    if end > tamanho:
      end = tamanho
  caminhoStr = ""
  for c in xrange(len(vCiclos)):
    caminhoStr+=str(vCiclos[c])+"-"
  caminhoStr+=str(vCiclos[0])
  print "Rota: "+caminhoStr
  print "Solucao: "+str(custoCaminho(vCiclos,mat))
    
def link(ciclos,mat,vCiclos):
  temp = []
  temp = list(ciclos)
  if len(vCiclos) == 0:
    vCiclos = list(temp)
    return vCiclos
  else:
    distMin = sys.maxint
    verticeMin = [-1,-1,-2,-2]        #ARMAZENAR VERTICES DE S E DO PARTICIONADO COM MENOR DISTANCIA
    for x in range(0,len(vCiclos)):
      s1 = vCiclos[x]
      if x+1 == len(vCiclos):
        s2 = vCiclos[0]
        pos2 = 0
      else:
        s2 = vCiclos[x+1]
        pos2 = x+1
      for y in range(0,len(temp)):
        v1 = temp[y]
        if y-1 == -1:
          v2 = temp[len(temp)-1]
          pos4 = len(temp)-1
        else:
          v2 = temp[y-1]
          pos4 = y-1
          
        if mat[s1][v1] + mat[s2][v2] < distMin:
          distMin = mat[s1][v1] + mat[s2][v2]
          verticeMin[0]=x
          verticeMin[1]=pos2
          verticeMin[2]=y
          verticeMin[3]=pos4
    tempS = []
    for x in range(0,len(vCiclos)):
      if x != verticeMin[0]:
        tempS.append(vCiclos[x])
      else:
        tempS.append(vCiclos[x])
        for x in range(verticeMin[2],len(temp)):
            tempS.append(temp[x])
        for x in range(0,verticeMin[2]):
            tempS.append(temp[x])
    return tempS

def bestWayMat(mat,vRandom, start,end,sizeSplit):
  global custo
  global menorCaminho
  global custoTotal
  arr={}
  count=0
  for e in range(start,end):
    arr[count] = vRandom[e]
    count+=1
  custo = sys.maxint                          # SET NUMERO MAXIMO
  recursivePermute(mat,arr,start,sizeSplit,0)

def custoCaminho(arr, mat):
  custoTemp = 0
  offsetMenor = arr[0]
  offsetMaior = arr[len(arr)-1]
  for x in range(0,len(arr)-1):
    p1 = arr[x]
    p2 = arr[x+1]
    custoTemp+=mat[p1][p2] 
  custoTemp+=mat[offsetMaior][offsetMenor]
  return custoTemp

def recursivePermute(mat,arr,start,sizeSplit,k):
  global custo
  if k == sizeSplit:
    custoTemp = custoCaminho(arr,mat)
    if custo > custoTemp:
      custo = custoTemp
      while len(menorCaminho) > 0:
        menorCaminho.pop()
      for y in arr:
        menorCaminho.append(arr[y]) 
  else:
    for i in range(k,sizeSplit):
      temp = arr[k]
      arr[k] = arr[i]
      arr[i] = temp
      recursivePermute(mat,arr,start,sizeSplit,k+1)
      temp = arr[i]
      arr[i] = arr[k]
      arr[k] = temp


# --------------------------------
#  MAIN
#---------------------------------
def main():
  ok = 1
  while ok == 1:
    ok=0
    matrizArquivo = raw_input("Digite o arquivo de entrada: ")
    if(matrizArquivo == ""):
      matrizArquivo = "Tsp10.txt"

    try:
      arquivo = open(matrizArquivo, 'r')
    except:
      ok=1
      print "Arquivo nao encontrado"
      
  tamanhoTipo = arquivo.readline()
  tamanhoTipo = tamanhoTipo.replace("  ", " ")          # tira os 2 espaços juntos
  tamanhoTipo = tamanhoTipo.replace("  ", " ")          # tira os 2 espaços juntos
  tamanhoTipo = tamanhoTipo.split(' ')
  
  tamanhoTipo[0] = tamanhoTipo[0].split('=')  #tamanhoTipo[0][1] valor de N
  tamanhoTipo[1] = tamanhoTipo[1].split('=')  #tamanhoTipo[3][1] valor de Tipo

  
  tamanho = int(tamanhoTipo[0][1])
  tipo = int(tamanhoTipo[1][1])
  print "N=%s Tipo=%s"%(tamanho,tipo)
  simetrica = 1
  mat = []
  
  if tipo == 1:
    for x in range(0,int(tamanhoTipo[0][1])):
        arrT = []
        tempZeros = ""
        temp = arquivo.readline()
        if(temp == ''):
          for i in range(0,int(tamanhoTipo[0][1])):
            arrT.append(int(0))
          mat.append(arrT)
          break
        temp = temp[:-1]                        # tira o /n no final de cada linha
        if temp[-1] == " ":
          temp = temp[0:-1]
        temp = temp.replace("  ", " ")          # tira os 2 espaços juntos
        if temp[0] == " ":                      # tira o espaço no começo no caso de numeros começando com espaço
          temp = temp[1:]
        for y in range(0, x+1):
          tempZeros += "0 "
        temp = tempZeros + temp
        temp = temp.split(' ')
        for i in temp:
          arrT.append(int(i))
        mat.append(arrT)

    for x in range(0,len(mat)):
      for y in range(0,len(mat)):
        if y > x:
          mat[y][x] = mat[x][y]

  #ENDIF TIPO 1          
  if tipo == 2:
    arrCartesiano = []
    for x in range(0,int(tamanhoTipo[0][1])):
      temp = arquivo.readline()
      temp = temp.replace("\t", " ")
      for r in xrange(5):
        temp = temp.replace("  ", " ")          # tira os 2 espaços juntos
      if temp[0] == " ":
          temp = temp[1:-1]
      temp = temp.split(' ')
      arrCartesiano.append(temp)

    for i in range(0, len(arrCartesiano)):
      iArr = []
      for j in range(0, len(arrCartesiano)):
        if i == j:
          iArr.append(0)
        else:
          ax = float(arrCartesiano[i][0])
          ay = float(arrCartesiano[i][1])
          bx = float(arrCartesiano[j][0])
          by = float(arrCartesiano[j][1])
          iArr.append(math.sqrt((ax-bx)**2 + (ay-by)**2))
      mat.append(iArr)
  #ENDIF TIPO 2 
  if tipo == 3:
    for x in range(0,int(tamanhoTipo[0][1])+1):
        arrT = []
        temp = arquivo.readline()
        if len(temp) > 1:
          temp = temp.replace("  ", " ")          # tira os 2 espaços juntos
          if temp[0] == " ":                      # tira o espaço no começo no caso de numeros começando com espaço
            temp = temp[1:]
          temp = temp.split(' ')
          for i in range(0,len(temp)):
            arrT.append(int(temp[i]))
          mat.append(list(arrT))
          
  arquivo.close()

  for tests in xrange(10):
    print "---------------------"
    INIT = time.time()
    splitMat(mat)
    print "Tempo execucao: %.2f segundos"%(time.time() - INIT)


main()

raw_input("\nAperte ENTER para sair")
