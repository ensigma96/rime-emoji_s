# rime-emoji_s
Yet another emoji / 繪文字 input scheme for RIME, including scripts used in generating it.

The source data comes from [gemoji](https://github.com/github/gemoji), and can be downloaded at https://github.com/github/gemoji/blob/master/db/emoji.json .

## Generating the files

This repo comes with ready-to-deploy files (in `dest/`), but you can still re-generate them yourself: `./main.sh` and that's all.

## Usage (with rime-ibus)

To add the new schema, rime-ibus users may follow these steps:

1. Enter the `dest/` directory and copy everything to `~/.config/ibus/rime/`.
2. Enter `~/.config/ibus/rime/` and edit `default.custom.yaml`. Add `emoji_s` to `schema_list` to enable the new scheme. Comment out the original `emoji` line (if it exists and) if you find that necessary.
3. `rm ~/.config/ibus/rime/default.yaml; ibus-daemon -drx`: Deploy!

Users of other flavors of RIME should go through similar steps. See Rime's [wiki](https://github.com/rime/home/wiki) for more information.
