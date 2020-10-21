import argparse
from typing import List, Dict, Union
import re


class RadioContactTracker:
    def __init__(self, all_txt_filename: str):
        self.all_txt_filename = all_txt_filename
        self.all_txt_records: List[Dict[str, Union[str, float]]] = []

    def read_all_txt(self) -> None:
        with open(self.all_txt_filename, "r") as alt_txt:
            for line in alt_txt.readlines():
                squeezed = re.sub("\s\s+", " ", line)
                squeezed = squeezed.split(" ")
                year = f"20{squeezed[0][:2]}"
                month = squeezed[0][2:4]
                day = squeezed[0][7:9]
                hour = squeezed[0][9:11]
                minute = squeezed[0][11:13]
                second = squeezed[0][13:15]
                print(year, month, day, hour, minute, second)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an ALL.txt file from WSJT-X")
    parser.add_argument("--input", type=str, help="Path to ALL.txt from WSJT-X", required=True)
    args = parser.parse_args()
    tracker = RadioContactTracker(args.input)
    tracker.read_all_txt()
