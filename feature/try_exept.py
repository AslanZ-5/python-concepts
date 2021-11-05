def outline(func):
    def inner(*args,**kwargs):
        print('-'*20)
        print(f'Function: {func.__name__}')
        return func(*args,**kwargs)

    return inner

@outline
def test_one(x,y):
    try:
        assert(x > 0)
        assert(y >0)
    except AssertionError:
        print('failed to assert ')
    except Exception as e:
        print(f'Essue : {e}')
    else:
        z = x/y
        print(f'Result: {z}')
    finally:
        print('good luck any way')

test_one(10,'ddd')


