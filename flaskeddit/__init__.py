from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler
import logging

from flaskeddit.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message_category = "danger"


def create_app(config=Config):
    """
    Factory method for creating the Flaskeddit Flask app.
    https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/
    """
    logging.basicConfig(level=logging.DEBUG)
    # 创建日志记录器，指明日志保存的路径，每个日志文件的最大值，保存的日志文件个数上限
    log_handle = RotatingFileHandler("log.txt", maxBytes=1024 * 1024, backupCount=5)
    # 创建日志记录的格式
    formatter = logging.Formatter("format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',")
    # 为创建的日志记录器设置日志记录格式
    log_handle.setFormatter(formatter)
    # 为全局的日志工具对象添加日志记录器
    logging.getLogger().addHandler(log_handle)
    logging.warning('Generally for printing the warning information')
    logging.error('Generally for printing the error message')
    logging.critical('Printing the critical information, it\'s the highest level')

    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    login_manager.init_app(app)

    from flaskeddit.auth import auth_blueprint
    from flaskeddit.communities import communities_blueprint
    from flaskeddit.community import community_blueprint
    from flaskeddit.feed import feed_blueprint
    from flaskeddit.post import post_blueprint
    from flaskeddit.reply import reply_blueprint
    from flaskeddit.user import user_blueprint
    from flaskeddit.cli import cli_app_group

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(communities_blueprint)
    app.register_blueprint(community_blueprint)
    app.register_blueprint(feed_blueprint)
    app.register_blueprint(post_blueprint)
    app.register_blueprint(reply_blueprint)
    app.register_blueprint(user_blueprint)
    app.cli.add_command(cli_app_group)

    return app
