import os
from app import create_app

# Cria a instância do app
app = create_app()

# Verifica se estamos rodando o arquivo principal
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)