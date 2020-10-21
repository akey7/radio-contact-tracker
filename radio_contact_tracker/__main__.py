import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an ALL.TXT file from WSJT-X")
    parser.add_argument("--input", type=str, help="Path to ALL.TXT from WSJT-X", required=True)
    args = parser.parse_args()
