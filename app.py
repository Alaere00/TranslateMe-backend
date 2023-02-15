from flask import Flask
from dotenv import load_dotenv

def create_app(test_config=None):
    app = Flask(__name__)

    load_dotenv()

    from src.fire_database import fire_bp
    app.register_blueprint(fire_bp)
    
    return app



if __name__ == '__main__':
    create_app(debug=True).run()