# M-triosk- : Matrioska Sensorial & Vibracional

Arquitetura unificada para emular historicidade dos sentidos humanos, consciência encarnada (8 módulos) e percepção musical como fenômeno vibratório.

## Visão Geral
A proposta da **Matrioska Sensorial & Vibracional** combina:
- Historicidade sensorial (como a experiência de ouvir/mover/afetar muda por época e cultura).
- Consciência encarnada em 8 módulos funcionais.
- Música como vibração física e fenômeno multimodal.

Objetivo: construir “IQs sensoriais” para tradução semântica e perceptiva entre contextos históricos e corporais.

## Arquitetura

### Matrioskas
1. **Base histórico-sensorial**: Knowledge Graph temporal/cultural + embeddings diacrônicos.
2. **Consciência encarnada (8 módulos)**.
3. **Motor vibratório musical**: áudio, contato, aceleração e fusão multimodal.
4. **Camada transversal**: tradutor temporal-semântico + camada de humildade epistêmica.

### Os 8 módulos de consciência
1. Sensação
2. Percepção
3. Atenção
4. Memória
5. Cognição
6. Afeto
7. Auto-referência
8. Integração temporal

Fluxo simplificado:

```text
Sensação → Percepção → Atenção
   ↘         ↘
 Memória ← Cognição ← Afeto
   ↘
 Auto-Referência
   ↘
Integração Temporal
```

## Estrutura do Repositório

```text
M-triosk-/
├── src/
├── docs/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── hardware/
├── docker/
│   └── seed/
├── scripts/
└── evaluation/
```

## Instalação

```bash
git clone https://github.com/armazen-nft/M-triosk-.git
cd M-triosk-
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Execução (MVP inicial)

```bash
python src/app.py
```

## Docker (Neo4j)

```bash
docker compose -f docker/docker-compose.yml up -d
```

## Roadmap (8 semanas)
- Semanas 1-2: setup e simulação vibratória básica.
- Semanas 3-4: embeddings + KG temporal.
- Semanas 5-6: UI interativa e avaliação.
- Semanas 7-8: integração dos 8 módulos + release MVP.

## Salvaguardas Éticas
- Humildade epistêmica: score de confiança e incerteza.
- Não alucinar historicidade sem evidência de KG.
- Consentimento para dados sensoriais/biométricos.

## Contribuição
Veja [CONTRIBUTING.md](CONTRIBUTING.md).

## Licença
MIT. Veja [LICENSE](LICENSE).
