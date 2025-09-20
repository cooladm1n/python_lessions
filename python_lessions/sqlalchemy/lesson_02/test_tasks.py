from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tasks import Base, User, Post, Tag, UserPost


def test_user_model():
    user = User(username="alice", email="alice@example.com")
    assert user.username == "alice"
    assert user.email == "alice@example.com"
    assert str(user) == "User(alice)"


def test_post_model():
    post = Post(title="My First Post", content="This is my first post")
    assert post.title == "My First Post"
    assert post.content == "This is my first post"
    assert str(post) == "Post(My First Post)"


def test_tag_model():
    tag = Tag(name="python")
    assert tag.name == "python"
    assert str(tag) == "Tag(python)"


def test_user_post_association():
    user_post = UserPost(rating=5)
    assert user_post.rating == 5
    assert str(user_post) == "UserPost(rating=5)"


def test_relationships():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create user
    user = User(username="bob", email="bob@example.com")
    session.add(user)
    session.commit()
    
    # Create post
    post = Post(title="Test Post", content="Test content", author_id=user.id)
    session.add(post)
    session.commit()
    
    # Create tag
    tag = Tag(name="test")
    session.add(tag)
    session.commit()
    
    # Add tag to post
    post.tags.append(tag)
    session.commit()
    
    # Verify relationships
    assert len(user.posts) == 1
    assert user.posts[0].title == "Test Post"
    assert len(post.tags) == 1
    assert post.tags[0].name == "test"
    
    session.close()


