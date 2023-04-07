import React from 'react'
import { useParams, Link, useHistory } from 'react-router-dom';
import { useContext } from 'react';
import api from './api/post'
import DataContext from './context/DataContext';

const PostPage = () => {
  const { posts, setPosts } = useContext(DataContext);
  const { id } = useParams();
  const post = posts.find(post => (post.id).toString() === id);
  const history = useHistory();
  const handleDelete = async (id) => {
    try {
      await api.delete(`/blog/delete/${id}`);
      const postList = posts.filter((post) => post.id !== id);
      setPosts(postList);
      history.push("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };
  return (
    <main>
      <article className='PostPage'>
        {post &&
          <>
            <h2>{post.title}</h2>
            <p className='postDate'>{post.datetime}</p>
            <p className='postBody'>{post.body}</p>
            <Link to={`/blog/update/${post.id}`}>
              <button className='editButton'>Edit Post</button>
            </Link>
            <button className='deleteButton' onClick={() => handleDelete(post.id)}>
              Delete Post
            </button>
          </>
          }
          {!post &&
          <>
            <h2>Post Not Found</h2>
            <p>Well, that's disappointing</p>
            <p>
              <Link to='/'>Visit Our Homepage</Link>
            </p>
          </>
          }
      </article>
    </main>
  )
}

export default PostPage
