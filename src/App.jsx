import { BrowserRouter, Routes, Route } from 'react-router-dom';
import NavBar from './components/NavBar';
import Home from './components/Home';
import MiniGame1 from './components/MiniGame1';
import MiniGame2 from './components/MiniGame2';
import MiniGame3 from './components/MiniGame3';
import MiniGame4 from './components/MiniGame4';
import MiniGame5 from './components/MiniGame5';
import './index.css';

function App() {
  return (
    <BrowserRouter basename="/minijuegos-musica-siglo-xx">
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/minijuego1" element={<MiniGame1 />} />
        <Route path="/minijuego2" element={<MiniGame2 />} />
        <Route path="/minijuego3" element={<MiniGame3 />} />
        <Route path="/minijuego4" element={<MiniGame4 />} />
        <Route path="/minijuego5" element={<MiniGame5 />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
