#!/usr/bin/env bash

if [ -z "$1" ]; then
    days=$(seq 1 25)
else
    days="$1"
fi

for day in $days; do
    day=$(printf "%02d" "$day")
    dst="day$day"

    if [ -d "$dst" ]; then
        echo "skipping $dst (already exists)"
        continue
    fi

    cp -r day00 "$dst"
    sed -i "s/package day00/package day$day/" "$dst/day00.odin"
    mv "$dst/day00.odin" "$dst/day$day.odin"
    > "$dst/test.txt"
    > "$dst/input.txt"

    echo "generated $dst"
done
