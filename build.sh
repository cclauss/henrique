#!/bin/bash

UISOURCEDIR=./qtdesigner
UIBUILDDIR=./henrique/qtdesigner
UICOMPILER=pyuic4

function compileui {
    if [ ! -d "$UIBUILDDIR" ]; then
        echo "mkdir -p $UIBUILDDIR"
        mkdir -p $UIBUILDDIR
    fi

    if [ ! -f "$UIBUILDDIR/__init__.py" ]; then
        echo "touch $UIBUILDDIR/__init__.py"
        touch "$UIBUILDDIR/__init__.py"
    fi
        

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
