# Guia de Deploy com Docker e Docker Compose

## Comandos Docker Básicos

### Gerenciamento de Containers
```bash
# Listar containers em execução
docker ps

# Listar todos os containers (incluindo parados)
docker ps -a

# Iniciar um container
docker start <nome_do_container>

# Parar um container
docker stop <nome_do_container>

# Remover um container
docker rm <nome_do_container>

# Ver logs de um container
docker logs <nome_do_container>

# Entrar em um container em execução
docker exec -it <nome_do_container> bash
```

### Gerenciamento de Imagens
```bash
# Listar imagens
docker images

# Remover uma imagem
docker rmi <nome_da_imagem>

# Construir uma imagem a partir do Dockerfile
docker build -t <nome_da_imagem> .
```

### Gerenciamento de Volumes
```bash
# Listar volumes
docker volume ls

# Remover um volume
docker volume rm <nome_do_volume>

# Inspecionar um volume
docker volume inspect <nome_do_volume>
```

## Comandos Docker Compose

```bash
# Iniciar todos os serviços
docker-compose up -d

# Parar todos os serviços
docker-compose down

# Reconstruir e iniciar serviços
docker-compose up -d --build

# Ver logs de todos os serviços
docker-compose logs

# Ver logs de um serviço específico
docker-compose logs <nome_do_serviço>

# Executar comando em um serviço
docker-compose exec <nome_do_serviço> <comando>
```

## Passo a Passo para Deploy

### 1. Preparação do Ambiente

1. Instale o Docker e Docker Compose no servidor
2. Clone o repositório do projeto
3. Crie um arquivo `.env` com as variáveis de ambiente necessárias

### 2. Configuração do Docker Compose

1. Crie ou ajuste o arquivo `docker-compose.yml`:
   ```yaml
   services:
     web:
       build: .
       command: gunicorn biblioteca.wsgi:application --bind 0.0.0.0:8000
       volumes:
         - .:/app
         - static_volume:/app/static
         - media_volume:/app/media
       ports:
         - "8080:8000"
       environment:
         - DJANGO_SETTINGS_MODULE=biblioteca.settings
         - DJANGO_SECRET_KEY=sua_chave_secreta
         - DJANGO_DEBUG=False
         - DJANGO_ALLOWED_HOSTS=seu_dominio.com
         - POSTGRES_DB=nome_do_banco
         - POSTGRES_USER=usuario
         - POSTGRES_PASSWORD=senha
       depends_on:
         - db

     db:
       image: postgres:13
       volumes:
         - postgres_data:/var/lib/postgresql/data
       environment:
         - POSTGRES_DB=nome_do_banco
         - POSTGRES_USER=usuario
         - POSTGRES_PASSWORD=senha

   volumes:
     postgres_data:
     static_volume:
     media_volume:
   ```

### 3. Configuração do Nginx (Opcional)

1. Crie um arquivo de configuração do Nginx:
   ```nginx
   server {
       listen 80;
       server_name seu_dominio.com;

       location / {
           proxy_pass http://localhost:8080;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }

       location /static/ {
           alias /var/www/acervolight/static/;
       }

       location /media/ {
           alias /var/www/acervolight/media/;
       }
   }
   ```

### 4. Deploy da Aplicação

1. Construa e inicie os containers:
   ```bash
   docker-compose up -d --build
   ```

2. Execute as migrações do banco de dados:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. Crie um superusuário:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

4. Colete arquivos estáticos:
   ```bash
   docker-compose exec web python manage.py collectstatic --noinput
   ```

### 5. Backup e Restauração

1. Fazer backup do banco de dados:
   ```bash
   docker exec acervolight-db-1 pg_dump -U postgres -d acervolight > backup_$(date +%Y%m%d_%H%M%S).sql
   ```

2. Restaurar backup:
   ```bash
   cat backup.sql | docker exec -i acervolight-db-1 psql -U postgres -d acervolight
   ```

### 6. Manutenção

1. Atualizar a aplicação:
   ```bash
   git pull
   docker-compose up -d --build
   ```

2. Verificar logs:
   ```bash
   docker-compose logs -f
   ```

3. Reiniciar serviços:
   ```bash
   docker-compose restart
   ```

## Dicas de Segurança

1. Nunca exponha o PostgreSQL diretamente na internet
2. Use senhas fortes para o banco de dados
3. Mantenha o `DJANGO_DEBUG=False` em produção
4. Use HTTPS com certificados SSL
5. Mantenha as imagens Docker atualizadas

## Solução de Problemas Comuns

1. **Erro de conexão com o banco de dados**:
   - Verifique as variáveis de ambiente
   - Confirme se o container do PostgreSQL está rodando
   - Verifique os logs do container do banco de dados

2. **Erro 404 em arquivos estáticos**:
   - Verifique se o volume está montado corretamente
   - Confirme se o `collectstatic` foi executado
   - Verifique as permissões dos diretórios

3. **Erro 500 no servidor**:
   - Verifique os logs da aplicação
   - Confirme se todas as dependências estão instaladas
   - Verifique se as migrações foram aplicadas

## Monitoramento

1. Verificar uso de recursos:
   ```bash
   docker stats
   ```

2. Verificar espaço em disco:
   ```bash
   docker system df
   ```

3. Limpar recursos não utilizados:
   ```bash
   docker system prune
   ``` 