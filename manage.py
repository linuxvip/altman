from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps import create_app, db

# 调用创建flask应用文件中的应用生成函数，加入参数说明当前环境
app = create_app(config_name="develop")

manager = Manager(app)

Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    print(app.url_map)
    manager.run()
