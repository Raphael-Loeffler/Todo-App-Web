from flask import Flask, request, render_template

def run():
    app = Flask('/')
    
    @app.route('/')
    def index():
        return render_template('/index.html')
    
    app.run()

if __name__ == "__main__":
    run()