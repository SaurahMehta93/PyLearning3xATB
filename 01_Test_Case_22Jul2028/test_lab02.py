import pytest
@pytest.mark.smoke
def test_sub0():
    assert 2-2==0

@pytest.mark.regression
def test_sub1():
    assert 3-3==0

@pytest.mark.smoke
def test_sub2():
    assert 4-2==0

@pytest.mark.sanity
def test_sub3():
    assert 1-1==0

@pytest.mark.skil(reason="not working")
def test_sub4():
    assert 0-0!=0

#to run this below command use
#pytest -m "smoke" 01_Test_Case_22Jul2028/test_lab02.py

