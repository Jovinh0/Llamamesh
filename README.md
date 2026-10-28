# ♻️ LlamaMesh: Decentralized Recycling Traceability with Multimodal AI

> **Meta Global AI Developer Hackathon (Indie Developer Track)**  
> **Team:** Jovinho: EPN (Escuela Politécnica Nacional) — Quito, Ecuador[cite: 1, 2, 13]

---

## 📌 What is LlamaMesh?
LlamaMesh is a decentralized system designed to certify the recovery of hard-to-recycle materials (such as rigid plastics, multi-layer packaging, and cardboard) in recycling collection centers in Quito[cite: 1, 2]. It solves the double-counting problem in corporate sustainability goals through three main pillars:

1. **Frictionless Capture (WhatsApp):** The operator sends a single photo of the batch on the scale[cite: 2].
2. **Multimodal AI Extraction (Meta Llama):** Meta's open-weights model processes the image and extracts a strict JSON schema containing the net weight, material type, and confidence score[cite: 2].
3. **Anti-Fraud Validation & On-Chain Attestation (Base L2):** A perceptual hashing (`pHash`) filter blocks duplicates and generates a unique `nullifier` to issue public, immutable attestations on **Base Sepolia**, ensuring privacy with zero PII emissions[cite: 2].

---

## 🏗️ Repository Structure
```text
llamamesh/
├── ai_extractor/      # Module 1: Structured extraction with Llama & Pydantic
├── backend/           # Module 2: FastAPI server, validators, and duplicate detector (pHash)
├── contracts/         # Module 3: Solidity smart contract (LotRegistry.sol)
├── auditor_cli/       # Module 4: Independent CLI auditor tool via RPC node
└── dataset_eval/      # Dataset and local validation test cases

META, How to Run Locally
Clone the repository and set up the virtual environment:
git clone [https://github.com/your-username/llamamesh.git](https://github.com/your-username/llamamesh.git)
cd llamamesh
python -m venv venv

# Activate virtual environment (Windows PowerShell):
.\venv\Scripts\activate

# Install dependencies:
pip install -r requirements.txt

2. Configure Environment Variables:
Create a .env file in the root directory based on .env.example and add your API keys and RPC URL.
3. Run the AI Extractor Module:
python ai_extractor/extractor.py
4. Start the FastAPI Backend Server: 
uvicorn backend.main:app --reload
(Open your browser and navigate to http://127.0.0.1:8000/docs to test the interactive API endpoints).






*Spanish
*# ♻️ LlamaMesh: Trazabilidad Descentralizada de Reciclaje con IA

> **Meta Global AI Developer Hackathon (Track Indie Developer)**  
> **Equipo:** Jovinho: EPN (Escuela Politécnica Nacional) — Quito, Ecuador[cite: 1, 2, 13]

---

## 📌 ¿Qué es LlamaMesh?
LlamaMesh es un sistema descentralizado para certificar la recuperación de materiales de reciclaje difíciles de recolectar (como plástico rígido, envases multicapa y cartón) en centros de acopio en Quito[cite: 1, 2]. El sistema resuelve el problema del doble conteo en metas corporativas de responsabilidad ambiental mediante tres pilares:

1. **Captura sin fricción (WhatsApp):** El operador envía una sola foto del lote sobre la balanza[cite: 2].
2. **Extracción Multimodal (Meta Llama):** Un modelo de pesos abiertos de Meta procesa la imagen y extrae un esquema JSON estricto con el peso neto, material y confianza[cite: 2].
3. **Validación Anti-Fraude & On-Chain (Base L2):** Un filtro de hashes perceptuales (`pHash`) bloquea duplicados y genera un `nullifier` único para registrar atestaciones públicas e inmutables en **Base Sepolia**, protegiendo la privacidad (cero emisiones PII)[cite: 2].

---

## 🏗️ Estructura del Repositorio
```text
llamamesh/
├── ai_extractor/      # Módulo 1: Extracción estructurada con Llama y Pydantic
├── backend/           # Módulo 2: API FastAPI, validadores y detector de duplicados (pHash)
├── contracts/         # Módulo 3: Contrato inteligente Solidity (LotRegistry.sol)
├── auditor_cli/       # Módulo 4: Herramienta de auditoría independiente vía nodo RPC
└── dataset_eval/      # Conjunto de datos y pruebas de validación en terreno

🚀 Cómo Ejecutar el Proyecto Localmente
git clone [https://github.com/tu-usuario/llamamesh.git](https://github.com/tu-usuario/llamamesh.git)
cd llamamesh
python -m venv venv
# En Windows (PowerShell):
.\venv\Scripts\activate
pip install -r requirements.txt

2.Configurar variables de entorno: Copia el archivo .env.example a .env y añade tus claves de API y de la red Base Sepolia.
3. Ejecutar el Extractor de IA: python ai_extractor/extractor.py
python ai_extractor/extractor.py
4. Levantar el Servidor FastAPI:
uvicorn backend.main:app --reload
