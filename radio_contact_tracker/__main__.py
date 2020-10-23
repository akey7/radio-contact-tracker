import argparse
from typing import List, Dict, Union
import re
import maidenhead as mh
import pandas as pd


class RadioContactTracker:
    def __init__(self, all_txt_filename: str):
        self.all_txt_filename = all_txt_filename
        self.all_txt_records: List[Dict[str, Union[str, float]]] = []

    def read_all_txt(self) -> None:
        self.all_txt_records = []
        with open(self.all_txt_filename, "r") as alt_txt:
            for line in alt_txt.readlines():
                line = line.strip()
                squeezed = re.sub("\s\s+", " ", line)
                squeezed = squeezed.split(" ")
                if len(squeezed) == 10:
                    row = {
                        "year": f"20{squeezed[0][:2]}",
                        "month": squeezed[0][2:4],
                        "day": squeezed[0][7:9],
                        "mhz": squeezed[1],
                        "source": squeezed[8],
                        "grid_or_signal": squeezed[9]
                    }
                    self.all_txt_records.append(row)

    def process_received_callsigns(self):
        receiveds: List[Dict[str, str]] = []
        for row in self.all_txt_records:
            grid_or_signal = row["grid_or_signal"]
            is_a_grid_square = re.match("[A-Z][A-Z][0-9][0-9]", grid_or_signal) is not None
            if grid_or_signal != "RR73" and is_a_grid_square:
                receiveds.append(row)
        receiveds_lat_long: List[Dict[str, str]] = []
        sources = set()
        for row in receiveds:
            lat, lon = mh.to_location(row["grid_or_signal"])
            row["latitude"] = lat
            row["longitude"] = lon
            if row["source"] not in sources:
                receiveds_lat_long.append(row)
                sources.add(row["source"])
        df = pd.DataFrame(receiveds_lat_long)
        return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an ALL.txt file from WSJT-X")
    parser.add_argument("--input", type=str, help="Path to ALL.txt from WSJT-X", required=True)
    args = parser.parse_args()
    tracker = RadioContactTracker(args.input)
    tracker.read_all_txt()
    rcvds = tracker.process_received_callsigns()
    rcvds.to_csv("log.csv")
