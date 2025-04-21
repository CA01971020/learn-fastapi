from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#postgresql
SQLALCHEMY_DATABASE_URL = "postgresql://fastapiuser:fastapipass@0.0.0.0:5432/fleamarket"

#接続エンジンの作成
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#データベースセッションの作成・管理
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

#データベースクラス
Base = declarative_base()