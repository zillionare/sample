"""Console script for sample."""

import fire


def help():
    print("sample")
    print("=" * len("sample"))
    print("Skeleton project created by Python Project Wizard (ppw)")


def main():
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
