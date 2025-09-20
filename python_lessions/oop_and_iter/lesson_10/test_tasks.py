from tasks import Stack, LRUCache, Trie


def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.peek() is None


def test_lru_cache():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    cache.put("c", 3)  # Should evict "b"
    assert cache.get("b") is None
    assert cache.get("c") == 3


def test_trie():
    t = Trie()
    t.insert("hello")
    t.insert("world")
    assert t.search("hello") is True
    assert t.search("hell") is False
    assert t.starts_with("hel") is True
    assert t.starts_with("xyz") is False


