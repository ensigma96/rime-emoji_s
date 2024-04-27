#!/bin/bash

readonly DIR=`pwd`
readonly SRC="${DIR}/src"
readonly STUB="${DIR}/stub"
readonly DATA="${DIR}/data"
readonly EMOJILIB_DIR="${DATA}/emojilib"
readonly GEMOJI_DIR="${DATA}/gemoji"
readonly EMOJIPEDIA_DIR="${DATA}/Emojipedia"
readonly CONVERTER="${SRC}/converter"
readonly DIST="${DIR}/dist"

rm -rf "${DIST}"
mkdir -p "${DIST}"
cp -r "${STUB}/." "${DIST}"
python3 "${CONVERTER}/emojilib.py" "${EMOJILIB_DIR}/emojis.json" >> "${DIST}/emoji_s.dict/emoji_s.emojilib.dict.yaml"
python3 "${CONVERTER}/gemoji.py" "${GEMOJI_DIR}/db/emoji.json" >> "${DIST}/emoji_s.dict/emoji_s.gemoji.dict.yaml"
python3 "${CONVERTER}/emojipedia.py" "${EMOJIPEDIA_DIR}/Emoji.xml" >> "${DIST}/emoji_s.dict/emoji_s.emojipedia.dict.yaml"
