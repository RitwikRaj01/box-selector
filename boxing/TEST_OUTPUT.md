# Test Output

## Command
```bash
python manage.py test boxing
```

## Output

Found 4 test(s).

Creating test database for alias 'default'...

System check identified no issues (0 silenced).

....
Ran 4 tests in 0.010s
OK

Destroying test database for alias 'default'...

## Tests Covered
1. `test_recommends_cheapest_fitting_box` - Verifies cheapest box is selected for a small order
2. `test_no_box_when_too_heavy` - Verifies None returned when product exceeds all box weight limits
3. `test_large_box_for_big_order` - Verifies large box selected when small box weight limit exceeded
4. `test_no_box_found_returns_none` - Verifies None returned when product dimensions exceed all boxes