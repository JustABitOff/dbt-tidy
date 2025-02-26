#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <version>"
  exit 1
fi

VERSION="$1"

OUTPUT_DIR="tidy/manifest/$VERSION"

mkdir -p "$OUTPUT_DIR"

datamodel-codegen \
  --input-file-type jsonschema \
  --target-python-version 3.11 \
  --output-model-type pydantic_v2.BaseModel \
  --disable-timestamp \
  --class-name Manifest \
  --url "https://schemas.getdbt.com/dbt/manifest/$VERSION.json" \
  --output "$OUTPUT_DIR/manifest.py" \
  --reuse-model \
  --use-title-as-name \
  --disable-appending-item-suffix
