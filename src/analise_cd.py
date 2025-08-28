"""
Análise Estratégica: Novo Centro de Distribuição Magalu - Nordeste
Módulo principal para análise comparativa entre Recife e Salvador
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import folium
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances
import warnings
warnings.filterwarnings('ignore')

class AnaliseCD:
    """
    Classe para análise estratégica do novo Centro de Distribuição
    """
    
    def __init__(self):
        """Inicializa a análise carregando os dados"""
        self.cidades = pd.read_csv('data/cidades_nordeste.csv')
        self.infraestrutura = pd.read_csv('data/infraestrutura_logistica.csv')
        self.tempos_entrega = pd.read_csv('data/tempos_entrega.csv')
        
        # Configurações de estilo
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
    def analise_demografica(self):
        """Análise demográfica e econômica das cidades"""
        print("=== ANÁLISE DEMOGRÁFICA E ECONÔMICA ===\n")
        
        # População total atendida
        recife_pop = self.cidades[self.cidades['cidade'].isin(['Natal', 'João Pessoa', 'Maceió', 'Aracaju'])]['populacao'].sum()
        salvador_pop = self.cidades[self.cidades['cidade'].isin(['Maceió', 'Aracaju', 'Teresina', 'São Luís'])]['populacao'].sum()
        
        print(f"População total atendida por Recife: {recife_pop:,} habitantes")
        print(f"População total atendida por Salvador: {salvador_pop:,} habitantes")
        print(f"Diferença: {abs(recife_pop - salvador_pop):,} habitantes\n")
        
        # PIB total
        recife_pib = self.cidades[self.cidades['cidade'].isin(['Natal', 'João Pessoa', 'Maceió', 'Aracaju'])]['pib_milhoes'].sum()
        salvador_pib = self.cidades[self.cidades['cidade'].isin(['Maceió', 'Aracaju', 'Teresina', 'São Luís'])]['pib_milhoes'].sum()
        
        print(f"PIB total atendido por Recife: R$ {recife_pib:,} milhões")
        print(f"PIB total atendido por Salvador: R$ {salvador_pib:,} milhões")
        print(f"Diferença: R$ {abs(recife_pib - salvador_pib):,} milhões\n")
        
        return {
            'recife_populacao': recife_pop,
            'salvador_populacao': salvador_pop,
            'recife_pib': recife_pib,
            'salvador_pib': salvador_pib
        }
    
    def analise_custos_imobiliarios(self):
        """Análise comparativa de custos imobiliários"""
        print("=== ANÁLISE DE CUSTOS IMOBILIÁRIOS ===\n")
        
        recife_custo = self.cidades[self.cidades['cidade'] == 'Recife']['preco_terreno_m2'].iloc[0]
        salvador_custo = self.cidades[self.cidades['cidade'] == 'Salvador']['preco_terreno_m2'].iloc[0]
        
        print(f"Custo do terreno em Recife: R$ {recife_custo}/m²")
        print(f"Custo do terreno em Salvador: R$ {salvador_custo}/m²")
        print(f"Diferença: R$ {abs(recife_custo - salvador_custo)}/m²")
        print(f"Salvador é {(recife_custo/salvador_custo - 1)*100:.1f}% mais barato\n")
        
        return {
            'recife_custo': recife_custo,
            'salvador_custo': salvador_custo
        }
    
    def analise_tempos_entrega(self):
        """Análise de tempos de entrega para as capitais da região"""
        print("=== ANÁLISE DE TEMPOS DE ENTREGA ===\n")
        
        # Tempos médios de entrega
        recife_tempos = self.tempos_entrega[self.tempos_entrega['origem'] == 'Recife']['tempo_entrega_horas']
        salvador_tempos = self.tempos_entrega[self.tempos_entrega['origem'] == 'Salvador']['tempo_entrega_horas']
        
        print(f"Tempo médio de entrega - Recife: {recife_tempos.mean():.1f} horas")
        print(f"Tempo médio de entrega - Salvador: {salvador_tempos.mean():.1f} horas")
        print(f"Recife é {(salvador_tempos.mean()/recife_tempos.mean() - 1)*100:.1f}% mais rápido\n")
        
        # Cobertura de entrega rápida (< 6 horas)
        recife_rapido = len(recife_tempos[recife_tempos < 6])
        salvador_rapido = len(salvador_tempos[salvador_tempos < 6])
        
        print(f"Cidades com entrega < 6h - Recife: {recife_rapido}")
        print(f"Cidades com entrega < 6h - Salvador: {salvador_rapido}\n")
        
        return {
            'recife_tempo_medio': recife_tempos.mean(),
            'salvador_tempo_medio': salvador_tempos.mean(),
            'recife_entrega_rapida': recife_rapido,
            'salvador_entrega_rapida': salvador_rapido
        }
    
    def analise_infraestrutura(self):
        """Análise de infraestrutura logística"""
        print("=== ANÁLISE DE INFRAESTRUTURA LOGÍSTICA ===\n")
        
        recife_infra = self.infraestrutura[self.infraestrutura['cidade'] == 'Recife'].iloc[0]
        salvador_infra = self.infraestrutura[self.infraestrutura['cidade'] == 'Salvador'].iloc[0]
        
        print("RECIFE:")
        print(f"  - Porto: {'Sim' if recife_infra['porto'] else 'Não'}")
        print(f"  - Aeroporto: {'Sim' if recife_infra['aeroporto'] else 'Não'}")
        print(f"  - Rodovias Federais: {recife_infra['rodovias_federais']}")
        print(f"  - Ferrovias: {'Sim' if recife_infra['ferrovias'] else 'Não'}")
        print(f"  - Centros de Distribuição: {recife_infra['centros_distribuicao']}")
        print(f"  - Índice de Conectividade: {recife_infra['indice_connectividade']:.2f}\n")
        
        print("SALVADOR:")
        print(f"  - Porto: {'Sim' if salvador_infra['porto'] else 'Não'}")
        print(f"  - Aeroporto: {'Sim' if salvador_infra['aeroporto'] else 'Não'}")
        print(f"  - Rodovias Federais: {salvador_infra['rodovias_federais']}")
        print(f"  - Ferrovias: {'Sim' if salvador_infra['ferrovias'] else 'Não'}")
        print(f"  - Centros de Distribuição: {salvador_infra['centros_distribuicao']}")
        print(f"  - Índice de Conectividade: {salvador_infra['indice_connectividade']:.2f}\n")
        
        return {
            'recife_infra': recife_infra,
            'salvador_infra': salvador_infra
        }
    
    def calcular_score_estrategico(self):
        """Calcula score estratégico para cada cidade"""
        print("=== SCORE ESTRATÉGICO ===\n")
        
        # Pesos para cada critério
        pesos = {
            'populacao': 0.25,
            'pib': 0.20,
            'tempo_entrega': 0.25,
            'custo_imobiliario': 0.15,
            'infraestrutura': 0.15
        }
        
        # Normalizar dados
        demografica = self.analise_demografica()
        custos = self.analise_custos_imobiliarios()
        tempos = self.analise_tempos_entrega()
        infra = self.analise_infraestrutura()
        
        # Scores (0-100)
        recife_scores = {
            'populacao': (demografica['recife_populacao'] / (demografica['recife_populacao'] + demografica['salvador_populacao'])) * 100,
            'pib': (demografica['recife_pib'] / (demografica['recife_pib'] + demografica['salvador_pib'])) * 100,
            'tempo_entrega': (1 - tempos['recife_tempo_medio'] / (tempos['recife_tempo_medio'] + tempos['salvador_tempo_medio'])) * 100,
            'custo_imobiliario': (1 - custos['recife_custo'] / (custos['recife_custo'] + custos['salvador_custo'])) * 100,
            'infraestrutura': infra['recife_infra']['indice_connectividade'] * 100
        }
        
        salvador_scores = {
            'populacao': (demografica['salvador_populacao'] / (demografica['recife_populacao'] + demografica['salvador_populacao'])) * 100,
            'pib': (demografica['salvador_pib'] / (demografica['recife_pib'] + demografica['salvador_pib'])) * 100,
            'tempo_entrega': (1 - tempos['salvador_tempo_medio'] / (tempos['recife_tempo_medio'] + tempos['salvador_tempo_medio'])) * 100,
            'custo_imobiliario': (1 - custos['salvador_custo'] / (custos['recife_custo'] + custos['salvador_custo'])) * 100,
            'infraestrutura': infra['salvador_infra']['indice_connectividade'] * 100
        }
        
        # Score final ponderado
        recife_final = sum(recife_scores[k] * pesos[k] for k in pesos.keys())
        salvador_final = sum(salvador_scores[k] * pesos[k] for k in pesos.keys())
        
        print(f"Score Estratégico - Recife: {recife_final:.1f}/100")
        print(f"Score Estratégico - Salvador: {salvador_final:.1f}/100")
        print(f"Diferença: {abs(recife_final - salvador_final):.1f} pontos\n")
        
        vencedor = "Recife" if recife_final > salvador_final else "Salvador"
        print(f"🏆 RECOMENDAÇÃO: {vencedor.upper()}\n")
        
        return {
            'recife_score': recife_final,
            'salvador_score': salvador_final,
            'vencedor': vencedor,
            'recife_detalhado': recife_scores,
            'salvador_detalhado': salvador_scores
        }
    
    def gerar_visualizacoes(self):
        """Gera visualizações da análise"""
        print("Gerando visualizações...")
        
        # 1. Comparação de população e PIB
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # População
        cidades_principais = ['Recife', 'Salvador', 'Fortaleza']
        dados_principais = self.cidades[self.cidades['cidade'].isin(cidades_principais)]
        
        axes[0].bar(dados_principais['cidade'], dados_principais['populacao'], 
                   color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        axes[0].set_title('População das Principais Cidades', fontsize=14, fontweight='bold')
        axes[0].set_ylabel('População')
        axes[0].tick_params(axis='x', rotation=45)
        
        # PIB
        axes[1].bar(dados_principais['cidade'], dados_principais['pib_milhoes'], 
                   color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        axes[1].set_title('PIB das Principais Cidades (Milhões R$)', fontsize=14, fontweight='bold')
        axes[1].set_ylabel('PIB (Milhões R$)')
        axes[1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('reports/comparacao_populacao_pib.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # 2. Mapa de calor de tempos de entrega
        pivot_tempos = self.tempos_entrega.pivot(index='origem', columns='destino', values='tempo_entrega_horas')
        
        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot_tempos, annot=True, cmap='YlOrRd', fmt='.1f', cbar_kws={'label': 'Tempo (horas)'})
        plt.title('Tempos de Entrega entre Cidades', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('reports/mapa_tempos_entrega.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # 3. Radar chart comparativo
        scores = self.calcular_score_estrategico()
        
        categorias = list(scores['recife_detalhado'].keys())
        recife_values = list(scores['recife_detalhado'].values())
        salvador_values = list(scores['salvador_detalhado'].values())
        
        angles = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()
        recife_values += recife_values[:1]
        salvador_values += salvador_values[:1]
        angles += angles[:1]
        
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
        
        ax.plot(angles, recife_values, 'o-', linewidth=2, label='Recife', color='#FF6B6B')
        ax.fill(angles, recife_values, alpha=0.25, color='#FF6B6B')
        
        ax.plot(angles, salvador_values, 'o-', linewidth=2, label='Salvador', color='#4ECDC4')
        ax.fill(angles, salvador_values, alpha=0.25, color='#4ECDC4')
        
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels([cat.replace('_', ' ').title() for cat in categorias])
        ax.set_ylim(0, 100)
        ax.set_title('Comparação Estratégica: Recife vs Salvador', size=16, fontweight='bold')
        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
        
        plt.tight_layout()
        plt.savefig('reports/radar_chart_comparativo.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print("Visualizações salvas na pasta 'reports/'")
    
    def gerar_relatorio_final(self):
        """Gera relatório final da análise"""
        print("=== RELATÓRIO FINAL ===\n")
        
        # Executar todas as análises
        demografica = self.analise_demografica()
        custos = self.analise_custos_imobiliarios()
        tempos = self.analise_tempos_entrega()
        infra = self.analise_infraestrutura()
        scores = self.calcular_score_estrategico()
        
        # Gerar visualizações
        self.gerar_visualizacoes()
        
        print("=== PRINCIPAIS FATORES DA DECISÃO ===\n")
        
        if scores['vencedor'] == 'Recife':
            print("✅ RECIFE - VANTAGENS:")
            print("  • Melhor posicionamento geográfico para atendimento rápido")
            print("  • Infraestrutura logística superior")
            print("  • Tempos de entrega menores para a maioria das capitais")
            print("  • Maior índice de conectividade")
            print("\n❌ RECIFE - DESVANTAGENS:")
            print("  • Custos imobiliários mais elevados")
            print("  • População total atendida menor")
            
        else:
            print("✅ SALVADOR - VANTAGENS:")
            print("  • Maior população total atendida")
            print("  • Custos imobiliários mais baixos")
            print("  • Maior PIB total da região atendida")
            print("\n❌ SALVADOR - DESVANTAGENS:")
            print("  • Tempos de entrega maiores")
            print("  • Posicionamento geográfico menos estratégico")
        
        print(f"\n🎯 RECOMENDAÇÃO FINAL: {scores['vencedor'].upper()}")
        print(f"Score: {scores[scores['vencedor'].lower() + '_score']:.1f}/100")
        
        return scores

if __name__ == "__main__":
    # Executar análise completa
    analise = AnaliseCD()
    resultado = analise.gerar_relatorio_final()
