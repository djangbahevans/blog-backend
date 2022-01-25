from sqlalchemy import (BigInteger, Boolean, Column, DateTime, ForeignKey,
                        String, text)
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, PhoneNumberType

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    given_name = Column("given_name", String, nullable=True)
    additional_name = Column("additional_name", String, nullable=True)
    family_name = Column("family_name", String, nullable=True)
    phone_number = Column("phone_number", PhoneNumberType,
                          nullable=True, unique=True)
    email = Column("email", EmailType, nullable=True, unique=True)
    username = Column("username", String, nullable=False, unique=True)
    password_hash = Column("password_hash", String, nullable=True)
    last_login = Column("last_login", DateTime, nullable=True)
    intro = Column("intro", String, nullable=True)
    profile = Column("profile", String, nullable=True)
    created_at = Column("created_at", DateTime(
        timezone=True), nullable=False, server_default=text("now()"))


class Tag(Base):
    __tablename__ = "tag"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    title = Column("title", String, nullable=False)
    meta_title = Column("meta_title", String, nullable=True)
    slug = Column("slug", String, nullable=False)
    content = Column("content", String, nullable=True)


class Post(Base):
    __tablename__ = "post"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    author_id = Column("author_id", BigInteger, ForeignKey(
        "user.id", ondelete="CASCADE"), nullable=False)
    parent_id = Column("parent_id", String, nullable=True)
    title = Column("title", String, nullable=False)
    meta_title = Column("meta_title", String, nullable=True)
    slug = Column("slug", String, nullable=False)
    summary = Column("summary", String, nullable=True)
    published = Column("published", Boolean, nullable=False, default=False)
    content = Column("content", String, nullable=True)
    updated_at = Column("updated_at", DateTime, nullable=True)
    published_at = Column("published_at", DateTime, nullable=True)
    created_at = Column("created_at", DateTime(
        timezone=True), nullable=False, server_default=text("now()"))

    owner = relationship("User")


class PostTag(Base):
    __tablename__ = "tag_category"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    post_id = Column("post_id", BigInteger, ForeignKey(
        "post.id", ondelete="CASCADE"), nullable=False)
    category_id = Column("category_id", BigInteger, ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)

    post = relationship("Post")
    category = relationship("Category")


class PostMeta(Base):
    __tablename__ = "post_meta"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    post_id = Column("post_id", BigInteger, ForeignKey(
        "post.id", ondelete="CASCADE"), nullable=False)
    key = Column("key", BigInteger, nullable=False)
    content = Column("content", String, nullable=True)

    owner = relationship("Post")


class PostComment(Base):
    __tablename__ = "post_comment"

    id = Column("id", BigInteger, primary_key=True,
                nullable=False, unique=True)
    post_id = Column("post_id", BigInteger, ForeignKey(
        "post.id", ondelete="CASCADE"), nullable=False)
    parent_id = Column("parent_id", BigInteger, ForeignKey(
        "post_comment.id", ondelete="CASCADE"), nullable=True)
    title = Column("title", BigInteger, primary_key=True, nullable=False)
    content = Column("content", String, nullable=False)
    published = Column("published", Boolean, nullable=False, default=False)
    published_at = Column("published_at", DateTime, nullable=False)
    created_at = Column("created_at", DateTime(
        timezone=True), nullable=False, server_default=text("now()"))

    post = relationship("Post")
    comment = relationship("PostComment")


class PostCategory(Base):
    __tablename__ = "post_category"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    post_id = Column("post_id", BigInteger, ForeignKey(
        "post.id", ondelete="CASCADE"), nullable=False)
    category_id = Column("category_id", BigInteger, ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)

    post = relationship("Post")
    category = relationship("Category")


class Category(Base):
    __tablename__ = "category"

    id = Column("id", BigInteger, primary_key=True, nullable=False)
    parent_id = Column("parent_id", BigInteger, ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=True)
    title = Column("title", String, nullable=False)
    meta_title = Column("meta_title", String, nullable=True)
    slug = Column("slug", String, nullable=False)
    content = Column("content", String, nullable=True)

    parent = relationship("Category")
