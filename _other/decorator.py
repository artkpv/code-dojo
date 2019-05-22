import threading


def persistant_caller(max_calls=None, timeout_ms=None):
    def actual(function):
        def persistant_function(*args, **kwargs):
            count = 0
            while True:
                try:
                    count += 1
                    return function(*args, **kwargs)
                except Exception as e:
                    if count > max_calls:
                        # report exception
                        raise e
                    # report exception
                    if timeout_ms:
                        threading.sleep(timeout_ms)

        return persistant_function
    return actual


count = 0


@persistant_caller(max_calls=2, timeout_ms=100)
def printer(arg1, key1=None, key2=None):
    global count
    if count < 0:
        count += 1
        raise Exception('first exception')
    print('printer', arg1, key1, key2)


printer(1, key1='key1val', key2='key2val')
