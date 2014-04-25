#!/bin/bash

UISOURCEDIR=./ui
UIBUILDDIR=./henrique/ui
UICOMPILER=pyuic4

function compileui {
    for file in $UISOURCEDIR/*; do
        local destfile=$(basename $file)
        destfile=${destfile/.ui/.py}
        destfile="$UIBUILDDIR/$destfile"

        echo "$UICOMPILER $file -o $destfile"
        $UICOMPILER $file -o $destfile
    done
}

function clean {
    echo "rm -rf $UIBUILDDIR/*"
    rm -rf $UIBUILDDIR/*
}

clean
compileui
