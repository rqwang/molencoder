from argparse import ArgumentDefaultsHelpFormatter


def func(args, parser):
    pass

def configure_parser(sub_parsers):
    help = 'Train autoencoder'
    p = sub_parsers.add_parser('train', description=help, help=help,
                               formatter_class=ArgumentDefaultsHelpFormatter)
    p.set_defaults(func=func)
