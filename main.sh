#!/bin/bash

# generate the dictionary
python3 ./generate_dict.py

# copy the schema
cp src/schema/emoji_s.schema.yaml dest/
