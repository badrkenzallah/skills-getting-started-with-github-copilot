import importlib

modules = [
    'tests.test_unregister',
    'tests.test_signup_refresh'
]

for mod in modules:
    print(f'Running tests in {mod}')
    m = importlib.import_module(mod)
    for name in dir(m):
        if name.startswith('test_'):
            func = getattr(m, name)
            try:
                func()
                print(f'  OK: {name}')
            except AssertionError as e:
                print(f'  FAIL: {name} ->', e)
            except Exception as e:
                print(f'  ERROR: {name} ->', e)
