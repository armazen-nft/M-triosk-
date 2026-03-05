import os
from pathlib import Path
from typing import Optional

import gradio as gr
import librosa
import numpy as np
import soundfile as sf

try:
    from neo4j import GraphDatabase
except ImportError:  # optional dependency in runtime environments
    GraphDatabase = None


def create_neo4j_driver() -> Optional[object]:
    """Create a Neo4j driver from environment variables.

    Returns None when Neo4j is unavailable or misconfigured.
    """
    if GraphDatabase is None:
        return None

    uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    password = os.getenv("NEO4J_PASSWORD", "neo4j")

    try:
        driver = GraphDatabase.driver(uri, auth=(user, password))
        # validate connectivity fast-fail at startup
        driver.verify_connectivity()
        return driver
    except Exception:
        return None


NEO4J_DRIVER = create_neo4j_driver()


def query_kg(era: str) -> str:
    if not NEO4J_DRIVER:
        return "Fallback: Neo4j indisponível; usando contexto histórico padrão."

    cypher = """
    MATCH (e:Era {name: $era})-[:HAS]->(l:Lexema)
    OPTIONAL MATCH (e)-[:HAS_VIB]->(v:Vibracao)
    RETURN e.name AS era, l.lemma AS lexema, l.sense AS sentido,
           v.piece AS obra, v.freq AS freq, v.affect AS afeto
    LIMIT 1
    """
    try:
        with NEO4J_DRIVER.session() as session:
            rec = session.run(cypher, era=era).single()
            if not rec:
                return f"KG sem registros para a era '{era}'."
            return (
                f"KG: era={rec['era']} | lexema={rec['lexema']} | sentido={rec['sentido']} | "
                f"obra={rec['obra']} | freq={rec['freq']}Hz | afeto={rec['afeto']}"
            )
    except Exception as exc:
        return f"Erro na consulta KG: {exc}"


def extract_features(audio: tuple[np.ndarray, int]) -> dict:
    sr, y = audio
    y = np.asarray(y, dtype=np.float32)
    if y.ndim == 2:
        y = y.mean(axis=1)

    rms = float(librosa.feature.rms(y=y)[0].mean())
    centroid = float(librosa.feature.spectral_centroid(y=y, sr=sr)[0].mean())
    onsets = int(len(librosa.onset.onset_detect(y=y, sr=sr)))
    dom_freq = float(np.clip(centroid * 0.7, 40, 220))

    return {
        "sr": sr,
        "signal": y,
        "rms": rms,
        "centroid": centroid,
        "onsets": onsets,
        "dom_freq": dom_freq,
    }


def synthesize_vibration(features: dict, output_path: Path) -> Path:
    sr = features["sr"]
    y = features["signal"]
    dom_freq = features["dom_freq"]

    t = np.arange(len(y), dtype=np.float32) / sr
    envelope = np.exp(-2.5 * t) * (1 - np.exp(-40 * t))
    vib = np.sin(2 * np.pi * dom_freq * t) * envelope * max(np.mean(np.abs(y)), 1e-3)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(output_path, vib, sr)
    return output_path


def build_narrative(era: str, features: dict, kg_info: str) -> str:
    motif = "short-short-short-long" if features["rms"] > 0.07 else "modal"
    timbre = "dramatic_strings" if features["dom_freq"] < 150 else "bright_brass"

    return (
        f"=== {era.upper()} ===\n"
        f"1_Sensação: RMS {features['rms']:.3f} | vib {features['dom_freq']:.1f}Hz | "
        f"centroid {features['centroid']:.1f}Hz | onsets {features['onsets']}\n"
        f"2_Percepção: motivo={motif} | timbre={timbre}\n"
        f"3_Atenção: foco no impacto vibratório\n"
        f"4_Memória(KG): {kg_info}\n"
        f"5_Cognição: a energia vibratória modela interpretação histórica\n"
        f"6_Afeto: tonalidade inferida a partir de densidade e frequência dominante\n"
        f"7_AutoReferência: descrição gerada por emulador textual (não percepção biológica)\n"
        f"8_IntegraçãoTemporal: a consulta semântica conecta era e escuta atual."
    )


def process_audio(audio: Optional[tuple[np.ndarray, int]], era: str):
    if audio is None:
        return "Envie um áudio para análise.", None, "Sem processamento.", ""

    features = extract_features(audio)
    output = synthesize_vibration(features, Path("outputs/vibracao_simulada.wav"))
    kg_info = query_kg(era)
    narrative = build_narrative(era, features, kg_info)
    status = f"Processado com sucesso: {len(features['signal']) / features['sr']:.2f}s"
    return narrative, str(output), status, kg_info


def build_app() -> gr.Blocks:
    with gr.Blocks(title="Matrioska Sensorial e Vibracional") as demo:
        gr.Markdown("# 🌀 Matrioska Sensorial e Vibracional\nIntegração Gradio + Neo4j + simulação vibratória")

        with gr.Tab("Análise"):
            audio = gr.Audio(label="Áudio", type="numpy", sources=["upload", "microphone"])
            era = gr.Dropdown(
                ["1200_Chartres", "1700_Lisboa", "1960_NYC"],
                value="1200_Chartres",
                label="Era",
            )
            btn = gr.Button("Analisar")
            narrative = gr.Textbox(label="Narrativa", lines=12)
            file_out = gr.File(label="Vibração simulada (.wav)")
            status = gr.Textbox(label="Status")
            kg = gr.Textbox(label="Contexto KG")
            btn.click(process_audio, inputs=[audio, era], outputs=[narrative, file_out, status, kg])

        with gr.Tab("Consulta KG"):
            era2 = gr.Dropdown(["1200_Chartres", "1700_Lisboa", "1960_NYC"], label="Era")
            kg_btn = gr.Button("Consultar")
            kg_out = gr.Textbox(label="Resultado")
            kg_btn.click(query_kg, inputs=era2, outputs=kg_out)

    return demo


if __name__ == "__main__":
    app = build_app()
    app.launch(server_name="0.0.0.0")
