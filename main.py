#!/usr/bin/env python3
"""
Script principal para execução da análise estratégica do novo CD do Magalu
"""

import sys
import os
from src.analise_simples import AnaliseCDSimples

def main():
    """Função principal que executa a análise completa"""
    
    print("🏢 ANÁLISE ESTRATÉGICA - NOVO CENTRO DE DISTRIBUIÇÃO MAGALU")
    print("=" * 70)
    print("Comparação entre Recife e Salvador para localização do novo CD")
    print("=" * 70)
    
    try:
        # Inicializar análise
        analise = AnaliseCDSimples()
        
        # Executar análise completa
        resultado = analise.gerar_relatorio_final()
        
        print("\n" + "=" * 70)
        print("✅ ANÁLISE CONCLUÍDA COM SUCESSO!")
        print("=" * 70)
        
        print(f"\n🏆 RESULTADO FINAL:")
        print(f"Vencedor: {resultado['vencedor'].upper()}")
        print(f"Score Recife: {resultado['recife_score']:.1f}/100")
        print(f"Score Salvador: {resultado['salvador_score']:.1f}/100")
        
        print(f"\n📊 RELATÓRIOS GERADOS:")
        print(f"• Relatório Executivo: reports/relatorio_executivo.md")
        print(f"• Notebook de Análise: notebooks/analise_cd_magalu.ipynb")
        print(f"• Visualizações: reports/")
        
        print(f"\n📈 PRÓXIMOS PASSOS:")
        print(f"1. Revisar o relatório executivo")
        print(f"2. Executar o notebook para análises interativas")
        print(f"3. Apresentar resultados para a diretoria")
        
        return resultado
        
    except Exception as e:
        print(f"\n❌ ERRO NA EXECUÇÃO: {str(e)}")
        print("Verifique se todos os arquivos de dados estão presentes na pasta 'data/'")
        return None

if __name__ == "__main__":
    resultado = main()
