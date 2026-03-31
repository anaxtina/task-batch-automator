import webbrowser
import os
import time
from typing import Dict, List

class RoutineAutomator:
    """
    Classe responsável por gerenciar e executar fluxos de trabalho automatizados.
    Resolve o problema de perda de tempo com configurações repetitivas de ambiente.
    """

    def __init__(self):
        # Estrutura de dados que armazena os fluxos de trabalho
        self.workflows: Dict[str, List[str]] = {
            "Estudo": [
                "https://github.com/",
                "https://stackoverflow.com/",
                "https://www.youtube.com/c/suacanaldeestudo"
            ],
            "Administrativo": [
                "https://mail.google.com/",
                "https://calendar.google.com/"
            ]
        }

    def start_workflow(self, name: str):
        """
        Executa um fluxo específico, tratando a abertura de cada recurso.
        Inclui um pequeno delay para garantir que o sistema operacional processe as requisições.
        """
        if name in self.workflows:
            print(f"🛠️  Iniciando fluxo: {name}...")
            for url in self.workflows[name]:
                print(f"🌐 Abrindo: {url}")
                webbrowser.open(url)
                time.sleep(0.8)  # Delay técnico para estabilidade do browser
            print("✅ Fluxo concluído com sucesso.")
        else:
            print(f"⚠️ Fluxo '{name}' não encontrado.")

# --- Demonstração de Uso ---
if __name__ == "__main__":
    # Instancia a ferramenta
    app = RoutineAutomator()
    
    # Exemplo: Iniciando o dia de estudos
    # O objetivo aqui é reduzir a carga cognitiva de abrir tudo manualmente.
    app.start_workflow("Estudo")
