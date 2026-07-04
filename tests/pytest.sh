#!/bin/bash

echo "Running Unit tests"

pytest --random-order --cov=ai-trading-bot --cov-config=.coveragerc tests/
