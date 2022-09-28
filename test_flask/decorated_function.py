def dire_bonjour(function):
    def wrapper(*args):
        print('Bonjour toi!')
        function(args[0])
    return wrapper

@dire_bonjour
def mon_nom(name):
    print(f'Mon nom est {name}')


mon_nom("Ange")

