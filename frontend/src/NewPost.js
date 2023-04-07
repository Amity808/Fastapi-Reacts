import React from 'react'
import { useContext, useState } from 'react';
import DataContext from './context/DataContext';
import api from './api/post';
import format from 'date-fns/format';
import { useHistory } from 'react-router-dom';

const NewPost = () => {
    const [postTitle, setPostTitle] = useState("");
    const [postBody, setPostBody] = useState("");
    const { posts, setPosts } = useContext(DataContext);
    const history = useHistory();
    const handleSubmit = async (e) => {
        e.preventDefault();
        const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
        const postDat = format(new Date(), "MMMM dd, yyyyy pp");
        const newPost = { id, title: postTitle, postDat, body: postBody };
        try {
          const response = await api.post("/blog/create/", newPost);
          const allPosts = [...posts, response.data];
          setPosts(allPosts);
          setPostTitle("");
          setPostBody("");
          history.push("/");
        } catch (err) {
          console.log(`Error: ${err.message}`);
        }
      };
  return (
      <main className="NewPost">
          <h2>New Post</h2>
          <form className="newPostForm" onSubmit={handleSubmit}>
              <label htmlFor="postTitle">Title:</label>
              <input
                  id="postTitle"
                  type="text"
                  required
                  value={postTitle}
                  onChange={(e) => setPostTitle(e.target.value)}
              />
              <label htmlFor="postBody">Post:</label>
              <textarea
                  id="postBody"
                  required
                  value={postBody}
                  onChange={(e) => setPostBody(e.target.value)}
              />
              <button type="submit">Submit</button>
          </form>
      </main>
  )
}

export default NewPost