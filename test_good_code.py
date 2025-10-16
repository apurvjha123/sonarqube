# test_bad_code.py
import pytest
from bad_code import do_stuff, no_doc

def test_do_stuff():
    # simple test for do_stuff
    result = do_stuff(4, 2, 3)
    assert result == 10  # 2 + 3 + 2 + 3 = 10

def test_no_doc():
    # simple test for no_doc
    assert no_doc(3, 5) == 15

# Optional: run pytest main if executed directly
if __name__ == "__main__":
    import coverage
    cov = coverage.Coverage()
    cov.start()
    pytest.main([__file__])
    cov.stop()
    cov.save()
