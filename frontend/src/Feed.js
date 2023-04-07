import React from 'react';
import Post from './Post';

const Feed = ({ posts }) => {
  return (
    // fagment html
    <> 
      {posts.map(post => (
        <Post key={post.id} post={post}/>
      ))}
    </>
  )
}

export default Feed
