from main import init_app


app = init_app()


if __name__ == "__main__":
    app.run(host='192.168.2.22', port='8090', debug=True)
