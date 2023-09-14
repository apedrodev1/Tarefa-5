# Comparação Entre Modelos de Classificação para Reservas de Hotel

## Introdução
Este documento compara três métodos de classificação utilizados para prever o preço médio por quarto em reservas de hotel: Random Forest, Support Vector Classifier (SVC) e Regressão Logística.

## Comparação de Acurácia
- **Random Forest**: Acurácia de aproximadamente 86.45%.
- **Support Vector Classifier (SVC)**: Acurácia de aproximadamente 73.25%.
- **Regressão Logística**: Acurácia de aproximadamente 54.00%.

## Discussão


### Random Forest
O modelo Random Forest mostrou o melhor desempenho entre os três. Este método é conhecido por sua robustez e capacidade de lidar com uma grande variedade de tipos de dados.

### Support Vector Classifier (SVC)
O SVC também teve um desempenho razoável, mas foi superado pelo Random Forest. Este modelo pode ser mais adequado para conjuntos de dados onde as classes são bem separadas.

### Regressão Logística
O modelo de Regressão Logística teve o desempenho mais fraco. Embora seja um modelo mais simples e rápido de treinar, não conseguiu capturar a complexidade dos dados tão eficazmente quanto os outros métodos.

## Conclusão
O desempenho relativo desses três modelos pode ser influenciado por várias características dos dados e das configurações dos próprios modelos. Aqui estão algumas razões possíveis para o desempenho observado:

## Por que o Random Forest teve melhor desempenho que o SVC:
# Robustez a Overfitting: 
Random Forest tem mecanismos embutidos para evitar overfitting, tornando-o mais robusto para conjuntos de dados com muitas características.

# Manipulação de Variáveis Categóricas: 
Random Forest pode lidar diretamente com variáveis categóricas, o que pode melhorar o desempenho do modelo.

# Flexibilidade: 
Random Forest é capaz de modelar relações complexas e não-lineares entre as características, o que pode ser vantajoso em conjuntos de dados complexos.

# Ensemble Learning: 
Por ser um método de ensemble, o Random Forest combina múltiplos modelos de árvore de decisão, o que geralmente resulta em um desempenho melhorado.

## Por que a Regressão Logística ficou em último:
# Linearidade:
 A Regressão Logística assume que a relação entre as variáveis independentes e a variável dependente é linear. Se essa suposição não é satisfeita, o desempenho do modelo pode ser inferior.

# Simplicidade do Modelo:
 Embora seja fácil de implementar e rápido para treinar, a Regressão Logística pode não capturar a complexidade total de conjuntos de dados com múltiplas variáveis inter-relacionadas.

# Ausência de Regularização: 
Dependendo de como o modelo é configurado, a Regressão Logística pode sofrer de overfitting, especialmente quando o conjunto de dados tem muitas características.

# Probabilístico:
 A Regressão Logística é um modelo probabilístico, o que pode ser menos eficaz para tarefas de classificação onde as margens entre as classes não são tão bem definidas.

