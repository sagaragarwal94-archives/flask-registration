from app import app
from flask_script import Manager, Server

manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True))

if __name__ == '__main__':
    manager.run()
