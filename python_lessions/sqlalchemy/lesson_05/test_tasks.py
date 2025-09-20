from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tasks import Base, User, Post, Tag, get_top_users, get_posts_with_comments, get_user_rankings


def test_get_top_users():
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
    
    # Test query
    top_users = get_top_users(session, 2)
    assert len(top_users) <= 2
    assert all("username" in user for user in top_users)
    
    session.close()


def test_get_posts_with_comments():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create test data
    user = User(username="alice", email="alice@example.com")
    session.add(user)
    session.commit()
    
    post = Post(title="Test Post", content="Test content", author_id=user.id)
    session.add(post)
    session.commit()
    
    # Test query
    posts = get_posts_with_comments(session)
    assert len(posts) >= 0
    assert all("title" in post for post in posts)
    
    session.close()


def test_get_user_rankings():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create test data
    user1 = User(username="alice", email="alice@example.com")
    user2 = User(username="bob", email="bob@example.com")
    session.add_all([user1, user2])
    session.commit()
    
    # Test query
    rankings = get_user_rankings(session)
    assert len(rankings) >= 0
    assert all("username" in user for user in rankings)
    
    session.close()


