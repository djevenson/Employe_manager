import uvicorn
from source.framework.fast_api_app import create_app

if __name__ == "__main__":
    app = create_app()
    print("\n  Clean Architecture Employee Manager — REST API")
    print("  Running at http://localhost:8000\n")
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)  