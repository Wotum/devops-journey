#!/bin/bash
grep ERROR "$1" | cut -d' ' -f4- | sort | uniq -c | sort -nr
