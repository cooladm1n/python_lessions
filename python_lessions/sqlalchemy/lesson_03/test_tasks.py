from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tasks import Base, User, Post, Tag, get_user_with_posts, get_posts_by_tag, get_user_stats


def test_get_user_with_posts():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create test data
    user = User(username="alice", email="alice@example.com")
    session.add(user)
    session.commit()
    
    post1 = Post(title="Post 1", content="Content 1", author_id=user.id)
    post2 = Post(title="Post 2", content="Content 2", author_id=user.id)
    session.add_all([post1, post2])
    session.commit()
    
    # Test eager loading
    user_with_posts = get_user_with_posts(session, user.id)
    assert user_with_posts is not None
    assert len(user_with_posts.posts) == 2
    
    session.close()


def test_get_posts_by_tag():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create test data
    user = User(username="bob", email="bob@example.com")
    session.add(user)
    session.commit()
    
    post = Post(title="Python Post", content="Python content", author_id=user.id)
    session.add(post)
    session.commit()
    
    tag = Tag(name="python")
    session.add(tag)
    session.commit()
    
    post.tags.append(tag)
    session.commit()
    
    # Test query
    posts = get_posts_by_tag(session, "python")
    assert len(posts) == 1
    assert posts[0].title == "Python Post"
    
    session.close()


def test_get_user_stats():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create test data
    user1 = User(username="alice", email="alice@example.com")
    user2 = User(username="bob", email="bob@example.com")
    session.add_all([user1, user2])
    session.commit()
    
    post1 = Post(title="Post 1", content="Content 1", author_id=user1.id)
    post2 = Post(title="Post 2", content="Content 2", author_id=user1.id)
    post3 = Post(title="Post 3", content="Content 3", author_id=user2.id)
    session.add_all([post1, post2, post3])
    session.commit()
    
    # Test stats
    stats = get_user_stats(session)
    assert "total_users" in stats
    assert "total_posts" in stats
    assert stats["total_users"] == 2
    assert stats["total_posts"] == 3
    
    session.close()


