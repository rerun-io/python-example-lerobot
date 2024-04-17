#!/usr/bin/env python3

from __future__ import annotations

import rerun as rr
from datasets import load_dataset
from PIL import Image
from tqdm import tqdm


def log_dataset_to_rerun(dataset) -> None:
    # Special time-like columns
    TIME_LIKE = {"index", "frame_id", "timestamp"}

    # Ignore these columns
    IGNORE = {"episode_data_index_from", "episode_data_index_to", "episode_id"}

    num_rows = len(dataset)
    for row_nr in tqdm(range(num_rows)):
        row = dataset[row_nr]

        # Handle time-like columns first, since they set a state (time is an index in Rerun):
        for column_name in TIME_LIKE:
            if column_name in row:
                cell = row[column_name]
                if isinstance(cell, int):
                    rr.set_time_sequence(column_name, cell)
                elif isinstance(cell, float):
                    rr.set_time_seconds(column_name, cell)  # assume seconds
                else:
                    print(f"Unknown time-like column {column_name} with value {cell}")

        # Now log actual data columns
        for column_name in dataset.column_names:
            if column_name in TIME_LIKE or column_name in IGNORE:
                continue

            cell = row[column_name]
            if isinstance(cell, Image.Image):
                rr.log(column_name, rr.Image(cell))
            elif isinstance(cell, list):
                rr.log(column_name, rr.BarChart(cell))
            elif isinstance(cell, float) or isinstance(cell, int):
                rr.log(column_name, rr.Scalar(cell))
            else:
                rr.log(column_name, rr.TextDocument(str(cell)))


def main():
    print("Loading dataset…")
    # dataset = load_dataset("lerobot/pusht", split="train")
    dataset = load_dataset("lerobot/aloha_sim_transfer_cube_human", split="train")

    print("Selecting specific episode…")
    ds_subset = dataset.filter(lambda frame: frame["episode_id"] == 3)

    print("Starting Rerun…")
    rr.init("rerun_example_lerobot", spawn=True)

    print("Logging to Rerun…")
    log_dataset_to_rerun(ds_subset)


if __name__ == "__main__":
    main()
