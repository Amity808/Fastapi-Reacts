import Header from "./Header";
import NavBar from "./NavBar";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import EditPost from "./EditPost";
import About from "./About";
import Missing from './Missing'
import { Route, Switch } from "react-router-dom";
import { DataProvider } from "./context/DataContext";


function App() {
  


  // useEffect(() => {
  //   const fetchPosts = async () => {
  //     try {
  //       const response = await api.get('/posts')
  //       // if(response && response.data) to be carefull but it is in the range of 200 range response
  //       setPosts(response.data);
  //     } catch (err) {
  //       // if it is nit in the 200 response rage this is from documentation
  //       if(err.response) {
  //       console.log(err.response.data);
  //       console.log(err.response.status);
  //       console.log(err.response.headers)
  //       } else {
  //         console.log(`Error: ${err.message}`)
  //       }
  //     }
  //   }
  //   fetchPosts(); 
  // }, [])

  return (
    <div className="App">
        <Header title="React Js Blog & Fastapi" />
        <DataProvider>
        <NavBar />
        <Switch>
          <Route exact path="/" component={Home}/>
          <Route exact path="/blog" component={NewPost} />
          <Route path="/blog/update/:id" component={EditPost}/>
          <Route path="/blog/:id" component={PostPage}/>
          <Route path="/about" component={About} />
          <Route path="*" component={Missing} />
        </Switch>
        </DataProvider>
        <Footer />
    </div>
  );
}

export default App;
