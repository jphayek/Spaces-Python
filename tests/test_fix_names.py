from spaces import fix_names

def test_hello_world():
    assert True

def test_base(tmpdir):
    test_file = tmpdir / "hello world.txt"
    test_file.write("content")
    fix_names(tmpdir)
    assert (tmpdir / "hello_world.txt").exists()
    assert not (tmpdir / "hello world.txt").exists()