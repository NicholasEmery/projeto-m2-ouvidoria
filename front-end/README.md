# Sistema de Ouvidoria

Este projeto é um sistema de ouvidoria desenvolvido com Flask para o backend e Angular para o frontend. O sistema permite o gerenciamento de manifestações, incluindo criação, edição, deleção e listagem.

## Tecnologias Utilizadas

### Backend (Flask)
- **Flask**: Micro framework para Python utilizado para construir a API.
- **Flask-CORS**: Extensão para permitir solicitações CORS (Cross-Origin Resource Sharing).
- **Flask-SQLAlchemy**: ORM (Object-Relational Mapping) para facilitar a interação com o banco de dados.
- **PyMySQL**: Driver para conectar o Flask ao banco de dados MySQL.

### Frontend (Angular)
- **@angular/core**: Núcleo do framework Angular.
- **@angular/common**: Conjunto de funcionalidades comuns do Angular.
- **@angular/forms**: Módulo para criar e manipular formulários reativos.
- **@angular/router**: Módulo para gerenciar rotas e navegação.
- **bootstrap**: Biblioteca CSS para estilização e design responsivo.

## Instalação

### Backend
1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```
2. Navegue até a pasta do backend:
   ```bash
   cd backend
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Frontend
1. Navegue até a pasta do frontend:
   ```bash
   cd frontend
   ```
2. Instale as dependências:
   ```bash
   npm install
   ```

## Uso

1. Inicie o servidor backend:
   ```bash
   flask run
   ```

2. Inicie o servidor frontend:
   ```bash
   ng serve
   ```

3. Acesse o sistema através do navegador em `http://localhost:4200`.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
