# GPT-4o × FastAPI（MCPツール） × Streamlit

## 概要

このレポジトリは、以下の構成でMCPサーバーとStreamlit UIを接続します：

```
ユーザー → Streamlit（UI）→ GPT-4o（OpenAI）→ FastAPI（ツールサーバー）
```

## MCPツールエンドポイント

- FastAPIサーバーは `/tool/echo` を提供し、OpenAPI形式でGPT-4oから直接呼び出せます。

## FastAPI MCPのデプロイ手順（Render）

1. `fastapi_server/main.py` をRenderにアップロード
2. Start Command:
    ```
    uvicorn fastapi_server.main:app --host=0.0.0.0 --port=10000
    ```
3. 公開URLを `streamlit_frontend/app.py` に反映してください

## Streamlit Cloudの使い方

1. `streamlit_frontend/app.py` を GitHub にアップ
2. `.streamlit/secrets.toml` に以下を記載

```
OPENAI_API_KEY = "sk-xxx..."
```

3. Streamlit Cloud でデプロイ