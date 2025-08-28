# 📋 INSTRUÇÕES DE USO - ANÁLISE ESTRATÉGICA MAGALU

## 🚀 Como Executar a Análise

### Pré-requisitos
- Python 3.8 ou superior
- Bibliotecas Python: pandas, numpy, matplotlib

### 1. Instalação das Dependências
```bash
pip install pandas numpy matplotlib
```

### 2. Execução da Análise Completa
```bash
python main.py
```

### 3. Execução Individual dos Módulos
```bash
# Análise simplificada
python src/analise_simples.py

# Análise completa (requer bibliotecas adicionais)
python src/analise_cd.py
```

---

## 📊 Estrutura do Projeto

```
magalu-desafio/
├── README.md                    # Documentação principal
├── RESUMO_EXECUTIVO.md         # Resumo dos resultados
├── INSTRUCOES_USO.md           # Este arquivo
├── main.py                     # Script principal
├── requirements.txt            # Dependências
├── data/                       # Dados de entrada
│   ├── cidades_nordeste.csv
│   ├── infraestrutura_logistica.csv
│   └── tempos_entrega.csv
├── src/                        # Código fonte
│   ├── analise_simples.py      # Versão simplificada
│   └── analise_cd.py           # Versão completa
├── notebooks/                  # Análises interativas
│   └── analise_cd_magalu.ipynb
└── reports/                    # Relatórios e visualizações
    ├── relatorio_executivo.md
    ├── comparacao_populacao_pib.png
    └── mapa_tempos_entrega.png
```

---

## 📈 Interpretação dos Resultados

### Score Estratégico
- **Recife**: 57.0/100 🥇
- **Salvador**: 53.1/100 🥈
- **Diferença**: 3.9 pontos

### Critérios Analisados
1. **População** (25%): Potencial de consumo regional
2. **PIB** (20%): Poder de compra da região
3. **Tempo de Entrega** (25%): Eficiência logística
4. **Custo Imobiliário** (15%): Investimento inicial
5. **Infraestrutura** (15%): Conectividade e facilidades

### Recomendação Final
**RECIFE** é a localização mais estratégica para o novo CD do Magalu.

---

## 🔧 Personalização da Análise

### Modificando Pesos dos Critérios
Edite o arquivo `src/analise_simples.py`, linha ~100:

```python
pesos = {
    'populacao': 0.25,      # Peso da população
    'pib': 0.20,           # Peso do PIB
    'tempo_entrega': 0.25,  # Peso dos tempos de entrega
    'custo_imobiliario': 0.15,  # Peso dos custos
    'infraestrutura': 0.15  # Peso da infraestrutura
}
```

### Adicionando Novos Dados
1. Atualize os arquivos CSV em `data/`
2. Modifique as funções de análise em `src/analise_simples.py`
3. Execute novamente: `python main.py`

---

## 📊 Visualizações Geradas

### Gráficos Disponíveis
1. **comparacao_populacao_pib.png**: População e PIB das principais cidades
2. **mapa_tempos_entrega.png**: Mapa de calor dos tempos de entrega

### Como Visualizar
- Abra as imagens em qualquer visualizador de imagens
- Use o notebook Jupyter para análises interativas
- Consulte o relatório executivo para interpretação detalhada

---

## 🛠️ Solução de Problemas

### Erro: "ModuleNotFoundError"
```bash
# Instale as dependências básicas
pip install pandas numpy matplotlib
```

### Erro: "FileNotFoundError"
- Verifique se os arquivos CSV estão na pasta `data/`
- Execute o script a partir da pasta raiz do projeto

### Erro: "PermissionError"
- Verifique se a pasta `reports/` existe
- Certifique-se de ter permissões de escrita

---

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique se todas as dependências estão instaladas
2. Confirme que está executando na pasta correta
3. Consulte a documentação nos arquivos README.md

---

## 🎯 Próximos Passos

1. **Revisar Resultados**: Analise o relatório executivo
2. **Validar Dados**: Confirme a precisão dos dados utilizados
3. **Apresentar**: Use os gráficos e relatórios para apresentação
4. **Implementar**: Execute a recomendação aprovada

---

*Projeto desenvolvido para análise estratégica do Magalu*  
*Dezembro 2024*
