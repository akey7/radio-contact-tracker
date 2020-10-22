import argparse
from typing import List, Dict, Union
import re


class RadioContactTracker:
    def __init__(self, all_txt_filename: str):
        self.all_txt_filename = all_txt_filename
        self.all_txt_records: List[Dict[str, Union[str, float]]] = []

    def read_all_txt(self) -> None:
        self.all_txt_records = []
        with open(self.all_txt_filename, "r") as alt_txt:
            for line in alt_txt.readlines():
                squeezed = re.sub("\s\s+", " ", line)
                squeezed = squeezed.split(" ")

                row = {
                    "year": f"20{squeezed[0][:2]}",
                    "month": squeezed[0][2:4],
                    "day": squeezed[0][7:9],
                    "mhz": squeezed[1],
                    "source": squeezed[8],
                }

                self.all_txt_records.append(row)

    def unique_callsigns(self):
        sources = set(row["source"] for row in self.all_txt_records)
        return sources


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an ALL.txt file from WSJT-X")
    parser.add_argument("--input", type=str, help="Path to ALL.txt from WSJT-X", required=True)
    args = parser.parse_args()
    tracker = RadioContactTracker(args.input)
    tracker.read_all_txt()
    print(len(tracker.unique_callsigns()))
