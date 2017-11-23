#!/bin/bash

readonly DIR=`pwd`
readonly SRC="${DIR}/src"
readonly STUB="${SRC}/stub"
readonly DATA="${SRC}/data"
readonly EMOJILIB_DIR="${DATA}/emojilib"
readonly CONVERTER="${SRC}/converter"
readonly DIST="${DIR}/dist"

rm -rf "${DIST}"
mkdir -p "${DIST}"
cp -r "${STUB}/." "${DIST}"
python3 "${CONVERTER}/emojilib.py" "${EMOJILIB_DIR}/emojis.json" >> "${DIST}/emoji_s.dict/emoji_s.emojilib.dict.yaml"
