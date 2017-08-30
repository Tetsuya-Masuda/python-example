#False以外はTrue
def bool_test(candidate):
    if candidate == True:
        print('True')
    else:
        print('False')

bool_test(False)
bool_test(None)
bool_test(0)
bool_test(0.0)
bool_test('')
bool_test([])
bool_test(())
bool_test({})
bool_test(set())