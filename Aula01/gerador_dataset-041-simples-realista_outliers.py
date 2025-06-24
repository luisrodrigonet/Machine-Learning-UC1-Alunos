import random
import argparse
import csv
from datetime import datetime
from typing import Optional, Any

# Configurações
CAPITAIS = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Vitória']
CATEGORIAS = ['A', 'B']
FEEDBACKS = ['Bom', 'Regular', 'Ruim']

# Faixas normais
IDADE_MIN, IDADE_MAX = 16, 70
RENDA_MIN, RENDA_MAX = 1300, 13000
NOTA_MIN, NOTA_MAX = 0, 10

# Limites de outliers
IDADE_OUTLIER_MIN, IDADE_OUTLIER_MAX = 1, 120
RENDA_OUTLIER_MIN, RENDA_OUTLIER_MAX = 400, 50000
NOTA_OUTLIER_MIN, NOTA_OUTLIER_MAX = -5, 15

def gerar_idade(outlier: bool) -> Optional[int]:
    """Gera idade normal ou outlier conforme parâmetro."""
    if outlier:
        return random.choice([
            random.randint(IDADE_OUTLIER_MIN, IDADE_MIN - 1),
            random.randint(IDADE_MAX + 1, IDADE_OUTLIER_MAX)
        ])
    return random.randint(IDADE_MIN, IDADE_MAX)

def gerar_renda(outlier: bool) -> Optional[float]:
    """Gera renda normal ou outlier conforme parâmetro."""
    if outlier:
        return round(random.choice([
            random.uniform(RENDA_OUTLIER_MIN, RENDA_MIN - 1),
            random.uniform(RENDA_MAX + 1, RENDA_OUTLIER_MAX)
        ]), 2)
    return round(random.uniform(RENDA_MIN, RENDA_MAX), 2)

def gerar_nota(outlier: bool) -> Optional[float]:
    """Gera nota normal ou outlier conforme parâmetro."""
    if outlier:
        return round(random.choice([
            random.uniform(NOTA_OUTLIER_MIN, NOTA_MIN - 0.1),
            random.uniform(NOTA_MAX + 0.1, NOTA_OUTLIER_MAX)
        ]), 1)
    return round(random.uniform(NOTA_MIN, NOTA_MAX), 1)

def aplicar_dados_ausentes(valor: Any, missing_prob: float) -> Any:
    """Aplica dados ausentes com determinada probabilidade."""
    return valor if random.random() > missing_prob else None

def formatar_para_csv(valor: Any) -> str:
    """Converte valores para formato adequado no CSV (None vira string vazia)"""
    return '' if valor is None else str(valor)

def main():
    parser = argparse.ArgumentParser(
        description="""
        GERADOR DE DATASET SINTÉTICO - Região Sudeste
        Gera um dataset com dados realistas contendo:
        - Valores normais (faixas pré-definidas)
        - Outliers controlados
        - Dados ausentes controlados
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "qtd_linhas", 
        type=int, 
        help="Quantidade de registros a serem gerados (ex: 1000)"
    )
    parser.add_argument(
        "inicio_id", 
        type=int, 
        help="ID inicial para os registros (ex: 1)"
    )
    parser.add_argument(
        "outlier_percent", 
        type=float,
        help="Percentual de outliers (0-100) (ex: 5 para 5%%)"
    )
    parser.add_argument(
        "missing_percent", 
        type=float,
        help="Percentual de dados ausentes (0-100) (ex: 10 para 10%%)"
    )
    parser.add_argument(
        "-H", "--help-extended",
        action="store_true",
        help="Mostra ajuda detalhada com exemplos completos"
    )

    args = parser.parse_args()

    if args.help_extended:
        print("""
EXEMPLOS DE USO:

1. Dataset básico (100 registros, ID inicia em 1, 5% outliers, 10% missing):
   python gerador_dataset.py 100 1 5 10

2. Dataset sem outliers mas com 20% de dados ausentes:
   python gerador_dataset.py 500 1 0 20

3. Dataset com muitos outliers (30%) e poucos missing (2%):
   python gerador_dataset.py 1000 1 30 2

ESTRUTURA GERADA:
- id: Identificador único (nunca tem missing)
- idade: 16-70 (normal) ou 1-15/71-120 (outliers)
- renda: R$1300-R$13000 (normal) ou R$400-R$1299/R$13001-R$50000 (outliers)
- cidade: Capitais do Sudeste
- categoria: A ou B
- nota: 0-10 (normal) ou -5-0/10-15 (outliers)
- feedback: Bom, Regular ou Ruim

Todos os campos (exceto ID) podem conter valores ausentes.
        """)
        return

    # Validação dos argumentos
    if not 0 <= args.outlier_percent <= 100:
        raise ValueError("Percentual de outliers deve ser entre 0 e 100")
    if not 0 <= args.missing_percent <= 100:
        raise ValueError("Percentual de dados ausentes deve ser entre 0 e 100")

    outlier_prob = args.outlier_percent / 100
    missing_prob = args.missing_percent / 100
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"dataset_sudeste_simples_realista_outliers-{timestamp}.csv"
    
    with open(filename, mode="w", newline='', encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["id", "idade", "renda", "cidade", "categoria", "nota", "feedback"])

        for i in range(args.qtd_linhas):
            id_registro = args.inicio_id + i
            is_outlier = random.random() < outlier_prob
            
            # Gera os valores
            idade = aplicar_dados_ausentes(gerar_idade(is_outlier), missing_prob)
            renda = aplicar_dados_ausentes(gerar_renda(is_outlier), missing_prob)
            nota = aplicar_dados_ausentes(gerar_nota(is_outlier), missing_prob)
            cidade = aplicar_dados_ausentes(random.choice(CAPITAIS), missing_prob)
            categoria = aplicar_dados_ausentes(random.choice(CATEGORIAS), missing_prob)
            feedback = aplicar_dados_ausentes(random.choice(FEEDBACKS), missing_prob)

            writer.writerow([
                id_registro,
                formatar_para_csv(idade),
                formatar_para_csv(renda),
                formatar_para_csv(cidade),
                formatar_para_csv(categoria),
                formatar_para_csv(nota),
                formatar_para_csv(feedback)
            ])

    print(f"""
✅ Dataset gerado com sucesso!

Arquivo: {filename}
Registros: {args.qtd_linhas}
IDs: {args.inicio_id} a {args.inicio_id + args.qtd_linhas - 1}
Outliers: {args.outlier_percent}%
Dados ausentes: {args.missing_percent}%

Cidades incluídas: {', '.join(CAPITAIS)}
""")

if __name__ == "__main__":
    main()