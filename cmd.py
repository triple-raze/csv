from tabulate import tabulate
import argparse
import csv
from libs.core import csv_filter, csv_aggregate

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--file', type=str, required=True)
    parser.add_argument('--where', type=str)
    parser.add_argument('--aggregate', type=str)

    args = parser.parse_args()

    with open(args.file, 'r') as file:
        response = list(csv.DictReader(file))
        
        if args.where:
            response = csv_filter(response, args.where)

        if args.aggregate:
            response = csv_aggregate(response, args.aggregate)

        print(tabulate(response, headers='keys', tablefmt='rounded_outline'))

if __name__ == '__main__':
    main()