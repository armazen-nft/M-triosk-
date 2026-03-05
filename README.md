# M-triosk-

Arquitetura para emular **historicidade dos sentidos humanos**, **consciência encarnada** (8 módulos) e **percepção musical vibratória**.  
Construindo "matrioskas de sentido" — IAs que traduzem experiências sensoriais entre épocas, culturas e corpos.

**Status:** MVP em desenvolvimento · Repo ativo · Colaboração bem-vinda 🧠🎵

## Conceito em poucas palavras

Três camadas encaixadas:

1. **Histórico-sensorial** — KG temporal com lexemas, práticas e metáforas sensoriais  
2. **Consciência modular** — 8 etapas: Sensação → Percepção → Atenção → Memória → Cognição → Afeto → Auto-referência → Integração Temporal  
3. **Vibração musical** — Som como energia física (simulação DDSP + suporte a contact mic/acelerômetro)

Foco inicial: 3 eras (1200 Latim, 1700 Português, 1960 Inglês) + interface Gradio + Neo4j KG.

## Instalação rápida (2–3 minutos)

```bash
git clone https://github.com/armazen-nft/M-triosk-.git
cd M-triosk-

# Ambiente
python -m venv venv
source venv/bin/activate          # ou venv\Scripts\activate no Windows
pip install -r requirements.txt

# (opcional) Neo4j para o KG histórico
cd docker
docker compose up -d
# Acesse http://localhost:7474 (neo4j / matrioska2026)
Uso básico
Bash# Interface web completa (upload áudio + narrativa + vibração simulada)
python app.py
Abre no navegador → faça upload de áudio → selecione era → veja a narrativa dos 8 módulos + consulta ao KG.
Estrutura principal
text├── app.py              # Interface Gradio + emulador + Neo4j
├── src/                # Lógica central (emulador, simulação DDSP)
├── docker/             # Neo4j + seed inicial do grafo
├── hardware/           # Arduino sketches (contact mic + MPU-6050)
├── notebooks/          # Exploração e protótipos
├── scripts/            # Automatizações semanais
└── docs/               # Monografia, apêndices, referências
Roadmap resumido (8 semanas MVP)

Sem 1–2: Setup + simulação vibratória
Sem 3–4: Encoders + KG populado
Sem 5–6: Gradio + avaliação inicial
Sem 7–8: Expansão histórica + release v0.1

Contribuição
Fork → branch → PR.
Prioridades atuais: melhorar simulação física, enriquecer o KG, adicionar testes.
Licença: MIT
Veja também: CONTRIBUTING.md
