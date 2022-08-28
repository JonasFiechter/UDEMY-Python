class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'w+') as f:
            f.write(msg + '\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')

test = LogMixin()
test.write('TESTING')