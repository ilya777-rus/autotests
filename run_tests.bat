@echo off
for /l %%x in (1, 1, 15) do (
    pytest -s -v --tb=line test_scen3.py

)