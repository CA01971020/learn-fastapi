# FastAPI 仮想環境での実行方法

## 仮想環境作成

```
python -m venv env
```

## 仮想環境有効化

```
.\env\Scripts\activate
```

## パッケージインストール

```
pip install fastapi uvicorn
```

## アプリケーション実行

```
uvicorn api.main:app --reload
```

## 仮想環境無効化

```
deactivate
```

# 実行結果の確認

default  
http://127.0.0.1:8000

docs  
http://127.0.0.1:8000/docs

redoc  
http://127.0.0.1:8000/redoc
