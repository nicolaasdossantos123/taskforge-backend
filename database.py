from sqlalchemy import create_engine, text

DATABASE_URL = (
    "postgresql://postgres:night@localhost:5432/taskforge"
)

engine = create_engine(DATABASE_URL)

with engine.connect() as conexao:

    conexao.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS usuarios (

                id SERIAL PRIMARY KEY,

                nome VARCHAR(100),

                email VARCHAR(100),

                senha VARCHAR(100)
            )
            """
        )
    )

    conexao.commit()

print("Tabela criada!")

with engine.connect() as conexao:
    
    conexao.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS tarefas (

                id SERIAL PRIMARY KEY,

                titulo VARCHAR(100) NOT NULL,

                descricao TEXT,

                concluida BOOLEAN DEFAULT FALSE,

                usuario_id INTEGER NOT NULL
                    REFERENCES usuarios(id)
                    ON DELETE CASCADE
            )
            """
        )
    )

    conexao.commit()

print("Tabela criada!")