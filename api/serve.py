from uvicorn import run

if __name__ == '__main__':
    run("main:app", host="0.0.0.0", reload=True, port=8080)