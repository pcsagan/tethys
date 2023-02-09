from tethys.foobar import bar, fetch


def test_foobar():
    assert 'foo' == bar()


def test_fetch():
    status = fetch()
    assert status == 200
