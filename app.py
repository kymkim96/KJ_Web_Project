from main import init_app

import sys
print (sys.path)

app = init_app()


if __name__ == "__main__":
    app.run(host='localhost', port='8090', debug=True)
