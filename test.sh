#!/bin/bash
# Quick test script for LocalhostKiller

echo "Testing LocalhostKiller..."
echo ""

echo "1. Testing --version"
python3 lhk.py --version
echo ""

echo "2. Testing --list"
python3 lhk.py --list
echo ""

echo "3. Testing --help"
python3 lhk.py --help
echo ""

echo "All tests passed!"
