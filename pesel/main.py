"""Module is providing support for CLI"""
import argparse
import sys
from pesel import Pesel


def cli():
    """Support CLI commands and arguments"""
    parser = argparse.ArgumentParser(prog="pesel", usage='%(prog)s')

    subparser = parser.add_subparsers(dest='command')
    generator = subparser.add_parser('generate', help='Generate PESEL number')
    generator.add_argument('--year', '-y', type=int, help='Year of birth',
                           default=argparse.SUPPRESS, dest='year')
    generator.add_argument('--month', '-m', type=int, help='Month of birth',
                           default=argparse.SUPPRESS, dest='month')
    generator.add_argument('--day', '-d', type=int, help='Day of birth',
                           default=argparse.SUPPRESS, dest='day')
    male_parser = generator.add_mutually_exclusive_group(required=False)
    male_parser.add_argument('--male', help='It is male person',
                             default=argparse.SUPPRESS, action='store_true', dest='male')
    male_parser.add_argument('--female', help='It is female person',
                             default=argparse.SUPPRESS, action='store_false', dest='male')

    validate = subparser.add_parser('validate', help='Validate PESEL number')
    validate.add_argument('pesel', metavar='pesel', type=str, help='PESEL number')

    args, _ = parser.parse_known_args()
    args = vars(args)
    command = args.pop('command')

    cmd = getattr(Pesel, command)
    try:
        output = cmd(**args)
    except ValueError as err:
        print(err, file=sys.stderr)
        sys.exit(1)

    print(output)
