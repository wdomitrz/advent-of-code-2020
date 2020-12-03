#!/usr/bin/env bash
diff answers.txt <(for f in d*_part*.py ; do python3 $f ; done)
