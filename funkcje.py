#! /usr/bin/python


def print_dict(d):
    for key in samolot:
        print('{0},{1}'.format(key, d[key]))
if __name__ == '__main__': #od tad odpala skrypt
    samolot={'name': 'boeing',
    'przebieg': 10000,
    'type': 'pasazerski'}

    print_dict(samolot)
