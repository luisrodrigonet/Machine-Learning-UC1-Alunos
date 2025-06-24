"""
Exemplo de USO:
python .\gerador_dataset-012-relacionados.py 1000 1 5  

# Gera 1000 registros, ID inicia em 1, com até 5% de outliers

"""


import random
import argparse
import csv
from datetime import datetime
from typing import List, Dict, Any

# Configurações
CAPITAIS = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Vitória']
CATEGORIAS = ['A', 'B']

# Faixas normais
IDADE_MIN, IDADE_MAX = 16, 82
RENDA_MIN, RENDA_MAX = 1542, 46260
NOTA_MIN, NOTA_MAX = 5, 10

# Limites de outliers
IDADE_OUTLIER_MIN, IDADE_OUTLIER_MAX = 1, 120
RENDA_OUTLIER_MIN, RENDA_OUTLIER_MAX = 400, 92520
NOTA_OUTLIER_MIN = 0

# Regras de feedback
FEEDBACK_RULES = {
    'Bom': {
        'conditions': [
            {'nota': (7.5, 10), 'renda': (0, 3000), 'categoria': 'A'},
            {'nota': (7.5, 10), 'renda': (10000, float('inf'))}
        ],
        'default': True
    },
    'Regular': {
        'conditions': [
            {'nota': (4, 7.5), 'renda': (8000, float('inf'))},
            {'nota': (4, 7.5), 'categoria': 'B'},
            {'nota': (0, 4), 'renda': (2000, float('inf'))}
        ]
    },
    'Ruim': {
        'conditions': [
            {'nota': (0, 4), 'renda': (0, 2000)}
        ]
    }
}

def gerar_idade(outlier: bool) -> int:
    """Gera idade normal ou outlier conforme parâmetro."""
    if outlier:
        return random.choice([
            random.randint(IDADE_OUTLIER_MIN, IDADE_MIN - 1),
            random.randint(IDADE_MAX + 1, IDADE_OUTLIER_MAX)
        ])
    return random.randint(IDADE_MIN, IDADE_MAX)

def gerar_renda(outlier: bool) -> float:
    """Gera renda normal ou outlier conforme parâmetro."""
    if outlier:
        return round(random.choice([
            random.uniform(RENDA_OUTLIER_MIN, RENDA_MIN - 1),
            random.uniform(RENDA_MAX + 1, RENDA_OUTLIER_MAX)
        ]), 2)
    return round(random.uniform(RENDA_MIN, RENDA_MAX), 2)

def gerar_nota(outlier: bool) -> float:
    """Gera nota normal ou outlier conforme parâmetro."""
    if outlier:
        return round(random.uniform(NOTA_OUTLIER_MIN, NOTA_MIN - 0.1), 1)
    return round(random.uniform(NOTA_MIN, NOTA_MAX), 1)

def determinar_feedback(nota: float, renda: float, categoria: str) -> str:
    """Determina o feedback baseado em regras pré-definidas."""
    for feedback, rules in FEEDBACK_RULES.items():
        for condition in rules.get('conditions', []):
            nota_cond = condition.get('nota', (0, 10))
            renda_cond = condition.get('renda', (0, float('inf')))
            cat_cond = condition.get('categoria', None)
            
            if (nota_cond[0] <= nota <= nota_cond[1] and
                renda_cond[0] <= renda <= renda_cond[1] and
                (cat_cond is None or categoria == cat_cond)):
                return feedback
        
        if rules.get('default', False):
            return feedback
    return 'Regular'

def gerar_linha(id_registro: int, outlier_prob: float) -> List[Any]:
    """Gera uma linha de dados com possibilidade de outlier."""
    is_outlier = random.random() < outlier_prob
    idade = gerar_idade(is_outlier)
    renda = gerar_renda(is_outlier)
    cidade = random.choice(CAPITAIS)
    categoria = random.choice(CATEGORIAS)
    nota = gerar_nota(is_outlier)
    feedback = determinar_feedback(nota, renda, categoria)

    return [id_registro, idade, renda, cidade, categoria, nota, feedback]

def main():
    parser = argparse.ArgumentParser(
        description="Gera dataset sintético de usuários da região Sudeste com outliers controlados."
    )
    parser.add_argument("qtd_linhas", type=int, help="Quantidade de linhas do dataset")
    parser.add_argument("inicio_id", type=int, help="Valor inicial do ID")
    parser.add_argument("outlier_percent", type=float, 
                       help="Percentual máximo de outliers (0-100)")

    args = parser.parse_args()

    # Validação dos argumentos
    if not 0 <= args.outlier_percent <= 100:
        raise ValueError("O percentual de outliers deve estar entre 0 e 100")

    outlier_prob = args.outlier_percent / 100
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"dataset_sudeste_relacionados_outliers_{timestamp}.csv"
    
    with open(filename, mode="w", newline='', encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([
            "id", "idade", "renda", "cidade", 
            "categoria", "nota", "feedback"
        ])

        for i in range(args.qtd_linhas):
            id_registro = args.inicio_id + i
            linha = gerar_linha(id_registro, outlier_prob)
            writer.writerow(linha)

    print(f"""
Dataset gerado com sucesso!
Arquivo: {filename}
Registros: {args.qtd_linhas}
IDs: {args.inicio_id} a {args.inicio_id + args.qtd_linhas - 1}
Percentual máximo de outliers: {args.outlier_percent}%
Cidades: {', '.join(CAPITAIS)}
""")

if __name__ == "__main__":
    main()