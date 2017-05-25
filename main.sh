#!/bin/bash

readonly DIR=`pwd`
readonly SRC="${DIR}/src"
readonly SRC_DICT="${SRC}/dict"
readonly SRC_SCHEMA="${SRC}/schema"
readonly DEST="${DIR}/dest"
readonly DEST_DICT="${DEST}/emoji_s.dict"

cp "${SRC_DICT}/main.meta.yaml" "${DEST}/emoji_s.main.dict.yaml"

# make a directory for "real" dicts
mkdir -p "${DEST_DICT}"
cp "${SRC_DICT}/gemoji/gemoji.meta.yaml"  "${DEST_DICT}/emoji_s.gemoji.dict.yaml"
cp "${SRC_DICT}/emojipedia/emojipedia.meta.yaml"  "${DEST_DICT}/emoji_s.emojipedia.dict.yaml"

# generate the dictionaries
python3 ./gemoji.py "${SRC_DICT}/gemoji/emoji.json"  "${DEST_DICT}/emoji_s.gemoji.dict.yaml"
python3 ./emojipedia.py "${SRC_DICT}/emojipedia/Emoji.xml"  "${DEST_DICT}/emoji_s.emojipedia.dict.yaml"

# copy the schema
cp "${SRC_SCHEMA}/emoji_s.schema.yaml" "${DEST}/"
