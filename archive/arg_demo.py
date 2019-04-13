import argparse

print ('*'*70)
print (' run "python arg_demo.py  --h" for help msg ')
print ('*'*70)

parser = argparse.ArgumentParser()
parser.add_argument('--schemas', nargs='*', help='= set up some schema')
parser.add_argument('--tables', nargs='*', help='The table to dump')
parser.add_argument('--db', required=True, help='The database to dump')
parser.add_argument('--all', help='run on  all tables')
parser.add_argument('--date', required=True, help='execute day')

args = parser.parse_args()
tables = args.tables or []
schemas = args.schemas or []
reset_all = args.all or False


