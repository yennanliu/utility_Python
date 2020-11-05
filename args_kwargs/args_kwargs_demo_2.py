import json
import yaml
import sys
import argparse

# https://github.com/fishtown-analytics/dbt/blob/dev/kiyoshi-kuromiya/converter.py
# python args_kwargs_demo_2.py --job dummy_job_1 --workers 10

def yaml_type(fname):
    with open(fname) as f:
        return yaml.load(f)

def parse_args():
    parser = argparse.ArgumentParser()
    #parser.add_argument("--project", type=yaml_type, default="dev.yml")
    parser.add_argument("--job", required=True)
    parser.add_argument("--workers", required=True)
    return parser.parse_args()

def main():
    args = parse_args()
    if args.job not in ['dummy_job_1', 'dummy_job_2', 'dummy_job_3']:
        raise Exception("invalid job name")
    print(args)
    return {"job": args.job, "workers": args.workers}

if __name__ == "__main__":
    args = main()
    print (args)