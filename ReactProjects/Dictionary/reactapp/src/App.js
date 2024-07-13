import './App.css';
import Navbar from './components/Navbar'
import './Images/image1.jpg'

function App() {
  return (
    <body>
      <Navbar />
      <div class="card container col-6">
        <img src={require('./Images/image1.jpg')} class="card-img-top"></img>
        
      </div>
    </body>
  );
}

export default App;
