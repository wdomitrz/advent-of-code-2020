#!/usr/bin/env bash
diff answers.txt <(for f in d*.py ; do python3 $f ; done)
