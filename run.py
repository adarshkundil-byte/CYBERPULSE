from app import create_app

app = create_app()

if __name__ == "__main__":
    # Local development only. Never expose this server to the public internet.
    app.run(host="127.0.0.1", port=5000)
