from webhook.app import app
from webhook.scheduler import scheduler


if __name__ == '__main__':
    print('Starting scheduler')
    scheduler.start()
    print('Starting app')
    app.run('0.0.0.0', debug=True)
    print('Stopping scheduler')
    scheduler.shutdown()
    print('bye bye')
