import uvicorn
from source.framework.fast_api_app import create_app

if __name__ == "__main__":
    app = create_app()
    print("\n  Clean Architecture Employee Manager — REST API")
    print("  Running at http://127.0.0.1:8000\n")
    print("  Press CTRL+C to quit\n")
    print("  Press CTRL+R to reload\n")
    print("  http://127.0.0.1:8000/docs for API documentation Swagger\n")
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)  