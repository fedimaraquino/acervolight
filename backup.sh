#!/bin/bash

# Diretório de backup (fora do projeto)
BACKUP_DIR="/var/backups/acervolight"

# Criar diretório de backup se não existir
mkdir -p $BACKUP_DIR

# Nome do arquivo de backup com timestamp
BACKUP_FILE="$BACKUP_DIR/acervolight_$(date +%Y%m%d_%H%M%S).sql"

# Fazer backup
docker exec acervolight-db-1 pg_dump -U postgres -d acervolight > $BACKUP_FILE

# Compactar o backup
gzip $BACKUP_FILE

# Manter apenas os últimos 7 backups
ls -t $BACKUP_DIR/acervolight_*.sql.gz | tail -n +8 | xargs -r rm

echo "Backup concluído: ${BACKUP_FILE}.gz" 