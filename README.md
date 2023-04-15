# aprendizaje_maquina_II
Repositorio de material de trabajo, presentaciones , códigos e implementaciones.

# Las migrations estan en alembic
https://alembic.sqlalchemy.org/en/latest/

Para correr las migrations hay que cambiar el file migrations/sqlalchemy.url
y poner el conection string del postgres donde queramos correr las migrations

* Subir migration: alembic upgrade head
* roolback migration: alembic downgrade base