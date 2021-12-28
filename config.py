def config1(app, env):

    app['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///matches.db'
    app['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app['SECRET_KEY'] = 'secretkey1'
    app['TEMPLATES_AUTO_RELOAD'] = True

    env.auto_reload = True
    env.cache = {}