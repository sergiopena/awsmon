import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--stack",
        help="Stack name to check for"
    )
    parser.add_argument(
        "-i",
        "--interval",
        default=30,
        help="Iteration interval"
    )
    return parser.parse_args()
