import os
import hashlib
from PIL import Image
import imagehash

class ValidadorLoteReciclaje:
    def __init__(self, umbral_peso_min=0.2, umbral_peso_max=250.0):
        self.peso_min = umbral_peso_min
        self.peso_max = umbral_peso_max
        self.hashes_conocidos = set() # Memoria temporal para detectar duplicados por pHash

    def validar_rangos_fisicos(self, peso_neto: float) -> bool:
        """Verifica que el peso esté en el rango realista de recolección."""
        return self.peso_min <= peso_neto <= self.peso_max

    def calcular_phash(self, ruta_imagen: str) -> str:
        """Calcula el hash perceptual de la foto para evitar duplicados o reutilización de imágenes."""
        if not os.path.exists(ruta_imagen):
            raise FileNotFoundError(f"Imagen no encontrada para hashing: {ruta_imagen}")
        
        with Image.open(ruta_imagen) as img:
            phash_str = str(imagehash.phash(img))
            return phash_str

    def generar_nullifier(self, id_centro: str, timestamp_str: str, phash: str) -> str:
        """Genera un identificador pseudónimo único (nullifier) para la blockchain sin exponer PII."""
        combinado = f"{id_centro}-{timestamp_str}-{phash}"
        return "0x" + hashlib.sha256(combinado.encode("utf-8")).hexdigest()

    def procesar_validacion_completa(self, datos_ia: dict, ruta_imagen: str, id_centro: str, timestamp_str: str) -> dict:
        """Ejecuta toda la lógica de validación anti-fraude antes de enviar a la blockchain."""
        peso_neto = datos_ia.get("peso_neto_kg", 0.0)

        # 1. Validación de rangos físicos
        if not self.validar_rangos_fisicos(peso_neto):
            return {
                "aprobado": False,
                "motivo": f"Peso neto fuera de rango físico permitido ({peso_neto} kg)."
            }

        # 2. Cálculo de pHash y verificación de duplicados
        phash_actual = self.calcular_phash(ruta_imagen)
        if phash_actual in self.hashes_conocidos:
            return {
                "aprobado": False,
                "motivo": "Fraude detectado: La fotografía ya fue registrada anteriormente (duplicado)."
            }
        
        self.hashes_conocidos.add(phash_actual)

        # 3. Generación del Nullifier único para L2
        nullifier = self.generar_nullifier(id_centro, timestamp_str, phash_actual)

        return {
            "aprobado": True,
            "nullifier": nullifier,
            "phash": phash_actual,
            "peso_neto_validado": peso_neto,
            "material": datos_ia.get("material_detectado")
        }

if __name__ == "__main__":
    # Prueba local del validador
    validador = ValidadorLoteReciclaje()
    datos_ejemplo = {
        "peso_neto_kg": 14.5,
        "material_detectado": "plastico_rigido_PP"
    }
    resultado = validador.procesar_validacion_completa(
        datos_ejemplo, 
        "dataset_eval/prueba_lote.jpg", 
        id_centro="QUITO_NORTE_01", 
        timestamp_str="2026-10-28T13:10:00"
    )
    print("\n[OK] Resultado del Validador Anti-Fraude:")
    import json
    print(json.dumps(resultado, indent=2, ensure_ascii=False))