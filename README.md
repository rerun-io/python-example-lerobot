# Rerun visualization of HuggingFace datasets
Tested with LeRobot datasets:

* https://huggingface.co/lerobot
* https://huggingface.co/datasets/lerobot/pusht

https://github.com/rerun-io/python-example-lerobot/assets/1148717/19e9983c-531f-4c48-9b37-37c5cbe1e0bd


## Getting started
Requires Python 3.10 or higher.

```sh
pip install -r requirements.txt
python main.py
```

Example datasets to explore (use `python main.py --dataset`):
* `lerobot/aloha_sim_insertion_human`
* `lerobot/aloha_sim_insertion_scripted`
* `lerobot/aloha_sim_transfer_cube_human`
* `lerobot/aloha_sim_transfer_cube_scripted`
* `lerobot/pusht`
* `lerobot/xarm_lift_medium`
* `nateraw/kitti`
* `sayakpaul/nyu_depth_v2`

## Note for the maintainer
You can update this repository with the latest changes from https://github.com/rerun-io/rerun_template by running `scripts/template_update.py update --languages python`.
