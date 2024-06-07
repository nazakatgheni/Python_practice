from app import app

from app.controllers import user_controller, sight_controller

if __name__ == "__main__":
    app.run(debug=True)
